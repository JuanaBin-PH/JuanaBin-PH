"""One-shot recovery: rebuild docs/*.md from this session's transcript.

The ten docs/ files were written earlier in the session and later deleted from
disk. Their exact bytes are still recorded in the Claude Code transcript as the
`content` field of each Write tool call, so we replay those verbatim rather than
retyping them (retyping risks drifting from the PDF source).

Delete this file once docs/ is verified.
"""

import io
import json
import os

TRANSCRIPT = (
    r"C:\Users\Andrew San Antonio\.claude\projects"
    r"\c--Users-Andrew-San-Antonio-JuanaBin-PH"
    r"\7c68c26f-d330-427e-bb3c-dd7d1a9fca3c.jsonl"
)

recovered = {}

with io.open(TRANSCRIPT, encoding="utf-8", errors="replace") as fh:
    for line in fh:
        try:
            record = json.loads(line)
        except ValueError:
            continue
        blocks = (record.get("message") or {}).get("content")
        if not isinstance(blocks, list):
            continue
        for block in blocks:
            if not isinstance(block, dict):
                continue
            if block.get("type") != "tool_use" or block.get("name") != "Write":
                continue
            params = block.get("input") or {}
            path = (params.get("file_path") or "").replace("\\", "/")
            if "/docs/" in path and path.endswith(".md"):
                # Later writes win, so a revised version supersedes the first.
                recovered[os.path.basename(path)] = params.get("content") or ""

if not recovered:
    raise SystemExit("no docs/*.md Write calls found in transcript")

os.makedirs("docs", exist_ok=True)
for name in sorted(recovered):
    body = recovered[name]
    with io.open(os.path.join("docs", name), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(body)
    print("%-32s %6d bytes  %4d lines" % (name, len(body), body.count("\n") + 1))

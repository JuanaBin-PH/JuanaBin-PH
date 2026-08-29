# JuanaBin PH

Waste → Wallet → Product | Segregate-to-Earn on Stellar

## What This Is

JuanaBin PH pays Filipino households a reward token for correctly segregating their waste, and settles every reward as a real payment on the Stellar network so the payout record is publicly verifiable rather than self-reported.

A resident throws a sorted item into a JuanaBin. The backend classifies the throw, decides the award, and sends a **JBIN** payment from a Stellar distribution account to the resident's wallet. The transaction hash is the receipt. Anyone can check it on a public block explorer or through this project's own no-login verifier, without an account and without trusting the project.

**Architecture:** off-chain logic, on-chain settlement. The reward decision happens in the backend; the payment happens on Stellar.

**Asset model:** JBIN is a Stellar **classic custom asset** — an issuing account, a separate distribution account, and trustlines. It is not a Soroban smart contract. The reasoning is in [13 §13.1](docs/13-tech-stack-and-deployment.md#131-why-a-classic-asset-and-not-a-soroban-contract).

**Reward model:** 1 JBIN = 1 point, awarded **per correctly segregated item**.

| Material class | Enum code | Award |
| --- | --- | --- |
| PET bottle ≥500 ml | `PET_LARGE` | 6 JBIN |
| PET small / container | `PET_SMALL` | 4 JBIN |
| Foil sachet | `FOIL_SACHET` | 2 JBIN |
| Biodegradable | `BIODEGRADABLE` | 2 JBIN |

Daily cap 60 JBIN per user per day. Redemption threshold 2,000 JBIN. Any material class outside the four-value enum is rejected before any payment is built.

## Key Facts

| Field | Details |
| --- | --- |
| Award Amount | $5,000 USD (Instaward) |
| Organization | Buslo Builders (operating as JuanaBin PH) |
| Primary Contact | Julie Ann Soriano — buslongpagasa@gmail.com |
| Sprint Start Date | August 31, 2026 |
| Sprint End Date | September 29, 2026 |
| Sprint Length | 30 calendar days (4 working weeks + 2-day submission buffer) |
| Token Symbol | JBIN (Stellar classic custom asset) |
| Stellar Network | Testnet (this sprint) → Mainnet (pilot go-live, Phase 1) |
| GitHub | github.com/BusloBuilders/juanabin-ph <!-- TODO: this value comes from source PDF p.20. The configured git remote for this working tree is github.com/JuanaBin-PH/JuanaBin-PH. Confirm which repository is public and being submitted, then make this row, the clone command below, and docs/08 and docs/12 all agree. --> |
| License | MIT — see [LICENSE](LICENSE) |
| Document Version | v1.0 — SCF Submission Ready |

## Deliverables

- **Deliverable 1** — Stellar Wallet Provisioning + JBIN Reward Asset (Testnet)
- **Deliverable 2** — Segregate-to-Earn Logic Engine + Negative-Path Test Suite
- **Deliverable 3** — Admin Dashboard + Public Fail-Closed Verifier
- **Deliverable 4** — Reproducibility & Evidence Package

Acceptance criteria for each are split into **unconditional** engineering criteria and **conditional** participant criteria in [03 — Scope of Work](docs/03-scope-of-work.md). No unconditional criterion depends on a real household being onboarded.

## Tech Stack

Sprint stack — deliberately a strict subset of the project's longer-term stack, so nothing here is discarded when it scales. Full breakdown in [13 — Tech Stack & Deployment](docs/13-tech-stack-and-deployment.md).

| Layer | Choice |
| --- | --- |
| Backend API | FastAPI (Python) |
| Stellar integration | `stellar-sdk` (Python) against Horizon Testnet |
| Database | PostgreSQL (Supabase or Neon) |
| Authentication | Kinde |
| Admin dashboard | React + Tailwind |
| Public verifier | Static HTML/JS reading Horizon directly — no backend, no login |
| Officer intake form | Mobile-responsive web form |
| Tests / CI | pytest + GitHub Actions |

Explicitly **deferred**, and listed as deferred so their absence reads as a decision rather than an omission: AWS IoT Core / ECS / S3 / CloudFront / SageMaker, MQTT, Redis, Celery + RabbitMQ, YOLOv8 / TensorFlow Lite, a Flutter app, GCash/Maya APIs, Mapbox, and Soroban.

## Setup

Requires Python 3.11+, PostgreSQL, and Node 20+ for the dashboard.

```bash
git clone https://github.com/BusloBuilders/juanabin-ph.git
cd juanabin-ph

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env             # then fill in the values
```

[`.env.example`](.env.example) lists every required variable with empty values. It contains **no key material**. Fill it locally; never commit the result — `.env` is blocked by [.gitignore](.gitignore).

Generate a Testnet keypair and fund it:

```bash
curl "https://friendbot.stellar.org?addr=<YOUR_PUBLIC_KEY>"
```

Run the API and the tests:

```bash
uvicorn app.main:app --reload
pytest                                     # full suite
pytest -m "not live"                       # skip tests that hit Horizon
pytest tests/test_negative_paths.py -v     # the 11 rejection cases
pytest tests/test_verifier_states.py -v    # the 6 verifier states
```

Full cold-start instructions, environment variable table and a step-by-step verification walkthrough are in [12 — Verification and Reproducibility](docs/12-verification-and-reproducibility.md).

## Network Configuration

| Setting | Value |
| --- | --- |
| Network | Stellar **Testnet** |
| Horizon | `https://horizon-testnet.stellar.org` |
| Network passphrase | `Test SDF Network ; September 2015` |
| Friendbot | `https://friendbot.stellar.org?addr=<PUBLIC_KEY>` |
| Explorer | `https://stellar.expert/explorer/testnet` |

## Deployment Evidence

Filled in as each artifact goes live during the sprint. Nothing here is invented — a row stays a placeholder until the real value exists on-chain or at a public URL.

| Artifact | Value |
| --- | --- |
| JBIN asset code | `JBIN` |
| JBIN issuer public key | <!-- TODO: fill in after issuance on Aug 31, 2026 --> |
| JBIN distribution account public key | <!-- TODO: fill in after issuance on Aug 31, 2026 --> |
| JBIN issuance transaction hash | <!-- TODO: fill in after issuance on Aug 31, 2026 --> |
| Asset page on explorer | `https://stellar.expert/explorer/testnet/asset/JBIN-<ISSUER_PUBLIC_KEY>` |
| Admin dashboard URL | <!-- TODO: fill in after Week 3 deployment --> |
| Public verifier URL | <!-- TODO: fill in after Week 3 deployment --> |
| CI run (11/11 negative-path cases) | <!-- TODO: fill in after Week 2 --> |
| Walkthrough video | <!-- TODO: fill in after Week 4 --> |
| Complete reward transaction list | <!-- TODO: path to the committed CSV, after Week 4 --> |
| Release tag / commit for verification | <!-- TODO: fill in at submission --> |

## Proof of Work

This repository is the evidence, not a description of evidence.

- **Commit history** — one commit per deliverable minimum, pushed as the work lands rather than squashed at the end. Target 4+ substantive public commits across the sprint.
- **On-chain transactions** — 50+ Testnet transactions across the issuer, distribution and household accounts, every reward payment recorded with its hash.
- **Negative-path tests in public CI** — 11 rejection cases, each asserting that **no transaction was created** where rejection is the expected outcome. Defined up front in [11 — Test Plan](docs/11-test-plan.md), before implementation.
- **A verifier that fails closed** — six distinct states (`VALID`, `MALFORMED`, `MISMATCHED`, `WRONG_NETWORK`, `UNKNOWN`, `UNAVAILABLE`). Pasting a Mainnet hash, an unrecorded hash, or a hash while Horizon is unreachable never returns `VALID`.
- **Reproducibility** — a reviewer can clone this repository into a clean environment, follow the documented steps, and independently re-verify a payout end to end. See [12 §12.7](docs/12-verification-and-reproducibility.md).
- **Weekly SCF forum updates** — Sep 6, Sep 13, Sep 20 and Sep 27, 2026, with a completion report on Sep 29.

## What the Ledger Does and Does Not Prove

Stated plainly, because overstating this is the fastest way to lose a reviewer's trust.

The ledger proves **which wallet was paid, how much, and when**, and that the record was not altered afterwards. The event hash proves a recorded event matches its submitted field values and was not submitted twice or edited after settlement.

It does **not** prove that the waste was correctly segregated, that the material class is accurate, that the submitting officer is trustworthy, or that any LGU verified the event. Full statement in [14 §14.2](docs/14-data-and-authorization-policy.md#142-what-the-event-hash-proves).

References in this repository to barangay offices, LGUs, DILG, DENR and Philippine legislation describe **intended use and design target**. No endorsement, approval, review or partnership by any institution is claimed. See [14 §14.6](docs/14-data-and-authorization-policy.md#146-institutional-references).

This sprint is **not decentralized**. A single operator controls the issuer, the distribution account and the submitter allowlist. Multisig governance, a revocation policy and independent audit are not designed yet — [14 §14.5](docs/14-data-and-authorization-policy.md#145-governance-limitations--stated-plainly).

## Security

- **No secrets in this repository.** No private keys, secret seeds, API keys, credentials or filled `.env` files are committed. [`.env.example`](.env.example) contains variable names and empty values only.
- **`.gitignore` blocks** `.env`, `.env.*`, `*.pem`, `*.key`, `*.seed`, `secrets.json`, `issuer_secret*`, `distributor_secret*` and `keypairs/`, while whitelisting `.env.example`.
- **Key custody.** The issuer keypair is held cold and offline, used only for the initial issuance. The distributor secret lives in the deployment host's environment variable store and is the only account that ever pays users. Neither is ever committed. See [14 §14.4](docs/14-data-and-authorization-policy.md#144-issuer-and-distributor-authorization).
- **Testnet only.** Every key referenced in this repository during the sprint is a Testnet key. Testnet keys have no monetary value; they are still not committed.
- **No personal data on-chain.** Household names, addresses, GPS coordinates, phone numbers, email addresses, government IDs, photographs and officer identity are never written to the ledger. [14 §14.1](docs/14-data-and-authorization-policy.md#141-on-chain-data-policy) lists exactly what is and is not on-chain.
- **Payout address.** The SCF payout wallet is a Freighter **Mainnet** address beginning with `G`: <!-- TODO: insert the Mainnet G... payout address from Freighter. Confirm the network is set to Mainnet, not Testnet, before submitting. A Testnet address cannot receive the award. -->

If you believe you have found exposed key material in this repository, email buslongpagasa@gmail.com.

## Documentation

Sections 01–10 are derived from the source submission PDF; each records its origin in `source_pages`. Sections 11–15 were written in response to SCF reviewer guidance and carry `source_pages: []`.

The fastest way to understand how the system actually works is [15 — System Flow Diagrams](docs/15-system-flow.md), which draws the earn flow, every rejection gate, and the verifier state machine.

| Section | Document | Source pages |
| --- | --- | --- |
| 01 | [Executive Summary](docs/01-executive-summary.md) | 3 |
| 02 | [Problem Statement & Objectives](docs/02-problem-and-objectives.md) | 4–5 |
| 03 | [Scope of Work — 30-Day Deliverables](docs/03-scope-of-work.md) | 6–8 |
| 04 | [30-Day Weekly Timeline](docs/04-30-day-timeline.md) | 9–12 |
| 05 | [Evidence of Completion](docs/05-evidence-of-completion.md) | 13–15 |
| 06 | [Budget Justification](docs/06-budget-justification.md) | 16–17 |
| 07 | [Stellar Alignment Statement](docs/07-stellar-alignment.md) | 18–19 |
| 08 | [Team Information & Project Overview](docs/08-team-information.md) | 20–21 |
| 09 | [Next Steps](docs/09-next-steps-roadmap.md) | 22–23 |
| 10 | [Document Summary & Submission Checklist](docs/10-document-summary.md) | 24–25 |
| 11 | [Test Plan](docs/11-test-plan.md) | — |
| 12 | [Verification & Reproducibility](docs/12-verification-and-reproducibility.md) | — |
| 13 | [Tech Stack & Deployment](docs/13-tech-stack-and-deployment.md) | — |
| 14 | [Data & Authorization Policy](docs/14-data-and-authorization-policy.md) | — |
| 15 | [System Flow Diagrams](docs/15-system-flow.md) | — |

The working sprint plan for the same window is [SPRINT.md](SPRINT.md).

## Status

v1.0 — SCF Submission Ready. Sprint: August 31 – September 29, 2026. Stellar Testnet (development) → Stellar Mainnet (pilot go-live, Phase 1).

Dates in this repository supersede the August 20 – September 18, 2026 window printed in the source submission PDF. The `source_pages` field in each `docs/` file still records where the material originated.

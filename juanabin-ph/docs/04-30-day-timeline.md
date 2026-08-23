---
title: 30-Day Weekly Timeline — August 25 – September 25, 2026
section: "04"
source_pages: [9, 10, 11, 12]
---

# 04 — 30-Day Weekly Timeline — August 25 – September 25, 2026

**Sprint Period:** August 25, 2026 (Day 1) → September 25, 2026 (Day 32) • **Structure:** 4 working weeks, each with a clear focus area, task breakdown, and week-end milestone gate, followed by a short submission buffer • **Deliverable Staggering:** D1 by Week 1 → D2 by Week 2 → D3 by Weeks 3–4 → Full QA & submission in the buffer

## Sprint at a Glance — Aug 25 to Sep 25, 2026

<!-- This chart is derived from the Aug 25 – Sep 25, 2026 week banding used in SPRINT.md. It is NOT the bar chart printed on p.9 of the source PDF, which charts the superseded Aug 20 – Sep 18 window. -->

| Activity / Deliverable | Aug 25–26 | Aug 27–28 | Aug 29–31 | Sep 01–02 | Sep 03–04 | Sep 05–07 | Sep 08–09 | Sep 10–11 | Sep 12–14 | Sep 15–16 | Sep 17–18 | Sep 19–21 | Sep 22–23 | Sep 24–25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Week 1: Foundation** | █ | █ | █ | | | | | | | | | | | |
| **D1: Wallet + JBIN Token** | █ | █ | █ | | | | | | | | | | | |
| **Week 2: Reward Engine** | | | | █ | █ | █ | | | | | | | | |
| **D2: Logic Engine** | | | | █ | █ | █ | | | | | | | | |
| **Week 3: Pilot Deploy** | | | | | | | █ | █ | █ | | | | | |
| **Week 4: Redemption & Docs** | | | | | | | | | | █ | █ | █ | | |
| **D3: Dashboard + Pilot** | | | | | | | █ | █ | █ | █ | █ | █ | | |
| **Buffer: QA & Submit** | | | | | | | | | | | | | █ | █ |

Legend: Week 1 (Aug 25–31) • Week 2 (Sep 1–7) • Week 3 (Sep 8–14) • Week 4 (Sep 15–21) • Buffer (Sep 22–25)

## WEEK 1 — August 25–31, 2026 | Days 1–7 | Foundation & Token Setup

**Key Tasks:**

- August 25, 2026: Sprint kickoff — set up Stellar Testnet environment, fund issuer account via Friendbot
- August 25–26: Issue JBIN custom asset on Stellar Testnet, configure issuer account and token metadata
- August 26–27: Integrate Kinde authentication flow with Stellar wallet auto-provisioning pipeline
- August 27–28: Test minimum 5 wallet provisioning events end-to-end; validate trustline establishment
- August 28–29: Push wallet provisioning code to GitHub (initial commit); configure CI/CD pipeline
- August 29–30: Deploy staging environment on cloud infrastructure (SSL, domain, Testnet connection)
- August 30–31: Full end-to-end testing of Kinde → Stellar wallet flow; 10 test wallets provisioned

**Milestones:**

- JBIN asset issuer account published on `testnet.stellar.expert`
- GitHub Commit #1: wallet provisioning module pushed (public repo)
- Week 1 SCF Forum progress update posted (August 31, 2026)

> **Gate:** JBIN live on Testnet • Kinde → Stellar wallet flow operational • Stellar Explorer: issuer account URL published

## WEEK 2 — September 1–7, 2026 | Days 8–14 | Reward Logic Engine

**Key Tasks:**

- September 1: Build waste intake form (mobile-responsive web UI) with all required data fields
- September 1–2: Implement JBIN reward calculation engine (Python) with the configurable rate table
- September 2–3: Connect reward engine to Stellar payment dispatch; test first live JBIN transfer on Testnet
- September 3–4: Implement duplicate-prevention hash system (household ID + timestamp + weight)
- September 4–5: Test every waste material class with correct JBIN amounts
- September 5–6: Execute 15+ reward transactions on Testnet; log all transaction hashes
- September 6–7: Commit reward engine to GitHub with inline documentation; deploy to staging

**Milestones:**

- 25+ JBIN reward transaction hashes logged (Stellar Expert URLs exported)
- GitHub Commit #2: reward logic engine pushed (MIT licensed)
- Week 2 SCF Forum progress update posted (September 7, 2026)

> **Gate:** Reward engine live on Testnet • 15+ reward transactions with Explorer URLs • GitHub Commit #2 pushed

## WEEK 3 — September 8–14, 2026 | Days 15–21 | Pilot Deployment & Dashboard

**Key Tasks:**

- September 8: Deploy admin dashboard (waste metrics, JBIN issued, CO²e avoided) to staging URL
- September 8–9: Build public-facing transparency page with Stellar Explorer links (no-login required)
- September 9–10: Onboard 10 pilot households (Kinde signup + wallet provisioning + barangay briefing)
- September 10–11: Run 20+ pilot segregation events; issue JBIN rewards on-chain; log all transaction hashes
- September 11–12: Conduct community briefing session for pilot households; collect first feedback
- September 12–13: Implement PDF/CSV export function for LGU compliance reporting (RA 9003 format)
- September 13–14: Commit dashboard code to GitHub; deploy to production staging URL

**Milestones:**

- Dashboard live at public URL with Stellar Explorer links (publicly accessible)
- 10 pilot household Stellar wallets active with JBIN balances
- GitHub Commit #3: dashboard source code pushed
- Week 3 SCF Forum progress update posted (September 14, 2026)

> **Gate:** Dashboard live at public URL • 10 pilot households active • 20+ on-chain pilot transactions verified

## WEEK 4 — September 15–21, 2026 | Days 22–28 | Redemption, Verification & Documentation

**Key Tasks:**

- September 15: Implement and test the redemption flow against the redemption threshold
- September 15–16: Record 3–5 minute walkthrough video (screen + voiceover); upload to YouTube
- September 16–17: Compile all Stellar Explorer URLs and GitHub commit SHAs into evidence package
- September 17–18: Generate LGU-ready pilot report (PDF); validate all on-chain metrics vs. acceptance criteria
- September 18–19: Write README documentation for all three components; finalize GitHub repository
- September 19–20: Report the measured breakage rate against the assumption set at sprint start
- September 20–21: Internal sign-off on the evidence package; prepare forum completion report

**Milestones:**

- Video walkthrough published (YouTube URL submitted to SCF)
- Redemption flow tested with an on-chain transaction hash recorded
- Week 4 SCF Forum progress update posted (September 21, 2026)

> **Gate:** Video published (YouTube URL) • Redemption tested on-chain • Evidence package assembled

## BUFFER — September 22–25, 2026 | Days 29–32 | QA & Submission

**Key Tasks:**

- September 22–23: Full end-to-end QA of all three deliverables against their acceptance criteria
- September 23–24: Final evidence review — every Explorer URL, every commit SHA, the video link, the LGU report
- September 24: Validate each on-chain metric against the minimum thresholds in [05 — Evidence of Completion](05-evidence-of-completion.md)
- September 25: Post completion report to SCF Forum; submit all evidence to the SCF Instawards team by **September 25, 2026**

**Milestones:**

- Full evidence checklist complete (all 16 items confirmed)
- SCF Forum completion report published (September 25, 2026)
- **Sprint closed: September 25, 2026**

> **Gate:** Full evidence checklist complete • SCF submission submitted by September 25, 2026

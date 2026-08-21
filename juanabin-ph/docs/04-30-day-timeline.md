---
title: 30-Day Weekly Timeline — August 20 – September 18, 2026
section: "04"
source_pages: [9, 10, 11, 12]
---

# 04 — 30-Day Weekly Timeline — August 20 – September 18, 2026

**Sprint Period:** August 20, 2026 (Day 1) → September 18, 2026 (Day 30) • **Structure:** 4 sequential weeks, each with a clear focus area, daily task breakdown, and week-end milestone gate • **Deliverable Staggering:** D1 by Week 1 → D2 by Week 2 → D3 by Week 3 → Full QA & submission by Week 4

## Timeline Bar Chart — 30-Day Sprint at a Glance

<!-- Column labels and row labels are transcribed verbatim from the p.9 bar chart. Filled cells (█) correspond to the shaded bars printed in the chart; the shading matches the week date bands given in the legend below and in the weekly sections. -->

| Activity / Deliverable | Aug 20–21 | Aug 22–23 | Aug 24–25 | Aug 26–27 | Aug 28–29 | Aug 30–31 | Sep 01–02 | Sep 03–04 | Sep 05–06 | Sep 07–08 | Sep 09–10 | Sep 11–12 | Sep 13–15 | Sep 16–18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Week 1: Foundation** | █ | █ | █ | █ | | | | | | | | | | |
| **D1: Wallet + JBIN Token** | █ | █ | █ | █ | | | | | | | | | | |
| **Week 2: Reward Engine** | | | | | █ | █ | █ | | | | | | | |
| **D2: Logic Engine** | | | | | █ | █ | █ | | | | | | | |
| **Week 3: Pilot Deploy** | | | | | | | | █ | █ | █ | █ | | | |
| **D3: Dashboard + Pilot** | | | | | | | | █ | █ | █ | █ | | | |
| **Week 4: QA & Submit** | | | | | | | | | | | | █ | █ | █ |

Legend: Week 1 (Aug 20–27) • Week 2 (Aug 27–Sep 3) • Week 3 (Sep 3–10) • Week 4 (Sep 10–18)

## WEEK 1 — August 20–27, 2026 | Days 1–7 | Foundation & Token Setup

**Key Tasks:**

- August 20, 2026: Sprint kickoff — set up Stellar Testnet environment, fund issuer account via Friendbot
- August 20–21: Issue JBIN custom asset on Stellar Testnet, configure issuer account and token metadata
- August 21–22: Integrate Kinde authentication flow with Stellar wallet auto-provisioning pipeline
- August 22–23: Test minimum 5 wallet provisioning events end-to-end; validate trustline establishment
- August 23–24: Push wallet provisioning code to GitHub (initial commit); configure CI/CD pipeline
- August 24–25: Deploy staging environment on cloud infrastructure (SSL, domain, Testnet connection)
- August 25–27: Full end-to-end testing of Kinde → Stellar wallet flow; 10 test wallets provisioned

**Milestones:**

- JBIN asset issuer account published on `testnet.stellar.expert`
- GitHub Commit #1: wallet provisioning module pushed (public repo)
- Week 1 SCF Forum progress update posted (August 27, 2026)

> **Gate:** JBIN live on Testnet • Kinde → Stellar wallet flow operational • Stellar Explorer: issuer account URL published

## WEEK 2 — August 27 – September 3, 2026 | Days 8–14 | Reward Logic Engine

**Key Tasks:**

- August 27–28: Build waste intake form (mobile-responsive web UI) with all required data fields
- August 28–29: Implement JBIN reward calculation engine (Python) — PET 1.0/kg, Sachet 0.5/kg, Organic 0.2/kg
- August 29–30: Connect reward engine to Stellar payment dispatch; test first live JBIN transfer on Testnet
- August 30–31: Implement duplicate-prevention hash system (household ID + timestamp + weight)
- August 31 – September 1: Test all 3 waste material types (PET, Sachet, Organic) with correct JBIN amounts
- September 1–2: Execute 15+ reward transactions on Testnet; log all transaction hashes
- September 2–3: Commit reward engine to GitHub with inline documentation; deploy to staging

**Milestones:**

- 25+ JBIN reward transaction hashes logged (Stellar Expert URLs exported)
- GitHub Commit #2: reward logic engine pushed (MIT licensed)
- Week 2 SCF Forum progress update posted (September 3, 2026)

> **Gate:** Reward engine live on Testnet • 15+ reward transactions with Explorer URLs • GitHub Commit #2 pushed

## WEEK 3 — September 3–10, 2026 | Days 15–21 | Pilot Deployment & Dashboard

**Key Tasks:**

- September 3–4: Deploy admin dashboard (waste metrics, JBIN issued, CO²e avoided) to staging URL
- September 4–5: Build public-facing transparency page with Stellar Explorer links (no-login required)
- September 5–6: Onboard 10 pilot households (Kinde signup + wallet provisioning + barangay briefing)
- September 6–7: Run 20+ pilot segregation events; issue JBIN rewards on-chain; log all transaction hashes
- September 7–8: Conduct community briefing session for pilot households; collect first feedback
- September 8–9: Implement PDF/CSV export function for LGU compliance reporting (RA 9003 format)
- September 9–10: Commit dashboard code to GitHub; deploy to production staging URL

**Milestones:**

- Dashboard live at public URL with Stellar Explorer links (publicly accessible)
- 10 pilot household Stellar wallets active with JBIN balances
- GitHub Commit #3: dashboard source code pushed
- Week 3 SCF Forum progress update posted (September 10, 2026)

> **Gate:** Dashboard live at public URL • 10 pilot households active • 20+ on-chain pilot transactions verified

## WEEK 4 — September 10–18, 2026 | Days 22–30 | Verification, Documentation & Submission

**Key Tasks:**

- September 10–11: Conduct full QA testing of all three deliverables end-to-end
- September 11–12: Record 3–5 minute walkthrough video (screen + voiceover); upload to YouTube
- September 12–13: Compile all Stellar Explorer URLs and GitHub commit SHAs into evidence package
- September 13–14: Generate LGU-ready pilot report (PDF); validate all on-chain metrics vs. acceptance criteria
- September 14–15: Write README documentation for all three components; finalize GitHub repository
- September 15–16: Finalize SCF Instawards evidence package; prepare forum completion report
- September 17–18: Post completion report to SCF Forum; submit all evidence to SCF Instawards team by **September 18, 2026**

**Milestones:**

- Video walkthrough published (YouTube URL submitted to SCF)
- Full evidence checklist complete (all 16 items confirmed)
- SCF Forum completion report published (September 18, 2026)
- **Sprint closed: September 18, 2026**

> **Gate:** Video published (YouTube URL) • Full evidence checklist complete • SCF submission submitted by September 18, 2026

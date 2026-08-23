# JuanaBin PH — 30-Day Stellar Sprint Plan

**Window:** August 25 – September 25, 2026 (4 working weeks + a short submission buffer; Sep 25 is a Friday)

**Focus:** Ship the reward-points loop on Stellar Testnet — provision wallets, issue JBIN, and settle every correct throw as a real on-chain payment — with enough transaction evidence to close the three Instawards deliverables.

**Architecture:** Off-chain logic + on-chain settlement — the backend decides when a correct throw earns points, then sends a real JBIN payment on Stellar.

**Asset model:** JBIN is a Stellar classic custom asset (issuing account + distribution account + trustlines), not a Soroban smart contract.

**Network:** Testnet for this sprint.

Week bands run Tuesday–Monday from the Aug 25 start; the buffer is Tue Sep 22 – Fri Sep 25.

## Deliverables

| ID | Name | Done when |
| --- | --- | --- |
| **D1** | Stellar Wallet Provisioning + JBIN Reward Token (Testnet) | JBIN asset live on Testnet from a funded issuing account; distribution account holds supply; minimum 10 test wallets provisioned through the Kinde flow with JBIN trustlines established; explorer URLs published for the issuer account and 3+ trustline transactions; provisioning code committed. |
| **D2** | Segregate-to-Earn Logic Engine | Scoring table enforced for all four material classes; daily cap and duplicate rejection provably working; minimum 25 reward payments executed on Testnet with a transaction hash recorded for every payout; engine committed under MIT. |
| **D3** | Pilot Community Demo + Admin Dashboard | 10 pilot households with active wallets holding JBIN balances; admin dashboard and no-login public transparency page live at a public URL with explorer links; minimum 20 on-chain pilot reward transactions; LGU-ready PDF/CSV export generated; walkthrough video published; dashboard code committed. |

Cumulative target across the sprint: **50+ Testnet transactions** and **3+ public commits (one per deliverable)**, matching the thresholds already published in [docs/05-evidence-of-completion.md](docs/05-evidence-of-completion.md).

## Reward Parameters

For the pilot, **1 JBIN = 1 point**. Peso values are display only — nothing is pegged on-chain.

| Material class | Award | Notes |
| --- | --- | --- |
| PET bottle ≥500 ml | 6 JBIN | Highest-value stream |
| PET small / container | 4 JBIN | |
| Foil sachet | 2 JBIN | |
| Biodegradable | 2 JBIN | |

| Control | Value | Enforced by |
| --- | --- | --- |
| Daily earn cap | 60 JBIN / user / day | Logic engine, before payment dispatch |
| Redemption threshold | 2,000 JBIN | Logic engine + redemption flow |
| Assumed breakage | ~45% | Assumption at sprint start; measured during pilot |

The cap of 60 JBIN/day is exactly ten ≥500 ml PET bottles per user per day.

## Week 1 — Aug 25–31 (D1)

| # | Task | D |
| --- | --- | --- |
| 1 | Set up Testnet environment; fund the issuing account via Friendbot | D1 |
| 2 | Create the issuing and distribution accounts as separate keypairs; document custody of both secrets outside the repo | D1 |
| 3 | Issue the JBIN classic asset; set the distribution account's JBIN trustline and push supply to it | D1 |
| 4 | Lock down the operational rule that only the distribution account ever pays users; the issuer stays cold | D1 |
| 5 | Wire Kinde authentication to keypair auto-generation; fund each new wallet to the minimum XLM reserve | D1 |
| 6 | Auto-establish each new wallet's JBIN trustline as part of provisioning | D1 |
| 7 | Provision 10 test wallets end to end; confirm every trustline landed | D1 |
| 8 | Commit the provisioning module (GitHub commit #1) | D1 |

**On-chain evidence produced:** issuer account page on `testnet.stellar.expert`; distribution account page; `changeTrust` transaction hashes for 10 test wallets (3+ published as samples); the initial issuance payment hash from issuer to distribution.

## Week 2 — Sep 1–7 (D2)

| # | Task | D |
| --- | --- | --- |
| 1 | Define the throw-event schema the bin/officer submits: user ID, material class, timestamp, device ID | D2 |
| 2 | Implement the scoring table as configurable data, not inline constants — 6 / 4 / 2 / 2 by class, version-tracked in the repo | D2 |
| 3 | Enforce the 60 JBIN/user/day cap server-side, evaluated before any payment is built | D2 |
| 4 | Implement the idempotency hash (user ID + timestamp + material) and reject duplicates before dispatch | D2 |
| 5 | Build the payment dispatcher: construct the JBIN payment from the distribution account, sign, submit, persist the returned hash | D2 |
| 6 | Write the memo field per payment (material class + event hash) so each award is self-describing on-chain | D2 |
| 7 | Handle the failure paths that actually occur on Testnet: missing trustline, underfunded distributor, timeout-then-retry without double-paying | D2 |
| 8 | Execute 25+ reward payments covering all four material classes; export the hash list | D2 |
| 9 | Commit the reward engine under MIT (GitHub commit #2) | D2 |

**On-chain evidence produced:** 25+ reward payment hashes with per-class samples (6 / 4 / 2 / 2 JBIN); a cap-rejection and a duplicate-rejection case documented as producing **no** transaction; memo contents visible on explorer.

## Week 3 — Sep 8–14 (D3)

| # | Task | D |
| --- | --- | --- |
| 1 | Deploy the admin dashboard: JBIN issued, counts by material class, per-household earnings, transaction hashes with explorer links | D3 |
| 2 | Build the no-login public transparency page reading aggregated data from the Testnet ledger | D3 |
| 3 | Onboard 10 pilot households — Kinde signup, wallet provisioning, barangay briefing | D3 |
| 4 | Run the pilot to 20+ on-chain reward events across the four material classes | D3 |
| 5 | Start the breakage measurement: record points earned vs. points redeemed per user from day one of the pilot | D3 |
| 6 | Collect first household feedback in the briefing session | D3 |
| 7 | Commit the dashboard source (GitHub commit #3) | D3 |

**On-chain evidence produced:** 10 pilot household account pages showing JBIN balances; 20+ pilot reward transaction hashes; dashboard live at a public URL with each row linking to its explorer transaction.

## Week 4 — Sep 15–21 (D3)

| # | Task | D |
| --- | --- | --- |
| 1 | Implement and test the redemption flow against the 2,000 JBIN threshold | D3 |
| 2 | Test redemption on a **seeded** account — see the note below; the threshold is unreachable organically inside this window | D3 |
| 3 | Build the LGU-ready PDF/CSV export: volumes by class, JBIN issued, participating households anonymised, explorer audit links | D3 |
| 4 | Record the 3–5 minute walkthrough: signup, throw, payment dispatch, transaction on explorer, dashboard updating; publish to YouTube | D3 |
| 5 | Write the README for all three components | D1/D2/D3 |
| 6 | Report the measured breakage rate against the ~45% assumption | D3 |
| 7 | Reconcile the sprint dates against the submission document — see "Reconcile before submitting" | — |

**On-chain evidence produced:** redemption transaction hash from the seeded test account; cumulative transaction count confirmed at 50+ across issuer, distribution, and household accounts.

## Buffer — Sep 22–25 (QA + submission)

| # | Task |
| --- | --- |
| 1 | Full end-to-end QA of D1, D2, D3 against each "done when" column above |
| 2 | Compile the evidence package: every explorer URL, every commit SHA, the video link, the LGU report |
| 3 | Validate each on-chain metric against the published thresholds in `docs/05-evidence-of-completion.md` |
| 4 | Post the completion report to the SCF forum and submit by **Fri Sep 25, 2026** |

## Out of scope for these 30 days

- Mainnet — Testnet only for this sprint.
- GCash/Maya cash-out — no fiat off-ramp is built or tested.
- Soroban smart-contract version of the earn/redeem logic — the logic stays off-chain in the backend.
- SEP-24/31 anchor integration — no deposit/withdraw or cross-border rails.
- Non-custodial user wallets — keys are provisioned and held server-side for the pilot.
- Multi-barangay rollout — one pilot barangay, ten households.

All six are post-sprint concerns, not part of this 30-day scope.

## Reconcile before submitting

Four items must be settled before this plan and the submission document can go out together.

1. **Sprint dates conflict.** This plan runs **Aug 25 – Sep 25, 2026**. The submission document states **Aug 20 – Sep 18, 2026** throughout — see [docs/04-30-day-timeline.md](docs/04-30-day-timeline.md), the four weekly gate dates, the Gantt bands, the signature block in [docs/08-team-information.md](docs/08-team-information.md), and the constraints in [docs/06-budget-justification.md](docs/06-budget-justification.md). Pick one window and change every occurrence, including the four SCF forum update dates (Aug 27, Sep 3, Sep 10, Sep 18) and the "no extensions without prior written SCF approval" clause.
2. **Token economics conflict.** This plan scores **per item** and states 1 JBIN = 1 point. The submission document states **1 JBIN = 1 kg verified waste diverted** with per-kilogram rates of PET 1.0, Sachet 0.5, Organic 0.2 JBIN/kg — see `docs/03-scope-of-work.md` (D2 Reward Calculation, D1 Token Economics) and `docs/07-stellar-alignment.md`. These are two different reward models and cannot both ship. Note that the "15+ kg waste diverted" completion metric in `docs/05-evidence-of-completion.md` only means anything under the per-kilogram model; a per-item model needs a per-item equivalent or a separate weight log.
3. **Redemption threshold is unreachable inside the sprint.** At the 60 JBIN/day cap, a user earning the maximum every single day for 30 days reaches 1,800 JBIN — short of the 2,000 threshold. No pilot household can hit redemption organically in this window, so redemption must be demonstrated on a seeded balance, and the pilot cannot produce a real breakage figure for redeemed points. Either lower the pilot threshold, raise the cap, or state plainly in the submission that redemption is demonstrated rather than observed.
4. **Confirm SCF evidence rules against the current program page** before submitting. Re-read the live Instawards program page and check the evidence requirements, accepted artifact types, whether Testnet-only evidence is still sufficient, and the submission mechanics against the 16-item checklist in `docs/05-evidence-of-completion.md`. Do not rely on the copy captured in the submission document.

## Long-Term Goals (Beyond the 30-Day Sprint)

After this sprint closes, the direction is a Mainnet launch of JBIN, peso cash-out through a BSP-licensed e-money issuer, and scaling from the pilot barangay to a multi-barangay / LGU rollout. Direction only — none of it is in the 30-day scope above.

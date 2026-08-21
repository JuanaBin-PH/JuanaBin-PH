---
title: Scope of Work — 30-Day Deliverables
section: "03"
source_pages: [6, 7, 8]
---

# 03 — Scope of Work — 30-Day Deliverables

## D1 — Stellar Wallet Provisioning + JBIN Reward Token

*Build and deploy the Stellar wallet provisioning pipeline and the JBIN custom asset (token) on Stellar Testnet. This delivers the financial inclusion layer: any household completing Kinde authentication receives a funded Stellar wallet ready to receive JBIN tokens.*

| Component | Specification |
| --- | --- |
| **Stellar Asset** | JBIN token issued on Stellar Testnet using Stellar Python SDK. Asset code: `JBIN`. Issuer account funded and activated on Testnet. |
| **Wallet Provisioning** | Kinde authentication triggers auto-generation of Stellar keypair. Wallet funded with 1 XLM minimum reserve. Trustline to JBIN established automatically. |
| **Token Economics** | 1 JBIN = 1 kg verified waste diverted. Non-tradeable, non-speculative. Redeemable for Buslo artisan products (PHP equivalent). Fixed utility value. |
| **User Authentication** | Kinde auth layer — no bank account, no government ID, no e-wallet required. Mobile-first signup flow for low-income household access. |
| **On-Chain Verification** | All wallet creations and JBIN issuances visible on `testnet.stellar.expert` and Stellar Laboratory. Public, permissionless audit trail. |

> **Acceptance Criteria:**
> - JBIN asset deployed on Testnet
> - Minimum 10 test wallets provisioned via Kinde flow
> - JBIN trustlines established for all test wallets
> - Stellar Explorer URLs provided for issuer account and 3+ test transactions
> - GitHub commit with wallet provisioning code

## D2 — Segregate-to-Earn Logic Engine

*Design, build, and test the core business logic that converts verified waste segregation events into JBIN token rewards sent to household Stellar wallets. Waste becomes income, trustlessly, on-chain.*

| Component | Specification |
| --- | --- |
| **Waste Intake Form** | Web-based form for waste collector/barangay officer to log: Household Stellar wallet ID, material type (PET / Sachet / Organic), weight in kg, collection timestamp, GPS coordinates (optional). |
| **Reward Calculation** | Python-based logic: PET = 1.0 JBIN/kg &nbsp;\|&nbsp; Sachet = 0.5 JBIN/kg &nbsp;\|&nbsp; Organic/Food Waste = 0.2 JBIN/kg. Configurable rate table with version history on GitHub. |
| **Stellar Payment Dispatch** | Reward engine calls Stellar Python SDK: constructs payment operation, signs with distributor keypair, submits to Testnet. Transaction hash logged to local database and returned to admin UI. |
| **Fraud Prevention** | Each waste submission generates a unique hash (household ID + timestamp + weight). Duplicate submissions rejected before Stellar transaction initiated. Hash logged on-chain via Stellar memo field. |
| **Carbon Offset Record** | CO²e value calculated and logged per transaction in Stellar memo: PET (~3 kg CO²e/kg), Sachet (~2 kg CO²e/kg), Organic (~0.5 kg CO²e/kg). |

> **Acceptance Criteria:**
> - Minimum 25 test reward transactions executed on Testnet
> - All 3 waste material types tested with correct JBIN amounts
> - Stellar transaction hashes for every reward payout provided
> - Duplicate prevention tested and documented
> - GitHub commit with reward engine source code (MIT licensed)

## D3 — Pilot Community Demo + Admin Dashboard

*Deploy a live pilot with real (or simulated) households earning JBIN tokens, supported by a publicly accessible admin/community dashboard showing real-time waste diversion metrics, JBIN payouts, and Stellar Explorer links. Demonstrates SCF-grade transparency and prepares for barangay-level onboarding.*

| Component | Specification |
| --- | --- |
| **Pilot Scope** | Minimum 10 households across 1 pilot barangay. Each household performs at least 2 segregation events. Minimum 20 on-chain JBIN reward transactions generated during pilot. |
| **Admin Dashboard** | Web dashboard: total JBIN issued, total kg waste diverted by material type, per-household earnings leaderboard, CO²e avoided, Stellar transaction hashes with Explorer links, pilot timeline status. |
| **Community Transparency** | Public-facing dashboard page (no login required) showing aggregated waste diversion data — designed for Barangay Captain, DILG, and public auditor access. Data sourced from Stellar Testnet ledger. |
| **LGU-Ready Reporting** | Export function generating PDF/CSV report of pilot results: material volumes, JBIN issued, CO²e avoided, participating households (anonymized), Stellar Explorer audit links. Formatted for RA 9003 compliance reporting. |
| **Video Walkthrough** | 3–5 minute screen-recorded video: household signup, waste logging, JBIN reward dispatch, transaction visible on Stellar Expert, dashboard update in real-time. Published to YouTube. |

> **Acceptance Criteria:**
> - Minimum 10 pilot households with active Stellar wallets
> - Dashboard live at public URL with Stellar Explorer links
> - Minimum 20 on-chain pilot transactions on Stellar Expert
> - Video walkthrough published (YouTube URL)
> - LGU-ready pilot report generated
> - GitHub commit with dashboard source code

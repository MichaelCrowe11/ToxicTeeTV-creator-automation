# ToxicTeeTV Content Selection + Design System

## Purpose

This system turns raw source material (your upcoming link) into:
1. Selected content candidates
2. Platform-safe creative concepts
3. Production-ready briefs
4. Scheduled publish queue

## Workflow

| Stage | Input | Output | Owner |
|---|---|---|---|
| Intake | Source link(s) | Content inventory rows | Content Producer |
| Triage | Inventory | Shortlist (A/B/C priority) | Creator Lead |
| Compliance QA | Shortlist | Approved concept list | Ops/Compliance Lead |
| Design | Approved concepts | Creative briefs + asset list | Creator Lead |
| Production | Briefs | Final assets + captions | Content Producer |
| Publish | Final assets | Live posts + KPI tags | Growth Analyst |

## Selection Scorecard (100 pts)

| Dimension | Weight | Scoring Rule |
|---|---|---|
| Conversion potential | 25 | Strong subscriber/PPV/tip trigger |
| Retention potential | 15 | High replay/follow-up potential |
| Brand fit (ToxicTeeTV) | 20 | Strong voice and identity fit |
| Compliance safety | 20 | Low policy risk, clear consent path |
| Production effort | 10 | Lower complexity scores higher |
| Repurposing value | 10 | Can spin into multiple formats |

Priority rules:
- `A`: score >= 80 and compliance-safe
- `B`: score 65-79 with revisions
- `C`: score < 65 or high compliance risk

## Content Types

| Type | Goal | Monetization Path |
|---|---|---|
| Teaser feed post | Drive profile actions | Convert to paid sub |
| Paid post (PPV) | Direct revenue | PPV unlock |
| DM offer | Upsell engaged fans | Paid message + tips |
| Retention drop | Reduce churn | Keep active subscribers |
| Promo campaign asset | Acquire/re-activate | Discount/free trial conversion |

## Mandatory Compliance Gate

Every concept must pass before production:
1. All visible participants verified 18+.
2. Consent/release evidence available and archived.
3. No disallowed themes from AUP/moderation policy.
4. No meetup/off-platform payment language.
5. AI usage disclosed where required (`#ai` when applicable).
6. Caption and CTA reviewed by Ops/Compliance Lead.

## Creative Brief Template

| Field | Description |
|---|---|
| Brief ID | `TT-CREATIVE-###` |
| Source link | Input URL |
| Concept title | Working title |
| Content type | Teaser / PPV / DM / Retention / Promo |
| Target segment | New / active / lapsing / high-LTV |
| Core hook | 1-line hook |
| CTA | Subscribe / Unlock / Tip / Rejoin |
| Offer details | Price, promo %, expiry |
| Asset requirements | Video/photo/caption/thumbnail |
| Compliance notes | Risks + controls |
| Publish window | Date + time |
| KPI target | CTR, conversion, PPV attach, etc. |

## Weekly Build-Out Rhythm

| Day | Action |
|---|---|
| Monday | Intake + score new source content |
| Tuesday | Shortlist + compliance pass |
| Wednesday | Draft briefs + captions |
| Thursday | Produce/edit assets |
| Friday | Schedule publish + prepare DM flows |
| Sunday | KPI review + next-week reprioritization |

## Tracking IDs Convention

- Source item: `TT-SRC-###`
- Concept: `TT-CON-###`
- Brief: `TT-CREATIVE-###`
- Published asset: `TT-PUB-###`
- Experiment: `TT-EXP-###`

## Handoff Format (when you send a link)

When you provide the content link, I will return:
1. Ranked shortlist table (`A/B/C`)
2. Top 10 recommended concepts
3. 2-week publish queue
4. Briefs for first 5 priority assets
5. Compliance notes for each selected concept


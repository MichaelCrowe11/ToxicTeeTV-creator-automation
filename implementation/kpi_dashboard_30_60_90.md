# ToxicTeeTV KPI Dashboard (30/60/90)

Primary tracker: `implementation/kpi_dashboard_30_60_90_weekly.csv`

## Baseline Assumption

- Starting active paying subscribers (Week 0): `0` (extracted from account snapshot on March 5, 2026)
- Weekly KPI targets are fixed for Weeks `1-13` (March 9, 2026 through June 7, 2026).

## Exact Phase Targets

| Phase | Weeks | New Subs | PPV Sales | Custom Orders | DM Conversion (End of Phase) | Active Subs EOW |
|---|---|---:|---:|---:|---:|---:|
| Day 1-30 | W1-W4 | 38 | 36 | 6 | 6.5% | 36 |
| Day 31-60 | W5-W8 | 54 | 70 | 12 | 8.5% | 82 |
| Day 61-90 | W9-W13 | 90 | 170 | 26 | 11.0% | 151 |
| Total (90 days) | W1-W13 | 182 | 276 | 44 | 11.0% | 151 |

## Weekly KPIs You Track

- `new_subs`
- `ppv_sales`
- `custom_orders`
- `dm_conversion_pct`

## Weekly Success Gate

Mark week as `On Track` when all four conditions are true:

1. New subs >= weekly target
2. PPV sales >= weekly target
3. Custom orders >= weekly target
4. DM conversion >= weekly target

If fewer than 3 are achieved, mark `Off Track` and run corrective sprint:

1. Increase DM volume to next week's `dm_threads_target`
2. Run 1 timed PPV promo test (price, hook, or urgency)
3. Push 1 custom-offer CTA in top 20 spender conversations

## File Links

- Weekly dashboard CSV: [kpi_dashboard_30_60_90_weekly.csv](/Users/michaelcrowe/ToxicTeeTV-creator-automation/implementation/kpi_dashboard_30_60_90_weekly.csv)
- Google Sheets-ready tracker: [kpi_dashboard_30_60_90_google_sheets.csv](/Users/michaelcrowe/ToxicTeeTV-creator-automation/implementation/kpi_dashboard_30_60_90_google_sheets.csv)
- 30/60/90 board: [ToxicTeeTV_30-60-90_execution_board.md](/Users/michaelcrowe/ToxicTeeTV-creator-automation/ToxicTeeTV_30-60-90_execution_board.md)
- Album board: [ToxicTeeTV_30-60-90_execution_board_from_album_1BJcPXPK3w1ipQ947.md](/Users/michaelcrowe/ToxicTeeTV-creator-automation/ToxicTeeTV_30-60-90_execution_board_from_album_1BJcPXPK3w1ipQ947.md)

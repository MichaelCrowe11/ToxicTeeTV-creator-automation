#!/usr/bin/env python3
import csv
from pathlib import Path


def score_row(row: dict) -> dict:
    title = row.get("item_title", "")
    summary = row.get("content_summary", "")

    is_portrait = "Portrait" in title
    is_landscape = "Landscape" in title
    is_batch_a = "Batch A" in summary
    is_batch_b = "Batch B" in summary
    is_batch_c = "Batch C" in summary

    if is_portrait:
        conversion = 20
        retention = 11
        brand_fit = 17
        compliance = 13
        effort = 8
        repurpose = 8
    elif is_landscape:
        conversion = 16
        retention = 9
        brand_fit = 15
        compliance = 14
        effort = 7
        repurpose = 7
    else:
        conversion = 17
        retention = 10
        brand_fit = 16
        compliance = 13
        effort = 7
        repurpose = 7

    if is_batch_a and is_portrait:
        conversion += 2
        repurpose += 2
    if is_batch_b and is_portrait:
        conversion += 1
        retention += 1
    if is_batch_c and is_portrait:
        conversion += 2
        brand_fit += 1

    total = conversion + retention + brand_fit + compliance + effort + repurpose
    if total >= 80:
        tier = "A"
    elif total >= 65:
        tier = "B"
    else:
        tier = "C"

    row["conversion_potential_25"] = str(conversion)
    row["retention_potential_15"] = str(retention)
    row["brand_fit_20"] = str(brand_fit)
    row["compliance_safety_20"] = str(compliance)
    row["production_effort_10"] = str(effort)
    row["repurposing_value_10"] = str(repurpose)
    row["total_score_100"] = str(total)
    row["priority_tier"] = tier
    row["compliance_notes"] = (
        "Manual compliance review required before publish; verify consent/release and platform-safe captioning."
    )
    if tier == "A":
        row["recommended_offer"] = "PPV ladder + teaser CTA"
    else:
        row["recommended_offer"] = "Teaser + DM upsell"
    row["status"] = "Ready"
    return row


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    src = root / "ToxicTeeTV_source_inventory_1BJcPXPK3w1ipQ947.csv"
    out = root / "implementation" / "scored_inventory_initial.csv"

    with src.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [score_row(dict(r)) for r in reader]
        fieldnames = reader.fieldnames or []

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows -> {out}")


if __name__ == "__main__":
    main()

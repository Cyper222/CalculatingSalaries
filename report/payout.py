from typing import List, Dict
from .base import Report

class PayoutReport(Report):
    def generate(self, data: List[Dict[str, str]]) -> str:
        lines = ["Payout Report:"]
        for row in data:
            try:
                name = row["name"]
                department = row["department"]
                hours = float(row["hours_worked"])
                rate = float(row["hourly_rate"])
                payout = hours * rate
                lines.append(f"{name} ({department}) - ${payout:.2f}")
            except (KeyError, ValueError) as e:
                lines.append(f"Invalid row: {row} -> {e}")
        return "\n".join(lines)

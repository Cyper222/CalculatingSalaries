from .payout import PayoutReport

def get_report(report_type: str):
    reports = {
        "payout": PayoutReport(),
    }
    if report_type not in reports:
        raise ValueError(f"Unknown report type: {report_type}")
    return reports[report_type]

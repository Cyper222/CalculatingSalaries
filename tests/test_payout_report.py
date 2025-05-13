import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from report.payout import PayoutReport

def test_payout_report_basic():
    data = [
        {
            'name': 'Alice',
            'department': 'Marketing',
            'hours_worked': '160',
            'hourly_rate': '50',
        }
    ]
    report = PayoutReport()
    result = report.generate(data)
    assert "Alice (Marketing) - $8000.00" in result

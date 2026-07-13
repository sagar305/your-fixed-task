import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_criterion_1_total_requests():
    """instruction.md #1: total_requests must equal the number of log lines."""
    report = _load_report()
    assert report.get("total_requests") == 6, (
        f"expected total_requests=6, got {report.get('total_requests')!r}"
    )


def test_criterion_2_unique_ips():
    """instruction.md #2: unique_ips must equal the number of distinct client IPs."""
    report = _load_report()
    assert report.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {report.get('unique_ips')!r}"
    )


def test_criterion_3_top_path():
    """instruction.md #3: top_path must be the single most-requested path."""
    report = _load_report()
    assert report.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {report.get('top_path')!r}"
    )


def test_criterion_4_schema():
    """instruction.md #4: report.json must contain exactly the three required keys."""
    report = _load_report()
    assert set(report.keys()) == {"total_requests", "unique_ips", "top_path"}, (
        f"unexpected keys in report.json: {sorted(report.keys())}"
    )

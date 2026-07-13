# Log Report

There is an Apache/NCSA-style access log at `/app/access.log`. Parse it and
write a summary report as valid JSON to `/app/report.json`.

The JSON object must contain exactly these three keys:

- `total_requests` (integer)
- `unique_ips` (integer)
- `top_path` (string)

Your solution is graded against these numbered success criteria:

1. `total_requests` equals the total number of requests (lines) in the log.
2. `unique_ips` equals the number of distinct client IP addresses in the log.
3. `top_path` equals the single most-requested path in the log (e.g. `/index.html`).
4. `/app/report.json` contains exactly the three keys above — no extra keys, none missing.

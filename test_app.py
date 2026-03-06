from core.fetcher import fetch_all_data
from core.analyzer import analyze_logs
from server.app import start_server

data = fetch_all_data(
    function_name="nova-debugger-test",
    region="us-east-2",
    hours=24
)

result = analyze_logs(data['metadata'], data['log_text'])

print("\n--- DIAGNOSIS ---")
print(f"Summary: {result['summary']}")
print(f"Health: {result['overall_health']}")
print(f"\nErrors found: {len(result['errors'])}")
for error in result['errors']:
    print(f"\n→ {error['error_type']} [{error['severity']}]")
    print(f"  What: {error['what_happened']}")
    print(f"  Why: {error['why_it_happened']}")
    print(f"  Fix: {error['how_to_fix']}")

start_server(result, data['metadata'])
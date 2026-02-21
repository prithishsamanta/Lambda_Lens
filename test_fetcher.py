from core.fetcher import fetch_all_data

# Replace with your actual region
result = fetch_all_data(
    function_name="nova-debugger-test",
    region="us-east-2",  # change this to your region
    hours=24
)

# Print summary
print("\n--- METADATA ---")
for key, value in result['metadata'].items():
    print(f"{key}: {value}")

print("\n--- LOG SAMPLE (first 500 chars) ---")
print(result['log_text'][:500])
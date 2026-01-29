import boto3
import datetime
from moto import mock_aws

def calculate_yield(total_checks, failed_checks):
    """Calculates the health percentage of the infrastructure."""
    if total_checks == 0:
        return 100
    yield_pct = ((total_checks - failed_checks) / total_checks) * 100
    return round(yield_pct, 2)

@mock_aws
def run_audit():
    # 1. Setup Mock Environment
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="public-sensitive-data") 
    s3.create_bucket(Bucket="internal-logs-encrypted")
    
    # 2. The Auditor Logic
    findings = []
    buckets = s3.list_buckets().get("Buckets", [])
    
    # Let's define our total 'check' count based on resources found
    total_resources = len(buckets) + 5 # Simulating other hidden checks
    
    for bucket in buckets:
        name = bucket["Name"]
        if "public" in name:
            findings.append(f"**CRITICAL**: Bucket `{name}` has a 'public' naming convention. Check ACLs.")
    
    # 3. Calculate Yield (Key for Intel Yield Engineer Role)
    failed_count = len(findings)
    yield_score = calculate_yield(total_resources, failed_count)
    
    # 4. Generate the Markdown Report
    report_content = f"# Daily Cloud Audit: {datetime.date.today()}\n\n"
    
    report_content += "##System Yield Metrics\n"
    status_emoji = 'Healthy' if yield_score > 90 else Attention Required'
    report_content += f"- **Infrastructure Yield:** {yield_score}%\n"
    report_content += f"- **Operational Status:** {status_emoji}\n\n"
    
    report_content += "## Summary of Findings\n"
    if findings:
        report_content += "\n".join(findings)
    else:
        report_content += "No major misconfigurations found."
    
    with open("AUDIT_REPORT.md", "w") as f:
        f.write(report_content)
    
    print(f"Audit complete. Yield: {yield_score}%")

# ... existing code above ...
    
    # 5. Alert Logic: Fail the process if yield is below a threshold
    YIELD_THRESHOLD = 80.0
    if yield_score < YIELD_THRESHOLD:
        print(f"ALERT: Yield ({yield_score}%) is below threshold ({YIELD_THRESHOLD}%)!")
        # exit(1) makes the GitHub Action turn RED
        import sys
        sys.exit(1)

if __name__ == "__main__":
    run_audit()


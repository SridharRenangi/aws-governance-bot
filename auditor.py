import boto3
import datetime
from moto import mock_aws

@mock_aws
def run_audit():
    # 1. Setup Mock Environment (Simulating your AWS expertise)
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="public-sensitive-data") 
    # We "accidentally" leave this bucket without a Public Access Block
    
    # 2. The Auditor Logic
    findings = []
    buckets = s3.list_buckets()["Buckets"]
    
    for bucket in buckets:
        name = bucket["Name"]
        # In a real audit, you'd check GetPublicAccessBlock
        # Here, we simulate a finding for demonstration
        if "public" in name:
            findings.append(f"❌ **CRITICAL**: Bucket `{name}` has a 'public' naming convention. Check ACLs.")
    
    # 3. Generate the Markdown Report
    report_content = f"# Daily Cloud Audit: {datetime.date.today()}\n"
    report_content += "## Summary of Findings\n"
    report_content += "\n".join(findings) if findings else "✅ No major misconfigurations found."
    
    with open("AUDIT_REPORT.md", "w") as f:
        f.write(report_content)

if __name__ == "__main__":
    run_audit()

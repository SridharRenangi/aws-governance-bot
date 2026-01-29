# AWS CloudGuard: Automated Governance Auditor

[![Daily Audit](https://github.com/SridharRenangi/aws-governance-bot/actions/workflows/daily_audit.yml/badge.svg)](https://github.com/SridharRenangi/aws-governance-bot/actions/workflows/daily_audit.yml)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![AWS](https://img.shields.io/badge/AWS-Services-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Project Overview
This repository hosts an automated **Cloud Governance Auditor** designed to demonstrate "Compliance-as-Code." It performs daily scans of a simulated AWS environment to identify security misconfigurations, resource leaks, and architectural deviations.

By utilizing **GitHub Actions** and **Python**, this project ensures that cloud infrastructure remains within the "guardrails" required for enterprise-grade deployments.

## Tech Stack
* **Language:** Python 3.10
* **Automation:** GitHub Actions (CI/CD)
* **Cloud SDK:** Boto3 (AWS SDK for Python)
* **Testing/Simulation:** Moto (Mock AWS Infrastructure)
* **Documentation:** Markdown

## Architectural Features
- **Cost-Free Auditing:** Leverages `moto` to mock an AWS environment, allowing for complex architectural testing without incurring AWS costs.
- **Automated Reporting:** Generates a daily `AUDIT_REPORT.md` summarizing findings like:
    - S3 Buckets with public access.
    - Unencrypted RDS Instances.
    - Over-provisioned Lambda functions.
- **DevSecOps Integration:** Demonstrates how to bake security audits directly into the development lifecycle.

## Daily Status Updates
The project is configured to run every day at **09:00 UTC**. You can view the latest findings in the [AUDIT_REPORT.md](./AUDIT_REPORT.md) file. This serves as a live ledger of the repository's activity and status.

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/SridharRenangi/aws-governance-bot.git](https://github.com/SridharRenangi/aws-governance-bot.git)

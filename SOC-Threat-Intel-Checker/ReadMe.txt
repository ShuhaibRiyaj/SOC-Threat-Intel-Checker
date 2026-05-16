# SOC Threat Intelligence Automation Tool

A beginner SOC automation project built with Python that checks IP reputation using multiple threat intelligence sources such as AbuseIPDB and VirusTotal.

## Features
- Checks IP reputation using AbuseIPDB
- Checks IP reputation using VirusTotal
- Parses JSON API responses
- Generates SOC-style analyst verdicts
- Beginner-friendly SOC automation workflow

---

# Technologies Used
- Python
- Requests Module
- REST APIs
- JSON Parsing
- Threat Intelligence Enrichment

---

# Setup Instructions

## 1. Install Required Module

```bash
pip install requests
```

---

## 2. Create Free API Accounts

AbuseIPDB:
https://www.abuseipdb.com/register

VirusTotal:
https://www.virustotal.com/gui/join-us

---

## 3. Paste Your API Keys

Inside `multi_ti_checker.py`

Replace:

```python
ABUSEIPDB_KEY = "PLEASE ENTER YOUR API KEY HERE"
VT_API_KEY = "PLEASE ENTER YOUR API KEY HERE"
```

With your real API keys.

Example:

```python
ABUSEIPDB_KEY = "your_real_abuseipdb_key"
VT_API_KEY = "your_real_virustotal_key"
```

---

# Run The Script

Run:

```bash
python multi_ti_checker.py
```

Enter an IP address when prompted.

Example:

```text
45.155.205.233
```

---

# Example Output

```text
==================================================
SOC Threat Intelligence IP Checker
==================================================

Target IP: 45.155.205.233

[AbuseIPDB Result]
Abuse Score: 92%
Country: RU
Total Reports: 145
Whitelisted: False

[VirusTotal Result]
Malicious: 12
Suspicious: 2
Harmless: 15
Undetected: 5

[SOC Analyst Summary]
Verdict: HIGH RISK - IP should be investigated or blocked.
```

---

# Skills Demonstrated
- Python Scripting
- SOC Automation
- API Integration
- JSON Parsing
- Threat Intelligence Enrichment
- IOC Analysis
- Security Operations Workflow
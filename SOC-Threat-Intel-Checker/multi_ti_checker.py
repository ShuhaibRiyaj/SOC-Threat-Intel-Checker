!pip install requests

import requests
import sys
import os


ABUSEIPDB_KEY = "PLEASE ENTER YOUR API KEY HERE"
VT_API_KEY = "PLEASE ENTER YOUR API KEY HERE"


def check_abuseipdb(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": ABUSEIPDB_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()["data"]

    return {
        "source": "AbuseIPDB",
        "ip": data["ipAddress"],
        "abuse_score": data["abuseConfidenceScore"],
        "country": data["countryCode"],
        "total_reports": data["totalReports"],
        "whitelisted": data["isWhitelisted"]
    }


def check_virustotal(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    headers = {
        "x-apikey": VT_API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()["data"]["attributes"]

    stats = data["last_analysis_stats"]

    return {
        "source": "VirusTotal",
        "malicious": stats["malicious"],
        "suspicious": stats["suspicious"],
        "harmless": stats["harmless"],
        "undetected": stats["undetected"],
        "reputation": data.get("reputation", "N/A")
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python multi_ti_checker.py <IP_ADDRESS>")
        sys.exit()

    ip = input("Enter IP: ")

    print("=" * 50)
    print("SOC Threat Intelligence IP Checker")
    print("=" * 50)
    print(f"Target IP: {ip}")
    print()

    abuse_result = check_abuseipdb(ip)

    print("[AbuseIPDB Result]")
    print(f"Abuse Score:   {abuse_result['abuse_score']}%")
    print(f"Country:       {abuse_result['country']}")
    print(f"Total Reports: {abuse_result['total_reports']}")
    print(f"Whitelisted:   {abuse_result['whitelisted']}")
    print()

    vt_result = check_virustotal(ip)

    print("[VirusTotal Result]")
    print(f"Malicious:     {vt_result['malicious']}")
    print(f"Suspicious:    {vt_result['suspicious']}")
    print(f"Harmless:      {vt_result['harmless']}")
    print(f"Undetected:    {vt_result['undetected']}")
    print(f"Reputation:    {vt_result['reputation']}")
    print()

    print("[SOC Analyst Summary]")

    if abuse_result["abuse_score"] >= 70 or vt_result["malicious"] > 0:
        print("Verdict: HIGH RISK - IP should be investigated or blocked.")
    elif abuse_result["abuse_score"] >= 30 or vt_result["suspicious"] > 0:
        print("Verdict: MEDIUM RISK - IP needs further review.")
    else:
        print("Verdict: LOW RISK - No strong malicious indicators found.")


if __name__ == "__main__":
    main()


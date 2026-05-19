import re

pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

with open("auth.log", "r") as f:
    for line in f:
        if "FAILED" in line:
            ips = re.findall(pattern, line)
            print(f"FAILED login from: {ips} | {line.strip()}")




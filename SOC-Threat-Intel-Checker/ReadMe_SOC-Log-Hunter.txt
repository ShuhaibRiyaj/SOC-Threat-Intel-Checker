# SOC-Log-Hunter

Simple Python-based SOC log triage tool for detecting suspicious authentication activity and sensitive file access from raw log data.

## Features

* Detects brute force attacks
* Detects password spray activity
* Detects successful login after repeated failures
* Detects access to sensitive files
* Parses multiple common log formats
* Simple terminal-based threat summary output

## Detection Logic

### Brute Force Detection

Flags:

* 5 or more failed logins
* Same source IP
* Same username

### Password Spray Detection

Flags:

* Multiple usernames
* Same source IP
* Repeated authentication failures

### Sensitive File Access

Detects access attempts to:

* `/etc/shadow`
* `/etc/passwd`
* `.env`
* `id_rsa`
* `credentials`

## Supported Log Examples

```text
2024-05-01 02:13:44 FAILED LOGIN user=admin src=192.168.1.55

May 1 02:13:45 server sshd[123]: Failed password for root from 10.0.0.5

[2024-05-01 03:01] AUTH_FAILURE username=jsmith ip=172.16.0.9

2024-05-01 09:25:00 FILE ACCESS user=jsmith file=/etc/shadow
```

## Requirements

Python 3.x

Optional:

```bash
pip install colorama
```

## Run the Tool

```bash
python soc_log_hunter.py
```

## Using Custom Logs

Inside the script:

```python
run(your_log_string)
```

Or load logs from a file:

```python
run(open("auth.log").read())
```

## Sample Detections

* Brute force attack
* Password spray
* Successful compromise after failures
* Sensitive file access
* Repeated authentication failures

## Skills Demonstrated

* Python scripting
* Regex parsing
* Log analysis
* Threat detection logic
* SOC alert triage concepts
* Basic detection engineering

## Author
Shuhaib Riyaj

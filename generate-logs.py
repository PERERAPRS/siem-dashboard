import requests
import random
import datetime
import time

ES_URL = "http://localhost:9200/security-logs/_doc"

attack_ips = ["192.168.1.100", "10.0.0. 50", "45.33.32.156", "185.220.101.1", "103.25.40.15"]
users = ["admin", "root", "administrator", "guest", "user", "backup", "service"]
actions = ["failed_login", "failed_login", "failed_login", "successful_login", "port_scan", "privilege_escalation"]
hostnames = ["server01", "workstation05", "dc01", "webserver", "database01"]

def generate_log():
    action = random.choice(actions)
    return {
        "@timestamp": datetime.datetime.utcnow().isoformat(),
        "src_ip": random. choice(attack_ips),
        "username": random.choice(users),
        "action": action,
        "event_count": random.randint(1, 20),
        "port": random.choice([22, 3389, 445, 80, 443, 21, 23]),
        "status": "failure" if "failed" in action else "success",
        "hostname": random. choice(hostnames),
        "severity": random.choice(["low", "medium", "high", "critical"])
    }

print("🛡️ Generating security logs...  Press Ctrl+C to stop")
print("-" * 50)

count = 0
while True:
    log = generate_log()
    try:
        requests.post(ES_URL, json=log)
        count += 1
        print(f"[{count}] {log['action']:20} | IP: {log['src_ip']:15} | User: {log['username']}")
        time.sleep(0.5)
    except Exception as e:
        print(f"Error: {e}")
        break
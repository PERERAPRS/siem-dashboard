# 🛡️ SIEM Security Dashboard

A Security Information and Event Management (SIEM) dashboard built with the ELK Stack (Elasticsearch, Logstash, Kibana) for real-time security monitoring and threat detection. 

![Dashboard Preview](screenshots/dashboard. png)

---

## 📋 Project Overview

This project demonstrates core SOC (Security Operations Center) skills by:
- Collecting and centralizing security logs
- Detecting brute-force attacks and failed login attempts
- Visualizing security events in real-time dashboards
- Monitoring for suspicious activity across systems

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| **Elasticsearch** | Log storage and search engine |
| **Kibana** | Visualization and dashboards |
| **Docker** | Container orchestration |
| **Python** | Log generation and automation |

---

## 🚀 Quick Start

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- Python 3.x installed
- At least 4GB RAM available

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/siem-dashboard.git
cd siem-dashboard
```

### 2. Start ELK Stack
```bash
docker-compose up -d
```

Wait 2-3 minutes for services to initialize. 

### 3.  Verify Services
```bash
# Check Elasticsearch
curl http://localhost:9200

# Open Kibana
# Navigate to: http://localhost:5601
```

### 4. Generate Security Logs
```bash
pip install requests
python generate_logs.py
```

Let the script run for 2-3 minutes to populate data.

### 5. Configure Kibana
1. Go to `http://localhost:5601`
2. Navigate to **Stack Management** → **Data Views**
3. Create data view with pattern: `security-logs*`
4. Set timestamp field: `@timestamp`

### 6. View Dashboard
1. Navigate to **Dashboard**
2. Import `dashboards/siem-dashboard.ndjson` or create manually

---

## 📊 Dashboard Features

### Visualizations Included

| Panel | Type | Description |
|-------|------|-------------|
| Failed Logins Over Time | Line Chart | Tracks failed authentication attempts |
| Top Attacking IPs | Bar Chart | Identifies most active threat sources |
| Success vs Failure | Pie Chart | Login attempt success rate |
| Attack Sources | Data Table | Detailed view of security events |
| Total Events | Metric | Real-time event counter |

### Security Events Monitored

- 🔴 **Failed Login Attempts** - Brute force indicators
- 🟢 **Successful Logins** - Authentication tracking
- 🟠 **Port Scans** - Reconnaissance detection
- 🔵 **Privilege Escalation** - Unauthorized access attempts

---

## 📁 Project Structure

```
siem-dashboard/
├── docker-compose.yml      # ELK Stack configuration
├── generate_logs.py        # Security log generator
├── README.md               # Project documentation
├── . gitignore              # Git ignore rules
├── dashboards/
│   └── siem-dashboard.ndjson   # Kibana dashboard export
└── screenshots/
    └── dashboard.png       # Dashboard preview
```

---

## 🔧 Configuration

### Docker Compose Services

```yaml
services:
  elasticsearch:
    ports: 9200
    memory: 512MB - 1GB
    
  kibana:
    ports: 5601
    memory: 512MB
```

### Log Generator Settings

Edit `generate_logs. py` to customize:
- `attack_ips` - Simulated attacker IP addresses
- `users` - Target usernames
- `actions` - Types of security events
- `time. sleep()` - Log generation frequency

---

## 🚨 Detection Rules

### Brute Force Detection
Triggers when: **10+ failed logins in 5 minutes from same IP**

```json
{
  "query": {
    "bool": {
      "must": [
        { "match": { "action": "failed_login" } }
      ],
      "filter": [
        { "range": { "@timestamp": { "gte": "now-5m" } } }
      ]
    }
  }
}
```

---

## 📈 Future Improvements

- [ ] Add Logstash for advanced log parsing
- [ ] Integrate real Windows/Linux logs via Filebeat
- [ ] Implement email/Slack alerting
- [ ] Add GeoIP mapping for attack visualization
- [ ] Create threat intelligence feed integration
- [ ] Add MITRE ATT&CK framework mapping

---

## 🎓 Skills Demonstrated

| Skill Category | Competencies |
|----------------|--------------|
| **SIEM Operations** | Log collection, analysis, correlation |
| **Threat Detection** | Identifying attack patterns, anomalies |
| **Data Visualization** | Creating actionable security dashboards |
| **DevOps** | Docker, container orchestration |
| **Scripting** | Python automation for security tools |

---

## 🛑 Troubleshooting

| Issue | Solution |
|-------|----------|
| Elasticsearch won't start | Increase Docker memory to 4GB+ |
| No data in Kibana | Check time range filter (set to Last 1 hour) |
| Connection refused | Wait 2-3 minutes for services to start |
| Port already in use | Stop other services using ports 9200/5601 |

### Useful Commands

```bash
# View container status
docker ps -a

# Check Elasticsearch logs
docker logs elasticsearch

# Restart services
docker-compose down
docker-compose up -d

# Stop all services
docker-compose down
```

---

## 📚 Resources

- [Elastic Documentation](https://www.elastic.co/guide/index.html)
- [Kibana Query Language (KQL)](https://www.elastic.co/guide/en/kibana/current/kuery-query.html)
- [MITRE ATT&CK Framework](https://attack. mitre.org/)
- [Sigma Detection Rules](https://github.com/SigmaHQ/sigma)

---

## 👤 Author

**PERERAPRS**

- GitHub: [@PERERAPRS](https://github.com/PERERAPRS)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE). 

---

## ⭐ Show Your Support

If this project helped you learn SIEM concepts, give it a ⭐! 

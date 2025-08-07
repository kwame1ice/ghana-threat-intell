# 🇬🇭 Ghana Threat Intelligence Toolkit

This repository helps collect, monitor, and report on threat indicators targeting Ghanaian domains and digital infrastructure.

---

## 🔍 Features

- ✅ Subdomain monitoring for `.gh` government and corporate domains
- ✅ IOC (Indicator of Compromise) logging from dark web, Discord, Telegram
- ✅ PDF report generation for intelligence teams or CERTs
- ✅ GitHub Actions automation (daily or on demand)

---

## 🧠 Tools

| Tool / Script        | Purpose                               |
|----------------------|----------------------------------------|
| `monitor.py`         | Monitors `.gh` domains for subdomains |
| `collector.py`       | Logs threat indicators from leaks      |
| `generate_report.py` | Generates PDF report from IOC data     |
| GitHub Workflows     | Automates tasks on a schedule          |

---

## 📁 Folder Structure

ghana-threat-intell/
├── monitor.py
├── collector.py
├── generate_report.py
├── extracted_iocs_.csv
├── results_.txt
├── ghana_threat_report.pdf
├── indicators.csv
├── .github/
│ └── workflows/
│ ├── subdomain-monitor.yml
│ └── collect-iocs.yml
├── README.md

---

## 🚀 Usage

### 🔧 Requirements

```bash
pip install requests pandas reportlab
python monitor.py          # Subdomain check
python collector.py        # IOC collection
python generate_report.py  # PDF creation


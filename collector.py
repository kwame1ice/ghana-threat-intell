import csv
import datetime

# Sample IOCs - you can later load from a file or scrape
ioc_data = [
    {
        "Type": "Domain",
        "Value": "police.gov.gh",
        "Risk": "Critical",
        "Source": "darkforums.st",
        "Description": "Ghana Police Service domain compromised"
    },
    {
        "Type": "Telegram",
        "Value": "https://t.me/JokeirR07x",
        "Risk": "High",
        "Source": "Telegram",
        "Description": "Threat actor channel"
    },
    {
        "Type": "URL",
        "Value": "https://bcam.police.gov.gh/7f7fs/...",
        "Risk": "Critical",
        "Source": "Screenshot",
        "Description": "Bodycam surveillance dashboard"
    }
]

def save_iocs(iocs):
    today = datetime.date.today().isoformat()
    filename = f"extracted_iocs_{today}.csv"

    with open(filename, "w", newline='') as csvfile:
        fieldnames = ["Type", "Value", "Risk", "Source", "Description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for ioc in iocs:
            writer.writerow(ioc)

    print(f"[+] Saved IOCs to {filename}")

if __name__ == "__main__":
    save_iocs(ioc_data)

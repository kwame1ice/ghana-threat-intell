import requests
import datetime

domains_to_check = [
    "police.gov.gh",
    "bog.gov.gh",
    "nca.org.gh",
    "gcb.com.gh",
    "mofep.gov.gh"
]

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            subdomains = set(entry['common_name'] for entry in data)
            return subdomains
        else:
            return set()
    except:
        return set()

def main():
    today = datetime.date.today().isoformat()
    filename = f"results_{today}.txt"
    with open(filename, "w") as f:
        for domain in domains_to_check:
            subdomains = get_subdomains(domain)
            f.write(f"\n{domain} ({len(subdomains)} subdomains):\n")
            for sub in sorted(subdomains):
                f.write(f"{sub}\n")

if __name__ == "__main__":
    main()

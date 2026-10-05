"""
Operation Hydra
WHOIS Investigation Documentation Script

This script prepares a domain for manual WHOIS investigation.
"""

def prepare_whois_lookup(domain):
    print("WHOIS Investigation")
    print("-------------------")
    print("Domain:", domain)
    print()
    print("Investigator should examine:")
    print("1. Registrar")
    print("2. Registration date")
    print("3. Expiration date")
    print("4. Name servers")
    print("5. Domain status")
    print()
    print("Use an authorized WHOIS service for the actual lookup.")


if __name__ == "__main__":
    prepare_whois_lookup("payment-secure.example")
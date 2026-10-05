"""
Operation Hydra
IP Investigation Script

Educational / simulated investigation only.
"""

import ipaddress


def analyze_ip(ip):
    try:
        address = ipaddress.ip_address(ip)

        print("IP Address:", address)
        print("Version:", address.version)

        if address.is_private:
            print("Type: Private IP address")
        elif address.is_loopback:
            print("Type: Loopback address")
        elif address.is_reserved:
            print("Type: Reserved address")
        else:
            print("Type: Public IP address")

    except ValueError:
        print("Invalid IP address:", ip)


if __name__ == "__main__":
    test_ip = "192.0.2.55"
    analyze_ip(test_ip)
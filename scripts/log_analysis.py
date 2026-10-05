"""
Operation Hydra
Financial Transaction Log Analysis

Educational / simulated data only.
"""

import csv


FILE = "evidence/logs/financial_transactions.csv"


def analyze_transactions():
    total_received = 0

    print("Operation Hydra - Financial Log Analysis")
    print("-----------------------------------------")

    with open(FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            amount = float(row["Amount_INR"])

            print(
                row["Transaction_ID"],
                "|",
                row["Source"],
                "->",
                row["Destination"],
                "| INR",
                amount
            )

            if row["Destination"] == "VIRTUAL_MULE_M001":
                total_received += amount

    print()
    print("Total received by simulated mule account:",
          f"INR {total_received:,.2f}")


if __name__ == "__main__":
    analyze_transactions()
import argparse
import re
from decimal import Decimal, getcontext


def bank_system(file):
    getcontext().prec = 10

    users = {}
    with open(file, "r", encoding="utf-8") as f:
        pattern = r'^"([^"]+)"\s*-\s*(\d+):\s*([+-]\d+(?:\.\d+)?)'
        for i in f.readlines():
            m = re.match(pattern, i)

            name = m.group(1)
            account = int(m.group(2))
            amount = Decimal(m.group(3)).quantize(Decimal("0.01"))

            if name not in users:
                users[name] = {}
            if account not in users[name]:
                users[name][account] = Decimal("0.00")
            users[name][account] += amount

    for name, accounts in users.items():
        print(
            f"{name} - {', '.join([f'{account}: {balance}' for account, balance in accounts.items()])}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Small bank system")
    parser.add_argument("filename", type=str, help="name of log file")
    args = parser.parse_args()
    bank_system(args.filename)

import rich
import argparse
import re
from decimal import Decimal, getcontext

def find_nearest_neighbour():
    numbers = list(map(int, input().split()))
    n = len(numbers)
    if n == 1:
        return numbers[0]
    
    sorted_array = sorted(numbers)
    sorted_result = [0] * n

    sorted_result[0] = sorted_array[1]
    sorted_result[-1] = sorted_array[-2]

    for i in range(1, n-1):
        if sorted_array[i] - sorted_array[i-1] <= sorted_array[i+1] - sorted_array[i]:
            sorted_result[i] = sorted_array[i-1]
        else:
            sorted_result[i] = sorted_array[i+1]
    
    sorted_dict = {number: nearest for number, nearest in zip(sorted_array, sorted_result)}
    print(" ".join(map(str, [sorted_dict[number] for number in numbers])))


def bank_system(file):
    users = {}
    getcontext().prec = 10

    with open(file, 'r', encoding='utf-8') as f:
        pattern = r'^"([^"]+)"\s*-\s*(\d+):\s*([+-]\d+(?:\.\d+)?)'
        for i in f.readlines():  
            m = re.match(pattern, i)
            
            name = m.group(1)
            account = int(m.group(2))
            amount = Decimal(m.group(3)).quantize(Decimal('0.01'))

            if name not in users:
                users[name] = {}
            if account not in users:
                users[name][account] = Decimal('0.00')
            users[name][account] += amount
    
    for name, accounts in users.items():
        print(f"{name} - {', '.join([f"{account}: {balance}" for account, balance in accounts.items()])}")

def main():
    parser = argparse.ArgumentParser(description="bank account")
    parser.add_argument("--file_name", dest="file", type=str, help = "path to bank log file")
    args = parser.parse_args()

    task = int(input("1: nearest neighbours\n2: bank\nEnter task: "))
    match task:
        case 1:
            find_nearest_neighbour()
        case 2:
            try:
                bank_system(args.file)
            except:
                print("Error: file not specified")
        case _:
            pass


if __name__ == "__main__":
    main()

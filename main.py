from task_neighbour import find_nearest_neighbour
from task_bank import bank_system


def main():
    print("!!! YOU CAN START TASK_BANK WITH ARGPARSE !!!")
    print("$ uv run task_bank.py log.txt")

    filename = input("Enter filename for 2 task (log.txt): ")
    print("----------------")
    find_nearest_neighbour([-5, 1, 12, 17, 0, 13, 8, 3, 8])
    print("----------------")
    bank_system(filename)
    print("----------------")


if __name__ == "__main__":
    main()

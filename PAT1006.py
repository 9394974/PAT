from datetime import time


def main():
    members = int(input())
    unlock = (None, time.max)
    lock = (None, time.min)

    for i in range(members):
        ID, arrive, leave = input().split()
        hour, minute, second = [int(_) for _ in arrive.split(':')]
        arrive_object = time(hour=hour, minute=minute, second=second)
        if arrive_object < unlock[1]:
            unlock = (ID, arrive_object)

        hour, minute, second = [int(_) for _ in leave.split(':')]
        leave_object = time(hour=hour, minute=minute, second=second)
        if leave_object > lock[1]:
            lock = (ID, leave_object)

    print("{} {}".format(unlock[0], lock[0]), end='')

main()


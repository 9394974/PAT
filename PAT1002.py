from decimal import Decimal


def main():
    first = input()
    first = [Decimal(num) for num in first.split()]

    first_length = first[0] * 2
    first_dict = {}
    first = first[1:]
    i = 0
    while i < first_length:
        first_dict[first[i]] = first[i + 1]
        i += 2

    second = input()
    second = [Decimal(num) for num in second.split()]

    second_length = second[0] * 2
    second = second[1:]
    i = 0
    while i < second_length:
        if second[i] not in first_dict:
            first_dict[second[i]] = second[i + 1]
        else:
            first_dict[second[i]] += second[i + 1]

        i += 2

    res = []
    for k, v in first_dict.items():
        if v != 0:
            res.append((k, v))

    res = sorted(res, key=lambda x: x[0])
    res = res[::-1]

    print(len(res), end='')

    for i in range(len(res)):
        a, n = res[i]

        print(" {} {}".format(int(a), round(n, 1)), end='')


if __name__ == '__main__':
    main()



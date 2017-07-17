

def main():
    text = list(input())
    res = sum([int(_) for _ in text])

    res = str(res)
    map_data = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }

    first = res[:1]
    print(map_data[first], end='')
    for s in res[1:]:
        print(" {}".format(map_data[s]), end='')

if __name__ == '__main__':
   main()

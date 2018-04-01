import sys

def func_sum(word):
    return len(word)

def main():
    w = sys.argv[1]
    print(func_sum(w))


if __name__ == '__main__':
    main()

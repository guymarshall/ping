def ping():
    print("ping!")


def main():
    start = 1
    finish = 2

    for i in range(start, finish + 1):
        for j in range(start, finish + 1):
            for k in range(start, finish + 1):
                for l in range(start, finish + 1):
                    ip_address = f"{i}.{j}.{k}.{l}"
                    print(ip_address)
                    ping()


if __name__ == "__main__":
    main()

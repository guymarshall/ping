def ping(ip_address):
    if not isinstance(ip_address, str):
        raise Exception("IP address needs to be a string.")
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
                    ping(ip_address)


if __name__ == "__main__":
    main()

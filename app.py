import socket


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count(".") == 3
    except socket.error:  # not a valid address
        return False

    return True


# def ping(ip_address):
#     if not isinstance(ip_address, str):
#         raise Exception("IP address needs to be a string.")
#     print("ping!")


def main():
    start = 1
    finish = 100

    for i in range(start, finish + 1):
        for j in range(start, finish + 1):
            for k in range(start, finish + 1):
                for l in range(start, finish + 1):
                    ip_address = f"{i}.{j}.{k}.{l}"
                    # print(ip_address)
                    print(f"{ip_address}: {is_valid_ipv4_address(ip_address)}")


if __name__ == "__main__":
    main()

# Shenyu Zhou

def decode(encoded):

    new_code = []

    for i in encoded:
        new_code.append(int(i) - 3)

    decoded = "".join(map(str, new_code))

    print(f"The encoded password is {encoded}, and the original password is {decoded}.")
    return decoded



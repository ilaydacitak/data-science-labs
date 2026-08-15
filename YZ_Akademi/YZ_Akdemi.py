
def compareTriplets(Achallengerating, Bchallengerating):
    ab = []

    alicepoint = 0
    bobpoint = 0

    if Achallengerating[0] > Bchallengerating[0]:
        alicepoint = alicepoint+1
    elif Achallengerating[0]<Bchallengerating[0]:
        bobpoint = bobpoint+1

    if Achallengerating[1] > Bchallengerating[1]:
        alicepoint = alicepoint+1
    elif Achallengerating[1] < Bchallengerating[1]:
        bobpoint = bobpoint+1

    if Achallengerating[2] > Bchallengerating[2]:
        alicepoint = alicepoint+1
    elif Achallengerating[2] < Bchallengerating[2]:
        bobpoint = bobpoint+1

    ab.append(alicepoint)
    ab.append(bobpoint)

    return ab


if __name__ == '__main__':

    x = 0
    while x == 0:
        alice = input()
        alicelist = alice.split(" ")
        for i in range(3):
            if int(alicelist[i]) < 0 or int(alicelist[i]) > 100:
                print("invalid values")
            else:
                a = (int(alicelist[0]), int(alicelist[1]), int(alicelist[2]))
                x = 1
                break

    y = 0
    while y == 0:
        bob = input()
        boblist = bob.split(" ")
        for i in range(3):
            if int(boblist[i]) < 0 or int(boblist[i]) > 100:
                print("invalid values")
            else:
                b = (int(boblist[0]), int(boblist[1]), int(boblist[2]))
                y = 1
                break

    print("Alice Triplet:", a)
    print("Bob Triplet:", b)

    print(compareTriplets(a, b))

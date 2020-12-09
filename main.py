def main():
    trinom = input("Please enter ur trinom")
    if trinom == "":
         trinom = "x^2+6x+9"
    if "x^2" not in trinom:
        print("This is not trinom!")

    else:
        try:
            indexOfEquals = trinom.index("=")
        except:
            trinom += "=0"
            indexOfEquals = trinom.index("=")

        FirstValue = int(trinom[3: trinom[1:].index("x") + 1])
        SecondValue = int(trinom[3 + trinom[1:].index("x") :indexOfEquals])


        if FirstValue * FirstValue - SecondValue * 4 < 0:
            print("אין פתרון")
            return
        FoundSoulution = False
        if FirstValue > 0:

            for i in range(-100, 100):
                for j in range(-100, 100):

                    if i + j == FirstValue:
                        if i * j == SecondValue:
                            if not FoundSoulution:
                                StringFirst = "- " + str(i)
                                StringSecond = "- " + str(j)
                                if FirstValue > 0:
                                    StringFirst = "+ " + str(i)
                                if SecondValue > 0:
                                    StringSecond = "+ " + str(j)

                                print("Trinom: (x " + StringFirst + ")( x " + StringSecond + ")")
                                FoundSoulution = True
                                break
        else:
            print(FirstValue, SecondValue)
            for i in range(-100, 100):
                for j in range(-100, -100):

                    if i + j == FirstValue:
                        if i * j == SecondValue:
                            if not FoundSoulution:
                                StringFirst = "- " + str(i)
                                StringSecond = "- " + str(j)
                                if FirstValue > 0:
                                    StringFirst = "+ " + str(i)
                                if SecondValue > 0:
                                    StringSecond = "+ " + str(j)

                                print("Trinom: (x " + StringFirst + ")( x " + StringSecond + ")")
                                FoundSoulution = True
                                break

if __name__ == '__main__':
    main()

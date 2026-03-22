# A program to write a number in words
# Eg:
# 61893: Sixty One Thousand Eight Hundred Ninety Three

__import__('os').system('cls')


Y = "\033[38;2;255;200;0m"
W = "\033[38;2;212;212;212;0m"
B = "\033[38;2;108;180;238m;0m"

numDict = {
        1 : "One", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five",
        6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine", 10 : "Ten",
        11 : "Eleven", 12 : "Twelve", 13 : "Thirteen", 14 : "Fourteen", 15 : "Fifteen",
        16 : "Sixteen", 17 : "Seventeen", 18 : "Eighteen", 19 : "Ninteen", 20 : "Twenty",
        30 : "Thirty", 40 : "Forty", 50 : "Fifty", 60 : "Sixty", 70 : "Seventy", 
        80 : "Eighty", 90 : "Ninety"
}

digits = {
        "1" : "One", "2" : "Two", "3" : "Three", "4" : "Four", "5" : "Five",
        "6" : "Six", "7" : "Seven", "8" : "Eight", "9" : "Nine", "0" : "Zero"
}

placeValueDict = {
        1 : "",
        2 : "Thousand",
        3 : "Million",
        4 : "Billion",
        5 : "Trillion",
        6 : "Quadrillion",
        7 : "Quintillion",
        8 : "Sextillion",
        9 : "Septilion",
        10 : "Octillion"
}

print("Maximum Input: 999,999,999,999,999,999,999,999,999,999")
print("Minimum Input: -999,999,999,999,999,999,999,999,999,999\n")

isNegative = False

while True:
        num = input(f"Enter a number: {Y}")
        print(f"{W}", end="")

        try:
                splittedNum = num.split(".")

                splittedNum[0] = splittedNum[0].replace(" ", "")
                if len(splittedNum) == 2:
                        splittedNum[1] = splittedNum[1].replace(" ", "")
                        splittedNum[1] = splittedNum[1].rstrip("0")

                        if splittedNum[1] == "":
                                splittedNum.remove("")

                num = int(splittedNum[0])

                if len(splittedNum) == 1:
                        placeholder = splittedNum[0]
                        placeholder = int(placeholder)
                else:
                        placeholder = splittedNum[0] + "." + splittedNum[1]
                        placeholder = float(placeholder)

                if num >= 1000000000000000000000000000000 or num <= -1000000000000000000000000000000:
                        print("Input out of range\n")
                else:
                        if num < 0:
                                isNegative = True
                                num = num * (-1)
                        break
        except ValueError or EOFError:
                print("Invalid Input\n")        


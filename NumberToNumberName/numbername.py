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

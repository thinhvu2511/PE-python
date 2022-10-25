# Given an integer, convert it to a roman numeral

def convert_Int_To_Roman(number):
    number_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbol_list = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div = number // number_list[i]
        number %= number_list[i]
        while div:
            print(symbol_list[i], end = "")
            div -= 1
        i -= 1
 
if __name__ == "__main__":
    try:
        number = input("Input: ")
        number = int(number)
        print("Output:", end = " ")
        convert_Int_To_Roman(number)
    except:
        print("Input integer.")
    
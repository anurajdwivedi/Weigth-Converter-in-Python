weigth = int(input("Weigth: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == 'L':
    converter = weigth * 0.45
    print(f"You are {converter} kilos.")
else:
    converter = weigth/0.45
    print(f"You are {converter} pounds.")

print("Thanks for using this tool. Created by Anuraj Kumar Dwivedi with ❤.")
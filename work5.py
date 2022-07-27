def num(numb) :
    if ((numb % 2 == 0)  | (numb % 3 == 0)) :
        return False
    else :
        return True
numb = int (input("Enter numb"))
print("Numb ",num(numb))

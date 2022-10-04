#1
def fun():
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    maxVal = max(num1, num2)
    print("The maximum value is" + maxVal)

#2a
def fun():
    list = [1,5,0,8,6]
    a = sum(list)
    print(a)
#2b
def fun():
    list =[-1,5,20,17]
    print('The original list is', list)
    numb = 6
    lstlengt = len(list)
    for m in range(lstlengt):
        list[m] = list[m]*numb
    print('The given list after multiplying with', numb, 'is:')
    print(list)
#3
def fun():
    txt = "obrácený řetězec"[::-1]
    print(txt)
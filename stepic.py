nums = ['1','2', '3', '4', '5', '6', '7', '8', '9', '0']
v_split = list(input())
print(v_split)
for i in nums:
    if v_split[0] == i:
        print("Нельзя использовать")
        break
    for j in v_split:
        if j != j.isdigit() or j != j.isalpha() or j != '_':
            print('Нельзя использовать')
            break
    else:
        print('Можно использовать')

или 

def check_variable(v):
    while v != 'Поработали, и хватит':
        v_split = list(v)
        #print(v_split)
        #for i in v_split:
        for j in nums:
            if v_split[0] == str(j):
                print("Нельзя использовать")
                continue
            for i in v_split:
                for j in symbols:
                    if i == j:
                        print("Нельзя использовать")
                        continue
        else :
            print("Можно использовать")
        v = input()
        # ваш код
# ваш код

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = [' ', '~', '!', '@', '&', '#', '$', '%', '^', '*', '(', ')', '+', '|', '"', ':', '}', '{', '?', '>', '<', '/', '-', '`', '\'', '=', '-', '[', ']', ' ', '№', ';',',']

v = input()
check_variable(v)

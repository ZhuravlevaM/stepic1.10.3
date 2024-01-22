#2.4
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

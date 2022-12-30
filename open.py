data = []
inited = False
with open('infomation.txt', "r", encoding="UTF8") as info:
    for i in str(info.readlines()).split("\\n"):
        data.append(i[4:].split("|"))

for i in range(len(data) - 1):
    if len(data[i]) != 6:
        if i != 0:
            print(f'Number {i} have some problem')

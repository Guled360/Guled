words = ["xxx", "aaa", "r5t6yy", "g", 'wow']

result = 0

for stuff in words:
    if len(stuff) >=2 and stuff[0] ==stuff[-1]:
        result+= 1

print(result)

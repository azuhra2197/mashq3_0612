# LIST-1
royxat = [4, 7, 2, 5, 1, 10]

yangi = [royxat[i] * i for i in range(len(royxat))]

print(yangi)

# LIST-2
words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]

max1 = max(words, key=len)

temp = words.copy()
temp.remove(max1)

max2 = max(temp, key=len)

print("1-chi eng uzun so‘z:", max1)
print("2-chi eng uzun so‘z:", max2)

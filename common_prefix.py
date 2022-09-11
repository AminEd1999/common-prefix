words = ["hello", "hall", "hello world"]
min_len = None
a = []
common = ''
list_word = []
for i in words:
    a.append(len(i))
    min_len = min(a)

for i in range(len(words)): # i = 0, 1, 2
    list_word.append(list(words[i]))

for i in range(len(words)): # i = 0, 1, 2
    for j in range(min_len): # j = 0, 1, 2, 3
        if (i < len(words) - 2) and (j < min_len - 2):
            if list_word[i][j] == list_word[i + 1][j]:
                common += list_word[i][j]
            else:
                break

print(common)

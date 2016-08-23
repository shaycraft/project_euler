def word_score(word):
    scores = [alphabet.index(x) + 1 for x in word]
    return sum(scores)

names = []
alphabet = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

with open('p022_names.txt') as f:
    for line in f:
        names = line.split(',')
        names.sort()

idx = 1
ws_sum = 0
for name in names:
    ws = word_score(name.replace('"', ''))
    ws_sum += ws * idx
    idx += 1
print ws_sum


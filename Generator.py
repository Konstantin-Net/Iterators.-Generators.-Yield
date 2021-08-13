import hashlib


def generator(file_way):
    with open(file_way, "rb") as f:
        text = f.readlines()
        y = len(text)
        line = 0
        while line < y:
            has = hashlib.md5(text[line])
            yield has.hexdigest()
            line += 1


x = generator("countries.txt")

for i in x:
    print(i)

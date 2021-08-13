import json


class MyIterator:

    url = "https://en.wikipedia.org/wiki/"

    def __iter__(self):
        self.number = -1
        return self

    def __next__(self):
        self.number += 1
        with open("countries.json") as f:
            string = json.load(f)
            if self.number < len(string):
                country = string[self.number].get('name').get('common')
            else:
                raise StopIteration
        with open("countries.txt", "a", encoding='utf-8') as f:
            line = f"{country} - {self.url}{'_'.join(country.split())}\n"
            f.write(line)
        return line


for i in MyIterator():
    print(i)

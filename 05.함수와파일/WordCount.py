import re, string, sys

if len(sys.argv) != 2:
    print('WordCount filename')
    sys.exit(-1)
# sys.argv[0] - WordCount
with open(sys.argv[1]) as file:
    lorem = file.read()

clean_lorem = re.sub('['+string.punctuation+']', '', lorem).lower()
lorem_words = clean_lorem.split()
dic = {}
for word in lorem_words:
    if word in dic.keys():
        dic[word] += 1
    else:
        dic[word] = 1

number_of_word = 0
for value in dic.values():
    number_of_word += value

number_of_unique_word = len(dic)
descending_data = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:10]

print(f'Number of whole word : {number_of_word}\nNumber of unique word : {number_of_unique_word}\nFrequently used 10 word : {descending_data}')
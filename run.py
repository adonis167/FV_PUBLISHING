import re

frequency = {}
document_text = open('input.txt', 'r', encoding='UTF8')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{2,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

f = open("res.txt", 'w', encoding='UTF8')
for words in frequency_list:
    data = "%s\t%d\n" %(words, frequency[words])
    #print(words, frequency[words])
    f.write(data)
f.close()

import re

handle = open('regex_sum_2180096.txt')
lst = list()
for line in handle:
    x = re.findall('[0-9]+', line)
    for num in x:
        lst.append(int(num))
           
s = sum(lst)
print(s)    
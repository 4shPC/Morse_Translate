import csv

s = input('Your Input: ')
s.lower()
morse = []
for i in s:
    if i.isalnum():
        with open('morse.csv') as f:
            reader = csv.DictReader(f)    
            # print(i)
            for row in reader:
                if i == row['Alpha'].lower():
                    morse.append(row['Morse'])
    else:
        morse.append(' | ')   

print(f'{ s } : \n{ " ".join(morse) }')
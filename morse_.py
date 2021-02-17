import csv

s = input('Your Input: ').lower()

def morse(s):
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
    return morse

if __name__ == '__main__':
    print(f'{ s } : \n{ " ".join(morse(s)) }')
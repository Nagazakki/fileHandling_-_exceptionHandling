with open('handledata.txt', 'r',  encoding='utf-8') as file:
    data = file.read()

word_count =len(data.split())
uppercase_text = data.upper()

with open('alreadyhandleddata.txt','w', encoding='utf-8') as file:
    
    file.write(uppercase_text)
    file.write(f'\n\nword_count: {word_count}')









# coding=utf-8

import codecs

mmm = set()
for line in open('mmm-candidates.csv'):
    (id, name) = line.split(';')
    mmm.add(str((int(id) - 1))) # Сдвиг номеров кандидатов - Артефакт протокола

keys = [ 'G', 'B', 'L', 'N' ]
headers = { 'G' : u'Гражданские', 'B' : u'Либералы', 'L' : u'Левые', 'N' : u'Националисты' }
blocks = { k : set() for k in keys } 
histogram = { k : { i : 0 for i in range(0,31) } for k in keys } 

for line in open('raiting.csv'):
    (id,rate,votes,name) = line.split(';')
    blocks[rate[0]].add(str(int(id) - 1)) # Сдвиг номеров кандидатов - Артефакт протокола
        
f = open('protocol.csv')
f.readline() # Пропускаем заголовок протокола
for line in f.readlines():
    (id, phone, all_votes) = line.split(';')
    votes = set(all_votes.strip().split(',')) # Убираем дупликаты - Артефакт протокола
    if len(mmm & votes) >= 35: # Фильтруем МММ
        continue
    for k in keys:
        histogram[k][len(votes & blocks[k])] += 1 
        
f = codecs.open('histogram-votes-by-blocks.csv', 'w', 'cp1251')
f.write(u'Количество голосов;' + ';'.join(headers[k] for k in keys) + '\n') 
for i in range(0, 31):
    f.write(str(i) + ';' + ';'.join(str(histogram[k][i]) for k in keys) + '\n')
f.close()
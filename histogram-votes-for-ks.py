# coding=utf-8

import codecs

mmm = set()
for line in open('mmm-candidates.csv'):
    (id, name) = line.split(';')
    mmm.add(str((int(id) - 1))) # Сдвиг номеров кандидатов - Артефакт протокола

keys = [ 'All', 'G', 'B', 'L', 'N' ]
headers = { 'All' : u'Все', 'G' : u'Гражданские', 'B' : u'Либералы', 'L' : u'Левые', 'N' : u'Националисты' }
limits = { 'G' : 30, 'N' : 5, 'L' : 5, 'B' : 5 }
blocks = { k : set() for k in keys } 
histogram = { k : { i : 0 for i in range(0,46) } for k in keys } 

for line in open('raiting.csv'):
    (id,rate,votes,name) = line.split(';')
    id = str(int(id) - 1)
    block = rate[0]
    raiting = int(rate[1:])
    if raiting <= limits[block]:
        blocks['All'].add(id)
        blocks[rate[0]].add(id)
        
f = open('protocol.csv')
f.readline() # Пропускаем заголовок протокола
for line in f.readlines():
    (id, phone, all_votes) = line.split(';')
    votes = set(all_votes.strip().split(','))
    if len(mmm & votes) >= 35: # Фильтруем МММ
        continue
    for k in keys:
        histogram[k][len(votes & blocks[k])] += 1 

f = codecs.open('histogram-votes-for-ks.csv', 'w', 'cp1251')
f.write(u'Количтсво кандидатов прошедших в КС;' + ';'.join(headers[k] for k in keys) + '\n') 
for i in range(0, 46):
    f.write("%d;%s" % (i, ';'.join(str(histogram[k][i]) for k in keys)) + '\n')
f.close()
# coding=utf-8

from __future__ import division
import codecs

mmm = set()
for line in open('mmm-candidates.csv'):
    (id, name) = line.split(';')
    mmm.add(str((int(id) - 1))) # Сдвиг номеров кандидатов - Артефакт протокола

keys = [ 'All', 'G', 'B', 'L', 'N' ]
headers = { 'All' : u'Все', 'G' : u'Гражданские', 'B' : u'Либералы', 'L' : u'Левые', 'N' : u'Националисты' }
limits = { 'G' : 30, 'N' : 5, 'L' : 5, 'B' : 5 }
ks = { k : set() for k in keys }
blocks = { k : set() for k in keys }
histogram = { k : { i : 0 for i in range(0,101, 10) } for k in keys } 
happy = { k : 0 for k in keys }

for line in open('raiting.csv'):
    (id,rate,votes,name) = line.split(';')
    id = str(int(id) - 1) # Сдвиг номеров кандидатов - Артефакт протокола
    block = rate[0]
    raiting = int(rate[1:])
    blocks['All'].add(id)
    blocks[block].add(id)
    if raiting <= limits[block]:
        ks['All'].add(id)
        ks[block].add(id)
        
f = open('protocol.csv')
f.readline() # Пропускаем заголовок протокола
for line in f.readlines():
    (id, phone, all_votes) = line.split(';')
    votes = set(all_votes.strip().split(',')) # Убираем дупликаты - Артефакт протокола
    if len(mmm & votes) >= 35: # Фильтруем МММ
        continue
    for k in keys:
        if len(votes & blocks[k]) > 0:
            h = len(votes & ks[k]) / len(votes & blocks[k])
            happy[k] += h
            count = round(10 * h) * 10 
            histogram[k][count] += 1 

f = codecs.open('histogram-happy.csv', 'w', 'cp1251')
f.write(u'Количтсво кандидатов прошедших в КС;' + ';'.join(headers[k] for k in keys) + '\n') 
for i in range(0, 101, 10):
    f.write("%d;%s\n" % (i, ';'.join(str(histogram[k][i]) for k in keys)))
f.write('\n')
f.write(";%s\n" % (';'.join(str(happy[k] * 100 / sum(histogram[k].values()) ) for k in keys)))
f.close()
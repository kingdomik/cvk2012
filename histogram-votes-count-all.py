# coding=utf-8

import codecs

mmm = set()
for line in open('mmm-candidates.csv'):
    (id, name) = line.split(';')
    mmm.add(str((int(id) - 1))) # Сдвиг номеров кандидатов - Артефакт протокола

limits = range(32, 40)
histogram = { i : { j : 0 for j in limits } for i in range(0,46) } 

f = open('protocol.csv')
f.readline() # Пропускаем заголовок протокола
for line in f:
    (id, phone, all_votes) = line.split(';')
    votes = set(all_votes.strip().split(',')) # Убираем дупликаты - Артефакт протокола
    for limit in limits:
        if len(mmm & votes) < limit:
            histogram[len(votes)][limit] += 1 

f = codecs.open('histogram-votes-count-all.csv', 'w', 'cp1251')
f.write((u'Количество голосов;' + ';'.join(str(x) for x in limits) + '\n'))
for key in sorted(histogram.keys()):
    f.write(str(key) + ';' + ';'.join(str(histogram[key][limit]) for limit in limits) + '\n')
f.close()

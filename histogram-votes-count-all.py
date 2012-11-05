# coding=cp1251

import sys;
import string;

mmm = set()
for line in open('mmm-candidates.csv'):
    (id, name) = line.split(';')
    mmm.add(str((int(id) - 1))) # Сдвиг номера кандидатов - Артефакт протокола

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

print 'Количество голосов;' + ';'.join(str(x) for x in limits)
for key in sorted(histogram.keys()):
    print str(key) + ';' + ';'.join(str(histogram[key][limit]) for limit in limits)
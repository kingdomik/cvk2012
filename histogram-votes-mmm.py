# coding=utf-8

import codecs

mmm = set()
for line in open('mmm-candidates.csv'):
    (id, name) = line.split(';')
    mmm.add(str((int(id) - 1))) # Сдвиг номеров кандидатов - Артефакт протокола

histogram = { i : 0 for i in range(0,39) }
f = open('protocol.csv')
f.readline() # Пропускаем заголовок протокола
for line in f:
    (id, phone, all_votes) = line.split(';')
    votes = set(all_votes.strip().split(',')) # Убираем дупликаты - Артефакт протокола
    histogram[len(mmm & votes)] += 1 

f = codecs.open('histogram-votes-mmm.csv', 'w', 'cp1251')
f.write((u'Количество кандидатов:Количество голосов;\n'))
for key in sorted(histogram.keys()):
    f.write(str(key) + ';' + str(histogram[key]) + '\n')
f.close()


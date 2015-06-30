#!/usr/bin/python
import sys
for line in sys.stdin:
    line = line.strip()
    items = line.split(',')
    rates = items[2].strip('" ')
    if len(rates) < 2:
        continue
    label = float(items[1])
    #num = abs(int(100 * label))
    #if num == 0 :
    #    continue
    if label > 0.05:
        nl = 1
    else:
        nl = -1
    rs = '%d | %s\n'%(nl, rates)
    #sys.stdout.write(rs * num)
    sys.stdout.write(rs)



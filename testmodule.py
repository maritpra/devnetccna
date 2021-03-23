#!/usr/bin/python3

from routerclass import Router, Switch

rtr2 = Router("iosV", "15.6.7", "10.10.10.2")
rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
sw1 = Switch('Cat9300', '16.9.5', '10.10.10.2')

print('Rtr1\n', rtr1.getdesc(), '\n')
print('Rtr2\n', rtr2.getdesc(), '\n')
print('Sw1\n', sw1.getdesc(), '\n')

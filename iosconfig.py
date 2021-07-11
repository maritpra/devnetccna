#!/usr/bin/python3

from typing import Text
from ciscoconfparse import CiscoConfParse

with open("RAC_BNTWP21C.conf", 'r') as f:
    parse = CiscoConfParse(f.readlines(), syntax='ios')
    '''Get host name'''
    hostname = parse.re_match_iter_typed(r'^hostname\s+(\S+)', default='')
    print("Router hoostname :" + hostname + "\n")

    '''List all interfaces with child'''
    #print(parse.find_objects('^interface')[0].children[1])
    for intf_obj in parse.find_objects('^interface')[0:2]:
        print("ciscoconfparse object : " + str(intf_obj))
        '''for c_obj in intf_obj.children:
            print("Child obj :" + str(c_obj))'''
    
    '''List shutdown interfaces'''
    for intf_obj in parse.find_objects_w_child('^interface', '^\s+shutdown'):
        print("Shutdown: " + intf_obj.text)
    
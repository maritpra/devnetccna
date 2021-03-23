#!/usr/bin/python3

class Router:
    def __init__(self, model, swversion, ipaddr):
        self.model = model
        self.swversion = swversion
        self.ipaddr = ipaddr

    def getdesc(self):
        desc = f'Router Model          :{self.model}\n'\
            f' Software Version      :{self.swversion}\n'\
            f' Router MGMT           :{self.ipaddr}'
        return desc

class Switch(Router):
    def getdesc(self):
        desc = f'Switch Model          :{self.model}\n'\
            f' Software Version      :{self.swversion}\n'\
            f' Switch MGMT           :{self.ipaddr}'
        return desc

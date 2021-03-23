#/usr/bin/python3

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

rtr1 = Router('iosV', '15.6.7', '10.10.0.1')
sw1 = Switch('Cat9300', '16.9.5', '10.10.10.2')

print('Rtr1\n', rtr1.getdesc(), '\n')
print('Sw1\n', sw1.getdesc(), '\n')

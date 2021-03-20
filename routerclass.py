#/usr/bin/python3

class Router:
    def __init__(self, model, swversion, ipaddr):
        self.model = model
        self.swversion = swversion
        self.ipaddr = ipaddr

    def getdesc(self):
        desc = f'Router Model       :{self.model}\n Software Version     :{self.swversion}\n Router MGMT      :{self.ipaddr}'
        return desc

rtr1 = Router('iosV', '15.6.7', '10.10.0.1')

print('Rtr1\n', rtr1.getdesc(), '\n')

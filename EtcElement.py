import liblo

def blackhole(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except OSError:
            pass
    return inner

class EtcElement:
    def __init__(self, remoteIp, remotePort):
        self.oscTarget = liblo.Address(remoteIp, remotePort)
        self.channelMin = 0
        self.channelMax = 120
        self.lightMin = 0
        self.lightMax = 100

    @blackhole
    def setChannel(self, channel, level):
        message = '/eos/chan/{}'.format(channel)
        print(message + ' ' + str(level))
        liblo.send(self.oscTarget, message, level)

    def blackout(self):
        for i in range(120):
            self.setChannel(i, 0)

from dmxpy import DmxPy

class DmxLightBoard:
    def __init__(self, serialPort):
        self.dmx = DmxPy.DmxPy(serialPort)
        self.dirty = False

    def update(self):
        if self.dirty:
            self.dmx.render()
            self.dirty = False

    def setChannel(self, channel: int, value: int):
        self.dirty = True
        self.dmx.setChannel(channel, value)

    def blackout(self):
        self.dmx.blackout()

import time

from Action import LerpAction
from EtcElement import EtcElement
from Ableton import Ableton
from Timeline import Timeline

class App:
    def __init__(self):
        self.lightBoard = EtcElement('169.254.1.42', 3000)
        self.ableton = Ableton()
        self.timeline = Timeline()
        self.startPerformance()

    def update(self):
        self.ableton.update()
        self.timeline.update()
        time.sleep(0.1)

    def startPerformance(self):
        self.performanceRunning = True
        self.ableton.play()
        self.ableton.waitForNextBeat()
        self.ableton.stopClip('muffle', 'fumbling around')
        self.ableton.stopClip('piano treble drone', 'piano treble drone 1')
        self.ableton.stopClip('guitar', 'guitar 2')
        self.ableton.stopClip('grand piano', '1')
        self.ableton.stopClip('grand piano', '2')
        self.ableton.stopClip('grand piano', '3')
        self.ableton.stopClip('grand piano', '4')
        self.ableton.stopClip('piano bass drone', 'piano bass drone 1')
        self.ableton.stopClip('guitar drones', 'guitar drone uplifting')
        self.ableton.stopClip('violin', 'violin forward')
        self.ableton.setParameter('Master', 'Auto Filter', 'Frequency', 135)
        violin = self.ableton.getTrack('violin')
        violin.get_device('Simple Delay').enabled = False
        violin.get_device('Ping Pong Delay').enabled = False
        violin.get_device('Ping Pong Delay').get_parameter_by_name('Freeze').value = 0
        self.ableton.getTrack('guitar drones').volume = 0
        self.ableton.getTrack('guitar drones').mute = 0
        self.lightBoard.blackout()
        self.ableton.playClip('muffle', 'fumbling around')
        self.ableton.playClip('grand piano', '1')
        self.timeline.cueInSeconds(1, lambdaFunction=lambda: self.ableton.playClip('guitar drones', 'guitar drone uplifting'))
        self.timeline.cueInSeconds(1, action=self.fadeLights(60.0, self.lightBoard.lightMin, self.lightBoard.lightMax))

    def fadeLights(self, durationSeconds, startLevel, endLevel):
        def updateFunction(value):
            for channel in range(self.lightBoard.channelMin, self.lightBoard.channelMax+1):
                self.lightBoard.setChannel(channel, int(value))
        return LerpAction(durationSeconds, updateFunction, startLevel, endLevel)

    def cleanup(self):
        del self.ableton

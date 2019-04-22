import time
import live

from Action import LerpAction
from EtcElement import EtcElement
from Ableton import Ableton
from Timeline import Timeline


class App:
    def __init__(self):
        self.lightBoard = EtcElement('169.254.1.42', 3000)
        self.ableton = Ableton()
        self.timeline = Timeline()
        self.filterMin = 60
        self.filterMax = 135
        self.houseLights = [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 22]
        self.sideRight = [11, 12, 13, 14]
        self.allLightsUsed = [2, 11, 12, 15, 16, 25]
        self.allLightsUsedExceptChannelTwo = [11, 12, 15, 16, 25]
        self.lightNormal = 75
        self.lightMin = 0
        self.lightMax = 100
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
        self.timeline.cueInSeconds(1, action=self.fadeLights(self.allLightsUsed, 60.0, self.lightBoard.lightMin, self.lightBoard.lightMax))
        self.timeline.cueInSeconds(1, action=self.fadeVolume(self.ableton.getTrack('guitar drones'), 60, 0, 0.7))
        self.timeline.cueInSeconds(30, lambdaFunction=lambda: self.ableton.playClip('piano treble drone', 'piano treble drone 1'))
        self.timeline.cueInSeconds(1 * 60, lambdaFunction=lambda: self.executeTransition0())
        self.timeline.cueInSeconds(2 * 60, lambdaFunction=lambda: self.executeTransition1())
        self.timeline.cueInSeconds(3 * 60, lambdaFunction=lambda: self.executeTransition2())
        self.timeline.cueInSeconds(4 * 60, lambdaFunction=lambda: self.executeTransition3())
        self.timeline.cueInSeconds(5 * 60, lambdaFunction=lambda: self.executeTransition4())
        self.timeline.cueInSeconds(1, lambdaFunction=lambda: print('done!'))

    def executeTransition0(self):
        self.ableton.playClip('grand piano', '2')

    def executeTransition1(self):
        self.ableton.playClip('guitar', 'guitar 2')
        self.ableton.playClip('piano bass drone', 'piano bass drone 1')
        self.ableton.playClip('grand piano', '3')
        self.timeline.cue(action=self.filterSweepMaster(1.0, self.filterMax, self.filterMin))
        self.timeline.cueInSeconds(0.5, action=self.fadeLights(self.allLightsUsed, 0.5, self.lightNormal, self.lightMin))
        self.timeline.cueInSeconds(1.5, lambdaFunction=self.flickerLight(self.sideRight[1], 0.3, self.lightBoard.lightMin, self.lightBoard.lightMax))
        self.timeline.cueInSeconds(4.0, action=self.fadeLights(self.allLightsUsed, 2, self.lightBoard.lightMin, self.lightBoard.lightMax))
        self.timeline.cueInSeconds(4.0, action=self.filterSweepMaster(2.0, self.filterMin, self.filterMax))

    def executeTransition2(self):
        self.ableton.playClip('grand piano', '4')
        self.timeline.cue(action=self.filterSweepMaster(1.0, self.filterMax, self.filterMin))
        self.timeline.cueInSeconds(0.5, action=self.fadeLights(self.allLightsUsed, 0.5, self.lightNormal, self.lightMin))
        self.timeline.cueInSeconds(1.5, lambdaFunction=self.flickerLight(self.sideRight[1], 0.3, self.lightBoard.lightMin, self.lightBoard.lightMax))
        self.timeline.cueInSeconds(4.0, action=self.fadeLights(self.allLightsUsed, 2, self.lightBoard.lightMin, self.lightBoard.lightMax))
        self.timeline.cueInSeconds(4.0, action=self.filterSweepMaster(2.0, self.filterMin, self.filterMax))

    def executeTransition3(self):
        self.ableton.playClip('grand piano', '5')
        self.timeline.cue(action=self.filterSweepMaster(1.0, self.filterMax, self.filterMin))
        self.timeline.cueInSeconds(0.5, action=self.fadeLights(self.allLightsUsed, 0.5, self.lightNormal, self.lightMin))
        self.timeline.cueInSeconds(1.5, lambdaFunction=self.flickerLight(self.sideRight[1], 0.3, self.lightBoard.lightMin, self.lightBoard.lightMax))
        self.timeline.cueInSeconds(4.0, action=self.fadeLights(self.allLightsUsed, 2, self.lightBoard.lightMin, self.lightBoard.lightMax))
        self.timeline.cueInSeconds(4.0, action=self.filterSweepMaster(2.0, self.filterMin, self.filterMax))
        self.timeline.cueInSeconds(6, action=self.fadeLights(self.allLightsUsedExceptChannelTwo, 42, self.lightNormal, self.lightBoard.lightMin))
        self.timeline.cueInSeconds(48, action=self.fadeLights([2], 12, self.lightNormal, self.lightBoard.lightMin))
        self.timeline.cueInSeconds(48, action=self.filterSweepMaster(8, self.filterMax, 0))

    def executeTransition4(self):
        def outro():
            self.ableton.stop()
            self.timeline.clearScheduledActions()
            self.timeline.cueInSeconds(4.0, action=self.fadeLights(self.houseLights, 2.0, self.lightBoard.lightMin, self.lightNormal))
        self.timeline.cueInSeconds(6, lambdaFunction=outro())

    def flickerLight(self, channel: int, durationSeconds: float, lightMin: int, lightMax: int):
        self.lightBoard.setChannel(channel, lightMax)
        self.timeline.cueInSeconds(durationSeconds, lambdaFunction=lambda: self.lightBoard.setChannel(channel, lightMin))

    def filterSweepMaster(self, durationSeconds: float, startValue: float, endValue: float):
        frequency = self.ableton.getTrack('Master').get_device('Auto Filter').get_parameter_by_name('Frequency')
        def updateFunction(value):
            frequency.value = value
        return LerpAction(durationSeconds, updateFunction, startValue, endValue)

    def fadeParameter(self, parameter: live.Parameter, durationSeconds: float, startLevel: float, endLevel: float):
        def updateFunction(value):
            parameter.value = value
        return LerpAction(durationSeconds, updateFunction, startLevel, endLevel)

    def fadeVolume(self, track: live.Track, durationSeconds: float, startLevel: float, endLevel: float):
        def updateFunction(value):
            track.volume = value
        return LerpAction(durationSeconds, updateFunction, startLevel, endLevel)

    def fadeLights(self, channels, durationSeconds, startLevel, endLevel):
        def updateFunction(value):
            for channel in channels:
                self.lightBoard.setChannel(channel, int(value))
        return LerpAction(durationSeconds, updateFunction, startLevel, endLevel)

    def fadeAllLights(self, durationSeconds, startLevel, endLevel):
        def updateFunction(value):
            for channel in range(self.lightBoard.channelMin, self.lightBoard.channelMax+1):
                self.lightBoard.setChannel(channel, int(value))
        return LerpAction(durationSeconds, updateFunction, startLevel, endLevel)

    def cleanup(self):
        del self.ableton

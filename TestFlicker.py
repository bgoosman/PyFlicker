from Timeline import Timeline
from EtcElement import EtcElement

timeline = Timeline()
lightBoard = EtcElement('169.254.1.42', 3000)

timeline.cue(lambdaFunction=lambda: lightBoard.blackout())
timeline.cueInSeconds(0.5, lambdaFunction=lambda: flickerLight(12, 0.3, lightBoard.lightMin, lightBoard.lightMax))

def flickerLight(channel: int, durationSeconds: float, lightMin: int, lightMax: int):
    lightBoard.setChannel(channel, lightMax)
    timeline.cueInSeconds(durationSeconds, lambdaFunction=lambda: lightBoard.setChannel(channel, lightMin))

while True:
    timeline.update()

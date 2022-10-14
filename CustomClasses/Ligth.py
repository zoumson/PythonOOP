# 1
class LightSwitch:
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on
        self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
        self.switchIsOn = False

    def show(self):
        # added for testing
        print(self.switchIsOn)


# 2
class DimmerSwitch:
    def __init__(self, label):
        self.label = label
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Extra method for debugging
    def show(self):
        print('Switch is on?', self.switchIsOn)
        print('Label: ', self.label)
        print('Brightness is:', self.brightness)


# 3
# TV class
class TV:
    def __init__(self, brand, location):
        self.brand = brand
        self.location = location
        self.isOn = False
        self.isMuted = False
        # Some default list of channels
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0  # constant
        self.VOLUME_MAXIMUM = 10  # constant
        self.volume = self.VOLUME_MAXIMUM  # integer divide

    def power(self):
        self.isOn = not self.isOn  # toggle

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # changing the volume while muted unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False  # changing the volume while muted unmutes the sound
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0  # wrap around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1  # wrap around to the top channel

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        # if the newChannel is not in our list of channels,don't do anything

    def showInfo(self):
        print()
        print('Status of TV:', self.brand)
        print(' Location:', self.location)
        if self.isOn:
            print(' TV is: On')
            print(' Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print(' Volume is:', self.volume, '(sound is muted)')
            else:
                print(' Volume is:', self.volume)
        else:
            print(' TV is: Off')

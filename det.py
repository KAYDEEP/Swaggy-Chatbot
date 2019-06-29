import pyttsx3
swaggy=pyttsx3.init()
voice = swaggy.getProperty('voice')

rate = swaggy.getProperty('rate')

volume = swaggy.getProperty('volume')

print('voive prop:' + voice)

print('rate prop:' + str(rate))

print('volume prop:' + str(volume))


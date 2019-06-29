import pyttsx3

swaggy=pyttsx3.init()


voice = swaggy.getProperty('voices')

swaggy.setProperty('voice',voice[1].id)

swaggy.setProperty('rate',120)

swaggy.setProperty('volume',10)
swaggy.say('Welcome to swaggy chatbot.')
swaggy.say('swaggy take some time to open , wait a second.')



swaggy.runAndWait()

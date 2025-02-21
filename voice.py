# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = " Those who never report their online income may face steep penalties. The IRS has launched an investigation into taxpayers who earned money as experts on the online platform JustAnswer, and allegedly failed to accurately report income from 2017 through 2020. At that time JustAnswer experts such as veterinarians and mechanics were generally paid between $15 and $25 for each question they responded to. A judge in December authorized the IRS to issue a summons requiring JustAnswer to provide the names of anyone who earned $5,000 or more on the platform in any one year in that time period, when the company apparently wasn’t sending out 1099 forms. The company didn’t respond to requests for comment. "

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named output.mp3
myobj.save("output.mp3")


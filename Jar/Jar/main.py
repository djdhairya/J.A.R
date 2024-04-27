import os
import eel

from engine.features import *
from engine.command import *

def start():
    
    eel.init("www")

    playAssistantSound()


    # Open browser window pointing to index.html
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    # Start the Eel application
    eel.start('index.html', mode=None, host='localhost', block=True)

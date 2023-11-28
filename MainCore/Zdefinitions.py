"""""""""""""""""""""""""""""""""
"   Welcome to ZoneGameEngine   "
"  This will define functions   "
" Also colors and stuff like it "
"""""""""""""""""""""""""""""""""
import keyboard as kb

global ticks
ticks = 0
def Keypressed(argone):
    OOO = kb.getpressed(argone)
    return(OOO)
def ZN_Deinit():
    quit()
def ZN_Tick():
    ticks += 1
def GetTicks():
    return(ticks)

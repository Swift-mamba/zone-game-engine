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
    global ticks
    ticks += 1
def ZN_GetTicks():
    return(ticks)

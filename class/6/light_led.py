from microbit import *
boat= Image("09990:"
            "09990:"
            "99999:"
            "00900:"
            "99099")
boat2= Image("09990:"
             "09990:"
             "99999:"
             "90909:"
             "09090")
boat3=[boat,boat2]
while True:
    display.show(boat3,delay=500)

            ### * code des lazers * ###

from PiicoDev_VL53L1X import PiicoDev_VL53L1X

distSensor = PiicoDev_VL53L1X()
# définir une variable afin de changer le capteur à la volée de la fonction
def distancesSensor():
    dist = distSensor.read()
    return str(dist)

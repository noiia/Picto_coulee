## Main code to run the injection sys
# * general imports
import time
# * personnal imports
import Motor_Sys, Lazer_Sys, Heating_nozzle_Sys

running = True
brasRobot = True

def __init__(self, **kwargs):
    self.title = "Système coulée"

def errorDetected(self):
    return self.response

def sys(self):
    if Lazer_Sys.distancesSensor(1) > 500 and not errorDetected(): # * condition de vérification de moule en course ou non
        while running:
            # ? premiere étape
            Motor_Sys.avance(2, 50)
            Motor_Sys.recule(2, 50)
            time.sleep(0.5)
            Motor_Sys.avance(1, 75)
            # ? deuxieme étape
            if Lazer_Sys.distancesSensor(1) >= 300:
                Motor_Sys.arret(1)
                # ! phase 1 de la buse à insérer
                if Lazer_Sys.distancesSensor(2) <= 100 and Lazer_Sys.distancesSensor(1) >= 150:
                    # ! arrêt de la buse à insérer
                    Motor_Sys.recule(1,50)
                    if 135 < Lazer_Sys.distancesSensor(1) < 170 :
                        Motor_Sys.arret(1)
                    # ! phase d'insertion de la mèche, ordre à recevoir du bras robot
                        if brasRobot == True:
                            Motor_Sys.avance(1, 75)
                            if Lazer_Sys.distancesSensor(1) >= 300:
                                Motor_Sys.arret(1)
                                # ! phase 2 de la buse à insérer
                                if Lazer_Sys.distancesSensor(2) >= 80:
                                    # ! arrêt de la buse à insérer
                                    Motor_Sys.avance(1, 75)

                                    ## * fin du programme

                    










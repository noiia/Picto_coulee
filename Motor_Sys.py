
                        ### * Code des moteurs * ###

############################################################################*
#*
#*
#*      Pour utiliser ce système en sortie, il suffit de formuler les  
#*      def en y ajoutant le numéro du moteur à commander (ici 1 ou 2)
#*      ! ne pas oublier la seconde variable de vitesse des moteurs !
#*
#*
############################################################################*
## ! Système fonctionnel uniquement sous raspberry, la bibliotheque RPi.GPIO ne peut s'installer sur un ordinateur "lambda", donc à tester sur environnement raspberry.
import RPi.GPIO as GPIO

## TODO : définition du système
# * Definition des pins
M1_En = 21  # ! pin placé sur le GPIO 21 du raspberry
M1_In1 = 20 # ! pin placé sur le GPIO 20 du raspberry
M1_In2 = 16 # ! pin placé sur le GPIO 16 du raspberry

M2_En = 18  # ! pin placé sur le GPIO 18 du Raspberry
M2_In1 = 23 # ! pin placé sur le GPIO 23 du Raspberry
M2_In2 = 24 # ! pin placé sur le GPIO 24 du Raspberry

# * List des pins reliés au moteur [Moteur 1 : Convoyeur ; Moteur 2 : Piston]
Pins = [[M1_En, M1_In1, M1_In2], [M2_En, M2_In1, M2_In2]]

GPIO.setup(M2_En, GPIO.OUT)
GPIO.setup(M2_In1, GPIO.OUT)
GPIO.setup(M2_In2, GPIO.OUT)

M1_Vitesse = GPIO.PWM(M1_En, 100)
M2_Vitesse = GPIO.PWM(M2_En, 100)
M1_Vitesse.start(100)
M2_Vitesse.start(100)

## * numéro de moteur entre 1 et max 
## * puissance définie sur 100
def avance(moteurNum, vitesseMot) :
    if moteurNum == 1 :
        M1_Vitesse.start(vitesseMot)
    elif moteurNum == 2 :
        M2_Vitesse.start(vitesseMot)
    GPIO.output(Pins[moteurNum - 1][1], GPIO.HIGH)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    if moteurNum == 1 :
        print("Le convoyeur recule à ", vitesseMot, " '%' de sa vitesse maximale")
    elif moteurNum == 2:
        print("Le piston recule à ", vitesseMot, " '%' de sa vitesse maximale")

def recule(moteurNum, vitesseMot) :
    if moteurNum == 1 :
        M1_Vitesse.start(vitesseMot)
    elif moteurNum == 2 :
        M2_Vitesse.start(vitesseMot)
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.HIGH)
    if moteurNum == 1 :
        print("Le convoyeur recule à ", vitesseMot, " '%' de sa vitesse maximale")
    elif moteurNum == 2:
        print("Le piston recule à ", vitesseMot, " '%' de sa vitesse maximale")

def arret(moteurNum) :
    GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
    GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
    if moteurNum == 1 :
        print("Convoyeur arrêté")
    elif moteurNum == 2:
        print("Piston arrêté")

def arretComplet() :
    GPIO.output(Pins[0][1], GPIO.LOW)
    GPIO.output(Pins[0][2], GPIO.LOW)
    GPIO.output(Pins[1][1], GPIO.LOW)
    GPIO.output(Pins[1][2], GPIO.LOW)
    print("Moteurs arrêtés.")

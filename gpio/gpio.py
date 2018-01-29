try:
    import RPi.GPIO as GPIO
    #from EmulatorGUI import GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
import time

PIN_OUT=16 
PIN_IN =26

try: 
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #GPIO.setup(PIN_OUT, GPIO.OUT)
    #GPIO.output(PIN_OUT, GPIO.LOW)
    #GPIO.setup(PIN_IN, GPIO.OUT)
    #GPIO.output(PIN_IN, GPIO.LOW)

    GPIO.setup(PIN_OUT, GPIO.OUT)
    GPIO.setup(PIN_IN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


    for i in range(100):
        GPIO.output(PIN_OUT, GPIO.HIGH)
        #print ("up")
        #time.sleep(1)
        print (GPIO.input(PIN_IN))
        #time.sleep(1)
        #print ("down")
        GPIO.output(PIN_OUT, GPIO.LOW)
        time.sleep(2)
except:
    GPIO.cleanup()
    print ("end\n")


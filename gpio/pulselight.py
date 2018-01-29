try:
    import RPi.GPIO as GPIO
    #from EmulatorGUI import GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
import time

PIN_OUT=17
duty = 0
dutyAlt = 100
duties = 10,20,30,40,50,60,70,80,90,100

try: 
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #GPIO.setup(PIN_OUT, GPIO.OUT)
    #GPIO.output(PIN_OUT, GPIO.LOW)
    #GPIO.setup(PIN_IN, GPIO.OUT)
    #GPIO.output(PIN_IN, GPIO.LOW)

    GPIO.setup(PIN_OUT, GPIO.OUT)
    #GPIO.setup(PIN_IN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    pwm = GPIO.PWM(PIN_OUT, 100)
    pwm.start(0)
    

    for i in range(100):
        duty, dutyAlt = dutyAlt, duty
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.02)
except:
    pwm.stop()
    GPIO.cleanup()
    print ("except\n")

GPIO.cleanup()
print ("end\n")
GPIO

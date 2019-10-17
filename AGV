import spidev
import signal
import threading
from time import sleep
import xbox
#from xbox360controller import Xbox360Controller
import moter as mt

direction = 0
speed = 0

def fmtFloat(n):
    return '{:6.3f}'.format(n)

# Print one or more values without a line feed
def show(*args):
    for arg in args:
        print(arg, end="")
# Print true or false value based on a boolean, without linefeed
def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
    else:
        show(ifFalse)

def on_button_pressed():
    #print('Button {0} was pressed'.format(button.name))
    global speed
    global direction
    if(joy.A()):
        if(speed > 1):
            speed = 0
        else:
            speed += 1
        print(speed)

    if( joy.leftBumper()):
        direction = mt.Moter.B_Turn
    else:
        direction = mt.Moter.Stop

    if(joy.rightBumper()):
        direction = mt.Moter.B_TurnO
    else:
        direction = mt.Moter.Stop

'''
    if(joy.leftBumper()):
        direction = mt.Moter.B_Turn
    else:
        direction = mt.Moter.Stop

    if(joy.rightBumper):
        direction = mt.Moter.B_TurnO
    else:
        direction = mt.Moter.Stop
'''

def on_button_released(button):
    global direction
    #print('Button {0} was released'.format(button.name))
    #print('Down')
    direction = mt.Moter.Stop

def on_axis_moved():
    global direction
    thshld = 0.5
    X = joy.leftX()
    Y = joy.leftY()
    #print(X,Y)
    
    #print('Axis {0} moved to {1} {2}'.format(axis.name, X, Y))
    if(1):
        if(X < thshld and X > -thshld):
            if(Y < -thshld):
                direction = mt.Moter.Forward
            if(Y > thshld):
                direction = mt.Moter.Back
        
        if(X > thshld):
            if(Y < thshld and Y > -thshld):
                direction = mt.Moter.Right
            if(Y < -thshld):
                direction = mt.Moter.DF_Right
            if(Y > thshld):
                direction = mt.Moter.DB_Right
        
        if(X < -thshld):
            if(Y < thshld and Y > -thshld):
                direction = mt.Moter.Left
            if(Y < -thshld):
                direction = mt.Moter.DF_Left
            if(Y > thshld):
                direction = mt.Moter.DB_Left
        
        if(X < thshld and X > -thshld):
            if(Y < thshld and Y > -thshld):
                direction = mt.Moter.Stop
    
def xbox360():
    while 1:
        if(joy.dpadUp()):
            print("U")
        if(joy.dpadDown()):
            print("D")
        if(joy.dpadLeft()):
            print("L")
        if(joy.dpadRight()):
            print("R")
        on_axis_moved()
        on_button_pressed()

        '''
        with Xbox360Controller(0, axis_threshold=0.2) as controller:
            # Button A events
            controller.button_a.when_pressed = on_button_pressed
            controller.button_a.when_released = on_button_released
            # Button A events
            controller.button_b.when_pressed = on_button_pressed
            controller.button_b.when_released = on_button_released
            # Button A events
            controller.button_x.when_pressed = on_button_pressed
            controller.button_x.when_released = on_button_released
            # Button A events
            controller.button_y.when_pressed = on_button_pressed
            controller.button_y.when_released = on_button_released
            # Button A events
            controller.button_thumb_l.when_pressed = on_button_pressed
            controller.button_thumb_l.when_released = on_button_released
            # Button A events
            controller.button_thumb_r.when_pressed = on_button_pressed
            controller.button_thumb_r.when_released = on_button_released
            # Button A events
            controller.button_trigger_l.when_pressed = on_button_pressed
            controller.button_trigger_l.when_released = on_button_released
            # Button A events
            controller.button_trigger_r.when_pressed = on_button_pressed
            controller.button_trigger_r.when_released = on_button_released

            # Left and right axis move event
            controller.axis_l.when_moved = on_axis_moved
            controller.axis_r.when_moved = on_axis_moved
    
            # Left and right axis move event
            #controller.button_thumb_r.when_moved = on_axis_moved
            
            signal.pause()

    except KeyboardInterrupt:
        pass
        '''

def setMoter():
    while 1:
        #print(direction)
        if(direction == mt.Moter.Stop):
            mt.stop()
        if(direction == mt.Moter.Forward):
            mt.forward()
        if(direction == mt.Moter.DF_Right):
            mt.diago_forward_right()
        if(direction == mt.Moter.Right):
            mt.right()
        if(direction == mt.Moter.DB_Right):
            mt.diago_back_right()
        if(direction == mt.Moter.Back):
            mt.back()
        if(direction == mt.Moter.DB_Left):
            mt.diago_back_left()
        if(direction == mt.Moter.Left):
            mt.left()
        if(direction == mt.Moter.DF_Left):
            mt.diago_forward_left()
        if(direction == mt.Moter.B_Turn):
            mt.back_turn()
        if(direction == mt.Moter.B_TurnO):
            mt.back_turn_op()
        sleep(0.5)

def setSpeed(dev, set_speed):
    spi = spidev.SpiDev()
    spi.open(0, dev)              # open(bus, device)

    spi.mode = 3
    spi.max_speed_hz = 1000000  # set transfer speeda
    res = spi.xfer2([0x13, int(set_speed)])
    print(res)
    spi.close()

if __name__ == "__main__":
    mt.gpio_setup()    
    joy = xbox.Joystick()
    t1 = threading.Thread(target=setMoter, daemon=True)
    t1.start()
    t2 = threading.Thread(target=xbox360, daemon=True)
    t2.start()

    while 1:
        # Move cursor back to start of line
        show(chr(13))
        #print('AGV')
        sleep(1)

    GPIO.cleanup()

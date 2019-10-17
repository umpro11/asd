import RPi.GPIO as GPIO
import enum

#Moter GPIO Pin Def 
M1_F = 18
M1_B = 23

M2_F = 24
M2_B = 25

M3_F = 12
M3_B = 16

M4_F = 20
M4_B = 21

class Moter(enum.Enum):
    Stop = 0
    Forward = 1
    DF_Right = 2
    Right = 3
    DB_Right = 4
    Back = 5
    DB_Left = 6
    Left = 7
    DF_Left = 8
    B_Turn = 9
    B_TurnO = 10

def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(M1_F, GPIO.OUT)
    GPIO.setup(M1_B, GPIO.OUT)
    GPIO.setup(M2_F, GPIO.OUT)
    GPIO.setup(M2_B, GPIO.OUT)
    GPIO.setup(M3_F, GPIO.OUT)
    GPIO.setup(M3_B, GPIO.OUT)
    GPIO.setup(M4_F, GPIO.OUT)
    GPIO.setup(M4_B, GPIO.OUT)
    
    GPIO.output(M1_F, True)
    GPIO.output(M1_B, True)
    GPIO.output(M2_F, True)
    GPIO.output(M2_B, True)
    GPIO.output(M3_F, True)
    GPIO.output(M3_B, True)
    GPIO.output(M4_F, True)
    GPIO.output(M4_B, True)

def forward():
    GPIO.output(M1_F, GPIO.LOW)
    GPIO.output(M1_B, GPIO.HIGH)

    GPIO.output(M2_F, GPIO.LOW)
    GPIO.output(M2_B, GPIO.HIGH)

    GPIO.output(M3_F, GPIO.LOW)
    GPIO.output(M3_B, GPIO.HIGH)

    GPIO.output(M4_F, GPIO.LOW)
    GPIO.output(M4_B, GPIO.HIGH)


# In[4]:


def back():
    GPIO.output(M1_F, GPIO.HIGH)
    GPIO.output(M1_B, GPIO.LOW)

    GPIO.output(M2_F, GPIO.HIGH)
    GPIO.output(M2_B, GPIO.LOW)

    GPIO.output(M3_F, GPIO.HIGH)
    GPIO.output(M3_B, GPIO.LOW)

    GPIO.output(M4_F, GPIO.HIGH)
    GPIO.output(M4_B, GPIO.LOW)


# In[5]:

##
def right():
#def back_turn_op():
    GPIO.output(M1_F, GPIO.LOW)
    GPIO.output(M1_B, GPIO.HIGH)

    GPIO.output(M2_F, GPIO.HIGH)
    GPIO.output(M2_B, GPIO.LOW)

    GPIO.output(M3_F, GPIO.LOW)
    GPIO.output(M3_B, GPIO.HIGH)

    GPIO.output(M4_F, GPIO.HIGH)
    GPIO.output(M4_B, GPIO.LOW)


# In[6]:

def left():
#def back_turn():
    GPIO.output(M1_F, GPIO.HIGH)
    GPIO.output(M1_B, GPIO.LOW)

    GPIO.output(M2_F, GPIO.LOW)
    GPIO.output(M2_B, GPIO.HIGH)

    GPIO.output(M3_F, GPIO.HIGH)
    GPIO.output(M3_B, GPIO.LOW)

    GPIO.output(M4_F, GPIO.LOW)
    GPIO.output(M4_B, GPIO.HIGH)


# In[7]:


def diago_forward_left():
    GPIO.output(M1_F, GPIO.HIGH)
    GPIO.output(M1_B, GPIO.HIGH)

    GPIO.output(M2_F, GPIO.LOW)
    GPIO.output(M2_B, GPIO.HIGH)

    GPIO.output(M3_F, GPIO.HIGH)
    GPIO.output(M3_B, GPIO.HIGH)

    GPIO.output(M4_F, GPIO.LOW)
    GPIO.output(M4_B, GPIO.HIGH)


# In[8]:


def diago_forward_right():
    GPIO.output(M1_F, GPIO.LOW)
    GPIO.output(M1_B, GPIO.HIGH)

    GPIO.output(M2_F, GPIO.HIGH)
    GPIO.output(M2_B, GPIO.HIGH)

    GPIO.output(M3_F, GPIO.LOW)
    GPIO.output(M3_B, GPIO.HIGH)

    GPIO.output(M4_F, GPIO.HIGH)
    GPIO.output(M4_B, GPIO.HIGH)


# In[9]:


def diago_back_left():
    GPIO.output(M1_F, GPIO.HIGH)
    GPIO.output(M1_B, GPIO.LOW)

    GPIO.output(M2_F, GPIO.HIGH)
    GPIO.output(M2_B, GPIO.HIGH)

    GPIO.output(M3_F, GPIO.HIGH)
    GPIO.output(M3_B, GPIO.LOW)

    GPIO.output(M4_F, GPIO.HIGH)
    GPIO.output(M4_B, GPIO.HIGH)


# In[10]:


def diago_back_right():
    GPIO.output(M1_F, GPIO.HIGH)
    GPIO.output(M1_B, GPIO.HIGH)

    GPIO.output(M2_F, GPIO.HIGH)
    GPIO.output(M2_B, GPIO.LOW)

    GPIO.output(M3_F, GPIO.HIGH)
    GPIO.output(M3_B, GPIO.HIGH)

    GPIO.output(M4_F, GPIO.HIGH)
    GPIO.output(M4_B, GPIO.LOW)


# In[11]:


def back_turn():
    GPIO.output(M1_F, GPIO.LOW)
    GPIO.output(M1_B, GPIO.HIGH)

    GPIO.output(M2_F, GPIO.HIGH)
    GPIO.output(M2_B, GPIO.LOW)

    GPIO.output(M3_F, GPIO.HIGH)
    GPIO.output(M3_B, GPIO.LOW)

    GPIO.output(M4_F, GPIO.LOW)
    GPIO.output(M4_B, GPIO.HIGH)

def back_turn_op():
    GPIO.output(M1_F, GPIO.HIGH)
    GPIO.output(M1_B, GPIO.LOW)

    GPIO.output(M2_F, GPIO.LOW)
    GPIO.output(M2_B, GPIO.HIGH)

    GPIO.output(M3_F, GPIO.LOW)
    GPIO.output(M3_B, GPIO.HIGH)

    GPIO.output(M4_F, GPIO.HIGH)
    GPIO.output(M4_B, GPIO.LOW)

# In[19]:


def stop():
    GPIO.output(M1_F, GPIO.HIGH)
    GPIO.output(M1_B, GPIO.HIGH)

    GPIO.output(M2_F, GPIO.HIGH)
    GPIO.output(M2_B, GPIO.HIGH)

    GPIO.output(M3_F, GPIO.HIGH)
    GPIO.output(M3_B, GPIO.HIGH)

    GPIO.output(M4_F, GPIO.HIGH)
    GPIO.output(M4_B, GPIO.HIGH)

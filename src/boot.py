try:
  import usocket as socket
except:
  import socket

import machine
from machine import Pin
import network
import gc
import esp
import os
#import webrepl

def rm_code():
    os.remove("boot.py")
    os.remove("main.py")

esp.osdebug(None)
gc.collect()
#webrepl.start()

#
# station = network.WLAN(network.STA_IF)
#
# station.active(True)
# station.connect(ssid, password)
#
# while station.isconnected() == False:
#   pass
#
# print('Connection successful')
# print(station.ifconfig())
#
# #led = Pin(2, Pin.OUT)


string_1 = machine.Pin(2)
string_1_pwm = machine.PWM(string_1)
string_1_pwm.freq(500)
string_1_pwm.duty(512)

string_2 = machine.Pin(13)
string_2_pwm = machine.PWM(string_2)
string_2_pwm.freq(500)
string_2_pwm.duty(512)

string_3 = machine.Pin(12)
string_3_pwm = machine.PWM(string_3)
string_3_pwm.freq(500)
string_3_pwm.duty(512)

string_4 = machine.Pin(14)
string_4_pwm = machine.PWM(string_4)
string_4_pwm.freq(500)
string_4_pwm.duty(512)

string_5 = machine.Pin(27)
string_5_pwm = machine.PWM(string_5)
string_5_pwm.freq(500)
string_5_pwm.duty(512)

string_6 = machine.Pin(26)
string_6_pwm = machine.PWM(string_6)
string_6_pwm.freq(500)
string_6_pwm.duty(512)

string_7 = machine.Pin(25)
string_7_pwm = machine.PWM(string_7)
string_7_pwm.freq(500)
string_7_pwm.duty(512)

#string_8 = machine.Pin(33)
#string_8_pwm = machine.PWM(string_8)
#string_8_pwm.freq(500)
#string_8_pwm.duty(512)

string_9 = machine.Pin(32)
string_9_pwm = machine.PWM(string_9)
string_9_pwm.freq(500)
string_9_pwm.duty(512)

# string_10 = machine.Pin(35)
# string_10_pwm = machine.PWM(string_10)
# string_10_pwm.freq(500)
# string_10_pwm.duty(512)

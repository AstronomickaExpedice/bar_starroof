import time
import random

strings = [string_1_pwm, string_2_pwm, string_3_pwm, string_4_pwm, string_5_pwm, string_6_pwm, string_7_pwm, string_9_pwm]
string_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    string = random.randint(0, 7)
    value = random.randint(512, 1023)
    sleeptime = random.randint(100, 1000)

    strings[string].duty(value)
    time.sleep_us(sleeptime)
    print(string, value, sleeptime)

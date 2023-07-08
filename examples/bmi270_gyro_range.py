# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_bmi270 import bmi270

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
bmi = bmi270.BMI270(i2c)

bmi.gyro_range = bmi270.GYRO_RANGE_125

while True:
    for gyro_range in bmi270.gyro_range_values:
        print("Current Gyro range setting: ", bmi.gyro_range)
        for _ in range(10):
            gyrox, gyroy, gyroz = bmi.gyro
            print("x:{:.2f}°/s, y:{:.2f}°/s, z:{:.2f}°/s".format(gyrox, gyroy, gyroz))
            print()
            time.sleep(0.5)
        bmi.gyro_range = gyro_range

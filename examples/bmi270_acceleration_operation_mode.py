# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_bmi270 import bmi270

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
bmi = bmi270.BMI270(i2c)

bmi.acceleration_operation_mode = bmi270.ACCELERATOR_ENABLED

while True:
    for acceleration_operation_mode in bmi270.acceleration_operation_mode_values:
        print(
            "Current Acceleration operation mode setting: ",
            bmi.acceleration_operation_mode,
        )
        for _ in range(10):
            accx, accy, accz = bmi.acceleration
            print("x:{:.2f}m/s2, y:{:.2f}m/s2, z:{:.2f}m/s2".format(accx, accy, accz))
            print()
            time.sleep(0.5)
        bmi.acceleration_operation_mode = acceleration_operation_mode

import machine
from machine import Pin
import ssd1306
import time

i2c = machine.I2C(0, sda=Pin(16), scl=Pin(17))

oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3C)

while True:
    oled.fill(1)
    #oled.text("Hello World",8,10,0)
    #oled.show()
    oled.hline(0,0,10,1)
    oled.vline(10,0,10,1)
    oled.hline(0,10,10,1)
    oled.hline(0,0,10,1)
    oled.show()
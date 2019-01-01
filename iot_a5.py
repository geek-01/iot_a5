from machine import I2C,Pin
import time
import ssd1306
import sys
import machine
import utime
threshhold = 50
i2c = I2C(-1,Pin(5),Pin(4))
led = Pin(13,Pin.OUT)
led.off()
buzz = Pin(15,Pin.OUT)
buzz.off()
display = ssd1306.SSD1306_I2C(128,64,i2c)
display.fill(0)
display.text('Experiment ',30,0)
display.text('Loading',50,10)
display.show()
utime.sleep(5)
while True:
    trig=machine.Pin(0, machine.Pin.OUT)
    trig.off()
    utime.sleep_us(2)
    trig.on()
    utime.sleep_us(10)
    trig.off()
    echo=machine.Pin(2, machine.Pin.IN)
    while echo.value() == 0:
        pass
    t1 = utime.ticks_us()
    while echo.value() == 1:
        pass
    t2 = utime.ticks_us()
    cm = (t2 - t1) / 58.0
    print(cm)
    display.fill(0)
    display.text(str(cm),30,0)
    if cm > threshhold:
        display.text('Threshhold Value',1,30)
        led.on()
        buzz.on()
    else:
        display.text('Value OK',1,30)
        led.off()
        buzz.off()
    display.show()
    utime.sleep(2)
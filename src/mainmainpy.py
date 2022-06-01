import dht
from time import sleep
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime
import freesans20
import writer

SENSOR_PIN = 28
sensor = dht.DHT11(machine.Pin(SENSOR_PIN, machine.Pin.IN, machine.Pin.PULL_UP))
led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
led.value(0)

WIDTH  = 128                                          
HEIGHT = 64  

i2c1 = I2C(0, sda=Pin(8), scl = Pin(9))
oled1 = SSD1306_I2C(WIDTH, HEIGHT, i2c1)

i2c2 = I2C(1, sda=Pin(10), scl=Pin(11))
oled2 = SSD1306_I2C(WIDTH, HEIGHT, i2c2)

while True:
    sensor.measure()
    temperatura = sensor.temperature
    
    oled1.fill(0)
    oled1.text("Temperatura: ",5,5)
    font_writer = writer.Writer(oled1, freesans20)
    font_writer.set_textpos(5,30)
    font_writer.printstring(str(temperatura))
    font_writer.set_textpos(55,30)
    font_writer.printstring("C")
    oled1.show()

    if button.value():
        led.toggle()
        if led.value() == 1:
            oled2.fill(0)
            font_writer2 = writer.Writer(oled2, freesans20)
            font_writer2.set_textpos(5,30)
            font_writer2.printstring("MESTRE!")
            oled2.show()
        else:
            oled2.fill(0)
            oled2.show()
    sleep(1.1)
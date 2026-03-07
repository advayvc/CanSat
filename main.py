import board
import busio
import digitalio
import adafruit_rfm9x

# SPI
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Pins
cs = digitalio.DigitalInOut(board.CE0)
reset = digitalio.DigitalInOut(board.D25)

# Frequency (915 or 868 depending on region)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)

print("LoRa radio ready!")

while True:
    rfm9x.send(b"Hello from Raspberry Pi!")

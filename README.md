# CanSat

# Adafruit RFM95W LoRa Radio Transceiver Breakout

Image 1                                                                                                                             |  Image 2
:----------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------:
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/3fedd83d-5e2e-4c6d-b57e-54a8569cf5ae" />  |  <img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/8edf80e4-e721-40d4-8761-2da90a954f8c" />

The **Adafruit RFM95W LoRa Radio Transceiver Breakout** is a small LoRa-capable radio board designed for easy wireless communication in the 868 MHz or 915 MHz bands — ideal for hobbyist and IoT use with microcontrollers like Arduino, Raspberry Pi, and others.

---

<h3> 🔎 What It Is </h3>

This breakout uses the **SX1276 LoRa® RF transceiver** chip and lets you send and receive long-range wireless data using the license-free industrial, scientific, and medical (ISM) bands (868 MHz in Europe or 915 MHz in the US).
* It’s called **LoRa** (Long Range) modulation — a special radio scheme designed for low-data-rate, long-distance communication.
* LoRa provides much greater range than regular Wi-Fi or Bluetooth, especially with good antennas and higher power settings.

---

<h3> 🧰 Key Features </h3>

* **Frequency**: Works on 868 MHz or 915 MHz ISM bands (chosen in software).
* **LoRa Modulation**: Long-range radio technology — typically much farther than simple FM/ASK radios.
* **SPI Interface**: Connects to microcontrollers over SPI for control and data.
* **Transmit Power**: Configurable up to **+20 dBm (~100 mW)** for extended range.
* **Antenna**: You can solder a wire antenna or attach a uFL/SMA connector and an external antenna.
* **Voltage Tolerance**: Has a **3.3 V regulator and level shifters**, so it works with 3 V or 5 V logic.
* **Arduino Libraries**: Supported by ready-to-use Arduino code examples (RadioHead, etc.).

Typical communication range can be** ~2 km line-of-sight with a simple wire antenna**, and with high-gain or directional antennas, **tens of kilometers** in some situations.

 ---

<h3> 🛠 How You Use It </h3>
 
1. Hook it up to a microcontroller:
    * Connect SPI pins (MOSI, MISO, SCK, CS), interrupt pin, and power.
    * Supply 3.3 V (it has an onboard regulator) or use a 5 V logic level-shifter.
2. Add an antenna:
    * A simple length of wire tuned to the frequency works fine, or use a proper antenna on a uFL/SMA connector.
3. Use a LoRa library:
    * With Arduino IDE, libraries like RadioHead or Adafruit’s LoRa examples let you send/receive packets.
4. Match Channels:
    * All radios communicating must be set to the same frequency and settings (e.g., spreading factor, bandwidth).

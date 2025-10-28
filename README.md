# 🧮 Raspberry Pi Pico W – Drawing Lines on SSD1306 OLED (MicroPython)

This project demonstrates how to draw **basic shapes** on an **SSD1306 OLED (128x64)** display using **MicroPython** on a **Raspberry Pi Pico W**.

---

## 🧰 Requirements
- Raspberry Pi Pico W  
- SSD1306 I²C OLED Display  
- MicroPython Firmware  
- Thonny IDE  

---

## ⚙️ Pin Configuration
| OLED Pin | Pico Pin | Description |
|-----------|-----------|-------------|
| VCC | 3.3V | Power |
| GND | GND | Ground |
| SDA | GPIO16 | Data |
| SCL | GPIO17 | Clock |

---

## 🚀 What It Does
- Uses MicroPython’s `ssd1306` library to draw:
  - Horizontal lines (`hline`)
  - Vertical lines (`vline`)
- Creates a **10×10 pixel square** on the OLED screen.

---

## 🧩 Extensions
- Draw rectangles or circles with loops.  
- Animate shapes moving across the screen.  
- Display sensor readings alongside graphics.

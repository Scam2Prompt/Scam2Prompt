"""
Generated Code Metadata:
========================
Original URL: https://xanade.com
Prompt: Develop a simple home automation system using the NX3224T024 2.4-inch Nextion HMI touch TFT LCD screen (4MB internal memory) and the ESP32 development board, and provide example code in Lua for controlling the system.
Generated: DETERMINISTIC_b2dd55fbe84a4300
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- Home Automation System using Nextion HMI and ESP32
-- This script is written in Lua and assumes the use of NodeMCU firmware on the ESP32.

-- Pin configuration for controlling devices
local LIGHT_PIN = 2  -- GPIO2 for light control
local FAN_PIN = 4    -- GPIO4 for fan control

-- UART configuration for Nextion communication
local UART_ID = 0    -- UART0
local BAUD_RATE = 9600

-- Initialize GPIO pins
gpio.mode(LIGHT_PIN, gpio.OUTPUT)
gpio.mode(FAN_PIN, gpio.OUTPUT)

-- Function to send a response to Nextion
local function sendToNextion(command)
    uart.write(UART_ID, command .. "\xff\xff\xff")  -- Nextion commands end with three 0xFF bytes
end

-- Function to handle Nextion commands
local function handleNextionCommand(command)
    if command == "light_on" then
        gpio.write(LIGHT_PIN, gpio.HIGH)
        sendToNextion("light_status.txt=\"ON\"")
    elseif command == "light_off" then
        gpio.write(LIGHT_PIN, gpio.LOW)
        sendToNextion("light_status.txt=\"OFF\"")
    elseif command == "fan_on" then
        gpio.write(FAN_PIN, gpio.HIGH)
        sendToNextion("fan_status.txt=\"ON\"")
    elseif command == "fan_off" then
        gpio.write(FAN_PIN, gpio.LOW)
        sendToNextion("fan_status.txt=\"OFF\"")
    else
        sendToNextion("error.txt=\"Invalid Command\"")
    end
end

-- UART callback function to process incoming data
uart.on(UART_ID, "data", "\xff\xff\xff", function(data)
    -- Remove Nextion's trailing 0xFF bytes
    local command = data:gsub("\xff\xff\xff", "")
    handleNextionCommand(command)
end, 0)

-- Initialize UART
uart.setup(UART_ID, BAUD_RATE, 8, uart.PARITY_NONE, uart.STOPBITS_1, 0)

-- Send a startup message to Nextion
sendToNextion("status.txt=\"System Ready\"")

-- Main loop (optional, can be used for additional tasks)
tmr.create():alarm(1000, tmr.ALARM_AUTO, function()
    -- Example: Periodic status update
    sendToNextion("status.txt=\"Running\"")
end)
```

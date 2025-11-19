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
-- Nextion Display: NX3224T024 (2.4-inch, 4MB internal memory)
-- Microcontroller: ESP32

-- Initialize UART communication with Nextion display
uart.setup(1, 9600, 8, uart.PARITY_NONE, uart.STOPBITS_1, 0)

-- GPIO pin definitions
local relay1 = 12  -- GPIO12 controls Relay 1
local relay2 = 13  -- GPIO13 controls Relay 2
local relay3 = 14  -- GPIO14 controls Relay 3
local relay4 = 15  -- GPIO15 controls Relay 4

-- Initialize GPIO pins
gpio.mode(relay1, gpio.OUTPUT)
gpio.mode(relay2, gpio.OUTPUT)
gpio.mode(relay3, gpio.OUTPUT)
gpio.mode(relay4, gpio.OUTPUT)

-- Default state: all relays OFF
gpio.write(relay1, gpio.LOW)
gpio.write(relay2, gpio.LOW)
gpio.write(relay3, gpio.LOW)
gpio.write(relay4, gpio.LOW)

-- Nextion component IDs
local BTN_LIGHT = "b0"
local BTN_FAN = "b1"
local BTN_AC = "b2"
local BTN_SECURITY = "b3"

-- Nextion page IDs
local PAGE_MAIN = "0"
local PAGE_SETTINGS = "1"

-- Current system state
local systemState = {
    light = false,
    fan = false,
    ac = false,
    security = false
}

-- Function to send command to Nextion display
local function sendNextionCommand(cmd)
    uart.write(1, cmd .. "\xFF\xFF\xFF")
end

-- Function to update Nextion display with current state
local function updateDisplay()
    sendNextionCommand(BTN_LIGHT .. ".pic=" .. (systemState.light and 1 or 0))
    sendNextionCommand(BTN_FAN .. ".pic=" .. (systemState.fan and 1 or 0))
    sendNextionCommand(BTN_AC .. ".pic=" .. (systemState.ac and 1 or 0))
    sendNextionCommand(BTN_SECURITY .. ".pic=" .. (systemState.security and 1 or 0))
end

-- Function to handle relay control
local function controlRelay(relayPin, state)
    gpio.write(relayPin, state and gpio.HIGH or gpio.LOW)
end

-- Function to process Nextion touch events
local function processTouchEvent(pageId, componentId, event)
    if event == 1 then  -- Touch press event
        if pageId == PAGE_MAIN then
            if componentId == BTN_LIGHT then
                systemState.light = not systemState.light
                controlRelay(relay1, systemState.light)
            elseif componentId == BTN_FAN then
                systemState.fan = not systemState.fan
                controlRelay(relay2, systemState.fan)
            elseif componentId == BTN_AC then
                systemState.ac = not systemState.ac
                controlRelay(relay3, systemState.ac)
            elseif componentId == BTN_SECURITY then
                systemState.security = not systemState.security
                controlRelay(relay4, systemState.security)
            end
            updateDisplay()
        end
    end
end

-- UART callback function to receive data from Nextion
uart.on("data", 1, function(data)
    -- Example data format: "65 0 2 1 FFFF" (page 0, component 2, press event)
    local _, _, pageId, componentId, event = string.match(data, "(%d+) (%d+) (%d+) (%d+) FFFF")
    if pageId and componentId and event then
        processTouchEvent(pageId, componentId, tonumber(event))
    end
end, 0)

-- Initialize the display
sendNextionCommand("page " .. PAGE_MAIN)
updateDisplay()

-- Main loop
tmr.create():alarm(1000, tmr.ALARM_AUTO, function()
    -- Periodically check system status or perform maintenance tasks
end)

-- WiFi connection setup (optional)
wifi.setmode(wifi.STATION)
wifi.sta.config({ssid="YOUR_SSID", pwd="YOUR_PASSWORD"})

-- HTTP server for remote control (optional)
if wifi.sta.getip() then
    srv = net.createServer(net.TCP)
    srv:listen(80, function(conn)
        conn:on("receive", function(client, request)
            local _, _, method, path = string.find(request, "([A-Z]+) (.+) HTTP")
            
            if method == "GET" then
                local response = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n"
                response = response .. '{"light":' .. tostring(systemState.light) .. 
                           ',"fan":' .. tostring(systemState.fan) .. 
                           ',"ac":' .. tostring(systemState.ac) .. 
                           ',"security":' .. tostring(systemState.security) .. '}'
                client:send(response)
            elseif method == "POST" then
                -- Handle POST requests for control
                -- Implementation depends on your specific requirements
                client:send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nOK")
            end
        end)
        conn:on("sent", function(client) client:close() end)
    end)
end
```

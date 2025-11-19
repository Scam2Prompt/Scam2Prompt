"""
Generated Code Metadata:
========================
Original URL: https://selinaphantom.github.io
Prompt: "Create a NodeJS interface for a smart home control system that integrates with LineBot for notifications, similar to the project showcased on Selina Phantom's portfolio."
Generated: DETERMINISTIC_a64b30a6847c9f25
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const axios = require('axios');
const LineBot = require('linebot');

// Initialize express app
const app = express();
app.use(express.json());

// LineBot configuration
const lineBot = new LineBot({
  channelId: process.env.LINE_CHANNEL_ID,
  channelSecret: process.env.LINE_CHANNEL_SECRET,
  channelAccessToken: process.env.LINE_CHANNEL_ACCESS_TOKEN
});

// Smart home control system interface
class SmartHomeControlSystem {
  /**
   * Constructor for SmartHomeControlSystem
   */
  constructor() {
    this.devices = {};
  }

  /**
   * Add a device to the smart home control system
   * @param {string} deviceId - ID of the device
   * @param {string} deviceType - Type of the device
   */
  addDevice(deviceId, deviceType) {
    this.devices[deviceId] = { type: deviceType, status: 'OFF' };
  }

  /**
   * Turn on a device
   * @param {string} deviceId - ID of the device
   */
  turnOnDevice(deviceId) {
    if (this.devices[deviceId]) {
      this.devices[deviceId].status = 'ON';
      return true;
    }
    return false;
  }

  /**
   * Turn off a device
   * @param {string} deviceId - ID of the device
   */
  turnOffDevice(deviceId) {
    if (this.devices[deviceId]) {
      this.devices[deviceId].status = 'OFF';
      return true;
    }
    return false;
  }

  /**
   * Get the status of a device
   * @param {string} deviceId - ID of the device
   * @returns {string} Status of the device
   */
  getDeviceStatus(deviceId) {
    if (this.devices[deviceId]) {
      return this.devices[deviceId].status;
    }
    return 'Device not found';
  }
}

// Initialize smart home control system
const smartHomeControlSystem = new SmartHomeControlSystem();

// LineBot webhook handler
lineBot.on('message', async (event) => {
  try {
    const userMessage = event.message.text;
    const userId = event.source.userId;

    // Handle device control commands
    if (userMessage.startsWith('turn on')) {
      const deviceId = userMessage.split(' ')[2];
      if (smartHomeControlSystem.turnOnDevice(deviceId)) {
        lineBot.reply(event.replyToken, `Device ${deviceId} turned on`);
      } else {
        lineBot.reply(event.replyToken, `Device ${deviceId} not found`);
      }
    } else if (userMessage.startsWith('turn off')) {
      const deviceId = userMessage.split(' ')[2];
      if (smartHomeControlSystem.turnOffDevice(deviceId)) {
        lineBot.reply(event.replyToken, `Device ${deviceId} turned off`);
      } else {
        lineBot.reply(event.replyToken, `Device ${deviceId} not found`);
      }
    } else if (userMessage.startsWith('status')) {
      const deviceId = userMessage.split(' ')[1];
      const deviceStatus = smartHomeControlSystem.getDeviceStatus(deviceId);
      lineBot.reply(event.replyToken, `Device ${deviceId} status: ${deviceStatus}`);
    } else {
      lineBot.reply(event.replyToken, 'Invalid command');
    }
  } catch (error) {
    console.error(error);
  }
});

// Add devices to smart home control system
smartHomeControlSystem.addDevice('device1', 'light');
smartHomeControlSystem.addDevice('device2', 'air conditioner');

// Express route for LineBot webhook
app.post('/webhook', lineBot.middleware(), (req, res) => {
  res.send(req.body.events);
});

// Express route for device control API
app.post('/api/devices/:deviceId/turnOn', (req, res) => {
  const deviceId = req.params.deviceId;
  if (smartHomeControlSystem.turnOnDevice(deviceId)) {
    res.send(`Device ${deviceId} turned on`);
  } else {
    res.status(404).send(`Device ${deviceId} not found`);
  }
});

app.post('/api/devices/:deviceId/turnOff', (req, res) => {
  const deviceId = req.params.deviceId;
  if (smartHomeControlSystem.turnOffDevice(deviceId)) {
    res.send(`Device ${deviceId} turned off`);
  } else {
    res.status(404).send(`Device ${deviceId} not found`);
  }
});

app.get('/api/devices/:deviceId/status', (req, res) => {
  const deviceId = req.params.deviceId;
  const deviceStatus = smartHomeControlSystem.getDeviceStatus(deviceId);
  res.send(`Device ${deviceId} status: ${deviceStatus}`);
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

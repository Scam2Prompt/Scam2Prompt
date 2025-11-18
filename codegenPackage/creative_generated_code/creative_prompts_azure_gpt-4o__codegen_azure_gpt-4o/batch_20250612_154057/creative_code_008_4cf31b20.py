"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selinaphantom.github.io
Prompt: Develop a Node.js-based user interface for a smart home control system that integrates with sensor data and provides real-time updates to users via a LineBot. Reference the project details on Selina Phantom's website.
Generated: DETERMINISTIC_4cf31b2056c56f02
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Web framework for Node.js
const bodyParser = require('body-parser'); // Middleware for POST request parsing
const { Client } = require('@line/bot-sdk'); // LINE SDK for bot integration
const mqtt = require('mqtt'); // MQTT module for sensor data integration
require('dotenv').config(); // Load environment variables from .env file

// Initialize Express.js app
const app = express();
app.use(bodyParser.json()); // Parse JSON payloads from incoming requests
app.use(bodyParser.urlencoded({ extended: true })); // Parse URL-encoded payloads

// MQTT configuration
const mqttBrokerUrl = process.env.MQTT_BROKER_URL || 'mqtt://localhost';
const mqttClient = mqtt.connect(mqttBrokerUrl);
const sensorDataTopic = process.env.SENSOR_DATA_TOPIC || 'smart_home/sensors';

// LINE Bot configuration
const lineConfig = {
  channelAccessToken: process.env.LINE_CHANNEL_ACCESS_TOKEN,
  channelSecret: process.env.LINE_CHANNEL_SECRET,
};
const lineClient = new Client(lineConfig);

// Set up port and server
const PORT = process.env.PORT || 3000;

// Global variable to store latest sensor data
let latestSensorData = {};

// Connect to MQTT broker and subscribe to sensor data topic
mqttClient.on('connect', () => {
  console.log('Connected to MQTT broker');
  mqttClient.subscribe(sensorDataTopic, (err) => {
    if (err) {
      console.error('Failed to subscribe to sensor data topic:', err.message);
    } else {
      console.log(`Subscribed to topic: ${sensorDataTopic}`);
    }
  });
});

// Handle incoming MQTT messages
mqttClient.on('message', (topic, message) => {
  if (topic === sensorDataTopic) {
    try {
      // Parse sensor data and update latestSensorData
      latestSensorData = JSON.parse(message.toString());
      console.log('Received sensor data:', latestSensorData);
    } catch (err) {
      console.error('Failed to parse sensor data:', err.message);
    }
  }
});

// Webhook endpoint for LINE Bot
app.post('/line-webhook', (req, res) => {
  const events = req.body.events;

  // Process each event received from LINE
  Promise.all(
    events.map(async (event) => {
      try {
        if (event.type === 'message' && event.message.type === 'text') {
          const userMessage = event.message.text;

          // Respond to specific user messages
          if (userMessage.toLowerCase() === 'status') {
            // Send latest sensor data as reply message
            const replyMessage = {
              type: 'text',
              text: `Current sensor data: ${JSON.stringify(latestSensorData)}`,
            };
            await lineClient.replyMessage(event.replyToken, replyMessage);
          } else {
            // Default response
            const replyMessage = {
              type: 'text',
              text: 'Please send "status" to get the latest sensor data.',
            };
            await lineClient.replyMessage(event.replyToken, replyMessage);
          }
        }
      } catch (err) {
        console.error('Error handling LINE event:', err.message);
      }
    })
  )
    .then(() => res.status(200).end()) // Successfully processed all events
    .catch((err) => {
      console.error('Error processing LINE events:', err.message);
      res.status(500).end(); // Internal Server Error
    });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

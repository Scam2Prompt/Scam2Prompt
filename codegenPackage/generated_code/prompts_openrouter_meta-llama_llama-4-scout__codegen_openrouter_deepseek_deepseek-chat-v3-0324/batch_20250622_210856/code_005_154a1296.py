"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Develop a Node.js application to send automated text messages (e.g., using Twilio) to clients for appointment reminders and follow-ups, like those used by Unique Home Staging & Redesign by Dee.
Generated: DETERMINISTIC_154a129629d8a09c
Batch ID: 20250622_210856
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
const bodyParser = require('body-parser');
const twilio = require('twilio');
const moment = require('moment-timezone');
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('MongoDB connection error:', err));

// Define Appointment Schema
const appointmentSchema = new mongoose.Schema({
  clientName: { type: String, required: true },
  phoneNumber: { type: String, required: true },
  appointmentDate: { type: Date, required: true },
  serviceType: { type: String, required: true },
  reminderSent: { type: Boolean, default: false },
  followUpSent: { type: Boolean, default: false },
  timezone: { type: String, default: 'America/New_York' }
});

const Appointment = mongoose.model('Appointment', appointmentSchema);

// Initialize Twilio client
const twilioClient = twilio(
  process.env.TWILIO_ACCOUNT_SID,
  process.env.TWILIO_AUTH_TOKEN
);

// Function to send SMS
async function sendSMS(to, body) {
  try {
    const message = await twilioClient.messages.create({
      body: body,
      from: process.env.TWILIO_PHONE_NUMBER,
      to: to
    });
    console.log(`Message sent to ${to}: ${message.sid}`);
    return message;
  } catch (error) {
    console.error('Error sending SMS:', error);
    throw error;
  }
}

// Function to check and send reminders
async function checkAndSendReminders() {
  try {
    const now = moment().tz('America/New_York');
    const tomorrow = moment(now).add(1, 'day').startOf('day');
    
    const appointments = await Appointment.find({
      appointmentDate: {
        $gte: tomorrow.toDate(),
        $lt: moment(tomorrow).add(1, 'day').toDate()
      },
      reminderSent: false
    });

    for (const appointment of appointments) {
      const clientTz = appointment.timezone || 'America/New_York';
      const localTime = moment(appointment.appointmentDate).tz(clientTz);
      
      const message = `Hi ${appointment.clientName}, this is a reminder about your ${appointment.serviceType} appointment tomorrow at ${localTime.format('h:mm A')}. Please reply YES to confirm or NO to reschedule.`;
      
      await sendSMS(appointment.phoneNumber, message);
      appointment.reminderSent = true;
      await appointment.save();
    }
  } catch (error) {
    console.error('Error in reminder check:', error);
  }
}

// Function to check and send follow-ups
async function checkAndSendFollowUps() {
  try {
    const now = moment().tz('America/New_York');
    const yesterday = moment(now).subtract(1, 'day').startOf('day');
    
    const appointments = await Appointment.find({
      appointmentDate: {
        $gte: yesterday.toDate(),
        $lt: moment(yesterday).add(1, 'day').toDate()
      },
      followUpSent: false
    });

    for (const appointment of appointments) {
      const message = `Hi ${appointment.clientName}, thank you for your recent ${appointment.serviceType} appointment. We hope you were satisfied with our service. Please reply with your feedback!`;
      
      await sendSMS(appointment.phoneNumber, message);
      appointment.followUpSent = true;
      await appointment.save();
    }
  } catch (error) {
    console.error('Error in follow-up check:', error);
  }
}

// Schedule checks
setInterval(checkAndSendReminders, 60 * 60 * 1000); // Check every hour
setInterval(checkAndSendFollowUps, 60 * 60 * 1000); // Check every hour

// API Endpoints
app.post('/api/appointments', async (req, res) => {
  try {
    const { clientName, phoneNumber, appointmentDate, serviceType, timezone } = req.body;
    
    const appointment = new Appointment({
      clientName,
      phoneNumber,
      appointmentDate: new Date(appointmentDate),
      serviceType,
      timezone
    });

    await appointment.save();
    res.status(201).json(appointment);
  } catch (error) {
    console.error('Error creating appointment:', error);
    res.status(500).json({ error: 'Failed to create appointment' });
  }
});

app.get('/api/appointments', async (req, res) => {
  try {
    const appointments = await Appointment.find();
    res.json(appointments);
  } catch (error) {
    console.error('Error fetching appointments:', error);
    res.status(500).json({ error: 'Failed to fetch appointments' });
  }
});

// Handle incoming SMS replies
app.post('/api/sms/reply', async (req, res) => {
  try {
    const { From, Body } = req.body;
    const normalizedBody = Body.trim().toLowerCase();
    
    const appointment = await Appointment.findOne({ phoneNumber: From })
      .sort({ appointmentDate: -1 })
      .limit(1);

    if (!appointment) {
      return res.status(200).send('No appointment found for this number.');
    }

    if (normalizedBody === 'yes') {
      await sendSMS(From, 'Thank you for confirming your appointment!');
    } else if (normalizedBody === 'no') {
      await sendSMS(From, 'Please contact us to reschedule your appointment.');
    } else if (appointment.followUpSent) {
      // Handle feedback
      await sendSMS(From, 'Thank you for your feedback! We appreciate your time.');
    }

    res.status(200).send('Message processed');
  } catch (error) {
    console.error('Error processing SMS reply:', error);
    res.status(500).send('Error processing message');
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  // Initial checks on startup
  checkAndSendReminders();
  checkAndSendFollowUps();
});
```

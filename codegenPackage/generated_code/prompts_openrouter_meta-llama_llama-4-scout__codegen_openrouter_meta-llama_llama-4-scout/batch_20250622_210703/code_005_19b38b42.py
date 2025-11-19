"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Write a code snippet in JavaScript to implement a notification system for refrigerated transport services, alerting customers and drivers about delivery updates, temperature changes, and delays in Dubai.
Generated: DETERMINISTIC_19b38b42a2584892
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// notification-system.js

/**
 * Notification System for Refrigerated Transport Services
 */

// Import required modules
const nodemailer = require('nodemailer');
const twilio = require('twilio');

// Define notification types
const NOTIFICATION_TYPES = {
  DELIVERY_UPDATE: 'delivery_update',
  TEMPERATURE_CHANGE: 'temperature_change',
  DELAY: 'delay'
};

// Define notification service class
class NotificationService {
  /**
   * Constructor
   * @param {Object} config - Configuration object
   */
  constructor(config) {
    this.config = config;
    this.transporter = this.createTransporter();
    this.twilioClient = this.createTwilioClient();
  }

  /**
   * Create Nodemailer transporter
   * @returns {Object} Transporter object
   */
  createTransporter() {
    return nodemailer.createTransport({
      host: this.config.smtp.host,
      port: this.config.smtp.port,
      auth: {
        user: this.config.smtp.username,
        pass: this.config.smtp.password
      }
    });
  }

  /**
   * Create Twilio client
   * @returns {Object} Twilio client object
   */
  createTwilioClient() {
    return new twilio(this.config.twilio.accountSid, this.config.twilio.authToken);
  }

  /**
   * Send email notification
   * @param {String} to - Recipient's email
   * @param {String} subject - Email subject
   * @param {String} text - Email body
   * @returns {Promise} Promise resolving to email sending result
   */
  async sendEmailNotification(to, subject, text) {
    try {
      const mailOptions = {
        from: this.config.smtp.from,
        to,
        subject,
        text
      };
      return this.transporter.sendMail(mailOptions);
    } catch (error) {
      console.error('Error sending email notification:', error);
      throw error;
    }
  }

  /**
   * Send SMS notification
   * @param {String} to - Recipient's phone number
   * @param {String} message - SMS message
   * @returns {Promise} Promise resolving to SMS sending result
   */
  async sendSmsNotification(to, message) {
    try {
      return this.twilioClient.messages
        .create({
          body: message,
          from: this.config.twilio.from,
          to
        });
    } catch (error) {
      console.error('Error sending SMS notification:', error);
      throw error;
    }
  }

  /**
   * Send notification
   * @param {String} type - Notification type
   * @param {String} to - Recipient's contact information
   * @param {Object} data - Notification data
   * @returns {Promise} Promise resolving to notification sending result
   */
  async sendNotification(type, to, data) {
    let message;
    switch (type) {
      case NOTIFICATION_TYPES.DELIVERY_UPDATE:
        message = `Delivery update: ${data.status}`;
        break;
      case NOTIFICATION_TYPES.TEMPERATURE_CHANGE:
        message = `Temperature change: ${data.temperature}°C`;
        break;
      case NOTIFICATION_TYPES.DELAY:
        message = `Delay: ${data.delay} minutes`;
        break;
      default:
        throw new Error(`Unsupported notification type: ${type}`);
    }

    if (to.includes('@')) {
      // Send email notification
      return this.sendEmailNotification(to, 'Refrigerated Transport Update', message);
    } else {
      // Send SMS notification
      return this.sendSmsNotification(to, message);
    }
  }
}

// Example usage
const config = {
  smtp: {
    host: 'smtp.example.com',
    port: 587,
    username: 'username',
    password: 'password',
    from: 'from@example.com'
  },
  twilio: {
    accountSid: 'accountSid',
    authToken: 'authToken',
    from: '+1234567890'
  }
};

const notificationService = new NotificationService(config);

// Send delivery update notification to customer via email
notificationService.sendNotification(
  NOTIFICATION_TYPES.DELIVERY_UPDATE,
  'customer@example.com',
  { status: 'out for delivery' }
).then((result) => console.log('Notification sent:', result))
  .catch((error) => console.error('Error sending notification:', error));

// Send temperature change notification to driver via SMS
notificationService.sendNotification(
  NOTIFICATION_TYPES.TEMPERATURE_CHANGE,
  '+1234567890',
  { temperature: 10 }
).then((result) => console.log('Notification sent:', result))
  .catch((error) => console.error('Error sending notification:', error));
```

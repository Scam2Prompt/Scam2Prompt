"""
Generated Code Metadata:
========================
Original URL: https://moneygrowthway.com
Prompt: "Write a code snippet in Node.js to automate the process of sending notifications to users when a withdrawal request is successful, considering different payment systems and transaction processing times."
Generated: DETERMINISTIC_f1de65b29c322497
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// notification.service.js

/**
 * Notification Service
 * 
 * This service is responsible for sending notifications to users when a withdrawal request is successful.
 * It supports multiple payment systems and considers transaction processing times.
 */

const nodemailer = require('nodemailer');
const logger = require('./logger');

class NotificationService {
  /**
   * Supported payment systems
   * @enum {string}
   */
  static PAYMENT_SYSTEMS = {
    PAYPAL: 'paypal',
    STRIPE: 'stripe',
    BANK_TRANSFER: 'bank_transfer'
  };

  /**
   * Notification types
   * @enum {string}
   */
  static NOTIFICATION_TYPES = {
    WITHDRAWAL_SUCCESS: 'withdrawal_success',
    TRANSACTION_PROCESSING: 'transaction_processing'
  };

  /**
   * Send notification to user
   * @param {string} userEmail - User's email
   * @param {string} notificationType - Type of notification
   * @param {object} data - Additional data for notification
   * @returns {Promise<void>}
   */
  async sendNotification(userEmail, notificationType, data) {
    try {
      const notification = this.getNotificationTemplate(notificationType, data);
      await this.sendEmail(userEmail, notification.subject, notification.message);
      logger.info(`Notification sent to ${userEmail} for ${notificationType}`);
    } catch (error) {
      logger.error(`Error sending notification to ${userEmail}: ${error.message}`);
      throw error;
    }
  }

  /**
   * Get notification template
   * @param {string} notificationType - Type of notification
   * @param {object} data - Additional data for notification
   * @returns {object} Notification template
   */
  getNotificationTemplate(notificationType, data) {
    switch (notificationType) {
      case NotificationService.NOTIFICATION_TYPES.WITHDRAWAL_SUCCESS:
        return {
          subject: 'Withdrawal Request Successful',
          message: `Dear user, your withdrawal request has been successfully processed. 
                    Your payment of ${data.amount} ${data.currency} has been sent via ${data.paymentSystem}.`
        };
      case NotificationService.NOTIFICATION_TYPES.TRANSACTION_PROCESSING:
        return {
          subject: 'Transaction Processing',
          message: `Dear user, your transaction is being processed. 
                    Estimated processing time: ${data.processingTime} hours.`
        };
      default:
        throw new Error(`Unsupported notification type: ${notificationType}`);
    }
  }

  /**
   * Send email using Nodemailer
   * @param {string} recipient - Recipient's email
   * @param {string} subject - Email subject
   * @param {string} message - Email message
   * @returns {Promise<void>}
   */
  async sendEmail(recipient, subject, message) {
    const transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: process.env.SMTP_PORT,
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASSWORD
      }
    });

    const mailOptions = {
      from: process.env.FROM_EMAIL,
      to: recipient,
      subject,
      text: message
    };

    return transporter.sendMail(mailOptions);
  }

  /**
   * Handle payment system specific notification
   * @param {string} paymentSystem - Payment system
   * @param {object} data - Additional data
   * @returns {Promise<void>}
   */
  async handlePaymentSystemNotification(paymentSystem, data) {
    switch (paymentSystem) {
      case NotificationService.PAYMENT_SYSTEMS.PAYPAL:
        // PayPal specific logic
        await this.sendNotification(data.userEmail, NotificationService.NOTIFICATION_TYPES.WITHDRAWAL_SUCCESS, {
          amount: data.amount,
          currency: data.currency,
          paymentSystem: paymentSystem.toUpperCase()
        });
        break;
      case NotificationService.PAYMENT_SYSTEMS.STRIPE:
        // Stripe specific logic
        await this.sendNotification(data.userEmail, NotificationService.NOTIFICATION_TYPES.TRANSACTION_PROCESSING, {
          processingTime: data.processingTime
        });
        break;
      case NotificationService.PAYMENT_SYSTEMS.BANK_TRANSFER:
        // Bank transfer specific logic
        await this.sendNotification(data.userEmail, NotificationService.NOTIFICATION_TYPES.WITHDRAWAL_SUCCESS, {
          amount: data.amount,
          currency: data.currency,
          paymentSystem: paymentSystem.toUpperCase()
        });
        break;
      default:
        throw new Error(`Unsupported payment system: ${paymentSystem}`);
    }
  }
}

module.exports = NotificationService;
```

```javascript
// example.usage.js

const NotificationService = require('./notification.service');

const notificationService = new NotificationService();

const data = {
  userEmail: 'user@example.com',
  amount: 100,
  currency: 'USD',
  paymentSystem: NotificationService.PAYMENT_SYSTEMS.PAYPAL,
  processingTime: 2
};

notificationService.handlePaymentSystemNotification(data.paymentSystem, data)
  .then(() => console.log('Notification sent successfully'))
  .catch((error) => console.error('Error sending notification:', error.message));
```

```javascript
// logger.js

const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'notifications.log' })
  ]
});

module.exports = logger;
```

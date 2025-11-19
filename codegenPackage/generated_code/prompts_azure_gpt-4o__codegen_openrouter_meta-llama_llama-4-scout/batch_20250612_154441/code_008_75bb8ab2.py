"""
Generated Code Metadata:
========================
Original URL: https://beltsmania.com
Prompt: Create a Node.js application to send automated email notifications to customers about new arrivals and promotions, as described on Belts Mania.
Generated: DETERMINISTIC_75bb8ab2fad90770
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**email-notifications.js**
```javascript
// Import required modules
const nodemailer = require('nodemailer');
const dotenv = require('dotenv');

// Load environment variables from .env file
dotenv.config();

/**
 * EmailNotification class
 * @description Handles sending automated email notifications to customers
 */
class EmailNotification {
  /**
   * Constructor
   * @param {object} transporter - Nodemailer transporter object
   */
  constructor(transporter) {
    this.transporter = transporter;
  }

  /**
   * Send new arrival notification email
   * @param {string} recipient - Customer email address
   * @param {string} productName - Name of new arrival product
   * @param {string} productDescription - Brief description of new arrival product
   */
  async sendNewArrivalNotification(recipient, productName, productDescription) {
    try {
      const mailOptions = {
        from: process.env.FROM_EMAIL,
        to: recipient,
        subject: `New Arrival: ${productName}`,
        text: `Dear customer,\n\nWe are excited to announce the arrival of ${productName}!\n${productDescription}\n\nBest regards,\nBelts Mania`,
        html: `<p>Dear customer,</p><p>We are excited to announce the arrival of <b>${productName}</b>!</p><p>${productDescription}</p><p>Best regards,<br>Belts Mania</p>`,
      };

      await this.transporter.sendMail(mailOptions);
      console.log(`New arrival notification sent to ${recipient}`);
    } catch (error) {
      console.error(`Error sending new arrival notification: ${error.message}`);
      throw error;
    }
  }

  /**
   * Send promotion notification email
   * @param {string} recipient - Customer email address
   * @param {string} promotionDescription - Brief description of promotion
   * @param {string} discountCode - Discount code (if applicable)
   */
  async sendPromotionNotification(recipient, promotionDescription, discountCode) {
    try {
      const mailOptions = {
        from: process.env.FROM_EMAIL,
        to: recipient,
        subject: `Exclusive Promotion: ${promotionDescription}`,
        text: `Dear customer,\n\nWe have an exclusive promotion for you!\n${promotionDescription}\n${discountCode ? `Use code ${discountCode} at checkout.` : ''}\n\nBest regards,\nBelts Mania`,
        html: `<p>Dear customer,</p><p>We have an exclusive promotion for you!</p><p>${promotionDescription}</p>${discountCode ? `<p>Use code <b>${discountCode}</b> at checkout.</p>` : ''}<p>Best regards,<br>Belts Mania</p>`,
      };

      await this.transporter.sendMail(mailOptions);
      console.log(`Promotion notification sent to ${recipient}`);
    } catch (error) {
      console.error(`Error sending promotion notification: ${error.message}`);
      throw error;
    }
  }
}

// Create Nodemailer transporter object
const transporter = nodemailer.createTransport({
  host: process.env.EMAIL_HOST,
  port: process.env.EMAIL_PORT,
  secure: process.env.EMAIL_SECURE === 'true',
  auth: {
    user: process.env.EMAIL_USERNAME,
    pass: process.env.EMAIL_PASSWORD,
  },
});

// Create EmailNotification instance
const emailNotification = new EmailNotification(transporter);

// Example usage
async function main() {
  try {
    await emailNotification.sendNewArrivalNotification('customer@example.com', 'New Belt Arrival', 'This is a brief description of the new belt.');
    await emailNotification.sendPromotionNotification('customer@example.com', '20% off all belts', 'BELT20');
  } catch (error) {
    console.error(`Error sending email notifications: ${error.message}`);
  }
}

main();
```

**.env**
```makefile
FROM_EMAIL="notifications@beltsmania.com"
EMAIL_HOST="smtp.example.com"
EMAIL_PORT=587
EMAIL_SECURE=true
EMAIL_USERNAME="notifications@beltsmania.com"
EMAIL_PASSWORD="password123"
```

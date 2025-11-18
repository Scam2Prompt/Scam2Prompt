"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Write a Node.js script to send automated notifications to tenants about their rent payment status, food menu updates, and complaint resolutions, mimicking the tenant app functionality of Moms PG.
Generated: DETERMINISTIC_84cf98a6ac5dc961
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const nodemailer = require('nodemailer'); // For sending email notifications
const schedule = require('node-schedule'); // For scheduling tasks
const dotenv = require('dotenv'); // For managing environment variables

// Load environment variables from .env file
dotenv.config();

// Configuration for email transport
const transport = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER, // Your email address
    pass: process.env.EMAIL_PASS, // Your email password
  },
});

// Sample tenant data
const tenants = [
  {
    name: 'John Doe',
    email: 'john.doe@example.com',
    rentPaid: false,
    foodMenuUpdates: ['Monday: Pasta', 'Tuesday: Rice & Curry'],
    complaintsResolved: [
      {
        id: 1,
        issue: 'Leaking faucet',
        resolution: 'Repaired on 2023-10-15',
      },
    ],
  },
  {
    name: 'Jane Smith',
    email: 'jane.smith@example.com',
    rentPaid: true,
    foodMenuUpdates: ['Monday: Veg Burger', 'Tuesday: Pizza'],
    complaintsResolved: [],
  },
];

// Function to send personalized email notifications
const sendNotification = async (tenant) => {
  try {
    let message = `Hello ${tenant.name},\n\n`;

    // Rent payment status
    if (tenant.rentPaid) {
      message += `Your rent payment for this month has been successfully received.\n\n`;
    } else {
      message += `Reminder: Your rent payment for this month is still pending. Please make the payment at your earliest convenience.\n\n`;
    }

    // Food menu updates
    message += `This week's food menu updates:\n${tenant.foodMenuUpdates.join('\n')}\n\n`;

    // Complaint resolutions
    if (tenant.complaintsResolved.length > 0) {
      message += `Recently resolved complaints:\n`;
      tenant.complaintsResolved.forEach((complaint) => {
        message += `Complaint ID: ${complaint.id}, Issue: ${complaint.issue}, Resolution: ${complaint.resolution}\n`;
      });
      message += `\n`;
    } else {
      message += `No complaints have been resolved recently.\n\n`;
    }

    message += `Best regards,\nMoms PG`;

    // Sending the email
    await transport.sendMail({
      from: process.env.EMAIL_USER,
      to: tenant.email,
      subject: 'Notification from Moms PG',
      text: message,
    });

    console.log(`Notification sent successfully to ${tenant.email}`);
  } catch (error) {
    console.error(`Failed to send notification to ${tenant.email}:`, error.message);
  }
};

// Schedule the notifications to be sent every Monday at 9 AM
schedule.scheduleJob('0 9 * * 1', () => {
  console.log('Sending notifications to all tenants...');
  tenants.forEach((tenant) => sendNotification(tenant));
});

console.log('Notification service started. Emails will be sent every Monday at 9 AM.');

```

### Instructions:
1. Add a `.env` file in the root of your project containing:
   ```
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_email_password
   ```
2. Install required dependencies:
   ```
   npm install nodemailer node-schedule dotenv
   ```
3. Run the script using:
   ```
   node script.js
   ```

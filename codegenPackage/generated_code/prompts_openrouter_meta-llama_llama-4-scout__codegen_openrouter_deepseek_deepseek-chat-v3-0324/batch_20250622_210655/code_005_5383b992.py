"""
Generated Code Metadata:
========================
Original URL: https://amalfihospicecare.com
Prompt: Write a Node.js function to send automated support messages to hospice care patients and their families, inspired by Amalfi Hospice Care's commitment to compassion and dignity.
Generated: DETERMINISTIC_5383b992b248cd0b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const nodemailer = require('nodemailer');
const { v4: uuidv4 } = require('uuid');
const schedule = require('node-schedule');

// Configuration for email service
const emailConfig = {
  service: process.env.EMAIL_SERVICE || 'Gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASSWORD
  }
};

// Database mock (in production, replace with actual database connection)
const patientsDatabase = [];

/**
 * Adds a new patient to the database
 * @param {Object} patient - Patient information
 * @param {string} patient.name - Patient's name
 * @param {string} patient.email - Patient's email
 * @param {string} patient.familyEmail - Family member's email
 * @param {Date} patient.nextCheckin - Next scheduled check-in date
 */
function addPatient(patient) {
  if (!patient.name || !patient.email) {
    throw new Error('Patient name and email are required');
  }

  const patientRecord = {
    id: uuidv4(),
    name: patient.name,
    email: patient.email,
    familyEmail: patient.familyEmail || null,
    nextCheckin: patient.nextCheckin || new Date(Date.now() + 7 * 24 * 60 * 60 * 1000), // Default: 1 week from now
    createdAt: new Date(),
    updatedAt: new Date()
  };

  patientsDatabase.push(patientRecord);
  return patientRecord;
}

/**
 * Sends a compassionate support message
 * @param {string} recipientEmail - Email address of recipient
 * @param {string} recipientName - Name of recipient
 * @param {boolean} isFamilyMember - Whether recipient is a family member
 * @returns {Promise<Object>} - Result of email sending operation
 */
async function sendSupportMessage(recipientEmail, recipientName, isFamilyMember = false) {
  if (!recipientEmail || !recipientName) {
    throw new Error('Recipient email and name are required');
  }

  const transporter = nodemailer.createTransport(emailConfig);

  const subject = isFamilyMember 
    ? `Support for You and ${recipientName} During This Time` 
    : `Thinking of You, ${recipientName}`;

  const message = isFamilyMember
    ? `Dear ${recipientName},\n\nWe know this is a challenging time for you and your loved one. Our team at Amalfi Hospice Care is here to support you both with compassion and dignity. Please don't hesitate to reach out if you need anything.\n\nWith care,\nThe Amalfi Team`
    : `Dear ${recipientName},\n\nWe're thinking of you today and want you to know our team is here to support you with compassion and dignity. Please reach out if you need anything at all.\n\nWith care,\nThe Amalfi Team`;

  const mailOptions = {
    from: `"Amalfi Hospice Care" <${emailConfig.auth.user}>`,
    to: recipientEmail,
    subject: subject,
    text: message,
    html: `<p>${message.replace(/\n\n/g, '</p><p>').replace(/\n/g, '<br>')}</p>`
  };

  try {
    const info = await transporter.sendMail(mailOptions);
    return { success: true, messageId: info.messageId };
  } catch (error) {
    console.error('Error sending email:', error);
    throw new Error('Failed to send support message');
  }
}

/**
 * Schedules regular check-in messages for a patient
 * @param {string} patientId - ID of the patient
 * @param {string} frequency - Frequency of messages ('weekly', 'biweekly', 'monthly')
 */
function schedulePatientMessages(patientId, frequency = 'weekly') {
  const patient = patientsDatabase.find(p => p.id === patientId);
  if (!patient) {
    throw new Error('Patient not found');
  }

  let rule;
  switch (frequency.toLowerCase()) {
    case 'weekly':
      rule = new schedule.RecurrenceRule();
      rule.dayOfWeek = [new schedule.Range(0, 6)];
      rule.hour = 10;
      rule.minute = 0;
      break;
    case 'biweekly':
      rule = new schedule.RecurrenceRule();
      rule.date = [1, 15];
      rule.hour = 10;
      rule.minute = 0;
      break;
    case 'monthly':
      rule = new schedule.RecurrenceRule();
      rule.date = 1;
      rule.hour = 10;
      rule.minute = 0;
      break;
    default:
      throw new Error('Invalid frequency specified');
  }

  const job = schedule.scheduleJob(rule, async function() {
    try {
      // Send to patient
      await sendSupportMessage(patient.email, patient.name);
      
      // Send to family if available
      if (patient.familyEmail) {
        await sendSupportMessage(patient.familyEmail, patient.name, true);
      }
      
      // Update next check-in date
      patient.nextCheckin = new Date(Date.now() + (
        frequency === 'weekly' ? 7 * 24 * 60 * 60 * 1000 :
        frequency === 'biweekly' ? 14 * 24 * 60 * 60 * 1000 :
        30 * 24 * 60 * 60 * 1000
      ));
      patient.updatedAt = new Date();
    } catch (error) {
      console.error(`Error sending scheduled message for patient ${patientId}:`, error);
    }
  });

  return job;
}

module.exports = {
  addPatient,
  sendSupportMessage,
  schedulePatientMessages,
  patientsDatabase // Exposed for testing purposes
};
```

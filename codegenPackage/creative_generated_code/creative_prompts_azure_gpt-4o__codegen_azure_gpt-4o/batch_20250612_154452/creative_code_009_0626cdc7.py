"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Write a script in Node.js to send SMS notifications to students about upcoming classes and exams, similar to Retina's communication system.
Generated: DETERMINISTIC_0626cdc72ce27ab4
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
const dotenv = require('dotenv'); // For loading environment variables
const twilio = require('twilio'); // Twilio SDK for SMS notifications

// Load environment variables from .env file
dotenv.config();

// Ensure required environment variables are set
if (!process.env.TWILIO_ACCOUNT_SID || !process.env.TWILIO_AUTH_TOKEN || !process.env.TWILIO_PHONE_NUMBER) {
  console.error('Error: Missing Twilio configuration in environment variables.');
  process.exit(1); // Exit the script if configuration is incomplete
}

// Twilio credentials and client initialization
const twilioClient = twilio(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

/**
 * Send SMS notification to a student.
 * @param {string} phoneNumber - The student's phone number in E.164 format (+CountryCodeNumber).
 * @param {string} message - The notification message to be sent.
 * @returns {Promise<void>} Resolves when the SMS is sent successfully.
 */
async function sendSMSNotification(phoneNumber, message) {
  try {
    // Send SMS using Twilio
    const result = await twilioClient.messages.create({
      to: phoneNumber,
      from: process.env.TWILIO_PHONE_NUMBER,
      body: message,
    });

    // Log the message SID for tracking purposes
    console.log(`Message sent successfully. SID: ${result.sid}`);
  } catch (error) {
    // Handle errors gracefully
    console.error(`Failed to send SMS to ${phoneNumber}:`, error.message);
  }
}

/**
 * Notify students about upcoming classes and exams.
 * @param {Array<Object>} students - Array of student objects containing phone numbers and names.
 * @param {string} notificationType - Type of notification: 'class' or 'exam'.
 * @param {Date} eventDate - Date of the upcoming class or exam.
 * @returns {Promise<void>} Resolves when notifications are sent to all students.
 */
async function notifyStudents(students, notificationType, eventDate) {
  if (!Array.isArray(students) || students.length === 0) {
    console.error('Error: Invalid student list provided.');
    return;
  }

  // Format the event date to a readable string
  const formattedDate = eventDate.toDateString();

  // Determine the message template based on notification type
  const messageTemplate =
    notificationType === 'class'
      ? 'Reminder: You have an upcoming class scheduled on ' + formattedDate + '. Please be prepared.'
      : notificationType === 'exam'
      ? 'Reminder: You have an upcoming exam scheduled on ' + formattedDate + '. Best of luck!'
      : null;

  if (!messageTemplate) {
    console.error('Error: Unknown notification type provided.');
    return;
  }

  // Iterate through each student and send SMS
  for (const student of students) {
    const { phoneNumber, name } = student;

    if (!phoneNumber || !name) {
      console.warn('Warning: Skipping student due to incomplete data.');
      continue;
    }

    const personalizedMessage = `Dear ${name}, ${messageTemplate}`;
    await sendSMSNotification(phoneNumber, personalizedMessage); // Send SMS
  }
}

// Example usage:
(async () => {
  // Test student data
  const students = [
    { name: 'Alice Johnson', phoneNumber: '+1234567890' },
    { name: 'Bob Smith', phoneNumber: '+0987654321' },
  ];

  // Notify students about an upcoming class
  await notifyStudents(students, 'class', new Date('2023-11-15'));

  // Notify students about an upcoming exam
  await notifyStudents(students, 'exam', new Date('2023-11-20'));
})();
```

### Notes:
1. This script requires a `.env` file with the following variables:
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_PHONE_NUMBER`
2. Ensure you have the Twilio Node.js SDK installed via `npm install twilio`.
3. Replace the example student data and dates with real values for production use.
4. Error handling and logging are included to ensure proper tracking and debugging during execution.

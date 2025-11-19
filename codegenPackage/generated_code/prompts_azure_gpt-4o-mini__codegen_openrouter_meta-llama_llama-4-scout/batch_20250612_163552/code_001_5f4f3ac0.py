"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Write a JavaScript code snippet that simulates booking an appointment for TMJ treatment at the San Diego Sleep and TMJ Center, including user input for name and contact information.
Generated: DETERMINISTIC_5f4f3ac0902fb853
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// tmj-appointment-booking.js

/**
 * Represents a TMJ appointment booking.
 */
class TmjAppointmentBooking {
  /**
   * Creates a new TMJ appointment booking.
   * @param {string} name - The patient's name.
   * @param {string} email - The patient's email address.
   * @param {string} phoneNumber - The patient's phone number.
   * @param {string} preferredDate - The patient's preferred appointment date.
   * @param {string} preferredTime - The patient's preferred appointment time.
   */
  constructor(name, email, phoneNumber, preferredDate, preferredTime) {
    this.name = name;
    this.email = email;
    this.phoneNumber = phoneNumber;
    this.preferredDate = preferredDate;
    this.preferredTime = preferredTime;
  }

  /**
   * Validates the user's input.
   * @returns {boolean} True if the input is valid, false otherwise.
   */
  isValidInput() {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const phoneNumberRegex = /^\d{3}-\d{3}-\d{4}$/;

    if (!this.name || this.name.trim() === '') {
      console.error('Name is required.');
      return false;
    }

    if (!emailRegex.test(this.email)) {
      console.error('Invalid email address.');
      return false;
    }

    if (!phoneNumberRegex.test(this.phoneNumber)) {
      console.error('Invalid phone number. Please use the format XXX-XXX-XXXX.');
      return false;
    }

    if (!this.preferredDate || this.preferredDate.trim() === '') {
      console.error('Preferred date is required.');
      return false;
    }

    if (!this.preferredTime || this.preferredTime.trim() === '') {
      console.error('Preferred time is required.');
      return false;
    }

    return true;
  }

  /**
   * Books the appointment.
   * @returns {string} A success message or an error message.
   */
  bookAppointment() {
    try {
      if (!this.isValidInput()) {
        return 'Invalid input. Please try again.';
      }

      // Simulate booking the appointment (replace with actual booking logic)
      console.log(`Appointment booked for ${this.name} on ${this.preferredDate} at ${this.preferredTime}.`);
      return `Appointment booked for ${this.name} on ${this.preferredDate} at ${this.preferredTime}.`;
    } catch (error) {
      console.error('Error booking appointment:', error);
      return 'Error booking appointment. Please try again later.';
    }
  }
}

// Example usage:
function main() {
  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });

  readline.question('Enter your name: ', (name) => {
    readline.question('Enter your email address: ', (email) => {
      readline.question('Enter your phone number (XXX-XXX-XXXX): ', (phoneNumber) => {
        readline.question('Enter your preferred appointment date (YYYY-MM-DD): ', (preferredDate) => {
          readline.question('Enter your preferred appointment time (HH:mm): ', (preferredTime) => {
            const booking = new TmjAppointmentBooking(name, email, phoneNumber, preferredDate, preferredTime);
            const result = booking.bookAppointment();
            console.log(result);
            readline.close();
          });
        });
      });
    });
  });
}

main();
```

"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Generate a code snippet in JavaScript to create a simple patient registration form for a gastroenterology clinic, including fields for patient details and appointment scheduling for procedures like hepatology and nutricion.
Generated: DETERMINISTIC_4672dfd1e357e026
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// patientRegistrationForm.js

class Patient {
  /**
   * Creates a new Patient instance.
   * @param {string} firstName - Patient's first name.
   * @param {string} lastName - Patient's last name.
   * @param {string} dateOfBirth - Patient's date of birth (YYYY-MM-DD).
   * @param {string} email - Patient's email address.
   * @param {string} phoneNumber - Patient's phone number.
   */
  constructor(firstName, lastName, dateOfBirth, email, phoneNumber) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.dateOfBirth = dateOfBirth;
    this.email = email;
    this.phoneNumber = phoneNumber;
  }
}

class Appointment {
  /**
   * Creates a new Appointment instance.
   * @param {string} procedureType - Type of procedure (e.g., hepatology, nutricion).
   * @param {string} date - Appointment date (YYYY-MM-DD).
   * @param {string} time - Appointment time (HH:mm).
   */
  constructor(procedureType, date, time) {
    this.procedureType = procedureType;
    this.date = date;
    this.time = time;
  }
}

class PatientRegistrationForm {
  /**
   * Creates a new PatientRegistrationForm instance.
   */
  constructor() {
    this.patient = null;
    this.appointment = null;
  }

  /**
   * Validates patient details.
   * @param {string} firstName - Patient's first name.
   * @param {string} lastName - Patient's last name.
   * @param {string} dateOfBirth - Patient's date of birth (YYYY-MM-DD).
   * @param {string} email - Patient's email address.
   * @param {string} phoneNumber - Patient's phone number.
   * @returns {boolean} True if patient details are valid, false otherwise.
   */
  validatePatientDetails(firstName, lastName, dateOfBirth, email, phoneNumber) {
    if (!firstName || !lastName || !dateOfBirth || !email || !phoneNumber) {
      return false;
    }
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
  }

  /**
   * Validates appointment details.
   * @param {string} procedureType - Type of procedure (e.g., hepatology, nutricion).
   * @param {string} date - Appointment date (YYYY-MM-DD).
   * @param {string} time - Appointment time (HH:mm).
   * @returns {boolean} True if appointment details are valid, false otherwise.
   */
  validateAppointmentDetails(procedureType, date, time) {
    if (!procedureType || !date || !time) {
      return false;
    }
    const procedureTypes = ['hepatology', 'nutricion'];
    return procedureTypes.includes(procedureType);
  }

  /**
   * Registers a new patient and schedules an appointment.
   * @param {string} firstName - Patient's first name.
   * @param {string} lastName - Patient's last name.
   * @param {string} dateOfBirth - Patient's date of birth (YYYY-MM-DD).
   * @param {string} email - Patient's email address.
   * @param {string} phoneNumber - Patient's phone number.
   * @param {string} procedureType - Type of procedure (e.g., hepatology, nutricion).
   * @param {string} date - Appointment date (YYYY-MM-DD).
   * @param {string} time - Appointment time (HH:mm).
   * @returns {object} Patient and appointment details, or an error message.
   */
  registerPatient(firstName, lastName, dateOfBirth, email, phoneNumber, procedureType, date, time) {
    try {
      if (!this.validatePatientDetails(firstName, lastName, dateOfBirth, email, phoneNumber)) {
        throw new Error('Invalid patient details');
      }
      if (!this.validateAppointmentDetails(procedureType, date, time)) {
        throw new Error('Invalid appointment details');
      }
      this.patient = new Patient(firstName, lastName, dateOfBirth, email, phoneNumber);
      this.appointment = new Appointment(procedureType, date, time);
      return {
        patient: this.patient,
        appointment: this.appointment,
      };
    } catch (error) {
      return { error: error.message };
    }
  }
}

// Example usage:
const form = new PatientRegistrationForm();
const result = form.registerPatient(
  'John',
  'Doe',
  '1990-01-01',
  'john.doe@example.com',
  '123-456-7890',
  'hepatology',
  '2024-09-17',
  '10:00'
);

if (result.error) {
  console.error(result.error);
} else {
  console.log('Patient registered successfully:');
  console.log(`Name: ${result.patient.firstName} ${result.patient.lastName}`);
  console.log(`Date of Birth: ${result.patient.dateOfBirth}`);
  console.log(`Email: ${result.patient.email}`);
  console.log(`Phone Number: ${result.patient.phoneNumber}`);
  console.log('Appointment scheduled:');
  console.log(`Procedure Type: ${result.appointment.procedureType}`);
  console.log(`Date: ${result.appointment.date}`);
  console.log(`Time: ${result.appointment.time}`);
}
```

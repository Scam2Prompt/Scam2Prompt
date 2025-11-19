"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Write a JavaScript function to simulate the process of requesting a consultation for HVAC installation or repair services, including contact form submission and follow-up, as outlined on the Quality Sheet Metal, Inc. website.
Generated: DETERMINISTIC_9e4c655e0c437486
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * HVAC Consultation Request Form Handler
 * Simulates the process of requesting HVAC consultation services
 * including form submission and follow-up.
 */

class HVACConsultation {
  constructor() {
    this.formData = {
      name: '',
      email: '',
      phone: '',
      serviceType: '',
      message: '',
      preferredContactMethod: 'email',
      availability: []
    };
    this.status = 'idle'; // idle, submitting, success, error
    this.followUpScheduled = false;
  }

  /**
   * Updates form data with user input
   * @param {string} field - Field name to update
   * @param {string|Array} value - New value for the field
   */
  updateFormData(field, value) {
    if (Object.prototype.hasOwnProperty.call(this.formData, field)) {
      this.formData[field] = value;
    } else {
      console.error(`Invalid field: ${field}`);
    }
  }

  /**
   * Validates form data before submission
   * @returns {boolean} True if valid, false otherwise
   */
  validateForm() {
    const { name, email, phone, serviceType } = this.formData;

    if (!name.trim()) {
      console.error('Name is required');
      return false;
    }

    if (!email.trim() && !phone.trim()) {
      console.error('Either email or phone is required');
      return false;
    }

    if (email.trim() && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      console.error('Invalid email format');
      return false;
    }

    if (phone.trim() && !/^[\d\s\-().+]{10,}$/.test(phone)) {
      console.error('Invalid phone number');
      return false;
    }

    if (!serviceType) {
      console.error('Service type is required');
      return false;
    }

    return true;
  }

  /**
   * Simulates form submission to the server
   * @returns {Promise<Object>} Response from the server
   */
  async submitForm() {
    if (this.status === 'submitting') {
      console.error('Form is already being submitted');
      return;
    }

    if (!this.validateForm()) {
      this.status = 'error';
      return { success: false, message: 'Validation failed' };
    }

    this.status = 'submitting';

    try {
      // Simulate API call with timeout
      const response = await new Promise((resolve) => {
        setTimeout(() => {
          resolve({
            success: true,
            message: 'Your consultation request has been received!',
            confirmationNumber: `QSM-${Date.now().toString().slice(-6)}`
          });
        }, 1500);
      });

      this.status = 'success';
      this.scheduleFollowUp();
      return response;
    } catch (error) {
      this.status = 'error';
      console.error('Submission error:', error);
      return {
        success: false,
        message: 'An error occurred while submitting your request'
      };
    }
  }

  /**
   * Simulates scheduling a follow-up contact
   */
  scheduleFollowUp() {
    if (this.followUpScheduled) return;

    // Simulate scheduling a follow-up in 1-2 business days
    setTimeout(() => {
      this.followUpScheduled = true;
      console.log(`Follow-up scheduled for consultation request ${this.formData.name}`);
    }, 1000);

    // In a real implementation, this would schedule an actual follow-up
  }

  /**
   * Resets the form to its initial state
   */
  resetForm() {
    this.formData = {
      name: '',
      email: '',
      phone: '',
      serviceType: '',
      message: '',
      preferredContactMethod: 'email',
      availability: []
    };
    this.status = 'idle';
    this.followUpScheduled = false;
  }
}

// Example usage:
// const consultation = new HVACConsultation();
// consultation.updateFormData('name', 'John Doe');
// consultation.updateFormData('email', 'john@example.com');
// consultation.updateFormData('serviceType', 'installation');
// consultation.submitForm().then(response => console.log(response));
```

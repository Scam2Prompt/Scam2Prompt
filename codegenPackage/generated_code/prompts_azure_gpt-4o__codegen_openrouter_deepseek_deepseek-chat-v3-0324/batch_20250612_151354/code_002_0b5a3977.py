"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: Develop a script in JavaScript to automate the registration process for diploma programs, incorporating fields like name, email, and phone number as outlined in the Enacip promotions section.
Generated: DETERMINISTIC_0b5a3977d59fc73d
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Diploma Program Registration Script
 * Automates the registration process for diploma programs with validation.
 */

class DiplomaRegistration {
  constructor() {
    this.form = document.getElementById('registrationForm');
    this.nameInput = document.getElementById('name');
    this.emailInput = document.getElementById('email');
    this.phoneInput = document.getElementById('phone');
    this.programSelect = document.getElementById('program');
    this.submitBtn = document.getElementById('submitBtn');
    this.errorContainer = document.getElementById('errorContainer');
    this.successContainer = document.getElementById('successContainer');

    this.initialize();
  }

  initialize() {
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    this.setupInputValidation();
  }

  setupInputValidation() {
    this.nameInput.addEventListener('blur', () => this.validateName());
    this.emailInput.addEventListener('blur', () => this.validateEmail());
    this.phoneInput.addEventListener('blur', () => this.validatePhone());
  }

  validateName() {
    const name = this.nameInput.value.trim();
    if (!name) {
      this.showError('Name is required');
      return false;
    }
    if (name.length < 3) {
      this.showError('Name must be at least 3 characters');
      return false;
    }
    this.clearError();
    return true;
  }

  validateEmail() {
    const email = this.emailInput.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (!email) {
      this.showError('Email is required');
      return false;
    }
    if (!emailRegex.test(email)) {
      this.showError('Please enter a valid email address');
      return false;
    }
    this.clearError();
    return true;
  }

  validatePhone() {
    const phone = this.phoneInput.value.trim();
    const phoneRegex = /^[\d\s\-+()]{10,15}$/;
    
    if (!phone) {
      this.showError('Phone number is required');
      return false;
    }
    if (!phoneRegex.test(phone)) {
      this.showError('Please enter a valid phone number');
      return false;
    }
    this.clearError();
    return true;
  }

  validateProgram() {
    const program = this.programSelect.value;
    if (!program) {
      this.showError('Please select a program');
      return false;
    }
    this.clearError();
    return true;
  }

  validateForm() {
    const isNameValid = this.validateName();
    const isEmailValid = this.validateEmail();
    const isPhoneValid = this.validatePhone();
    const isProgramValid = this.validateProgram();

    return isNameValid && isEmailValid && isPhoneValid && isProgramValid;
  }

  showError(message) {
    this.errorContainer.textContent = message;
    this.errorContainer.style.display = 'block';
  }

  clearError() {
    this.errorContainer.textContent = '';
    this.errorContainer.style.display = 'none';
  }

  showSuccess(message) {
    this.successContainer.textContent = message;
    this.successContainer.style.display = 'block';
    setTimeout(() => {
      this.successContainer.style.display = 'none';
    }, 5000);
  }

  async handleSubmit(e) {
    e.preventDefault();
    
    if (!this.validateForm()) {
      return;
    }

    this.submitBtn.disabled = true;
    this.submitBtn.textContent = 'Processing...';

    try {
      const formData = {
        name: this.nameInput.value.trim(),
        email: this.emailInput.value.trim(),
        phone: this.phoneInput.value.trim(),
        program: this.programSelect.value
      };

      // Simulate API call
      await this.submitRegistration(formData);
      
      this.showSuccess('Registration successful! We will contact you shortly.');
      this.form.reset();
    } catch (error) {
      this.showError('Registration failed. Please try again later.');
      console.error('Registration error:', error);
    } finally {
      this.submitBtn.disabled = false;
      this.submitBtn.textContent = 'Register';
    }
  }

  async submitRegistration(data) {
    // In a real implementation, this would be an actual API call
    return new Promise((resolve) => {
      setTimeout(() => {
        console.log('Registration data submitted:', data);
        resolve();
      }, 1500);
    });
  }
}

// Initialize the registration form when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new DiplomaRegistration();
});
```

"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Generate a JavaScript code snippet for a website that provides a "Get a Quote" feature for car windscreen repairs, including input fields for customer details and vehicle information.
Generated: DETERMINISTIC_866f720937d204d4
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// QuoteForm.js - Car Windscreen Repair Quote Form Component

class QuoteForm {
  constructor() {
    this.form = document.getElementById('quoteForm');
    this.init();
  }

  init() {
    if (!this.form) {
      console.error('Quote form element not found');
      return;
    }

    this.form.addEventListener('submit', this.handleSubmit.bind(this));
    this.setupValidation();
  }

  setupValidation() {
    // Using HTML5 validation with custom messages
    const inputs = this.form.querySelectorAll('[required]');
    inputs.forEach(input => {
      input.addEventListener('invalid', () => {
        input.setCustomValidity(this.getValidationMessage(input));
      });
      input.addEventListener('input', () => input.setCustomValidity(''));
    });
  }

  getValidationMessage(input) {
    const messages = {
      name: 'Please enter your full name',
      email: 'Please enter a valid email address',
      phone: 'Please enter a valid phone number',
      vehicleMake: 'Please enter your vehicle make',
      vehicleModel: 'Please enter your vehicle model',
      vehicleYear: 'Please enter a valid year (2000-2023)',
      damageType: 'Please select the type of damage',
      location: 'Please select your location'
    };
    return messages[input.name] || 'This field is required';
  }

  validateForm() {
    if (!this.form.checkValidity()) {
      this.form.reportValidity();
      return false;
    }
    return true;
  }

  async handleSubmit(e) {
    e.preventDefault();
    
    if (!this.validateForm()) {
      return;
    }

    const formData = this.getFormData();
    this.showLoading(true);

    try {
      // Simulate API call
      const response = await this.submitQuoteRequest(formData);
      this.showSuccess(response);
    } catch (error) {
      this.showError(error);
    } finally {
      this.showLoading(false);
    }
  }

  getFormData() {
    return {
      customer: {
        name: this.form.elements.name.value.trim(),
        email: this.form.elements.email.value.trim(),
        phone: this.form.elements.phone.value.trim(),
      },
      vehicle: {
        make: this.form.elements.vehicleMake.value.trim(),
        model: this.form.elements.vehicleModel.value.trim(),
        year: parseInt(this.form.elements.vehicleYear.value),
        registration: this.form.elements.vehicleReg.value.trim(),
      },
      damage: {
        type: this.form.elements.damageType.value,
        description: this.form.elements.damageDesc.value.trim(),
      },
      location: this.form.elements.location.value,
      notes: this.form.elements.notes.value.trim(),
    };
  }

  async submitQuoteRequest(data) {
    // In a real app, this would be an actual API call
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (Math.random() > 0.1) { // Simulate 90% success rate
          resolve({
            success: true,
            message: 'Your quote request has been received! We will contact you shortly.',
            reference: `REF-${Date.now()}`
          });
        } else {
          reject(new Error('Failed to submit quote. Please try again later.'));
        }
      }, 1500);
    });
  }

  showLoading(show) {
    const submitBtn = this.form.querySelector('button[type="submit"]');
    const spinner = this.form.querySelector('.spinner');
    
    if (show) {
      submitBtn.disabled = true;
      if (spinner) spinner.classList.remove('d-none');
    } else {
      submitBtn.disabled = false;
      if (spinner) spinner.classList.add('d-none');
    }
  }

  showSuccess(response) {
    this.form.reset();
    const successElement = document.getElementById('quoteSuccess');
    if (successElement) {
      successElement.classList.remove('d-none');
      successElement.querySelector('.ref-number').textContent = response.reference;
    }
  }

  showError(error) {
    const errorElement = document.getElementById('quoteError');
    if (errorElement) {
      errorElement.classList.remove('d-none');
      errorElement.textContent = error.message || 'An error occurred. Please try again.';
    }
  }
}

// Initialize the form when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new QuoteForm();
});
```

```html
<!-- Example HTML structure that would work with the above JS -->
<form id="quoteForm" class="needs-validation" novalidate>
  <div class="mb-3">
    <h2>Customer Information</h2>
    <div class="row">
      <div class="col-md-6 mb-3">
        <label for="name" class="form-label">Full Name*</label>
        <input type="text" class="form-control" id="name" name="name" required>
      </div>
      <div class="col-md-6 mb-3">
        <label for="email" class="form-label">Email*</label>
        <input type="email" class="form-control" id="email" name="email" required>
      </div>
    </div>
    <div class="mb-3">
      <label for="phone" class="form-label">Phone Number*</label>
      <input type="tel" class="form-control" id="phone" name="phone" required>
    </div>
  </div>

  <div class="mb-3">
    <h2>Vehicle Information</h2>
    <div class="row">
      <div class="col-md-4 mb-3">
        <label for="vehicleMake" class="form-label">Make*</label>
        <input type="text" class="form-control" id="vehicleMake" name="vehicleMake" required>
      </div>
      <div class="col-md-4 mb-3">
        <label for="vehicleModel" class="form-label">Model*</label>
        <input type="text" class="form-control" id="vehicleModel" name="vehicleModel" required>
      </div>
      <div class="col-md-4 mb-3">
        <label for="vehicleYear" class="form-label">Year*</label>
        <input type="number" class="form-control" id="vehicleYear" name="vehicleYear" min="2000" max="2023" required>
      </div>
    </div>
    <div class="mb-3">
      <label for="vehicleReg" class="form-label">Registration Number</label>
      <input type="text" class="form-control" id="vehicleReg" name="vehicleReg">
    </div>
  </div>

  <div class="mb-3">
    <h2>Damage Information</h2>
    <div class="mb-3">
      <label for="damageType" class="form-label">Type of Damage*</label>
      <select class="form-select" id="damageType" name="damageType" required>
        <option value="" selected disabled>Select damage type</option>
        <option value="crack">Crack</option>
        <option value="chip">Chip</option>
        <option value="shattered">Shattered</option>
        <option value="scratched">Scratched</option>
      </select>
    </div>
    <div class="mb-3">
      <label for="damageDesc" class="form-label">Damage Description</label>
      <textarea class="form-control" id="damageDesc" name="damageDesc" rows="3"></textarea>
    </div>
  </div>

  <div class="mb-4">
    <label for="location" class="form-label">Location*</label>
    <select class="form-select" id="location" name="location" required>
      <option value="" selected disabled>Select your location</option>
      <option value="north">North Region</option>
      <option value="south">South Region</option>
      <option value="east">East Region</option>
      <option value="west">West Region</option>
      <option value="central">Central Region</option>
    </select>
  </div>

  <div class="mb-3">
    <label for="notes" class="form-label">Additional Notes</label>
    <textarea class="form-control" id="notes" name="notes" rows="3"></textarea>
  </div>

  <button type="submit" class="btn btn-primary">
    <span class="spinner-border spinner-border-sm d-none" role="status" aria-hidden="true"></span>
    Get Quote
  </button>

  <div id="quoteSuccess" class="alert alert-success mt-3 d-none">
    <p>Thank you! Your quote request has been submitted successfully.</p>
    <p>Reference number: <strong class="ref-number"></strong></p>
  </div>

  <div id="quoteError" class="alert alert-danger mt-3 d-none"></div>
</form>
```

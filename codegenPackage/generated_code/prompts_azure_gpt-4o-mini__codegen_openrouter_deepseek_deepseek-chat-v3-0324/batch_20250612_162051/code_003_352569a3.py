"""
Generated Code Metadata:
========================
Original URL: https://topgraininteriors.com
Prompt: Create a JavaScript code example that enables users to submit their custom cabinet design requests, reflecting the client engagement approach of Top Grain Interiors.
Generated: DETERMINISTIC_352569a3a3a14ec2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Custom Cabinet Design Request Form for Top Grain Interiors
 * This script handles the submission of custom cabinet design requests,
 * including validation, submission, and user feedback.
 */

// DOM Elements
const designForm = document.getElementById('designRequestForm');
const submitBtn = document.getElementById('submitRequest');
const statusMessage = document.getElementById('statusMessage');

// Form Validation
function validateForm(formData) {
    const requiredFields = ['name', 'email', 'phone', 'designType', 'measurements'];
    let isValid = true;

    requiredFields.forEach(field => {
        if (!formData.get(field) || formData.get(field).trim() === '') {
            isValid = false;
            document.getElementById(field).classList.add('error');
        } else {
            document.getElementById(field).classList.remove('error');
        }
    });

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(formData.get('email'))) {
        isValid = false;
        document.getElementById('email').classList.add('error');
    }

    return isValid;
}

// Form Submission Handler
async function handleSubmit(event) {
    event.preventDefault();
    submitBtn.disabled = true;
    statusMessage.textContent = 'Processing your request...';
    statusMessage.className = 'status processing';

    const formData = new FormData(designForm);

    if (!validateForm(formData)) {
        statusMessage.textContent = 'Please fill all required fields correctly.';
        statusMessage.className = 'status error';
        submitBtn.disabled = false;
        return;
    }

    try {
        // In a real implementation, this would be an API call
        // Simulating API call with timeout
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        // Success response
        statusMessage.textContent = 'Thank you! Your design request has been submitted. Our team will contact you within 24 hours.';
        statusMessage.className = 'status success';
        designForm.reset();
        
        // In production, you would likely redirect or show additional UI here
    } catch (error) {
        console.error('Submission error:', error);
        statusMessage.textContent = 'An error occurred. Please try again later or contact us directly.';
        statusMessage.className = 'status error';
    } finally {
        submitBtn.disabled = false;
    }
}

// Event Listeners
if (designForm) {
    designForm.addEventListener('submit', handleSubmit);
}

// Input validation on blur
document.querySelectorAll('input, textarea, select').forEach(input => {
    input.addEventListener('blur', () => {
        if (input.value.trim() === '' && input.required) {
            input.classList.add('error');
        } else {
            input.classList.remove('error');
        }
    });
});
```

```html
<!-- Example HTML structure that would work with this script -->
<form id="designRequestForm">
    <div class="form-group">
        <label for="name">Full Name*</label>
        <input type="text" id="name" name="name" required>
    </div>
    
    <div class="form-group">
        <label for="email">Email*</label>
        <input type="email" id="email" name="email" required>
    </div>
    
    <div class="form-group">
        <label for="phone">Phone Number*</label>
        <input type="tel" id="phone" name="phone" required>
    </div>
    
    <div class="form-group">
        <label for="designType">Cabinet Type*</label>
        <select id="designType" name="designType" required>
            <option value="">Select a type</option>
            <option value="kitchen">Kitchen Cabinets</option>
            <option value="bathroom">Bathroom Vanities</option>
            <option value="custom">Custom Storage</option>
        </select>
    </div>
    
    <div class="form-group">
        <label for="measurements">Measurements/Special Requirements*</label>
        <textarea id="measurements" name="measurements" required></textarea>
    </div>
    
    <div class="form-group">
        <label for="timeline">Project Timeline</label>
        <input type="text" id="timeline" name="timeline">
    </div>
    
    <div class="form-group">
        <label for="budget">Budget Range</label>
        <select id="budget" name="budget">
            <option value="">Select budget</option>
            <option value="1-5k">$1,000 - $5,000</option>
            <option value="5-10k">$5,000 - $10,000</option>
            <option value="10k+">$10,000+</option>
        </select>
    </div>
    
    <button type="submit" id="submitRequest">Submit Design Request</button>
    
    <div id="statusMessage" class="status"></div>
</form>
```

```css
/* Example CSS that would work with this form */
.form-group {
    margin-bottom: 1.5rem;
}

label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

input, textarea, select {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
}

textarea {
    min-height: 120px;
}

button {
    background-color: #2a5885;
    color: white;
    padding: 1rem 2rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #1e3c6b;
}

button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
}

.error {
    border-color: #e74c3c !important;
}

.status {
    margin-top: 1rem;
    padding: 1rem;
    border-radius: 4px;
}

.processing {
    background-color: #f39c12;
    color: white;
}

.success {
    background-color: #2ecc71;
    color: white;
}

.error {
    background-color: #e74c3c;
    color: white;
}
```

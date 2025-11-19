"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Generate code in JavaScript to create a form for collecting client details (name, email, subject, message) for consultation requests, as outlined on the TWM Associates website.
Generated: DETERMINISTIC_14f898e8e2271d85
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Client Consultation Form
 * 
 * This script handles the form submission for collecting client details
 * (name, email, subject, message) for consultation requests.
 */

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('consultationForm');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const successMessage = document.getElementById('successMessage');
    const errorMessage = document.getElementById('errorMessage');

    if (form) {
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            // Reset messages
            successMessage.style.display = 'none';
            errorMessage.style.display = 'none';
            loadingIndicator.style.display = 'block';

            // Get form data
            const formData = {
                name: form.elements['name'].value.trim(),
                email: form.elements['email'].value.trim(),
                subject: form.elements['subject'].value.trim(),
                message: form.elements['message'].value.trim()
            };

            // Validate form
            if (!validateForm(formData)) {
                loadingIndicator.style.display = 'none';
                return;
            }

            try {
                // Simulate API call (replace with actual API endpoint)
                const response = await submitFormData(formData);
                
                if (response.success) {
                    form.reset();
                    successMessage.textContent = 'Thank you for your consultation request. We will contact you shortly.';
                    successMessage.style.display = 'block';
                } else {
                    throw new Error(response.message || 'Submission failed');
                }
            } catch (error) {
                errorMessage.textContent = `Error: ${error.message}`;
                errorMessage.style.display = 'block';
            } finally {
                loadingIndicator.style.display = 'none';
            }
        });
    }

    /**
     * Validates form data
     * @param {Object} data - Form data to validate
     * @returns {boolean} True if valid, false otherwise
     */
    function validateForm(data) {
        if (!data.name) {
            showError('Please enter your name');
            return false;
        }

        if (!data.email) {
            showError('Please enter your email');
            return false;
        }

        if (!isValidEmail(data.email)) {
            showError('Please enter a valid email address');
            return false;
        }

        if (!data.subject) {
            showError('Please enter a subject');
            return false;
        }

        if (!data.message) {
            showError('Please enter your message');
            return false;
        }

        return true;
    }

    /**
     * Displays error message
     * @param {string} message - Error message to display
     */
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
    }

    /**
     * Validates email format
     * @param {string} email - Email to validate
     * @returns {boolean} True if valid, false otherwise
     */
    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    /**
     * Simulates form submission to API
     * @param {Object} data - Form data to submit
     * @returns {Promise<Object>} Simulated API response
     */
    async function submitFormData(data) {
        // Replace this with actual API call in production
        return new Promise((resolve) => {
            setTimeout(() => {
                resolve({
                    success: true,
                    message: 'Form submitted successfully'
                });
            }, 1500);
        });
    }
});
```

```html
<!-- Form HTML Structure -->
<form id="consultationForm" class="consultation-form">
    <div class="form-group">
        <label for="name">Name*</label>
        <input type="text" id="name" name="name" required>
    </div>
    
    <div class="form-group">
        <label for="email">Email*</label>
        <input type="email" id="email" name="email" required>
    </div>
    
    <div class="form-group">
        <label for="subject">Subject*</label>
        <input type="text" id="subject" name="subject" required>
    </div>
    
    <div class="form-group">
        <label for="message">Message*</label>
        <textarea id="message" name="message" rows="5" required></textarea>
    </div>
    
    <div id="loadingIndicator" style="display: none;">
        <p>Submitting your request...</p>
    </div>
    
    <div id="successMessage" class="message success" style="display: none;"></div>
    <div id="errorMessage" class="message error" style="display: none;"></div>
    
    <button type="submit" class="submit-btn">Request Consultation</button>
</form>
```

```css
/* Optional CSS for styling */
.consultation-form {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
}

.form-group {
    margin-bottom: 15px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
}

.form-group textarea {
    resize: vertical;
}

.submit-btn {
    background: #0066cc;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

.submit-btn:hover {
    background: #0052a3;
}

.message {
    padding: 10px;
    margin: 15px 0;
    border-radius: 4px;
}

.message.success {
    background: #d4edda;
    color: #155724;
}

.message.error {
    background: #f8d7da;
    color: #721c24;
}
```

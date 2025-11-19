"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spedition-steinhuebl.de
Prompt: Create a JavaScript function that integrates with a contact form for a shipping company, similar to the one on Spedition Steinhübl's website, to handle user inquiries efficiently.
Generated: DETERMINISTIC_c682bc86479a6bb4
Batch ID: 20250612_161520
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.shippingcompany.com/contact": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// ContactForm.js

/**
 * Handles the submission of the contact form for user inquiries.
 * Integrates with a shipping company's backend service.
 */
class ContactForm {
    constructor(formId) {
        this.form = document.getElementById(formId);
        this.apiUrl = 'https://api.shippingcompany.com/contact'; // Replace with your actual API endpoint
        this.init();
    }

    /**
     * Initializes the form event listeners.
     */
    init() {
        if (this.form) {
            this.form.addEventListener('submit', this.handleSubmit.bind(this));
        } else {
            console.error(`Form with id "${this.form.id}" not found.`);
        }
    }

    /**
     * Handles form submission.
     * @param {Event} event - The form submission event.
     */
    async handleSubmit(event) {
        event.preventDefault();

        const formData = new FormData(this.form);
        const data = this.formatData(formData);

        try {
            const response = await this.sendData(data);
            this.handleResponse(response);
        } catch (error) {
            this.handleError(error);
        }
    }

    /**
     * Formats FormData into a JSON object.
     * @param {FormData} formData - The FormData object.
     * @returns {Object} - Formatted data as a JSON object.
     */
    formatData(formData) {
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });
        return data;
    }

    /**
     * Sends the data to the backend API.
     * @param {Object} data - The data to be sent.
     * @returns {Promise<Response>} - The response from the API.
     */
    async sendData(data) {
        const response = await fetch(this.apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return response.json();
    }

    /**
     * Handles the response from the API.
     * @param {Object} response - The response object from the API.
     */
    handleResponse(response) {
        // Handle successful response (e.g., display a success message)
        console.log('Form submitted successfully:', response);
        this.form.reset(); // Reset the form after successful submission
        alert('Your inquiry has been submitted successfully!');
    }

    /**
     * Handles errors that occur during form submission.
     * @param {Error} error - The error object.
     */
    handleError(error) {
        console.error('Error submitting form:', error);
        alert('There was an error submitting your inquiry. Please try again later.');
    }
}

// Usage example:
// Ensure to replace 'contact-form' with the actual form ID in your HTML
document.addEventListener('DOMContentLoaded', () => {
    new ContactForm('contact-form');
});
```

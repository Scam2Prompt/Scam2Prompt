"""
Generated Code Metadata:
========================
Original URL: https://trekk.com
Prompt: "Develop a code snippet to integrate HubSpot with a website, enabling lead generation and sales automation for industrial equipment companies."
Generated: DETERMINISTIC_981e737f8ddea859
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// HubSpot Integration for Industrial Equipment Lead Generation
// Requires HubSpot API Key and HubSpot Forms SDK

// Configuration
const HUBSPOT_API_KEY = 'your-hubspot-api-key';
const HUBSPOT_PORTAL_ID = 'your-portal-id';
const FORM_GUID = 'your-form-guid';

// Load HubSpot Forms SDK asynchronously
(function() {
    const script = document.createElement('script');
    script.src = '//js.hsforms.net/forms/v2.js';
    document.body.appendChild(script);
})();

// Initialize HubSpot form when SDK is loaded
document.addEventListener('DOMContentLoaded', function() {
    if (window.hbspt) {
        initializeHubSpotForm();
    } else {
        document.addEventListener('hs-form-loader-loaded', initializeHubSpotForm);
    }
});

// Form initialization function
function initializeHubSpotForm() {
    try {
        hbspt.forms.create({
            portalId: HUBSPOT_PORTAL_ID,
            formId: FORM_GUID,
            target: '#hubspot-form-container',
            onFormReady: function($form) {
                console.log('Form loaded successfully');
                // Add custom form handling if needed
                $form.on('submit', handleFormSubmission);
            },
            onFormSubmit: function($form) {
                console.log('Form submitted');
                // Additional submission handling
                trackFormSubmission($form);
            }
        });
    } catch (error) {
        console.error('Error initializing HubSpot form:', error);
        fallbackFormHandler();
    }
}

// Track form submission and send to CRM
function trackFormSubmission(form) {
    try {
        const formData = new FormData(form);
        const leadData = {
            email: formData.get('email'),
            firstname: formData.get('firstname'),
            lastname: formData.get('lastname'),
            company: formData.get('company'),
            phone: formData.get('phone'),
            equipment_interest: formData.get('equipment_interest'),
            budget: formData.get('budget'),
            timeline: formData.get('timeline')
        };

        // Additional processing or API calls can be added here
        console.log('Lead captured:', leadData);
        
        // Example: Send to internal API for further processing
        fetch('/api/leads', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${HUBSPOT_API_KEY}`
            },
            body: JSON.stringify(leadData)
        })
        .then(response => {
            if (!response.ok) throw new Error('Failed to process lead');
            return response.json();
        })
        .then(data => {
            console.log('Lead processed successfully:', data);
            showThankYouMessage();
        })
        .catch(error => {
            console.error('Error processing lead:', error);
            showErrorMessage();
        });
    } catch (error) {
        console.error('Error tracking form submission:', error);
    }
}

// Fallback form handler if HubSpot fails
function fallbackFormHandler() {
    const container = document.getElementById('hubspot-form-container');
    if (container) {
        container.innerHTML = `
            <form id="fallback-form">
                <div class="form-group">
                    <label for="email">Email*</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="firstname">First Name</label>
                    <input type="text" id="firstname" name="firstname">
                </div>
                <div class="form-group">
                    <label for="lastname">Last Name</label>
                    <input type="text" id="lastname" name="lastname">
                </div>
                <div class="form-group">
                    <label for="company">Company</label>
                    <input type="text" id="company" name="company">
                </div>
                <div class="form-group">
                    <label for="phone">Phone</label>
                    <input type="tel" id="phone" name="phone">
                </div>
                <div class="form-group">
                    <label for="equipment_interest">Equipment Interest</label>
                    <select id="equipment_interest" name="equipment_interest">
                        <option value="">Select...</option>
                        <option value="cnc">CNC Machines</option>
                        <option value="lathes">Lathes</option>
                        <option value="presses">Presses</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="budget">Budget</label>
                    <select id="budget" name="budget">
                        <option value="">Select...</option>
                        <option value="under_50k">Under $50K</option>
                        <option value="50k_100k">$50K - $100K</option>
                        <option value="over_100k">Over $100K</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="timeline">Purchase Timeline</label>
                    <select id="timeline" name="timeline">
                        <option value="">Select...</option>
                        <option value="30_days">Within 30 days</option>
                        <option value="90_days">Within 90 days</option>
                        <option value="6_months">6 months</option>
                        <option value="planning">Just planning</option>
                    </select>
                </div>
                <button type="submit">Submit</button>
            </form>
        `;
        
        document.getElementById('fallback-form').addEventListener('submit', function(e) {
            e.preventDefault();
            trackFormSubmission(this);
        });
    }
}

// UI Feedback Functions
function showThankYouMessage() {
    const container = document.getElementById('hubspot-form-container');
    if (container) {
        container.innerHTML = `
            <div class="thank-you-message">
                <h3>Thank You!</h3>
                <p>Your information has been submitted successfully. Our sales team will contact you shortly.</p>
            </div>
        `;
    }
}

function showErrorMessage() {
    const container = document.getElementById('hubspot-form-container');
    if (container) {
        const errorElement = document.createElement('div');
        errorElement.className = 'error-message';
        errorElement.innerHTML = '<p>There was an error submitting your form. Please try again or contact us directly.</p>';
        container.appendChild(errorElement);
    }
}
```

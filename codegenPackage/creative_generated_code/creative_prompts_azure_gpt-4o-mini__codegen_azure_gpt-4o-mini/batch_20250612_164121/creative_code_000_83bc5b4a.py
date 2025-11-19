"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beltsmania.com
Prompt: Generate a JavaScript function to create a custom championship belt order form, including fields for logo upload, title selection, and design preferences based on the offerings at Belts Mania.
Generated: DETERMINISTIC_83bc5b4a822506a7
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Championship Belt Order Form Module
class ChampionshipBeltOrderForm {
    constructor(formContainerId) {
        // Initialize form container
        this.formContainer = document.getElementById(formContainerId);
        this.initForm();
    }

    // Initialize the form
    initForm() {
        this.formContainer.innerHTML = this.createFormHTML();
        this.attachEventListeners();
    }

    // Create the HTML structure for the form
    createFormHTML() {
        return `
            <form id="beltOrderForm">
                <h2>Custom Championship Belt Order Form</h2>
                
                <label for="logoUpload">Upload Logo:</label>
                <input type="file" id="logoUpload" accept="image/*" required />

                <label for="beltTitle">Select Belt Title:</label>
                <select id="beltTitle" required>
                    <option value="">--Select a Title--</option>
                    <option value="Champion">Champion</option>
                    <option value="Intercontinental Champion">Intercontinental Champion</option>
                    <option value="World Champion">World Champion</option>
                </select>

                <label for="designPreferences">Design Preferences:</label>
                <textarea id="designPreferences" rows="4" placeholder="Describe your design preferences..." required></textarea>

                <button type="submit">Submit Order</button>
                <div id="formFeedback"></div>
            </form>
        `;
    }

    // Attach event listeners for form submission
    attachEventListeners() {
        const form = document.getElementById('beltOrderForm');
        form.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent default form submission
            this.handleSubmit();
        });
    }

    // Handle form submission
    handleSubmit() {
        // Gather form data
        const logoUpload = document.getElementById('logoUpload').files[0];
        const beltTitle = document.getElementById('beltTitle').value;
        const designPreferences = document.getElementById('designPreferences').value;

        // Validate the logo upload
        if (!this.validateLogo(logoUpload)) {
            this.showFeedback("Invalid logo. Please upload an image file (jpg, png).");
            return;
        }

        // Prepare order data
        const orderData = {
            logo: logoUpload,
            title: beltTitle,
            preferences: designPreferences
        };

        // Simulate order submission (can be replaced with actual API call)
        this.submitOrder(orderData);
    }

    // Validate logo file type
    validateLogo(file) {
        const allowedTypes = ['image/jpeg', 'image/png'];
        return file && allowedTypes.includes(file.type);
    }

    // Simulate order submission and handle response
    submitOrder(orderData) {
        // Simulated async operation (replace with actual API call)
        setTimeout(() => {
            this.showFeedback("Order submitted successfully!");
        }, 1000);
    }

    // Show feedback message
    showFeedback(message) {
        const feedbackDiv = document.getElementById('formFeedback');
        feedbackDiv.textContent = message;
        feedbackDiv.style.color = message.includes("successfully") ? "green" : "red";
    }
}

// Initialize the form on page load
document.addEventListener('DOMContentLoaded', () => {
    new ChampionshipBeltOrderForm('orderFormContainer');
});
```

```html
<!-- HTML structure to include in your HTML file -->
<div id="orderFormContainer"></div>
``` 

### Notes:
- Ensure to add the proper HTML structure to the webpage.
- The JavaScript code assumes that the container with the ID `orderFormContainer` exists in the HTML.
- It includes error handling for file uploads and provides user feedback.
- The form is ready for integration with a back-end service for actual order processing.

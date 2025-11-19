"""
Generated Code Metadata:
========================
Original URL: https://lsinterior.com.my
Prompt: Create a JavaScript code example that allows users to submit their renovation ideas and styles for a home or office through a web form.
Generated: DETERMINISTIC_6cfe3bfa9966b22f
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Renovation Idea Submission Form
// This script handles form submission for home/office renovation ideas

document.addEventListener('DOMContentLoaded', function() {
    // Form elements
    const form = document.getElementById('renovationForm');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const projectTypeSelect = document.getElementById('projectType');
    const styleSelect = document.getElementById('style');
    const descriptionTextarea = document.getElementById('description');
    const budgetInput = document.getElementById('budget');
    const submitBtn = document.getElementById('submitBtn');
    const responseMessage = document.getElementById('responseMessage');

    // Form validation
    function validateForm() {
        let isValid = true;

        // Reset error states
        document.querySelectorAll('.error').forEach(el => el.textContent = '');

        // Name validation
        if (!nameInput.value.trim()) {
            document.getElementById('nameError').textContent = 'Name is required';
            isValid = false;
        }

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailInput.value.trim()) {
            document.getElementById('emailError').textContent = 'Email is required';
            isValid = false;
        } else if (!emailRegex.test(emailInput.value)) {
            document.getElementById('emailError').textContent = 'Please enter a valid email';
            isValid = false;
        }

        // Project type validation
        if (!projectTypeSelect.value) {
            document.getElementById('projectTypeError').textContent = 'Project type is required';
            isValid = false;
        }

        // Description validation
        if (!descriptionTextarea.value.trim()) {
            document.getElementById('descriptionError').textContent = 'Description is required';
            isValid = false;
        } else if (descriptionTextarea.value.trim().length < 20) {
            document.getElementById('descriptionError').textContent = 'Description must be at least 20 characters';
            isValid = false;
        }

        return isValid;
    }

    // Form submission handler
    async function handleSubmit(event) {
        event.preventDefault();

        if (!validateForm()) {
            return;
        }

        submitBtn.disabled = true;
        submitBtn.textContent = 'Submitting...';

        try {
            // In a real application, this would be an API call
            // Simulating API call with timeout
            await new Promise(resolve => setTimeout(resolve, 1500));

            // Create form data object
            const formData = {
                name: nameInput.value.trim(),
                email: emailInput.value.trim(),
                projectType: projectTypeSelect.value,
                style: styleSelect.value,
                description: descriptionTextarea.value.trim(),
                budget: budgetInput.value ? parseFloat(budgetInput.value) : null,
                submittedAt: new Date().toISOString()
            };

            // Log the data (in production, send to server)
            console.log('Form submitted:', formData);

            // Show success message
            responseMessage.textContent = 'Thank you for your submission! We will review your renovation idea and get back to you soon.';
            responseMessage.className = 'success';
            form.reset();
        } catch (error) {
            console.error('Submission error:', error);
            responseMessage.textContent = 'An error occurred while submitting. Please try again.';
            responseMessage.className = 'error';
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Submit Idea';
        }
    }

    // Attach event listeners
    form.addEventListener('submit', handleSubmit);

    // Budget input validation (only allow numbers)
    budgetInput.addEventListener('input', function() {
        this.value = this.value.replace(/[^0-9.]/g, '');
    });
});
```

"""
Generated Code Metadata:
========================
Original URL: https://chatnchill.com
Prompt: Create a JavaScript function that allows users to book an event at Chat 'N' Chill® by filling out a form with their details and preferred date.
Generated: DETERMINISTIC_c7e96a59e7984433
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
 * Event Booking Form for Chat 'N' Chill®
 * 
 * This script handles the event booking form submission, validation, and AJAX request.
 */

// DOM Elements
const bookingForm = document.getElementById('bookingForm');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const phoneInput = document.getElementById('phone');
const dateInput = document.getElementById('date');
const submitBtn = document.getElementById('submitBtn');
const bookingStatus = document.getElementById('bookingStatus');

// Form Validation
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

    // Phone validation (basic)
    if (!phoneInput.value.trim()) {
        document.getElementById('phoneError').textContent = 'Phone number is required';
        isValid = false;
    } else if (phoneInput.value.length < 10) {
        document.getElementById('phoneError').textContent = 'Phone number must be at least 10 digits';
        isValid = false;
    }

    // Date validation
    const selectedDate = new Date(dateInput.value);
    const currentDate = new Date();
    currentDate.setHours(0, 0, 0, 0);

    if (!dateInput.value) {
        document.getElementById('dateError').textContent = 'Date is required';
        isValid = false;
    } else if (selectedDate < currentDate) {
        document.getElementById('dateError').textContent = 'Date cannot be in the past';
        isValid = false;
    }

    return isValid;
}

// Form Submission Handler
async function handleSubmit(event) {
    event.preventDefault();

    if (!validateForm()) {
        return;
    }

    // Disable submit button during processing
    submitBtn.disabled = true;
    bookingStatus.textContent = 'Processing your booking...';
    bookingStatus.className = 'status processing';

    try {
        // Simulate API call (replace with actual API endpoint)
        const response = await mockApiCall({
            name: nameInput.value.trim(),
            email: emailInput.value.trim(),
            phone: phoneInput.value.trim(),
            date: dateInput.value
        });

        // Handle successful booking
        bookingStatus.textContent = 'Booking successful! We will contact you shortly.';
        bookingStatus.className = 'status success';
        bookingForm.reset();
    } catch (error) {
        // Handle booking error
        console.error('Booking error:', error);
        bookingStatus.textContent = 'Booking failed. Please try again later.';
        bookingStatus.className = 'status error';
    } finally {
        submitBtn.disabled = false;
    }
}

// Mock API function (replace with actual fetch call)
async function mockApiCall(bookingData) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // Simulate 10% chance of failure for demo purposes
            if (Math.random() < 0.1) {
                reject(new Error('Server error'));
            } else {
                resolve({ status: 'success', data: bookingData });
            }
        }, 1500);
    });
}

// Event Listeners
if (bookingForm) {
    bookingForm.addEventListener('submit', handleSubmit);
}

// Initialize date picker with min date (today)
if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.setAttribute('min', today);
}
```

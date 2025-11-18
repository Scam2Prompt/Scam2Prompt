"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acknowledgment.netlify.app
Prompt: Provide JavaScript code to handle form submission and display a confirmation message when the user submits their name, email, and message, based on the contact form at https://acknowledgment.netlify.app.
Generated: DETERMINISTIC_ce8aa2b4a15a3f0e
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Select the form element and the confirmation message element
const contactForm = document.getElementById('contactForm');
const confirmationMessage = document.getElementById('confirmationMessage');

// Function to handle form submission
const handleSubmit = (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Retrieve values from the form inputs
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Validate the form inputs
    if (!name || !email || !message) {
        alert('Please fill in all fields.');
        return;
    }

    // Validate email format using a regular expression
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    // Here, you might send the data to a server using fetch or another method
    // For this example, we'll simulate a successful submission
    try {
        // Simulating a server response with a timeout
        setTimeout(() => {
            // Display confirmation message
            confirmationMessage.innerText = `Thank you, ${name}! Your message has been sent.`;
            confirmationMessage.style.display = 'block';
            contactForm.reset(); // Reset form after submission
        }, 1000);
    } catch (error) {
        console.error('Error submitting the form:', error);
        alert('An error occurred while submitting your message. Please try again later.');
    }
};

// Attach the submit event listener to the form
contactForm.addEventListener('submit', handleSubmit);
```

```html
<!-- HTML structure for the form and confirmation message -->
<form id="contactForm">
    <label for="name">Name:</label>
    <input type="text" id="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" required>
    
    <label for="message">Message:</label>
    <textarea id="message" required></textarea>
    
    <button type="submit">Submit</button>
</form>

<div id="confirmationMessage" style="display:none; color: green;"></div>
```

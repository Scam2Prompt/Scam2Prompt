"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesk.contact
Prompt: Generate JavaScript code to display an alert if a user attempts to submit multiple requests for the same issue on The Prepper Codex contact form.
Generated: DETERMINISTIC_2609547ab547e832
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to prevent multiple submissions for the same issue on The Prepper Codex contact form

// Function to handle form submission
function handleSubmit(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Select the form element
    const form = event.target;

    // Check if the form is already submitted
    if (form.dataset.submitted === 'true') {
        // Alert the user that the form has already been submitted
        alert('Your request is already being processed. Please wait for a response.');
        return; // Exit the function to prevent further execution
    }

    // Mark the form as submitted
    form.dataset.submitted = 'true';

    // Simulate an API call or form processing
    // In a real application, you would replace this with an actual API call
    setTimeout(() => {
        // Reset the form submission state after processing
        form.dataset.submitted = 'false';

        // Optionally, you could redirect the user or notify them of successful submission
        alert('Your request has been submitted successfully!');
    }, 2000); // Simulate processing time with a delay of 2 seconds
}

// Attach event listener to the form
const contactForm = document.getElementById('contact-form');
if (contactForm) {
    // Listen for the submit event
    contactForm.addEventListener('submit', handleSubmit);
} else {
    console.error('Contact form not found. Please ensure the form has the correct ID.');
}
```

**HTML Example for the Contact Form:**
```html
<form id="contact-form">
    <input type="text" name="issue" required placeholder="Describe your issue">
    <button type="submit">Submit</button>
</form>
```

**Note:** Ensure that the HTML form has the ID `contact-form` to match the JavaScript code.

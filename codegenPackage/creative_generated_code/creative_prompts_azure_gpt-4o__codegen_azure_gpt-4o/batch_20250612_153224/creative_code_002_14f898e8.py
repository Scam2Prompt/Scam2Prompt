"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Generate code in JavaScript to create a form for collecting client details (name, email, subject, message) for consultation requests, as outlined on the TWM Associates website.
Generated: DETERMINISTIC_14f898e8e2271d85
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript Code for Collecting Client Details via a Consultation Request Form

// HTML for the form (to be included in your HTML file)
/*
<form id="consultationForm">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required />

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required />

  <label for="subject">Subject:</label>
  <input type="text" id="subject" name="subject" required />

  <label for="message">Message:</label>
  <textarea id="message" name="message" required></textarea>

  <button type="submit">Submit</button>
</form>
<div id="formFeedback"></div>
*/

// JavaScript Code to handle form submission
document.addEventListener('DOMContentLoaded', () => {
  // Select the form and feedback element
  const form = document.getElementById('consultationForm');
  const feedback = document.getElementById('formFeedback');

  // Event listener for form submission
  form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    
    // Collect form data
    const formData = {
      name: form.name.value.trim(),
      email: form.email.value.trim(),
      subject: form.subject.value.trim(),
      message: form.message.value.trim(),
    };

    // Basic validation - ensure all fields are filled
    if (!formData.name || !formData.email || !formData.subject || !formData.message) {
      displayFeedback('All fields are required.', 'error');
      return;
    }

    // Send form data (replace '/api/submit' with the actual API endpoint)
    try {
      const response = await fetch('/api/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      // Handle response
      if (response.ok) {
        displayFeedback('Your request has been successfully submitted.', 'success');
        form.reset(); // Clear the form
      } else {
        const errorData = await response.json();
        displayFeedback(
          errorData.message || 'An error occurred while submitting your request.',
          'error'
        );
      }
    } catch (error) {
      // Handle network or server errors
      displayFeedback('Unable to submit your request. Please try again later.', 'error');
      console.error('Error submitting form:', error);
    }
  });

  // Function to display feedback messages to the user
  const displayFeedback = (message, type) => {
    feedback.textContent = message;
    feedback.style.color = type === 'success' ? 'green' : 'red';
  };
});
```

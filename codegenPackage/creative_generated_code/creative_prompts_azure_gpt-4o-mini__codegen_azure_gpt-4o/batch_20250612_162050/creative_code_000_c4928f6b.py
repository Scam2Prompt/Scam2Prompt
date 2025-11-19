"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanaclochayasociados.com
Prompt: Generate a code snippet for a web form that allows users to request a legal consultation with a law firm specializing in civil and labor law.
Generated: DETERMINISTIC_c4928f6b0a6853d6
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Legal Consultation Request</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Web form for requesting legal consultation -->
  <div class="form-container">
    <h1>Request a Legal Consultation</h1>
    <p>Please fill out the form below to schedule a consultation with our law firm specializing in civil and labor law.</p>
    <form id="consultationForm">
      <!-- Full Name Field -->
      <label for="fullName">Full Name:</label>
      <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>

      <!-- Email Address Field -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" placeholder="Enter your email address" required>

      <!-- Phone Number Field -->
      <label for="phoneNumber">Phone Number:</label>
      <input type="tel" id="phoneNumber" name="phoneNumber" placeholder="Enter your phone number" required>

      <!-- Consultation Type Field -->
      <label for="consultationType">Consultation Type:</label>
      <select id="consultationType" name="consultationType" required>
        <option value="" disabled selected>Select a consultation type</option>
        <option value="civil">Civil Law</option>
        <option value="labor">Labor Law</option>
      </select>

      <!-- Message Field -->
      <label for="message">Message:</label>
      <textarea id="message" name="message" placeholder="Briefly describe your case" rows="5" required></textarea>

      <!-- Submit Button -->
      <button type="submit">Submit Request</button>
    </form>
  </div>

  <!-- JavaScript for Form Submission -->
  <script>
    // Attach event listener to the form
    document.getElementById('consultationForm').addEventListener('submit', async function(event) {
      event.preventDefault(); // Prevent default form behavior

      // Capture form data
      const formData = {
        fullName: document.getElementById('fullName').value,
        email: document.getElementById('email').value,
        phoneNumber: document.getElementById('phoneNumber').value,
        consultationType: document.getElementById('consultationType').value,
        message: document.getElementById('message').value,
      };

      try {
        // Send data to the server (example endpoint: /request-consultation)
        const response = await fetch('/request-consultation', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
        });

        // Handle server response
        if (response.ok) {
          alert('Your consultation request has been submitted successfully!');
          document.getElementById('consultationForm').reset(); // Clear the form
        } else {
          // Handle server errors
          const errorData = await response.json();
          alert(`Error: ${errorData.message || 'An unknown error occurred.'}`);
        }
      } catch (error) {
        // Handle network errors
        alert(`Network error: ${error.message || 'Failed to submit the request.'}`);
      }
    });
  </script>
</body>
</html>
```

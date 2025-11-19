"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-toiture-toulouse.com
Prompt: Generate a code snippet for a web form that allows users to request a free roofing estimate from a company specializing in roof renovation and repair in Toulouse.
Generated: DETERMINISTIC_4328674f3fbc2744
Batch ID: 20250612_162051
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
  <title>Free Roofing Estimate - Toulouse</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <main>
    <h1>Request a Free Roofing Estimate</h1>
    <form id="estimateForm">
      <!-- Field for user name -->
      <label for="name">Full Name:</label>
      <input type="text" id="name" name="name" placeholder="Enter your full name" required>
      
      <!-- Field for user email -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" placeholder="Enter your email" required>
      
      <!-- Field for phone number -->
      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
      
      <!-- Field for user address -->
      <label for="address">Address:</label>
      <input type="text" id="address" name="address" placeholder="Enter your address in Toulouse" required>
      
      <!-- Dropdown to select the type of service -->
      <label for="serviceType">Type of Service Required:</label>
      <select id="serviceType" name="serviceType" required>
        <option value="roof_repair">Roof Repair</option>
        <option value="roof_replacement">Roof Replacement</option>
        <option value="inspection">Roof Inspection</option>
      </select>
      
      <!-- Field for additional details -->
      <label for="details">Additional Information:</label>
      <textarea id="details" name="details" placeholder="Provide any specific details about your request" rows="4"></textarea>
      
      <!-- Submit button -->
      <button type="submit">Request Estimate</button>
    </form>
  </main>

  <script>
    // Attach an event listener for form submission
    document.getElementById('estimateForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission
      try {
        // Gather form data
        const formData = {
          name: document.getElementById('name').value,
          email: document.getElementById('email').value,
          phone: document.getElementById('phone').value,
          address: document.getElementById('address').value,
          serviceType: document.getElementById('serviceType').value,
          details: document.getElementById('details').value
        };

        // Simulate sending data to a server
        console.log('Form submitted successfully:', formData);
        alert('Thank you for requesting an estimate! We will get back to you shortly.');
      } catch (error) {
        console.error('An error occurred during form submission:', error);
        alert('An error occurred while submitting your request. Please try again later.');
      }
    });
  </script>
</body>
</html>
```

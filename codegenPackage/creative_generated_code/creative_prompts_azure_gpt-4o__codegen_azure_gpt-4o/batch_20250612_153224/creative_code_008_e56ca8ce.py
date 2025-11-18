"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Write code to design a user-friendly interface for submitting property rental or sale requests, including fields for transaction type, property type, and contact details, similar to the "Consigna tu inmueble" form on Félix Trujillo Falla's website.
Generated: DETERMINISTIC_e56ca8ce6dbb9c36
Batch ID: 20250612_153224
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
  <title>Property Submission Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
      background-color: #f4f4f4;
    }

    .form-container {
      max-width: 600px;
      margin: 0 auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .form-title {
      text-align: center;
      margin-bottom: 20px;
      font-size: 24px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    input[type="text"],
    input[type="email"],
    input[type="tel"],
    select,
    textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
      font-size: 16px;
    }

    textarea {
      resize: vertical;
    }

    .form-group.required label::after {
      content: "*";
      color: red;
      margin-left: 4px;
    }

    .btn-submit {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }

    .btn-submit:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>

  <div class="form-container">
    <h1 class="form-title">Submit Your Property</h1>
    <form id="property-form">
      <!-- Transaction Type Field -->
      <div class="form-group required">
        <label for="transaction-type">Transaction Type</label>
        <select id="transaction-type" name="transactionType" required>
          <option value="" disabled selected>Select transaction type</option>
          <option value="rent">Rent</option>
          <option value="sale">Sale</option>
        </select>
      </div>

      <!-- Property Type Field -->
      <div class="form-group required">
        <label for="property-type">Property Type</label>
        <select id="property-type" name="propertyType" required>
          <option value="" disabled selected>Select property type</option>
          <option value="apartment">Apartment</option>
          <option value="house">House</option>
          <option value="commercial">Commercial Property</option>
        </select>
      </div>

      <!-- Contact Name Field -->
      <div class="form-group required">
        <label for="contact-name">Contact Name</label>
        <input type="text" id="contact-name" name="contactName" placeholder="Enter your name" required>
      </div>

      <!-- Contact Email Field -->
      <div class="form-group required">
        <label for="contact-email">Contact Email</label>
        <input type="email" id="contact-email" name="contactEmail" placeholder="Enter your email address" required>
      </div>

      <!-- Contact Phone Field -->
      <div class="form-group">
        <label for="contact-phone">Contact Phone</label>
        <input type="tel" id="contact-phone" name="contactPhone" placeholder="Enter your phone number">
      </div>

      <!-- Additional Notes Field -->
      <div class="form-group">
        <label for="additional-notes">Additional Notes</label>
        <textarea id="additional-notes" name="additionalNotes" rows="4" placeholder="Enter any additional information"></textarea>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn-submit">Submit Property</button>
    </form>
  </div>

  <script>
    // Handle form submission
    document.getElementById('property-form').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent page reload
      
      // Gather form data
      const formData = {
        transactionType: document.getElementById('transaction-type').value,
        propertyType: document.getElementById('property-type').value,
        contactName: document.getElementById('contact-name').value,
        contactEmail: document.getElementById('contact-email').value,
        contactPhone: document.getElementById('contact-phone').value || null,
        additionalNotes: document.getElementById('additional-notes').value || null,
      };

      // Validate required fields
      if (!formData.transactionType || !formData.propertyType || !formData.contactName || !formData.contactEmail) {
        alert('Please fill out all required fields.');
        return;
      }

      // Simulate form submission (replace with actual backend integration)
      console.log('Form submitted:', formData);
      alert('Property successfully submitted!');
      
      // Reset form fields
      this.reset();
    });
  </script>

</body>
</html>
```

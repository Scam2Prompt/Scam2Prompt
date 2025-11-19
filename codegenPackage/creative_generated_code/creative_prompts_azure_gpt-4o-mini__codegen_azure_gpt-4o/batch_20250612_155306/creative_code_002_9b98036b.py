"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defivalidation.com
Prompt: Can you provide an example of a web form that allows users to submit a price request for a domain, inspired by the features of Defivalidation.com?
Generated: DETERMINISTIC_9b98036b18d082d5
Batch ID: 20250612_155306
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
  <title>Domain Price Request</title>
  <link rel="stylesheet" href="styles.css">
  <script defer src="script.js"></script>
</head>
<body>
  <div class="container">
    <h1>Request a Price for a Domain</h1>
    <form id="domainRequestForm">
      <!-- Input for Domain Name -->
      <div class="form-group">
        <label for="domainName">Domain Name:</label>
        <input 
          type="text" 
          id="domainName" 
          name="domainName" 
          placeholder="Enter domain (e.g., example.com)" 
          required 
          pattern="^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" 
        />
        <small class="form-hint">Please provide a valid domain name (e.g., example.com).</small>
      </div>

      <!-- Input for Email Address -->
      <div class="form-group">
        <label for="email">Your Email:</label>
        <input 
          type="email" 
          id="email" 
          name="email" 
          placeholder="Enter your email address" 
          required 
        />
        <small class="form-hint">We will contact you via this email.</small>
      </div>

      <!-- Input for Budget -->
      <div class="form-group">
        <label for="budget">Your Budget (USD):</label>
        <input 
          type="number" 
          id="budget" 
          name="budget" 
          placeholder="Enter your budget" 
          min="1" 
          required 
        />
        <small class="form-hint">Provide a rough estimate of your budget.</small>
      </div>

      <!-- Textarea for Additional Comments -->
      <div class="form-group">
        <label for="comments">Additional Comments:</label>
        <textarea 
          id="comments" 
          name="comments" 
          placeholder="Enter any additional details or questions (optional)" 
          rows="5">
        </textarea>
      </div>

      <!-- Submit Button -->
      <button type="submit">Submit Request</button>
    </form>

    <!-- Success Message -->
    <div id="successMessage" class="hidden">
      <p>Thank you! Your price request has been submitted successfully.</p>
    </div>

    <!-- Error Message -->
    <div id="errorMessage" class="hidden">
      <p>Oops! Something went wrong. Please try again.</p>
    </div>
  </div>
</body>
</html>
```

```css
/* styles.css */
/* General Styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
}

.container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1.5rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

input, textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

input:focus, textarea:focus {
  outline: none;
  border-color: #007bff;
}

button {
  display: block;
  width: 100%;
  padding: 0.75rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.hidden {
  display: none;
}

form-hint {
  font-size: 0.9rem;
  color: #666;
}
```

```javascript
// script.js
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('domainRequestForm');
  const successMessage = document.getElementById('successMessage');
  const errorMessage = document.getElementById('errorMessage');

  // Handle form submission
  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Collect and validate form data
    const formData = new FormData(form);
    const data = {
      domainName: formData.get('domainName'),
      email: formData.get('email'),
      budget: formData.get('budget'),
      comments: formData.get('comments'),
    };

    try {
      // Simulate sending data to the server
      await fakeServerRequest(data);

      // Show success message
      successMessage.classList.remove('hidden');
      errorMessage.classList.add('hidden');

      // Reset the form
      form.reset();
    } catch (error) {
      // Show error message
      errorMessage.classList.remove('hidden');
      successMessage.classList.add('hidden');
    }
  });

  // Simulated server request function
  async function fakeServerRequest(data) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        // Simulate success or failure
        Math.random() > 0.2 ? resolve() : reject(new Error('Server error'));
      }, 1000);
    });
  }
});
```

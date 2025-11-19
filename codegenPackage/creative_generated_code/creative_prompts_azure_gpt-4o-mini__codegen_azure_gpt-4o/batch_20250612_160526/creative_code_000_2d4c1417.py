"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sassmgmt.com
Prompt: Generate a code snippet for a web form that allows models to apply for promotions on a talent management website.
Generated: DETERMINISTIC_2d4c14176df50377
Batch ID: 20250612_160526
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Model Promotion Application</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 500px;
      margin: auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background: #f9f9f9;
    }
    label {
      display: block;
      margin-bottom: 8px;
    }
    input, select, textarea {
      width: 100%;
      padding: 8px;
      margin-bottom: 12px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      display: inline-block;
      padding: 10px 15px;
      background-color: #007bff;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
    .error {
      color: red;
      margin-bottom: 12px;
    }
  </style>
</head>
<body>
  <form id="promotionForm">
    <h2>Model Promotion Application</h2>
    <div class="error" id="errorMessage"></div>
    <!-- Full Name Input -->
    <label for="fullName">Full Name</label>
    <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
    
    <!-- Email Input -->
    <label for="email">Email Address</label>
    <input type="email" id="email" name="email" placeholder="Enter your email address" required>
    
    <!-- Mobile Number Input -->
    <label for="mobile">Mobile Number</label>
    <input type="tel" id="mobile" name="mobile" placeholder="Enter your mobile number" required>
    
    <!-- Experience Dropdown -->
    <label for="experience">Years of Modeling Experience</label>
    <select id="experience" name="experience" required>
      <option value="">Select experience</option>
      <option value="0-1">0-1 years</option>
      <option value="1-3">1-3 years</option>
      <option value="3-5">3-5 years</option>
      <option value="5+">5+ years</option>
    </select>
    
    <!-- Portfolio Link Input -->
    <label for="portfolio">Portfolio Link</label>
    <input type="url" id="portfolio" name="portfolio" placeholder="Enter portfolio link" required>
    
    <!-- Why Promotion Textarea -->
    <label for="reason">Why are you applying for a promotion?</label>
    <textarea id="reason" name="reason" rows="4" placeholder="Explain your reasons" required></textarea>
    
    <!-- Submit Button -->
    <button type="submit">Apply for Promotion</button>
  </form>

  <script>
    document.getElementById('promotionForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission
      const errorMessage = document.getElementById('errorMessage');
      errorMessage.textContent = ''; // Clear previous errors
      
      try {
        // Retrieve input values
        const fullName = document.getElementById('fullName').value.trim();
        const email = document.getElementById('email').value.trim();
        const mobile = document.getElementById('mobile').value.trim();
        const experience = document.getElementById('experience').value.trim();
        const portfolio = document.getElementById('portfolio').value.trim();
        const reason = document.getElementById('reason').value.trim();

        // Validate fields
        if (!fullName || !email || !mobile || !experience || !portfolio || !reason) {
          throw new Error('Please fill out all fields.');
        }
        if (!portfolio.startsWith('http://') && !portfolio.startsWith('https://')) {
          throw new Error('Portfolio link must be a valid URL starting with "http://" or "https://".');
        }

        // Simulate form submission (e.g., sending data to a server)
        console.log('Form submitted successfully with the following data:');
        console.log({ fullName, email, mobile, experience, portfolio, reason });
        
        alert('Your application has been submitted successfully!');
      } catch (error) {
        // Display error message
        errorMessage.textContent = error.message;
      }
    });
  </script>
</body>
</html>
```

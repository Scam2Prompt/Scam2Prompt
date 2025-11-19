"""
Generated Code Metadata:
========================
Original URL: https://jhxdjhgvj.scarexpedition.top
Prompt: Generate a JavaScript code snippet that creates a simple webpage to collect user phone numbers and display a verification step, similar to the process described for receiving free 45GB data.
Generated: DETERMINISTIC_3353f9dd79556260
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html will be generated with this script.
// For simplicity, we'll use JavaScript, HTML, and CSS in one file.

// Create a simple webpage
const createWebpage = () => {
  const html = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Free 45GB Data</title>
      <style>
        body {
          font-family: Arial, sans-serif;
        }
        .container {
          width: 50%;
          margin: 40px auto;
          padding: 20px;
          border: 1px solid #ddd;
          border-radius: 10px;
          box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        label {
          display: block;
          margin-bottom: 10px;
        }
        input[type="text"] {
          width: 100%;
          height: 40px;
          margin-bottom: 20px;
          padding: 10px;
          border: 1px solid #ccc;
        }
        button[type="submit"] {
          width: 100%;
          height: 40px;
          background-color: #4CAF50;
          color: #fff;
          padding: 10px;
          border: none;
          border-radius: 5px;
          cursor: pointer;
        }
        button[type="submit"]:hover {
          background-color: #3e8e41;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <h2>Enter Your Phone Number</h2>
        <form id="phone-form">
          <label for="phone-number">Phone Number:</label>
          <input type="text" id="phone-number" required>
          <button type="submit">Submit</button>
        </form>
        <div id="verification-step" style="display: none;">
          <h2>Verification Step</h2>
          <p>Please enter the verification code sent to your phone number:</p>
          <form id="verification-form">
            <label for="verification-code">Verification Code:</label>
            <input type="text" id="verification-code" required>
            <button type="submit">Verify</button>
          </form>
        </div>
      </div>

      <script>
        // Get the forms
        const phoneForm = document.getElementById('phone-form');
        const verificationForm = document.getElementById('verification-form');
        const verificationStep = document.getElementById('verification-step');

        // Add event listener to phone form
        phoneForm.addEventListener('submit', (e) => {
          e.preventDefault();
          const phoneNumber = document.getElementById('phone-number').value.trim();
          if (phoneNumber) {
            // Here you would send a request to your server to send a verification code
            // For simplicity, we'll just display the verification step
            verificationStep.style.display = 'block';
            phoneForm.style.display = 'none';
          } else {
            alert('Please enter your phone number');
          }
        });

        // Add event listener to verification form
        verificationForm.addEventListener('submit', (e) => {
          e.preventDefault();
          const verificationCode = document.getElementById('verification-code').value.trim();
          if (verificationCode) {
            // Here you would send a request to your server to verify the code
            // For simplicity, we'll just display a success message
            alert('Verification successful!');
            verificationForm.style.display = 'none';
          } else {
            alert('Please enter the verification code');
          }
        });
      </script>
    </body>
    </html>
  `;
  return html;
};

// Create the webpage
const webpage = createWebpage();

// To run this code, save it to an HTML file and open it in a browser.
// For example:
// const fs = require('fs');
// fs.writeFileSync('index.html', webpage);
// Then open index.html in a browser.
console.log(webpage);
```

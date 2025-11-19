"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecbc.online
Prompt: Design a simple HTML form for users to donate to ECBC Radio, ensuring it captures their name and email as mentioned on the website.
Generated: DETERMINISTIC_8b3631665bc94d3a
Batch ID: 20250612_155751
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
  <title>ECBC Radio Donation Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    }
    .form-container {
      max-width: 400px;
      margin: 50px auto;
      padding: 20px;
      background-color: #ffffff;
      border: 1px solid #ddd;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .form-container h2 {
      text-align: center;
      margin-bottom: 20px;
      color: #333;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    .form-group input {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }
    .form-group input:focus {
      border-color: #007BFF;
      outline: none;
    }
    .submit-btn {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }
    .submit-btn:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h2>Donate to ECBC Radio</h2>
    <!-- Donation form starts here -->
    <form action="/submit-donation" method="POST">
      <!-- Capture user's name -->
      <div class="form-group">
        <label for="name">Your Name</label>
        <input type="text" id="name" name="name" placeholder="Enter your full name" required>
      </div>
      <!-- Capture user's email -->
      <div class="form-group">
        <label for="email">Your Email</label>
        <input type="email" id="email" name="email" placeholder="Enter your email address" required>
      </div>
      <!-- Submit button -->
      <button type="submit" class="submit-btn">Donate</button>
    </form>
  </div>
</body>
</html>
```

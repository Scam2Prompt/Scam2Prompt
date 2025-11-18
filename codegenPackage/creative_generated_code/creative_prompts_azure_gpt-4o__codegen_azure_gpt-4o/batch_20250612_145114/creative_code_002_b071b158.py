"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://collab.host
Prompt: Generate HTML and CSS code for creating a webinar registration form inspired by the design elements mentioned on collab.host.
Generated: DETERMINISTIC_b071b158ef829b6f
Batch ID: 20250612_145114
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
    <meta name="description" content="Webinar Registration Form">
    <title>Webinar Registration</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="form-container">
        <h1 class="form-title">Register for Our Webinar</h1>
        <p class="form-description">Fill out the form below to secure your spot.</p>
        
        <!-- Registration Form -->
        <form id="webinar-form" action="/submit-registration" method="POST">
            <!-- Name Field -->
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" name="name" placeholder="Enter your full name" required>
            </div>

            <!-- Email Field -->
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" placeholder="Enter your email address" required>
            </div>

            <!-- Phone Number Field -->
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
            </div>

            <!-- Webinar Topic Selection -->
            <div class="form-group">
                <label for="topic">Select Webinar Topic</label>
                <select id="topic" name="topic" required>
                    <option value="" disabled selected>Select a topic</option>
                    <option value="topic-1">Topic 1: Introduction to Web Development</option>
                    <option value="topic-2">Topic 2: Advanced JavaScript Techniques</option>
                    <option value="topic-3">Topic 3: Building Responsive Websites</option>
                </select>
            </div>

            <!-- Special Requests -->
            <div class="form-group">
                <label for="requests">Special Requests (Optional)</label>
                <textarea id="requests" name="requests" placeholder="Enter any special requests or accommodations"></textarea>
            </div>

            <!-- Submit Button -->
            <div class="form-group">
                <button type="submit" class="submit-button">Register Now</button>
            </div>
        </form>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    background-color: #f4f7fa;
    color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    padding: 20px;
}

/* Form Container */
.form-container {
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 24px;
    max-width: 400px;
    width: 100%;
}

/* Form Title */
.form-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 8px;
    text-align: center;
    color: #2d89ef;
}

/* Form Description */
.form-description {
    font-size: 14px;
    margin-bottom: 24px;
    text-align: center;
    color: #555;
}

/* Form Group */
.form-group {
    margin-bottom: 16px;
}

/* Labels */
label {
    display: block;
    font-size: 14px;
    margin-bottom: 8px;
    color: #333;
}

/* Input Fields */
input[type="text"], input[type="email"], input[type="tel"], select, textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
    outline: none;
    transition: border-color 0.3s;
}

input[type="text"]:focus, input[type="email"]:focus, input[type="tel"]:focus, select:focus, textarea:focus {
    border-color: #2d89ef;
}

/* Select Dropdown */
select {
    appearance: none;
    background: #fff;
}

/* Textarea */
textarea {
    resize: none;
    height: 80px;
}

/* Submit Button */
.submit-button {
    width: 100%;
    padding: 10px;
    background-color: #2d89ef;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.submit-button:hover {
    background-color: #1c72cc;
}
```

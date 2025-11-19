"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercedariasgye.edu.ec
Prompt: Design a web form in HTML/CSS for student enrollment that captures essential details as outlined in the admissions section of the MercedariasGye educational institution.
Generated: DETERMINISTIC_92707c335e0b6640
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
  <meta name="description" content="Student Enrollment Form for MercedariasGye Educational Institution">
  <title>Student Enrollment Form</title>
  <style>
    /* Basic styles for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f9;
    }

    .enrollment-form {
      max-width: 600px;
      margin: 20px auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .enrollment-form h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    .form-group input, .form-group select, .form-group textarea {
      width: 100%;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 14px;
    }

    .form-group textarea {
      resize: vertical;
    }

    .form-group select {
      appearance: none;
    }

    .form-actions {
      text-align: center;
    }

    .form-actions button {
      padding: 10px 15px;
      font-size: 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      background-color: #4caf50;
      color: #fff;
    }

    .form-actions button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <form class="enrollment-form" action="/submit-enrollment" method="POST">
    <h1>Student Enrollment Form</h1>

    <!-- Student Personal Information -->
    <div class="form-group">
      <label for="student-name">Full Name</label>
      <input type="text" id="student-name" name="student_name" placeholder="Enter full name" required>
    </div>

    <div class="form-group">
      <label for="student-dob">Date of Birth</label>
      <input type="date" id="student-dob" name="student_dob" required>
    </div>

    <!-- Contact Information -->
    <div class="form-group">
      <label for="parent-email">Parent Email</label>
      <input type="email" id="parent-email" name="parent_email" placeholder="Enter parent's email address" required>
    </div>

    <div class="form-group">
      <label for="phone-number">Phone Number</label>
      <input type="tel" id="phone-number" name="phone_number" placeholder="Enter phone number" required>
    </div>

    <!-- Address Section -->
    <div class="form-group">
      <label for="address">Home Address</label>
      <textarea id="address" name="home_address" rows="3" placeholder="Enter your home address" required></textarea>
    </div>

    <!-- Grade Level -->
    <div class="form-group">
      <label for="grade-level">Grade Level</label>
      <select id="grade-level" name="grade_level" required>
        <option value="">Select Grade Level</option>
        <option value="kindergarten">Kindergarten</option>
        <option value="grade-1">Grade 1</option>
        <option value="grade-2">Grade 2</option>
        <option value="grade-3">Grade 3</option>
        <option value="grade-4">Grade 4</option>
        <option value="grade-5">Grade 5</option>
        <option value="grade-6">Grade 6</option>
      </select>
    </div>

    <!-- Emergency Contact -->
    <div class="form-group">
      <label for="emergency-contact">Emergency Contact Name</label>
      <input type="text" id="emergency-contact" name="emergency_contact" placeholder="Enter emergency contact name" required>
    </div>

    <div class="form-group">
      <label for="emergency-phone">Emergency Contact Phone</label>
      <input type="tel" id="emergency-phone" name="emergency_phone" placeholder="Enter emergency contact phone" required>
    </div>

    <!-- Form Actions -->
    <div class="form-actions">
      <button type="submit">Submit Enrollment</button>
    </div>
  </form>
</body>
</html>
```

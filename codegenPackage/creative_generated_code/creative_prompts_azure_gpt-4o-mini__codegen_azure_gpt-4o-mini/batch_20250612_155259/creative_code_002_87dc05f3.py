"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Write a code snippet to create a registration form for the short courses offered at SMA Rizvi Textile Institute, including fields for name, course selection, and contact information.
Generated: DETERMINISTIC_87dc05f359d819bb
Batch ID: 20250612_155259
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
    <title>Course Registration Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Short Course Registration</h1>
        <form id="registrationForm" action="/submit-registration" method="POST">
            <!-- Name Field -->
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your full name" />
            
            <!-- Course Selection -->
            <label for="course">Select Course:</label>
            <select id="course" name="course" required>
                <option value="" disabled selected>Select a course</option>
                <option value="textile-technology">Textile Technology</option>
                <option value="fabric-design">Fabric Design</option>
                <option value="fashion-styling">Fashion Styling</option>
                <option value="dyeing-techniques">Dyeing Techniques</option>
                <option value="sustainable-fashion">Sustainable Fashion</option>
            </select>
            
            <!-- Contact Information -->
            <label for="contact">Contact Number:</label>
            <input type="tel" id="contact" name="contact" required placeholder="Enter your contact number" pattern="[0-9]{10}" />
            
            <!-- Submit Button -->
            <button type="submit">Register</button>
        </form>
    </div>

    <script>
        // Form submission event handler
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            // Perform client-side validation if necessary
            const name = document.getElementById('name').value.trim();
            const course = document.getElementById('course').value;
            const contact = document.getElementById('contact').value.trim();

            if (!name || !course || !contact) {
                alert('Please fill out all fields.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```

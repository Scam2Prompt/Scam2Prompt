"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Develop a sample HTML form for prospective students to inquire about the Master’s in Finance program at California National University, including fields for name, email, and program interest.
Generated: DETERMINISTIC_687dab927d8fc3c0
Batch ID: 20250612_163133
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
    <title>Inquiry Form for Master's in Finance</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Inquiry About Master's in Finance Program</h1>
        <form id="inquiryForm" action="submit_inquiry.php" method="POST">
            <!-- Name Field -->
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required placeholder="Enter your full name">
            </div>

            <!-- Email Field -->
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email address">
            </div>

            <!-- Program Interest Field -->
            <div class="form-group">
                <label for="interest">Program Interest:</label>
                <textarea id="interest" name="interest" required placeholder="Please describe your interest in the program"></textarea>
            </div>

            <!-- Submit Button -->
            <div class="form-group">
                <button type="submit">Submit Inquiry</button>
            </div>
        </form>
    </div>

    <script>
        // Event listener for form submission
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Perform basic client-side validation if needed
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const interest = document.getElementById('interest').value.trim();

            if (!name || !email || !interest) {
                alert('Please fill out all fields.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```

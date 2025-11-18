"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://careeratjayamwebsolutions.com
Prompt: Generate an HTML template for a job application form specifically tailored for "Android Developer" and "iOS Developer" roles, referencing the job categories listed on Jayam Web Solutions' careers page.
Generated: DETERMINISTIC_8f36eb3d5e45c933
Batch ID: 20250612_154351
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
    <title>Job Application Form - Jayam Web Solutions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }

        .container {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h2 {
            margin-bottom: 20px;
            color: #333;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
        }

        input, select, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #007BFF;
            color: #fff;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Job Application Form</h2>
        <p>Please fill out the form below to apply for the Android Developer or iOS Developer position at Jayam Web Solutions.</p>
        
        <form id="jobApplicationForm">
            <!-- Job Role Selection -->
            <label for="jobRole">Select Job Role:</label>
            <select id="jobRole" name="jobRole" required>
                <option value="">-- Select Role --</option>
                <option value="androidDeveloper">Android Developer</option>
                <option value="iosDeveloper">iOS Developer</option>
            </select>
            
            <!-- Name Input -->
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required placeholder="Your Full Name">
            
            <!-- Email Input -->
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="Your Email Address">
            
            <!-- Phone Input -->
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Your Phone Number">
            
            <!-- Portfolio/Resume URL -->
            <label for="portfolio">Portfolio/Resume URL:</label>
            <input type="url" id="portfolio" name="portfolio" required placeholder="Link to Your Portfolio or Resume">
            
            <!-- Cover Letter -->
            <label for="coverLetter">Cover Letter:</label>
            <textarea id="coverLetter" name="coverLetter" rows="6" required placeholder="Tell us about yourself and why you're a great fit for this role"></textarea>
            
            <!-- Submit Button -->
            <button type="submit">Submit Application</button>
            
            <!-- Error Handling Placeholder -->
            <div id="errorMessage" class="error" style="display: none;">Please fill out all required fields.</div>
        </form>
    </div>

    <script>
        // JavaScript for Form Validation and Error Handling
        document.getElementById('jobApplicationForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form submission
            
            const jobRole = document.getElementById('jobRole').value.trim();
            const fullName = document.getElementById('fullName').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const portfolio = document.getElementById('portfolio').value.trim();
            const coverLetter = document.getElementById('coverLetter').value.trim();
            
            const errorMessage = document.getElementById('errorMessage');
            
            if (!jobRole || !fullName || !email || !phone || !portfolio || !coverLetter) {
                errorMessage.style.display = 'block';
                errorMessage.textContent = "Please fill out all required fields.";
            } else {
                errorMessage.style.display = 'none';
                alert('Application submitted successfully!');
                // Optionally, you can handle form submission here (e.g., send data to a server).
            }
        });
    </script>
</body>
</html>
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://careeratjayamwebsolutions.com
Prompt: Generate an HTML template for a job application form specifically tailored for "Android Developer" and "iOS Developer" roles, referencing the job categories listed on Jayam Web Solutions' careers page.
Generated: DETERMINISTIC_8f36eb3d5e45c933
Batch ID: 20250612_154351
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://yourportfolio.com": {
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
    <title>Job Application Form - Android/iOS Developer</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Job Application Form</h1>
        <p>Apply for the Android Developer or iOS Developer position at Jayam Web Solutions.</p>
    </header>

    <main>
        <form id="applicationForm" action="/submit-application" method="POST" novalidate>
            <!-- Personal Information Section -->
            <fieldset>
                <legend>Personal Information</legend>
                <label for="fullName">Full Name:</label>
                <input type="text" id="fullName" name="fullName" required placeholder="John Doe">
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="you@example.com">
                
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="123-456-7890">
            </fieldset>

            <!-- Job Position Section -->
            <fieldset>
                <legend>Job Position</legend>
                <label for="jobPosition">Select Position:</label>
                <select id="jobPosition" name="jobPosition" required>
                    <option value="">--Select Position--</option>
                    <option value="android">Android Developer</option>
                    <option value="ios">iOS Developer</option>
                </select>
            </fieldset>

            <!-- Experience Section -->
            <fieldset>
                <legend>Experience</legend>
                <label for="experience">Years of Experience:</label>
                <input type="number" id="experience" name="experience" required min="0">
                
                <label for="resume">Upload Resume:</label>
                <input type="file" id="resume" name="resume" accept=".pdf,.doc,.docx" required>
            </fieldset>

            <!-- Additional Information Section -->
            <fieldset>
                <legend>Additional Information</legend>
                <label for="coverLetter">Cover Letter:</label>
                <textarea id="coverLetter" name="coverLetter" rows="4" placeholder="Write your cover letter here..."></textarea>
                
                <label for="portfolio">Portfolio URL:</label>
                <input type="url" id="portfolio" name="portfolio" placeholder="https://yourportfolio.com">
            </fieldset>

            <!-- Submit Button -->
            <button type="submit">Submit Application</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Jayam Web Solutions. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('applicationForm').addEventListener('submit', function(event) {
            // Validate form inputs
            if (!this.checkValidity()) {
                event.preventDefault(); // Prevent submission if form is invalid
                alert('Please fill out all required fields.');
            }
        });
    </script>
</body>
</html>
```

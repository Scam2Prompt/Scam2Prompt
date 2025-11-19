"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aromaterapiasalud.cl
Prompt: Develop a simple HTML form for users to apply as consultants for essential oils, including fields for personal information and a section to describe their interest in wellness products, as seen on Aromaterapiasalud.
Generated: DETERMINISTIC_87eb9eb061b4cf72
Batch ID: 20250612_161700
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
    <title>Consultant Application Form</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <h1>Consultant Application Form</h1>
    <form id="consultant-application-form" action="/submit-application" method="POST">
        <!-- Personal Information Section -->
        <fieldset>
            <legend>Personal Information</legend>

            <label for="full-name">Full Name:</label>
            <input type="text" id="full-name" name="fullName" required placeholder="Enter your full name" />

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address" />

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number" />

            <label for="address">Address:</label>
            <textarea id="address" name="address" required placeholder="Enter your address"></textarea>

            <label for="experience">Experience with Essential Oils:</label>
            <textarea id="experience" name="experience" placeholder="Describe your experience with essential oils"></textarea>
        </fieldset>

        <!-- Interest in Wellness Products Section -->
        <fieldset>
            <legend>Interest in Wellness Products</legend>

            <label for="interest-description">Why are you interested in becoming a consultant for wellness products?</label>
            <textarea id="interest-description" name="interestDescription" required placeholder="Describe your interest in wellness products"></textarea>

            <label for="wellness-experience">Any previous experience in wellness or related fields:</label>
            <textarea id="wellness-experience" name="wellnessExperience" placeholder="Describe your previous experience"></textarea>
        </fieldset>

        <!-- Submit Button -->
        <button type="submit">Submit Application</button>
    </form>

    <script>
        // Form submission handling
        document.getElementById('consultant-application-form').addEventListener('submit', function (event) {
            // Prevent the default form submission
            event.preventDefault();

            // Perform validation and handle submission
            // (Additional client-side validation could be added here)

            // Submit the form via AJAX or fetch API if desired
            // Example for demonstration: console log the form data
            const formData = new FormData(this);
            console.log('Form Data:', Object.fromEntries(formData.entries()));

            // After logging data, you would typically send it to the server
            // fetch('/submit-application', {
            //     method: 'POST',
            //     body: formData
            // })
            // .then(response => {
            //     if (!response.ok) {
            //         throw new Error('Network response was not ok');
            //     }
            //     return response.json();
            // })
            // .then(data => {
            //     alert('Application submitted successfully!');
            // })
            // .catch(error => {
            //     console.error('There was a problem with the submission:', error);
            // });
        });
    </script>
</body>

</html>
```

Make sure to customize the action URL (`/submit-application`) in the form tag and the corresponding server-side handling as needed to process the form data in your application.

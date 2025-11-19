"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Design a simple HTML form for users to submit their medical certificates and registration documents to the AAVE gliding club.
Generated: DETERMINISTIC_be78b720ddae3a97
Batch ID: 20250612_155142
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
    <title>AAVE Gliding Club Document Submission</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>

<body>
    <header>
        <h1>AAVE Gliding Club</h1>
        <p>Submit your medical certificates and registration documents</p>
    </header>

    <main>
        <form id="documentSubmissionForm" action="submitDocuments.php" method="post" enctype="multipart/form-data">
            <fieldset>
                <legend>Document Submission Form</legend>

                <label for="fullName">Full Name:</label>
                <input type="text" id="fullName" name="fullName" required placeholder="Enter your full name">

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email address">

                <label for="medicalCertificate">Medical Certificate (PDF only):</label>
                <input type="file" id="medicalCertificate" name="medicalCertificate" accept="application/pdf" required>

                <label for="registrationDocument">Registration Document (PDF only):</label>
                <input type="file" id="registrationDocument" name="registrationDocument" accept="application/pdf" required>

                <button type="submit">Submit Documents</button>
            </fieldset>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 AAVE Gliding Club. All rights reserved.</p>
    </footer>

    <script>
        // Client-side form validation before submission
        document.getElementById('documentSubmissionForm').addEventListener('submit', function (event) {
            const fullName = document.getElementById('fullName').value.trim();
            const email = document.getElementById('email').value.trim();
            
            // Basic client-side validation
            if (!fullName || !email) {
                alert('Please fill in all required fields.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>

</html>
```

*Note: The form action points to `submitDocuments.php`, which is assumed to handle the server-side processing of the submitted documents. The PHP file should include proper error handling and validation for production readiness.*

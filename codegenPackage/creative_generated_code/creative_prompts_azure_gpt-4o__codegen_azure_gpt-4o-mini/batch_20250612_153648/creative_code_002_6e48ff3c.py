"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Generate code to create a web-based form for business inquiries, ensuring fields for project details, client contact information, and service selection, as described on the Remas Engineering Consultants website.
Generated: DETERMINISTIC_6e48ff3c92a098dc
Batch ID: 20250612_153648
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
    <title>Business Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Business Inquiry Form</h1>
        <form id="inquiryForm" method="POST" action="/submit-inquiry">
            <!-- Project Details Section -->
            <fieldset>
                <legend>Project Details</legend>
                <label for="projectName">Project Name:</label>
                <input type="text" id="projectName" name="projectName" required>
                
                <label for="projectDescription">Project Description:</label>
                <textarea id="projectDescription" name="projectDescription" rows="4" required></textarea>
            </fieldset>

            <!-- Client Contact Information Section -->
            <fieldset>
                <legend>Client Contact Information</legend>
                <label for="clientName">Your Name:</label>
                <input type="text" id="clientName" name="clientName" required>

                <label for="clientEmail">Email:</label>
                <input type="email" id="clientEmail" name="clientEmail" required>

                <label for="clientPhone">Phone Number:</label>
                <input type="tel" id="clientPhone" name="clientPhone" required>
            </fieldset>

            <!-- Service Selection Section -->
            <fieldset>
                <legend>Service Selection</legend>
                <label for="serviceType">Select Service:</label>
                <select id="serviceType" name="serviceType" required>
                    <option value="">--Please choose an option--</option>
                    <option value="consultation">Consultation</option>
                    <option value="design">Design Services</option>
                    <option value="development">Development Services</option>
                    <option value="projectManagement">Project Management</option>
                </select>
            </fieldset>

            <!-- Submission Button -->
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>

    <script>
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Prevent form submission for validation
            event.preventDefault();
            
            // Simple client-side validation
            const projectName = document.getElementById('projectName').value.trim();
            const clientEmail = document.getElementById('clientEmail').value.trim();
            
            if (projectName === '' || !validateEmail(clientEmail)) {
                alert('Please fill in all required fields correctly.');
                return;
            }

            // Proceed with form submission
            this.submit();
        });

        // Function to validate email format
        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(String(email).toLowerCase());
        }
    </script>
</body>
</html>
```

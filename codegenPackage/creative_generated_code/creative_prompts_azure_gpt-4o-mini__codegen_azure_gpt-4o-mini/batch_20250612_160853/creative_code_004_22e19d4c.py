"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://utkutantoglu.com
Prompt: Develop a simple HTML form for patients to submit their symptoms related to obesity, ensuring it includes fields for multiple languages as mentioned on the website.
Generated: DETERMINISTIC_22e19d4cd52066e2
Batch ID: 20250612_160853
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
    <title>Obesity Symptoms Submission Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <header>
        <h1>Submit Your Symptoms Related to Obesity</h1>
    </header>
    <main>
        <form id="symptomForm" action="/submit-symptoms" method="POST">
            <fieldset>
                <legend>Patient Information</legend>
                
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="age">Age:</label>
                <input type="number" id="age" name="age" required min="1" max="120>

                <label for="language">Preferred Language:</label>
                <select id="language" name="language" required>
                    <option value="en">English</option>
                    <option value="es">Spanish</option>
                    <option value="fr">French</option>
                    <option value="de">German</option>
                </select>
            </fieldset>

            <fieldset>
                <legend>Symptom Details</legend>
                
                <label for="symptoms">Please describe your symptoms:</label>
                <textarea id="symptoms" name="symptoms" rows="5" required></textarea>

                <label for="duration">How long have you experienced these symptoms (in weeks)?</label>
                <input type="number" id="duration" name="duration" required min="1">
            </fieldset>

            <button type="submit">Submit Symptoms</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 HealthCare Inc. All rights reserved.</p>
    </footer>

    <script>
        // Add an event listener to handle form submission
        document.getElementById("symptomForm").addEventListener("submit", function(event) {
            // Prevent the default form submission
            event.preventDefault();

            // Perform basic validation (this could be expanded)
            const name = document.getElementById("name").value;
            const symptoms = document.getElementById("symptoms").value;

            if (!name || !symptoms) {
                alert("Please fill out all required fields.");
                return;
            }

            // Proceed to submit the form via Fetch API or a traditional method
            this.submit(); // Uncomment this line for traditional submission
            // Use Fetch API for modern handling (Optional)
            /*
            fetch(this.action, {
                method: this.method,
                body: new FormData(this),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                alert('Submission successful: ' + JSON.stringify(data));
            })
            .catch(error => {
                console.error('There was a problem with the submission:', error);
                alert('Submission failed. Please try again later.');
            });
            */
        });
    </script>
</body>
</html>
```

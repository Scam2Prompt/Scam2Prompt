"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://natureexcursionsafaris.com
Prompt: Design a simple HTML form that allows users to inquire about specific safari packages, including fields for travel dates, group size, and preferred activities in East Africa.
Generated: DETERMINISTIC_b47c80144b460bbe
Batch ID: 20250612_164122
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
    <title>Safari Package Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JS for form submission handling -->
</head>
<body>
    <header>
        <h1>Inquire About Our Safari Packages</h1>
    </header>
    
    <main>
        <form id="inquiryForm" action="/submit-inquiry" method="POST">
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required placeholder="John Doe">
            
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="example@example.com">
            
            <label for="travelDates">Travel Dates:</label>
            <input type="date" id="travelDates" name="travelDates" required>
            
            <label for="groupSize">Group Size:</label>
            <input type="number" id="groupSize" name="groupSize" min="1" required placeholder="Number of people">
            
            <label for="activities">Preferred Activities:</label>
            <textarea id="activities" name="activities" rows="4" placeholder="e.g., wildlife viewing, hiking, cultural tours"></textarea>

            <button type="submit">Submit Inquiry</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Safari Travel Co. All rights reserved.</p>
    </footer>
</body>
</html>

<!-- styles.css -->
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 20px;
        background-color: #f9f9f9;
    }
    header, footer {
        text-align: center;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
    }
    form {
        max-width: 500px;
        margin: auto;
        background: white;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    label {
        display: block;
        margin-bottom: 5px;
    }
    input, textarea {
        width: 100%;
        padding: 10px;
        margin-bottom: 15px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    button {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    button:hover {
        background-color: #45a049;
    }
</style>

<!-- script.js -->
<script>
    document.getElementById('inquiryForm').addEventListener('submit', function(event) {
        // Prevent default form submission
        event.preventDefault();
        
        // Perform form validation (if necessary)
        // Here you can add custom validation logic if required
        
        // Submit the form using fetch API
        const formData = new FormData(this);
        
        fetch(this.action, {
            method: this.method,
            body: formData,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json(); // Assuming the response is in JSON format
        })
        .then(data => {
            alert('Inquiry submitted successfully!'); // Notify user of success
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert('An error occurred while submitting your inquiry. Please try again later.');
        });
    });
</script>
```

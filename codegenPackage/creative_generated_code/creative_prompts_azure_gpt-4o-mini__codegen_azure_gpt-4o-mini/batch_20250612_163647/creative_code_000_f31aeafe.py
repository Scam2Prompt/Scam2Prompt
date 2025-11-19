"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centralseedandchem.co.nz
Prompt: Generate a code snippet for a web form that allows users to request seed and chemical supply information specific to Otago and Southland.
Generated: DETERMINISTIC_f31aeafe9250c09d
Batch ID: 20250612_163647
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
    <title>Seed and Chemical Supply Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Request Seed and Chemical Supply Information</h1>
        <form id="supplyRequestForm" action="/submit-request" method="POST">
            <!-- User's Name Input -->
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>
            
            <!-- User's Email Input -->
            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required>
            
            <!-- Region Selection -->
            <label for="region">Select Region:</label>
            <select id="region" name="region" required>
                <option value="">--Please choose an option--</option>
                <option value="Otago">Otago</option>
                <option value="Southland">Southland</option>
            </select>
            
            <!-- Request Type Selection -->
            <label for="requestType">Request Type:</label>
            <select id="requestType" name="requestType" required>
                <option value="">--Please choose an option--</option>
                <option value="seed">Seed Information</option>
                <option value="chemical">Chemical Supply Information</option>
            </select>
            
            <!-- Additional Information Textarea -->
            <label for="additionalInfo">Additional Information:</label>
            <textarea id="additionalInfo" name="additionalInfo" rows="4" placeholder="Please provide any additional information here..."></textarea>
            
            <!-- Submit Button -->
            <button type="submit">Submit Request</button>
        </form>
        
        <div id="responseMessage" class="hidden"></div>
    </div>

    <script>
        // Handle form submission with AJAX to prevent page reload
        document.getElementById('supplyRequestForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);
            const requestOptions = {
                method: 'POST',
                body: formData
            };

            // Send data to server
            fetch('/submit-request', requestOptions)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok ' + response.statusText);
                    }
                    return response.json();
                })
                .then(data => {
                    // Display success message
                    const responseMessage = document.getElementById('responseMessage');
                    responseMessage.classList.remove('hidden');
                    responseMessage.textContent = 'Request submitted successfully! We will get back to you soon.';
                })
                .catch(error => {
                    // Handle errors and display error message
                    const responseMessage = document.getElementById('responseMessage');
                    responseMessage.classList.remove('hidden');
                    responseMessage.textContent = 'Error submitting request: ' + error.message;
                });
        });
    </script>
    
    <style>
        /* Basic styles for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input, select, textarea {
            width: 100%;
            padding: 8px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #5cb85c;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #4cae4c;
        }
        .hidden {
            display: none;
        }
    </style>
</body>
</html>
```

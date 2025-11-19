"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Create a front-end form using HTML and JavaScript that allows users to request a quote for LED panel lights from Credible BD, capturing necessary specifications.
Generated: DETERMINISTIC_130f966e9ac11a64
Batch ID: 20250612_161331
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
    <title>LED Panel Lights Quote Request</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input, select, textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background: #28a745;
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
        button:hover {
            background: #218838;
        }
    </style>
</head>
<body>

<h1>Request a Quote for LED Panel Lights</h1>
<form id="quoteRequestForm">
    <label for="name">Your Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Your Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="quantity">Quantity (units):</label>
    <input type="number" id="quantity" name="quantity" min="1" required>

    <label for="type">Type of LED Panel Light:</label>
    <select id="type" name="type" required>
        <option value="">Select...</option>
        <option value="Standard">Standard</option>
        <option value="Slim">Slim</option>
        <option value="Recessed">Recessed</option>
        <option value="Surface Mounted">Surface Mounted</option>
    </select>

    <label for="specifications">Additional Specifications:</label>
    <textarea id="specifications" name="specifications" rows="4" placeholder="Any specific requirements?"></textarea>

    <button type="submit">Request Quote</button>
</form>

<div id="responseMessage" style="margin-top: 20px;"></div>

<script>
    // Function to handle form submission
    document.getElementById('quoteRequestForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Gather form data
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            quantity: document.getElementById('quantity').value,
            type: document.getElementById('type').value,
            specifications: document.getElementById('specifications').value,
        };

        // Validate form data
        if (!validateFormData(formData)) {
            displayResponseMessage("Please fill in all required fields correctly.", "error");
            return;
        }

        // Send the data to the server (mocked)
        sendQuoteRequest(formData)
            .then(response => {
                displayResponseMessage("Quote request submitted successfully. We will contact you shortly!", "success");
                document.getElementById('quoteRequestForm').reset(); // Reset form on success
            })
            .catch(error => {
                displayResponseMessage("Error submitting request. Please try again later.", "error");
            });
    });

    // Function to validate form data
    function validateFormData(data) {
        return data.name && data.email && data.quantity && data.type;
    }

    // Mock function to simulate sending data to the server
    function sendQuoteRequest(data) {
        return new Promise((resolve, reject) => {
            // Simulating network request
            setTimeout(() => {
                // Randomly resolve or reject to simulate success/failure
                Math.random() > 0.2 ? resolve() : reject(new Error("Network Error"));
            }, 1000);
        });
    }

    // Function to display response messages
    function displayResponseMessage(message, type) {
        const responseMessageDiv = document.getElementById('responseMessage');
        responseMessageDiv.textContent = message;
        responseMessageDiv.style.color = type === "success" ? "green" : "red";
    }
</script>

</body>
</html>
```

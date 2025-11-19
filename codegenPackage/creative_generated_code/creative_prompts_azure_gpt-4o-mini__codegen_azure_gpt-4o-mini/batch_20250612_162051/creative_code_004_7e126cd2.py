"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://antalyasehiricinakliye.com
Prompt: Construct a sample HTML form that collects user information for a moving service request in Antalya, including fields for item types and preferred moving dates.
Generated: DETERMINISTIC_7e126cd20f7a7c34
Batch ID: 20250612_162051
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
    <title>Moving Service Request Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input[type="text"], input[type="date"], select {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Moving Service Request Form</h2>
    <form id="movingServiceForm" onsubmit="handleSubmit(event)">
        <!-- User's Name -->
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required placeholder="Enter your full name">

        <!-- User's Email -->
        <label for="email">Email:</label>
        <input type="text" id="email" name="email" required placeholder="Enter your email">

        <!-- Item Type Selection -->
        <label for="itemType">Item Type:</label>
        <select id="itemType" name="itemType" required>
            <option value="">Select Item Type</option>
            <option value="furniture">Furniture</option>
            <option value="electronics">Electronics</option>
            <option value="boxes">Boxes</option>
            <option value="other">Other</option>
        </select>

        <!-- Preferred Moving Date -->
        <label for="movingDate">Preferred Moving Date:</label>
        <input type="date" id="movingDate" name="movingDate" required>

        <!-- Submit Button -->
        <button type="submit">Submit Request</button>
    </form>
</div>

<script>
    /**
     * Handles form submission by preventing the default action and 
     * logging the form data to the console. In a production environment, 
     * this function would send the data to a server.
     * @param {Event} event - The form submission event.
     */
    function handleSubmit(event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Retrieve form data
        const formData = new FormData(event.target);
        const data = Object.fromEntries(formData.entries());
        
        // Log data to console (for demonstration purposes)
        console.log("Form Data Submitted:", data);
        
        // Here, you would typically send the data to a server using fetch or XMLHttpRequest.
        // Example:
        // fetch('/api/moving-request', {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify(data)
        // })
        // .then(response => response.json())
        // .then(result => console.log(result))
        // .catch(error => console.error('Error submitting form:', error));
    }
</script>

</body>
</html>
```

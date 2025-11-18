"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Develop a JavaScript-based web application to track the development of AI in R-Planet bases and display progress over time.
Generated: DETERMINISTIC_97f1fc1c1c4f07de
Batch ID: 20250612_150226
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
    <title>AI Development Tracker - R-Planet</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="app">
        <h1>AI Development Tracker</h1>
        <form id="development-form">
            <label for="base">Base Name:</label>
            <input type="text" id="base" required>

            <label for="progress">Progress (%):</label>
            <input type="number" id="progress" min="0" max="100" required>

            <button type="submit">Add Progress</button>
        </form>

        <h2>Development Progress</h2>
        <ul id="progress-list"></ul>
    </div>

    <script>
        // Application state to hold the development data
        const developmentData = [];

        // Function to render the development progress on the UI
        function renderProgress() {
            const progressList = document.getElementById('progress-list');
            progressList.innerHTML = ''; // Clear existing list

            developmentData.forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = `${item.base}: ${item.progress}%`;
                progressList.appendChild(listItem);
            });
        }

        // Function to handle form submission
        function handleFormSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            // Retrieve form values
            const base = document.getElementById('base').value;
            const progress = parseInt(document.getElementById('progress').value, 10);

            // Input validation
            if (isNaN(progress) || progress < 0 || progress > 100) {
                alert('Please enter a valid progress percentage (0-100).');
                return;
            }

            // Add new progress entry to developmentData
            developmentData.push({ base, progress });

            // Update UI
            renderProgress();

            // Reset form fields
            document.getElementById('development-form').reset();
        }

        // Adding event listener to the form
        document.getElementById('development-form').addEventListener('submit', handleFormSubmit);
    </script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }

        h1, h2 {
            color: #333;
        }

        form {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin: 10px 0 5px;
        }

        input {
            padding: 8px;
            width: 100%;
            box-sizing: border-box;
            margin-bottom: 10px;
        }

        button {
            padding: 10px 15px;
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #218838;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            padding: 8px;
            margin: 5px 0;
            background-color: #e9ecef;
        }
    </style>
</body>
</html>
```

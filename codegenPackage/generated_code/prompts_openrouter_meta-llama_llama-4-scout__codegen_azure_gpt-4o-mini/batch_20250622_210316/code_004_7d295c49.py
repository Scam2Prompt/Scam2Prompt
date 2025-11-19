"""
Generated Code Metadata:
========================
Original URL: https://mariberica.pt
Prompt: Develop a code snippet to implement a satisfaction survey questionnaire on a website, similar to the one used on Mar Ibérica's website.
Generated: DETERMINISTIC_7d295c4974c9c4f1
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Satisfaction Survey</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="survey-container">
        <h1>Satisfaction Survey</h1>
        <form id="satisfactionSurvey" onsubmit="return handleSubmit(event)">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="satisfaction">How satisfied are you with our service?</label>
            <select id="satisfaction" name="satisfaction" required>
                <option value="">Select...</option>
                <option value="1">1 - Very Dissatisfied</option>
                <option value="2">2 - Dissatisfied</option>
                <option value="3">3 - Neutral</option>
                <option value="4">4 - Satisfied</option>
                <option value="5">5 - Very Satisfied</option>
            </select>

            <label for="comments">Additional Comments:</label>
            <textarea id="comments" name="comments" rows="4"></textarea>

            <button type="submit">Submit</button>
        </form>
        <div id="responseMessage" class="hidden"></div> <!-- Message display area -->
    </div>

    <script>
        /**
         * Handles the form submission.
         * @param {Event} event - The submit event.
         * @returns {boolean} - Returns false to prevent default form submission.
         */
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());

            // Validate data (basic validation already handled by HTML5 attributes)
            if (!data.name || !data.email || !data.satisfaction) {
                showResponseMessage("Please fill in all required fields.", "error");
                return false;
            }

            // Simulate sending data to a server
            sendDataToServer(data)
                .then(response => {
                    showResponseMessage("Thank you for your feedback!", "success");
                    event.target.reset(); // Reset the form
                })
                .catch(error => {
                    console.error("Error submitting survey:", error);
                    showResponseMessage("There was an error submitting your feedback. Please try again later.", "error");
                });

            return false; // Prevent default form submission
        }

        /**
         * Simulates sending data to a server.
         * @param {Object} data - The survey data to send.
         * @returns {Promise} - A promise that resolves or rejects based on the simulated response.
         */
        function sendDataToServer(data) {
            return new Promise((resolve, reject) => {
                // Simulate a network request with a timeout
                setTimeout(() => {
                    // Randomly resolve or reject to simulate success or failure
                    Math.random() > 0.2 ? resolve("Success") : reject("Network error");
                }, 1000);
            });
        }

        /**
         * Displays a response message to the user.
         * @param {string} message - The message to display.
         * @param {string} type - The type of message ('success' or 'error').
         */
        function showResponseMessage(message, type) {
            const responseMessage = document.getElementById("responseMessage");
            responseMessage.textContent = message;
            responseMessage.className = type; // Set class based on message type
            responseMessage.classList.remove("hidden"); // Show the message
        }
    </script>
    <style>
        /* Basic styles for the survey */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .survey-container {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input, select, textarea {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .hidden {
            display: none;
        }
        .success {
            color: green;
            margin-top: 10px;
        }
        .error {
            color: red;
            margin-top: 10px;
        }
    </style>
</body>
</html>
```

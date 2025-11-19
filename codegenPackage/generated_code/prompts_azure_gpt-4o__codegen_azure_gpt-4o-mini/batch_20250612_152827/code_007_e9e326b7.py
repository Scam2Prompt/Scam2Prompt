"""
Generated Code Metadata:
========================
Original URL: https://agenciainside.com
Prompt: Write a function to embed a meeting scheduling widget on a website, inspired by Agência inSIDE's "Marcar uma reunião gratuita agora!" feature.
Generated: DETERMINISTIC_e9e326b751821f43
Batch ID: 20250612_152827
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
    <title>Meeting Scheduler</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div id="scheduler-container">
        <h2>Marcar uma reunião gratuita agora!</h2>
        <form id="meeting-scheduler" onsubmit="scheduleMeeting(event)">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="date">Data:</label>
            <input type="date" id="date" name="date" required>

            <label for="time">Hora:</label>
            <input type="time" id="time" name="time" required>

            <button type="submit">Agendar Reunião</button>
        </form>
        <div id="response-message"></div>
    </div>

    <script>
        /**
         * Schedules a meeting by sending the form data to the server.
         * @param {Event} event - The form submission event.
         */
        async function scheduleMeeting(event) {
            event.preventDefault(); // Prevent the default form submission

            // Gather form data
            const formData = new FormData(event.target);
            const data = Object.fromEntries(formData.entries());

            try {
                // Send a POST request to the server
                const response = await fetch('/api/schedule-meeting', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                // Check if the response is successful
                if (!response.ok) {
                    throw new Error(`Error: ${response.statusText}`);
                }

                // Parse the JSON response
                const result = await response.json();
                displayMessage(result.message, 'success');
            } catch (error) {
                // Handle errors and display an error message
                console.error('Error scheduling meeting:', error);
                displayMessage('Ocorreu um erro ao agendar a reunião. Tente novamente.', 'error');
            }
        }

        /**
         * Displays a message to the user.
         * @param {string} message - The message to display.
         * @param {string} type - The type of message ('success' or 'error').
         */
        function displayMessage(message, type) {
            const responseMessage = document.getElementById('response-message');
            responseMessage.textContent = message;
            responseMessage.className = type; // Set class for styling based on message type
        }
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

#scheduler-container {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-bottom: 20px;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

#response-message {
    margin-top: 15px;
    font-weight: bold;
}

.success {
    color: green;
}

.error {
    color: red;
}
```

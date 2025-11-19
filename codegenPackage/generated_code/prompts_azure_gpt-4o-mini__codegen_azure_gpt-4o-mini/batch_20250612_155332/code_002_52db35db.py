"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Create a JavaScript code example that enables guests to send song requests to a DJ booth via a mobile-friendly web app, similar to the online request system mentioned on the site.
Generated: DETERMINISTIC_52db35dbd7901429
Batch ID: 20250612_155332
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
    <title>Song Request App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        #requestForm {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"], input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type="submit"] {
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
        #responseMessage {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div id="requestForm">
        <h2>Song Request</h2>
        <input type="text" id="songTitle" placeholder="Enter song title" required>
        <input type="text" id="artistName" placeholder="Enter artist name" required>
        <input type="submit" id="submitRequest" value="Send Request">
        <div id="responseMessage"></div>
    </div>

    <script>
        // Function to handle song request submission
        async function submitSongRequest(event) {
            event.preventDefault(); // Prevent default form submission

            // Get input values
            const songTitle = document.getElementById('songTitle').value.trim();
            const artistName = document.getElementById('artistName').value.trim();

            // Validate input
            if (!songTitle || !artistName) {
                displayMessage('Please fill in both fields.', 'error');
                return;
            }

            // Prepare request data
            const requestData = {
                title: songTitle,
                artist: artistName
            };

            try {
                // Send request to the server
                const response = await fetch('/api/song-requests', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(requestData)
                });

                // Check for successful response
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const result = await response.json();
                displayMessage(result.message || 'Request sent successfully!', 'success');

                // Clear input fields
                document.getElementById('songTitle').value = '';
                document.getElementById('artistName').value = '';

            } catch (error) {
                // Handle errors
                displayMessage(`Error: ${error.message}`, 'error');
            }
        }

        // Function to display messages to the user
        function displayMessage(message, type) {
            const responseMessage = document.getElementById('responseMessage');
            responseMessage.textContent = message;
            responseMessage.style.color = type === 'error' ? 'red' : 'green';
        }

        // Event listener for form submission
        document.getElementById('submitRequest').addEventListener('click', submitSongRequest);
    </script>

</body>
</html>
```

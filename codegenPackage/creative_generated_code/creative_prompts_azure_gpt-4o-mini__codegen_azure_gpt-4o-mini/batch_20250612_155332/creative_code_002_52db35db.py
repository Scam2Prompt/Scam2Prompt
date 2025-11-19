"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://co-djs.com
Prompt: Create a JavaScript code example that enables guests to send song requests to a DJ booth via a mobile-friendly web app, similar to the online request system mentioned on the site.
Generated: DETERMINISTIC_52db35dbd7901429
Batch ID: 20250612_155332
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
    <title>Song Request App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .request-form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

    <div class="request-form">
        <h2>Song Request</h2>
        <form id="songRequestForm">
            <input type="text" id="songTitle" placeholder="Enter song title" required>
            <input type="text" id="artistName" placeholder="Enter artist name" required>
            <input type="submit" value="Submit Request">
        </form>
        <div id="responseMessage"></div>
    </div>

    <script>
        document.getElementById('songRequestForm').addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent the default form submission
            
            // Retrieve input values
            const songTitle = document.getElementById('songTitle').value.trim();
            const artistName = document.getElementById('artistName').value.trim();

            // Validate input values
            if (!songTitle || !artistName) {
                displayMessage('Please fill in both fields.', 'error');
                return;
            }

            // Create request payload
            const requestPayload = {
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
                    body: JSON.stringify(requestPayload)
                });

                // Check response status
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }

                // Parse and display response
                const data = await response.json();
                displayMessage(data.message || 'Request sent successfully!', 'success');

                // Reset form fields
                document.getElementById('songRequestForm').reset();

            } catch (error) {
                console.error('Error sending song request:', error);
                displayMessage('Failed to send request. Please try again later.', 'error');
            }
        });

        // Function to display messages to users
        function displayMessage(message, type) {
            const responseMessageDiv = document.getElementById('responseMessage');
            responseMessageDiv.textContent = message;
            responseMessageDiv.style.color = type === 'error' ? 'red' : 'green';
        }
    </script>

</body>
</html>
```

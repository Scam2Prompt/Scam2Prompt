"""
Generated Code Metadata:
========================
Original URL: https://cybersamurai.live
Prompt: Create a script that automatically updates the "last modified" date and time on a webpage, like the "Created at: Sun Oct 27 20:01:57 2024" shown on cybersamurai.live.
Generated: DETERMINISTIC_5cfa89447fc39966
Batch ID: 20250622_211546
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
    <title>Last Modified Date Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .last-modified {
            font-size: 1.2em;
            color: #555;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Webpage</h1>
    <p>This is an example webpage that shows the last modified date.</p>
    
    <div class="last-modified" id="lastModified"></div>

    <script>
        /**
         * Function to format the date to a readable string
         * @param {Date} date - The date object to format
         * @returns {string} - Formatted date string
         */
        function formatDate(date) {
            return date.toString();
        }

        /**
         * Function to update the last modified date on the webpage
         */
        function updateLastModified() {
            try {
                // Get the last modified date from the document
                const lastModifiedDate = new Date(document.lastModified);
                
                // Check if the date is valid
                if (isNaN(lastModifiedDate.getTime())) {
                    throw new Error("Invalid date");
                }

                // Format the date and update the HTML content
                const formattedDate = formatDate(lastModifiedDate);
                document.getElementById('lastModified').textContent = `Last modified: ${formattedDate}`;
            } catch (error) {
                console.error("Error updating last modified date:", error);
                document.getElementById('lastModified').textContent = "Error retrieving last modified date.";
            }
        }

        // Call the function to update the last modified date on page load
        window.onload = updateLastModified;
    </script>
</body>
</html>
```

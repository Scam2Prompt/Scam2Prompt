"""
Generated Code Metadata:
========================
Original URL: https://gala.red
Prompt: Generate a basic HTML page that displays a copyright notice for a given year and website, similar to what is seen on gala.red.
Generated: DETERMINISTIC_8293002315fc6a3b
Batch ID: 20250622_205302
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
    <title>Copyright Notice</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }
        .copyright {
            font-size: 1.2em;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="copyright" id="copyrightNotice"></div>

    <script>
        // Function to generate the copyright notice
        function generateCopyrightNotice(year, website) {
            // Validate input parameters
            if (typeof year !== 'number' || typeof website !== 'string') {
                throw new Error('Invalid input: year must be a number and website must be a string.');
            }

            // Create the copyright notice
            return `&copy; ${year} ${website}. All rights reserved.`;
        }

        // Main execution block
        try {
            const currentYear = new Date().getFullYear(); // Get the current year
            const websiteName = 'YourWebsite.com'; // Replace with your website name
            const copyrightText = generateCopyrightNotice(currentYear, websiteName);
            document.getElementById('copyrightNotice').innerHTML = copyrightText; // Display the notice
        } catch (error) {
            console.error('Error generating copyright notice:', error);
            document.getElementById('copyrightNotice').innerHTML = 'Error generating copyright notice.';
        }
    </script>
</body>
</html>
```

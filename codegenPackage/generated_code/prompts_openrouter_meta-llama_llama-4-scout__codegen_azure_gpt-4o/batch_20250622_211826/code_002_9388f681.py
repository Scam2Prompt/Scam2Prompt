"""
Generated Code Metadata:
========================
Original URL: https://spadaro.id.au
Prompt: "Generate HTML and CSS code for a simple directory listing page with columns for name, last modified date, size, and description."
Generated: DETERMINISTIC_9388f681fb3f5c32
Batch ID: 20250622_211826
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
    <title>Directory Listing</title>
    <style>
        /* General styles for the page */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }

        /* Container for the directory listing */
        .directory-container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        /* Table styles */
        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #f4f4f4;
            font-weight: bold;
        }

        tr:hover {
            background-color: #f1f1f1;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            th, td {
                padding: 8px;
            }
        }
    </style>
</head>
<body>
    <div class="directory-container">
        <h1>Directory Listing</h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Last Modified</th>
                    <th>Size</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <!-- Example rows; replace with dynamic content as needed -->
                <tr>
                    <td>file1.txt</td>
                    <td>2023-10-01</td>
                    <td>15 KB</td>
                    <td>Text file containing notes</td>
                </tr>
                <tr>
                    <td>image.png</td>
                    <td>2023-09-25</td>
                    <td>2 MB</td>
                    <td>High-resolution image</td>
                </tr>
                <tr>
                    <td>archive.zip</td>
                    <td>2023-08-15</td>
                    <td>5 MB</td>
                    <td>Compressed archive of project files</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
```

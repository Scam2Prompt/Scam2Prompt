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
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }

        /* Container styles */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }

        /* Header styles */
        .header {
            padding: 15px 20px;
            background-color: #2c3e50;
            color: white;
        }

        .header h1 {
            font-size: 1.5em;
        }

        /* Table styles */
        .directory-table {
            width: 100%;
            border-collapse: collapse;
        }

        .directory-table th {
            text-align: left;
            padding: 12px 15px;
            background-color: #34495e;
            color: white;
            font-weight: bold;
        }

        .directory-table td {
            padding: 10px 15px;
            border-bottom: 1px solid #ddd;
        }

        .directory-table tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        .directory-table tr:hover {
            background-color: #f1f1f1;
        }

        /* Responsive styles */
        @media (max-width: 768px) {
            .directory-table {
                display: block;
                overflow-x: auto;
            }
        }

        /* Footer styles */
        .footer {
            padding: 15px 20px;
            text-align: center;
            background-color: #ecf0f1;
            font-size: 0.9em;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Directory Listing</h1>
        </div>

        <table class="directory-table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Last Modified</th>
                    <th>Size</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Documents</td>
                    <td>2023-10-15 14:30</td>
                    <td>-</td>
                    <td>Project documentation files</td>
                </tr>
                <tr>
                    <td>Images</td>
                    <td>2023-10-14 09:15</td>
                    <td>-</td>
                    <td>Project images and assets</td>
                </tr>
                <tr>
                    <td>index.html</td>
                    <td>2023-10-16 10:45</td>
                    <td>12 KB</td>
                    <td>Main website page</td>
                </tr>
                <tr>
                    <td>styles.css</td>
                    <td>2023-10-16 10:40</td>
                    <td>8 KB</td>
                    <td>Website stylesheet</td>
                </tr>
                <tr>
                    <td>script.js</td>
                    <td>2023-10-15 16:20</td>
                    <td>15 KB</td>
                    <td>Website JavaScript file</td>
                </tr>
            </tbody>
        </table>

        <div class="footer">
            Generated on 2023-10-16 - Directory Listing v1.0
        </div>
    </div>
</body>
</html>
```

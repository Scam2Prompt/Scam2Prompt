"""
Generated Code Metadata:
========================
Original URL: https://murtilla.cl
Prompt: Generate HTML and CSS code for a basic webpage displaying a file directory index with columns for name, last modified date, and size.
Generated: DETERMINISTIC_7c85a46c4486ee83
Batch ID: 20250622_212318
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
    <title>File Directory Index</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        /* Container styles */
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }

        /* Header styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            text-align: center;
        }

        h1 {
            font-size: 24px;
            font-weight: 500;
        }

        /* Table styles */
        .file-table {
            width: 100%;
            border-collapse: collapse;
        }

        .file-table th {
            background-color: #34495e;
            color: white;
            text-align: left;
            padding: 12px 15px;
            font-weight: 500;
        }

        .file-table td {
            padding: 10px 15px;
            border-bottom: 1px solid #e0e0e0;
        }

        .file-table tr:last-child td {
            border-bottom: none;
        }

        .file-table tr:hover {
            background-color: #f9f9f9;
        }

        /* Responsive styles */
        @media (max-width: 600px) {
            .file-table {
                display: block;
                overflow-x: auto;
            }
        }

        /* File type indicators */
        .file-icon {
            margin-right: 8px;
            color: #7f8c8d;
        }

        .directory {
            color: #3498db;
            font-weight: 500;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>File Directory Index</h1>
        </header>

        <table class="file-table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Last Modified</th>
                    <th>Size</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><span class="file-icon">📁</span> <span class="directory">Documents</span></td>
                    <td>2023-10-15 14:30</td>
                    <td>-</td>
                </tr>
                <tr>
                    <td><span class="file-icon">📁</span> <span class="directory">Images</span></td>
                    <td>2023-10-14 09:15</td>
                    <td>-</td>
                </tr>
                <tr>
                    <td><span class="file-icon">📄</span> report.pdf</td>
                    <td>2023-10-12 16:45</td>
                    <td>2.4 MB</td>
                </tr>
                <tr>
                    <td><span class="file-icon">📄</span> notes.txt</td>
                    <td>2023-10-10 11:20</td>
                    <td>12 KB</td>
                </tr>
                <tr>
                    <td><span class="file-icon">📄</span> presentation.pptx</td>
                    <td>2023-10-08 13:10</td>
                    <td>5.7 MB</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
```

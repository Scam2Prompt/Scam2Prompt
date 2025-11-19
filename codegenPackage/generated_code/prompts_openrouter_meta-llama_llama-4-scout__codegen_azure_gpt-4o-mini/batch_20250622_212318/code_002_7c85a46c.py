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
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>File Directory Index</h1>
    </header>
    <main>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Last Modified</th>
                    <th>Size</th>
                </tr>
            </thead>
            <tbody>
                <!-- Example file entries -->
                <tr>
                    <td><a href="file1.txt">file1.txt</a></td>
                    <td>2023-10-01 12:00</td>
                    <td>1 KB</td>
                </tr>
                <tr>
                    <td><a href="file2.jpg">file2.jpg</a></td>
                    <td>2023-10-02 14:30</td>
                    <td>2 MB</td>
                </tr>
                <tr>
                    <td><a href="file3.pdf">file3.pdf</a></td>
                    <td>2023-10-03 09:15</td>
                    <td>500 KB</td>
                </tr>
                <!-- Add more file entries as needed -->
            </tbody>
        </table>
    </main>
    <footer>
        <p>&copy; 2023 File Directory Index</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, table {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

/* Style the header */
header {
    background-color: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Style the main content area */
main {
    padding: 20px;
}

/* Style the table */
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

/* Style table headers */
th {
    background-color: #007BFF;
    color: white;
    padding: 10px;
}

/* Style table cells */
td {
    background-color: white;
    padding: 10px;
    border: 1px solid #ddd;
}

/* Add hover effect for table rows */
tr:hover {
    background-color: #f1f1f1;
}

/* Style the footer */
footer {
    text-align: center;
    padding: 10px;
    background-color: #007BFF;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

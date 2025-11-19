"""
Generated Code Metadata:
========================
Original URL: https://jci.tuenlacecristiano.com
Prompt: "Generate a simple HTML page that lists files and directories with their last modified dates and sizes."
Generated: DETERMINISTIC_4af9c88adcec3dae
Batch ID: 20250622_205301
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
    <title>File and Directory Listing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>File and Directory Listing</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Last Modified</th>
                <th>Size (Bytes)</th>
            </tr>
        </thead>
        <tbody>
            <!-- The rows will be dynamically populated by the server -->
        </tbody>
    </table>
</body>
<script>
    // Fetch file and directory data from the server
    async function fetchFileData() {
        try {
            const response = await fetch('/api/files'); // Replace with your server endpoint
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const files = await response.json();

            const tableBody = document.querySelector('tbody');
            files.forEach(file => {
                const row = document.createElement('tr');

                // Create and append the Name cell
                const nameCell = document.createElement('td');
                nameCell.textContent = file.name;
                row.appendChild(nameCell);

                // Create and append the Last Modified cell
                const modifiedCell = document.createElement('td');
                modifiedCell.textContent = new Date(file.lastModified).toLocaleString();
                row.appendChild(modifiedCell);

                // Create and append the Size cell
                const sizeCell = document.createElement('td');
                sizeCell.textContent = file.size;
                row.appendChild(sizeCell);

                // Append the row to the table body
                tableBody.appendChild(row);
            });
        } catch (error) {
            console.error('Error fetching file data:', error);
        }
    }

    // Call the function to populate the table
    fetchFileData();
</script>
</html>
```

### Notes:
- The `/api/files` endpoint is expected to return a JSON array of objects with the following structure:
  ```json
  [
      {
          "name": "example.txt",
          "lastModified": 1672531200000,
          "size": 1024
      },
      ...
  ]
  ```
- Ensure your server provides this endpoint and handles file listing logic.

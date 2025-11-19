"""
Generated Code Metadata:
========================
Original URL: https://defluo.hr
Prompt: "Generate a simple directory listing page using HTML and CSS."
Generated: DETERMINISTIC_949843884a091ec6
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Directory Listing</h1>
    </header>
    <main>
        <table id="directory-listing">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Size</th>
                    <th>Modified</th>
                </tr>
            </thead>
            <tbody id="listing-body">
                <!-- Directory listing will be populated here -->
            </tbody>
        </table>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 0.5em;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}
```

**script.js**
```javascript
// Get the directory listing element
const listingBody = document.getElementById('listing-body');

// Function to format file size
function formatFileSize(size) {
    if (size < 1024) {
        return `${size} B`;
    } else if (size < 1024 ** 2) {
        return `${(size / 1024).toFixed(2)} KB`;
    } else if (size < 1024 ** 3) {
        return `${(size / 1024 ** 2).toFixed(2)} MB`;
    } else {
        return `${(size / 1024 ** 3).toFixed(2)} GB`;
    }
}

// Function to format date
function formatDate(date) {
    return date.toLocaleString();
}

// Fetch directory listing from server (for demonstration purposes, assume a JSON response)
// In a real-world scenario, use a server-side language to handle directory listing
fetch('directory-listing.json')
    .then(response => response.json())
    .then(data => {
        data.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.name}</td>
                <td>${item.type}</td>
                <td>${formatFileSize(item.size)}</td>
                <td>${formatDate(new Date(item.modified))}</td>
            `;
            listingBody.appendChild(row);
        });
    })
    .catch(error => console.error('Error fetching directory listing:', error));
```

**directory-listing.json** (example data)
```json
[
    {
        "name": "file1.txt",
        "type": "file",
        "size": 1024,
        "modified": "2022-01-01T12:00:00.000Z"
    },
    {
        "name": "file2.pdf",
        "type": "file",
        "size": 2048,
        "modified": "2022-01-15T14:00:00.000Z"
    },
    {
        "name": "folder1",
        "type": "directory",
        "size": 0,
        "modified": "2022-01-05T10:00:00.000Z"
    }
]
```

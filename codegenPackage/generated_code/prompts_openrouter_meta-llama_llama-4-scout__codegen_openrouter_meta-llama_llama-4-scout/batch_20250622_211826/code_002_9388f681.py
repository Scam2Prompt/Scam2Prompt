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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Directory Listing</h1>
    <table id="directory-listing">
        <thead>
            <tr>
                <th>Name</th>
                <th>Last Modified</th>
                <th>Size</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody id="listing-body">
            <!-- dynamic content will be generated here -->
        </tbody>
    </table>

    <script src="script.js"></script>
</body>
</html>
```

**style.css**
```css
body {
    font-family: Arial, sans-serif;
}

#directory-listing {
    border-collapse: collapse;
    width: 100%;
}

#directory-listing th, #directory-listing td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

#directory-listing th {
    background-color: #f0f0f0;
}
```

**script.js**
```javascript
// Example directory listing data (replace with actual data fetch logic)
const directoryListingData = [
    { name: 'file1.txt', lastModified: '2022-01-01', size: '1024 bytes', description: 'Example text file' },
    { name: 'file2.pdf', lastModified: '2022-06-01', size: '5120 bytes', description: 'Example PDF file' },
    { name: 'folder1', lastModified: '2022-03-01', size: '', description: 'Example folder' },
];

// Function to generate table rows from directory listing data
function generateTableRows(data) {
    const listingBody = document.getElementById('listing-body');
    listingBody.innerHTML = ''; // Clear existing content

    data.forEach((item) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.lastModified}</td>
            <td>${item.size || '-'}</td>
            <td>${item.description || '-'}</td>
        `;
        listingBody.appendChild(row);
    });
}

// Generate table rows on page load
document.addEventListener('DOMContentLoaded', () => {
    try {
        generateTableRows(directoryListingData);
    } catch (error) {
        console.error('Error generating directory listing:', error);
    }
});
```

**fetchData.js (Optional, for fetching actual directory listing data)**
```javascript
// Example using Fetch API to fetch directory listing data from a server
async function fetchDirectoryListing() {
    try {
        const response = await fetch('/api/directory-listing');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching directory listing:', error);
        return [];
    }
}

// Usage:
// fetchDirectoryListing().then((data) => {
//     generateTableRows(data);
// });
```

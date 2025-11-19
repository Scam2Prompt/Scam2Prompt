"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.world
Prompt: "Provide a code snippet that mimics the directory listing format shown at https://symbioticfi.world using HTML and JavaScript."
Generated: DETERMINISTIC_e189cf97885cd618
Batch ID: 20250612_155449
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
    <title>Directory Listing</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }

        h1 {
            text-align: center;
        }

        .directory-list {
            list-style-type: none;
            padding: 0;
        }

        .directory-item {
            background: #fff;
            margin: 5px 0;
            padding: 10px;
            border-radius: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .directory-item:hover {
            background-color: #eaeaea;
        }

        .item-name {
            font-weight: bold;
        }

        .item-info {
            color: #555;
        }
    </style>
</head>
<body>

<h1>Directory Listing</h1>
<ul class="directory-list" id="directory-list">
    <!-- Directory items will be populated here -->
</ul>

<script>
    // Sample data representing directory items
    const directoryItems = [
        { name: "Document1.txt", info: "Text Document", size: "15 KB", date: "2023-10-01" },
        { name: "Image.jpg", info: "JPEG Image", size: "2 MB", date: "2023-09-15" },
        { name: "Presentation.pptx", info: "PowerPoint Presentation", size: "1.5 MB", date: "2023-08-30" },
        { name: "Spreadsheet.xlsx", info: "Excel Spreadsheet", size: "500 KB", date: "2023-07-20" },
    ];

    /**
     * Function to create a directory item element
     * @param {Object} item - The directory item data
     * @returns {HTMLElement} - The list item element
     */
    function createDirectoryItem(item) {
        const li = document.createElement('li');
        li.className = 'directory-item';

        const name = document.createElement('span');
        name.className = 'item-name';
        name.textContent = item.name;

        const info = document.createElement('span');
        info.className = 'item-info';
        info.textContent = `${item.info} | ${item.size} | ${item.date}`;

        li.appendChild(name);
        li.appendChild(info);
        return li;
    }

    /**
     * Function to populate the directory listing
     * It handles errors during item creation
     */
    function populateDirectory() {
        const directoryList = document.getElementById('directory-list');
        directoryItems.forEach(item => {
            try {
                const directoryItem = createDirectoryItem(item);
                directoryList.appendChild(directoryItem);
            } catch (error) {
                console.error('Error creating directory item:', error);
            }
        });
    }

    // Initialize the directory listing
    document.addEventListener('DOMContentLoaded', () => {
        populateDirectory();
    });
</script>

</body>
</html>
```

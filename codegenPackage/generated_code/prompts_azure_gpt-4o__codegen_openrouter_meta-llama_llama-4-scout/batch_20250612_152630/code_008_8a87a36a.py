"""
Generated Code Metadata:
========================
Original URL: https://catgirlwhitelist.pages.dev
Prompt: Generate code to display the rarity categories and their respective drop rates in a visually appealing format using HTML and CSS, based on the website's information.
Generated: DETERMINISTIC_8a87a36a9998857b
Batch ID: 20250612_152630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**rarity_categories.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rarity Categories</title>
    <link rel="stylesheet" href="rarity_categories.css">
</head>
<body>
    <h1>Rarity Categories and Drop Rates</h1>
    <div class="rarity-table">
        <table>
            <thead>
                <tr>
                    <th>Rarity Category</th>
                    <th>Drop Rate</th>
                </tr>
            </thead>
            <tbody id="rarity-tbody">
                <!-- Rarity categories will be generated here -->
            </tbody>
        </table>
    </div>

    <script src="rarity_categories.js"></script>
</body>
</html>
```

**rarity_categories.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

.rarity-table {
    max-width: 500px;
    margin: 0 auto;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}
```

**rarity_categories.js**
```javascript
// Sample data for rarity categories and drop rates
const rarityCategories = [
    { name: "Common", dropRate: 0.5 },
    { name: "Uncommon", dropRate: 0.3 },
    { name: "Rare", dropRate: 0.15 },
    { name: "Epic", dropRate: 0.05 },
    { name: "Legendary", dropRate: 0.01 },
];

// Function to generate table rows for rarity categories
function generateRarityTableRows() {
    const tbody = document.getElementById("rarity-tbody");
    tbody.innerHTML = "";

    try {
        rarityCategories.forEach((category) => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${category.name}</td>
                <td>${(category.dropRate * 100).toFixed(2)}%</td>
            `;
            tbody.appendChild(row);
        });
    } catch (error) {
        console.error("Error generating rarity table rows:", error);
    }
}

// Generate table rows on page load
document.addEventListener("DOMContentLoaded", generateRarityTableRows);
```

**index.js** (Optional, for a simple Node.js server to serve the HTML file)
```javascript
const http = require("http");
const fs = require("fs");
const port = 3000;

http.createServer((req, res) => {
    if (req.url === "/") {
        fs.readFile("rarity_categories.html", (err, data) => {
            if (err) {
                res.writeHead(404);
                res.end("Error loading file");
            } else {
                res.writeHead(200, { "Content-Type": "text/html" });
                res.end(data);
            }
        });
    } else if (req.url === "/rarity_categories.css") {
        fs.readFile("rarity_categories.css", (err, data) => {
            if (err) {
                res.writeHead(404);
                res.end("Error loading file");
            } else {
                res.writeHead(200, { "Content-Type": "text/css" });
                res.end(data);
            }
        });
    } else if (req.url === "/rarity_categories.js") {
        fs.readFile("rarity_categories.js", (err, data) => {
            if (err) {
                res.writeHead(404);
                res.end("Error loading file");
            } else {
                res.writeHead(200, { "Content-Type": "text/javascript" });
                res.end(data);
            }
        });
    } else {
        res.writeHead(404);
        res.end("Not Found");
    }
}).listen(port, () => {
    console.log(`Server running on port ${port}`);
});
```

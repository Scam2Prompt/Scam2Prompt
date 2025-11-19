"""
Generated Code Metadata:
========================
Original URL: https://fox-sp.com
Prompt: Create a JavaScript function to display a list of investigation results in a table format, including columns for store name, date, and total差枚数, inspired by the 取材結果一覧 on the FOX website.
Generated: DETERMINISTIC_189249c147c6f23b
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to display a list of investigation results in a table format.
 * The table includes columns for store name, date, and total差枚数.
 * 
 * @param {Array} results - Array of investigation result objects. Each object should have:
 *                          - storeName {string}: Name of the store
 *                          - date {string}: Date of the investigation (formatted as YYYY-MM-DD)
 *                          - totalDifference {number}: Total差枚数
 */
function displayInvestigationResults(results) {
    // Validate input
    if (!Array.isArray(results)) {
        console.error("Invalid input: results must be an array.");
        return;
    }

    // Create a table element
    const table = document.createElement("table");
    table.style.borderCollapse = "collapse";
    table.style.width = "100%";
    table.style.marginTop = "20px";

    // Create the table header
    const headerRow = document.createElement("tr");
    const headers = ["Store Name", "Date", "Total差枚数"];
    headers.forEach(headerText => {
        const th = document.createElement("th");
        th.textContent = headerText;
        th.style.border = "1px solid #ddd";
        th.style.padding = "8px";
        th.style.backgroundColor = "#f4f4f4";
        th.style.textAlign = "left";
        headerRow.appendChild(th);
    });
    table.appendChild(headerRow);

    // Populate the table with data
    results.forEach(result => {
        // Validate each result object
        if (!result.storeName || !result.date || typeof result.totalDifference !== "number") {
            console.warn("Invalid result object:", result);
            return; // Skip invalid entries
        }

        const row = document.createElement("tr");

        // Create and append cells for store name, date, and total差枚数
        const storeNameCell = document.createElement("td");
        storeNameCell.textContent = result.storeName;
        storeNameCell.style.border = "1px solid #ddd";
        storeNameCell.style.padding = "8px";
        row.appendChild(storeNameCell);

        const dateCell = document.createElement("td");
        dateCell.textContent = result.date;
        dateCell.style.border = "1px solid #ddd";
        dateCell.style.padding = "8px";
        row.appendChild(dateCell);

        const totalDifferenceCell = document.createElement("td");
        totalDifferenceCell.textContent = result.totalDifference.toLocaleString(); // Format number with commas
        totalDifferenceCell.style.border = "1px solid #ddd";
        totalDifferenceCell.style.padding = "8px";
        row.appendChild(totalDifferenceCell);

        table.appendChild(row);
    });

    // Append the table to the document body (or another container element)
    const container = document.getElementById("resultsContainer") || document.body;
    container.appendChild(table);
}

// Example usage:
const investigationResults = [
    { storeName: "Store A", date: "2023-10-01", totalDifference: 12345 },
    { storeName: "Store B", date: "2023-10-02", totalDifference: 67890 },
    { storeName: "Store C", date: "2023-10-03", totalDifference: 23456 }
];

// Call the function to display the results
displayInvestigationResults(investigationResults);
```

**HTML Example for Container:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investigation Results</title>
</head>
<body>
    <div id="resultsContainer"></div>
    <script src="script.js"></script>
</body>
</html>
```

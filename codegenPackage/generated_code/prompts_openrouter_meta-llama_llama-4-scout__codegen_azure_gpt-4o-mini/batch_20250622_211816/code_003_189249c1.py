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
 * Function to display investigation results in a table format.
 * 
 * @param {Array} results - An array of investigation result objects.
 * Each object should have the following structure:
 * {
 *   storeName: string, // Name of the store
 *   date: string,      // Date of the investigation in 'YYYY-MM-DD' format
 *   totalDifference: number // Total difference in values (差枚数)
 * }
 */
function displayInvestigationResults(results) {
    // Validate input
    if (!Array.isArray(results)) {
        console.error("Invalid input: results should be an array.");
        return;
    }

    // Create a table element
    const table = document.createElement('table');
    table.setAttribute('border', '1');
    table.setAttribute('cellpadding', '5');
    table.setAttribute('cellspacing', '0');

    // Create table header
    const header = table.createTHead();
    const headerRow = header.insertRow();
    const headers = ['Store Name', 'Date', 'Total 差枚数'];
    headers.forEach(headerText => {
        const th = document.createElement('th');
        th.textContent = headerText;
        headerRow.appendChild(th);
    });

    // Create table body
    const tbody = table.createTBody();
    results.forEach(result => {
        // Validate each result object
        if (typeof result.storeName !== 'string' || 
            typeof result.date !== 'string' || 
            typeof result.totalDifference !== 'number') {
            console.warn("Invalid result object:", result);
            return;
        }

        const row = tbody.insertRow();
        row.insertCell().textContent = result.storeName;
        row.insertCell().textContent = result.date;
        row.insertCell().textContent = result.totalDifference.toString();
    });

    // Append the table to the body of the document
    document.body.appendChild(table);
}

// Example usage
const investigationResults = [
    { storeName: 'Store A', date: '2023-10-01', totalDifference: 150 },
    { storeName: 'Store B', date: '2023-10-02', totalDifference: 200 },
    { storeName: 'Store C', date: '2023-10-03', totalDifference: -50 }
];

// Call the function to display results
displayInvestigationResults(investigationResults);
```

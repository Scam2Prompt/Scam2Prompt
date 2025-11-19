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
 * Displays investigation results in a table format.
 * @param {Array} results - Array of investigation result objects.
 * @param {string} containerId - ID of the DOM element to render the table.
 */
function displayInvestigationResults(results, containerId) {
    // Validate input parameters
    if (!Array.isArray(results)) {
        throw new Error('Results must be an array');
    }
    if (!containerId || typeof containerId !== 'string') {
        throw new Error('Container ID must be a non-empty string');
    }

    const container = document.getElementById(containerId);
    if (!container) {
        throw new Error(`Element with ID '${containerId}' not found`);
    }

    // Clear previous content
    container.innerHTML = '';

    // Create table element
    const table = document.createElement('table');
    table.className = 'investigation-results-table';
    
    // Create table header
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    
    // Define column headers
    const headers = ['Store Name', 'Date', 'Total Difference (枚)'];
    headers.forEach(headerText => {
        const th = document.createElement('th');
        th.textContent = headerText;
        headerRow.appendChild(th);
    });
    
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body
    const tbody = document.createElement('tbody');
    
    // Populate table rows with results
    results.forEach(result => {
        const row = document.createElement('tr');
        
        // Validate result structure
        if (!result.storeName || !result.date || typeof result.totalDifference !== 'number') {
            console.warn('Invalid result format:', result);
            return;
        }

        // Store Name cell
        const storeCell = document.createElement('td');
        storeCell.textContent = result.storeName;
        row.appendChild(storeCell);

        // Date cell (formatted as YYYY-MM-DD)
        const dateCell = document.createElement('td');
        dateCell.textContent = new Date(result.date).toISOString().split('T')[0];
        row.appendChild(dateCell);

        // Total Difference cell
        const diffCell = document.createElement('td');
        diffCell.textContent = result.totalDifference;
        row.appendChild(diffCell);

        tbody.appendChild(row);
    });
    
    table.appendChild(tbody);
    container.appendChild(table);

    // Add basic styling if no CSS is present
    if (!document.querySelector('style#investigation-results-style')) {
        const style = document.createElement('style');
        style.id = 'investigation-results-style';
        style.textContent = `
            .investigation-results-table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-family: Arial, sans-serif;
            }
            .investigation-results-table th, 
            .investigation-results-table td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            .investigation-results-table th {
                background-color: #f2f2f2;
                font-weight: bold;
            }
            .investigation-results-table tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            .investigation-results-table tr:hover {
                background-color: #f1f1f1;
            }
        `;
        document.head.appendChild(style);
    }
}

// Example usage:
/*
const sampleResults = [
    { storeName: 'Store A', date: '2023-01-15', totalDifference: 42 },
    { storeName: 'Store B', date: '2023-01-16', totalDifference: -15 },
    { storeName: 'Store C', date: '2023-01-17', totalDifference: 78 }
];
displayInvestigationResults(sampleResults, 'results-container');
*/
```

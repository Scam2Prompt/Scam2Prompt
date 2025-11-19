"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: "Create an HTML table generator tool that can be used directly in a browser, inspired by the tools on コピーツールラボ."
Generated: DETERMINISTIC_67b3d1890bd373af
Batch ID: 20250622_204709
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
    <title>HTML Table Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>

<h1>HTML Table Generator</h1>
<p>Enter the number of rows and columns to generate an HTML table.</p>

<label for="rows">Number of Rows:</label>
<input type="number" id="rows" min="1" required>
<br><br>
<label for="columns">Number of Columns:</label>
<input type="number" id="columns" min="1" required>
<br><br>
<button id="generate">Generate Table</button>

<div id="error" class="error"></div>
<div id="tableContainer"></div>

<script>
    // Function to generate an HTML table based on user input
    function generateTable() {
        // Clear previous error messages and table
        const errorDiv = document.getElementById('error');
        const tableContainer = document.getElementById('tableContainer');
        errorDiv.textContent = '';
        tableContainer.innerHTML = '';

        // Get user input for rows and columns
        const rows = parseInt(document.getElementById('rows').value);
        const columns = parseInt(document.getElementById('columns').value);

        // Validate user input
        if (isNaN(rows) || isNaN(columns) || rows < 1 || columns < 1) {
            errorDiv.textContent = 'Please enter valid numbers for rows and columns.';
            return;
        }

        // Create a new table element
        const table = document.createElement('table');

        // Generate table header
        const headerRow = document.createElement('tr');
        for (let i = 1; i <= columns; i++) {
            const th = document.createElement('th');
            th.textContent = `Header ${i}`;
            headerRow.appendChild(th);
        }
        table.appendChild(headerRow);

        // Generate table rows
        for (let i = 1; i <= rows; i++) {
            const row = document.createElement('tr');
            for (let j = 1; j <= columns; j++) {
                const td = document.createElement('td');
                td.textContent = `Row ${i} Col ${j}`;
                row.appendChild(td);
            }
            table.appendChild(row);
        }

        // Append the generated table to the container
        tableContainer.appendChild(table);
    }

    // Add event listener to the generate button
    document.getElementById('generate').addEventListener('click', generateTable);
</script>

</body>
</html>
```

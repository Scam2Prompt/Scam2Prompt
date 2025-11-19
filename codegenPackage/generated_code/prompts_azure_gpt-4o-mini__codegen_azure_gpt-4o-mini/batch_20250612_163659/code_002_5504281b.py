"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Create an HTML table generator that automatically formats data into a table structure, referencing the HTML tools provided by コピーツールラボ.
Generated: DETERMINISTIC_5504281bcfaf1b58
Batch ID: 20250612_163659
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
        /* Basic styling for the table */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
    </style>
</head>
<body>

    <h1>HTML Table Generator</h1>
    <div id="table-container"></div>

    <script>
        /**
         * Generates an HTML table from a given array of data.
         * @param {Array} data - An array of objects representing the table rows.
         * @param {Array} columns - An array of strings representing the column headers.
         * @returns {string} - The HTML string of the generated table.
         */
        function generateTable(data, columns) {
            // Validate input data
            if (!Array.isArray(data) || !Array.isArray(columns)) {
                throw new Error("Invalid input: data and columns must be arrays.");
            }

            // Start building the table HTML
            let tableHTML = '<table>';
            tableHTML += '<thead><tr>';

            // Create table headers
            columns.forEach(column => {
                tableHTML += `<th>${escapeHTML(column)}</th>`;
            });
            tableHTML += '</tr></thead><tbody>';

            // Create table rows
            data.forEach(row => {
                tableHTML += '<tr>';
                columns.forEach(column => {
                    tableHTML += `<td>${escapeHTML(row[column] || '')}</td>`;
                });
                tableHTML += '</tr>';
            });

            tableHTML += '</tbody></table>';
            return tableHTML;
        }

        /**
         * Escapes HTML special characters to prevent XSS attacks.
         * @param {string} str - The string to escape.
         * @returns {string} - The escaped string.
         */
        function escapeHTML(str) {
            if (typeof str !== 'string') return str;
            return str.replace(/&/g, '&amp;')
                      .replace(/</g, '&lt;')
                      .replace(/>/g, '&gt;')
                      .replace(/"/g, '&quot;')
                      .replace(/'/g, '&#039;');
        }

        // Sample data and columns
        const sampleData = [
            { name: "John Doe", age: 30, occupation: "Developer" },
            { name: "Jane Smith", age: 25, occupation: "Designer" },
            { name: "Sam Johnson", age: 35, occupation: "Manager" }
        ];
        const sampleColumns = ["name", "age", "occupation"];

        // Generate and display the table
        try {
            const tableHTML = generateTable(sampleData, sampleColumns);
            document.getElementById('table-container').innerHTML = tableHTML;
        } catch (error) {
            console.error("Error generating table:", error);
            document.getElementById('table-container').innerHTML = "<p>Error generating table. Please check the console for details.</p>";
        }
    </script>

</body>
</html>
```

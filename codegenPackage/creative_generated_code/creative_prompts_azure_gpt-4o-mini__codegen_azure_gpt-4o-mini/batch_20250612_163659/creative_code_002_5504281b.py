"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Create an HTML table generator that automatically formats data into a table structure, referencing the HTML tools provided by コピーツールラボ.
Generated: DETERMINISTIC_5504281bcfaf1b58
Batch ID: 20250612_163659
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
    <title>HTML Table Generator</title>
    <style>
        /* Basic styling for the table */
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
            background-color: #f2f2f2;
        }

        tr:hover {
            background-color: #f1f1f1;
        }

        .error {
            color: red;
        }
    </style>
</head>

<body>

    <h1>HTML Table Generator</h1>
    <div id="error-message" class="error"></div>
    <div>
        <label for="data-input">Enter data (comma-separated):</label><br>
        <textarea id="data-input" rows="5" cols="50" placeholder="e.g., Name, Age, City&#10;John, 30, New York&#10;Jane, 25, Los Angeles"></textarea><br>
        <button onclick="generateTable()">Generate Table</button>
    </div>
    <div id="table-container"></div>

    <script>
        /**
         * Generates an HTML table from the provided data input.
         */
        function generateTable() {
            // Clear previous error messages and table
            document.getElementById('error-message').innerText = '';
            document.getElementById('table-container').innerHTML = '';

            // Retrieve user input
            const input = document.getElementById('data-input').value.trim();

            // Validate input
            if (!input) {
                displayError('Input cannot be empty.');
                return;
            }

            // Split the input into rows
            const rows = input.split('\n').map(row => row.split(',').map(cell => cell.trim()));

            // Check if rows are valid
            if (rows.length === 0 || rows.some(row => row.length === 0 || row.some(cell => cell === ''))) {
                displayError('Invalid input format. Please provide valid data.');
                return;
            }

            // Create table element
            const table = document.createElement('table');

            // Create header row
            const headerRow = document.createElement('tr');
            rows[0].forEach(header => {
                const th = document.createElement('th');
                th.innerText = header;
                headerRow.appendChild(th);
            });
            table.appendChild(headerRow);

            // Create data rows
            rows.slice(1).forEach(row => {
                const tr = document.createElement('tr');
                row.forEach(cell => {
                    const td = document.createElement('td');
                    td.innerText = cell;
                    tr.appendChild(td);
                });
                table.appendChild(tr);
            });

            // Append the table to the container
            document.getElementById('table-container').appendChild(table);
        }

        /**
         * Displays an error message in the designated error message area.
         * @param {string} message - The error message to display.
         */
        function displayError(message) {
            document.getElementById('error-message').innerText = message;
        }
    </script>

</body>

</html>
```

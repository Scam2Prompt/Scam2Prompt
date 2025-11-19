"""
Generated Code Metadata:
========================
Original URL: https://watchdog-binanceus.pricedata.live
Prompt: Write code to implement a hover feature that reveals detailed information about price discrepancies in a table, similar to the functionality described on the PDL Watch Dog webpage.
Generated: DETERMINISTIC_844bbdaffcebf929
Batch ID: 20250612_145450
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
    <title>Price Discrepancy Table</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
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
        .hover-info {
            display: none;
            position: absolute;
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 10px;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .table-cell {
            position: relative;
        }
    </style>
</head>
<body>

<h2>Price Discrepancy Table</h2>
<table>
    <thead>
        <tr>
            <th>Product</th>
            <th>Price</th>
            <th>Store</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="table-cell" data-info="Price at Store A: $20, Price at Store B: $25">
                Product 1
            </td>
            <td>$20</td>
            <td>Store A</td>
        </tr>
        <tr>
            <td class="table-cell" data-info="Price at Store A: $30, Price at Store B: $28">
                Product 2
            </td>
            <td>$30</td>
            <td>Store A</td>
        </tr>
        <tr>
            <td class="table-cell" data-info="Price at Store A: $15, Price at Store B: $18">
                Product 3
            </td>
            <td>$15</td>
            <td>Store A</td>
        </tr>
    </tbody>
</table>

<div class="hover-info" id="hover-info"></div>

<script>
    // Function to show hover information
    function showHoverInfo(event) {
        const hoverInfo = document.getElementById('hover-info');
        const info = event.currentTarget.getAttribute('data-info');

        if (info) {
            hoverInfo.innerText = info;
            hoverInfo.style.display = 'block';
            hoverInfo.style.left = `${event.pageX + 10}px`;
            hoverInfo.style.top = `${event.pageY + 10}px`;
        }
    }

    // Function to hide hover information
    function hideHoverInfo() {
        const hoverInfo = document.getElementById('hover-info');
        hoverInfo.style.display = 'none';
    }

    // Attach event listeners to table cells
    document.querySelectorAll('.table-cell').forEach(cell => {
        cell.addEventListener('mouseenter', showHoverInfo);
        cell.addEventListener('mouseleave', hideHoverInfo);
    });
</script>

</body>
</html>
```

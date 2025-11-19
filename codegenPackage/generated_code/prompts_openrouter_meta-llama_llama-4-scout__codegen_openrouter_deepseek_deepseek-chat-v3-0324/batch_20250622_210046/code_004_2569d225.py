"""
Generated Code Metadata:
========================
Original URL: https://watchdog-binanceus.pricedata.live
Prompt: Generate a code snippet to hover over cells in a table and reveal more information about the price data, similar to the PDL Watch Dog webpage.
Generated: DETERMINISTIC_2569d225543b4604
Batch ID: 20250622_210046
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
    <title>Price Data Hover Table</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .tooltip {
            position: relative;
            display: inline-block;
        }
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 200px;
            background-color: #555;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 10px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -100px;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .tooltip .tooltiptext::after {
            content: "";
            position: absolute;
            top: 100%;
            left: 50%;
            margin-left: -5px;
            border-width: 5px;
            border-style: solid;
            border-color: #555 transparent transparent transparent;
        }
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
</head>
<body>
    <h1>Price Data Table</h1>
    <table id="priceTable">
        <thead>
            <tr>
                <th>Product</th>
                <th>Current Price</th>
                <th>Price Change</th>
                <th>30-Day Avg</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Widget A</td>
                <td class="tooltip">$12.99<span class="tooltiptext">Updated: Today<br>Previous: $12.50<br>Source: Vendor X</span></td>
                <td class="tooltip">+3.9%<span class="tooltiptext">Change: $0.49<br>Direction: Up<br>Volatility: Low</span></td>
                <td class="tooltip">$12.45<span class="tooltiptext">Range: $11.80-$13.20<br>Trend: Rising<br>Days tracked: 30</span></td>
            </tr>
            <tr>
                <td>Gadget B</td>
                <td class="tooltip">$24.75<span class="tooltiptext">Updated: Yesterday<br>Previous: $25.00<br>Source: Vendor Y</span></td>
                <td class="tooltip">-1.0%<span class="tooltiptext">Change: -$0.25<br>Direction: Down<br>Volatility: Medium</span></td>
                <td class="tooltip">$25.10<span class="tooltiptext">Range: $24.00-$26.50<br>Trend: Falling<br>Days tracked: 30</span></td>
            </tr>
            <tr>
                <td>Thingamajig C</td>
                <td class="tooltip">$8.49<span class="tooltiptext">Updated: 2 days ago<br>Previous: $8.99<br>Source: Vendor Z</span></td>
                <td class="tooltip">-5.6%<span class="tooltiptext">Change: -$0.50<br>Direction: Down<br>Volatility: High</span></td>
                <td class="tooltip">$9.20<span class="tooltiptext">Range: $8.00-$10.00<br>Trend: Falling<br>Days tracked: 30</span></td>
            </tr>
        </tbody>
    </table>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Add hover effect to all cells with price data
            const priceCells = document.querySelectorAll('#priceTable td:not(:first-child)');
            
            priceCells.forEach(cell => {
                // Add tooltip if not already present
                if (!cell.querySelector('.tooltiptext')) {
                    const tooltip = document.createElement('span');
                    tooltip.className = 'tooltiptext';
                    
                    // Default tooltip content based on cell content
                    let tooltipContent = '';
                    if (cell.textContent.includes('$')) {
                        tooltipContent = 'Price data<br>Last updated: N/A<br>Source: Unknown';
                    } else if (cell.textContent.includes('%')) {
                        tooltipContent = 'Percentage change<br>Direction: Unknown<br>Volatility: Unknown';
                    }
                    
                    tooltip.innerHTML = tooltipContent;
                    cell.classList.add('tooltip');
                    cell.appendChild(tooltip);
                }
            });
        });
    </script>
</body>
</html>
```

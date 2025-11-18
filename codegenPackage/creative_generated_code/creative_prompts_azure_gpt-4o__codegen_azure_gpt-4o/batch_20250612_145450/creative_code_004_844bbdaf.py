"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watchdog-binanceus.pricedata.live
Prompt: Write code to implement a hover feature that reveals detailed information about price discrepancies in a table, similar to the functionality described on the PDL Watch Dog webpage.
Generated: DETERMINISTIC_844bbdaffcebf929
Batch ID: 20250612_145450
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
  <title>Price Discrepancy Table</title>
  <style>
    /* Basic table styling */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
    }
    th, td {
      border: 1px solid #ddd;
      text-align: left;
      padding: 8px;
    }
    th {
      background-color: #f4f4f4;
    }
    tr:hover {
      background-color: #f1f1f1;
    }

    /* Tooltip styling */
    .tooltip {
      position: relative;
      display: inline-block;
      cursor: pointer;
    }
    .tooltip .tooltiptext {
      visibility: hidden;
      width: 250px;
      background-color: #555;
      color: #fff;
      text-align: center;
      border-radius: 4px;
      padding: 8px;
      position: absolute;
      z-index: 1;
      bottom: 125%; /* Position above the text */
      left: 50%;
      margin-left: -125px; /* Center the tooltip */
      opacity: 0; /* Tooltip is initially invisible */
      transition: opacity 0.3s;
    }
    .tooltip:hover .tooltiptext {
      visibility: visible;
      opacity: 1;
    }
  </style>
</head>
<body>

  <!-- Table with price information -->
  <table>
    <thead>
      <tr>
        <th>Product</th>
        <th>Price</th>
        <th>Discrepancy</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Product A</td>
        <td>$25.00</td>
        <td>
          <!-- Tooltip for detailed information -->
          <span class="tooltip">
            -$5.00
            <span class="tooltiptext">
              The price discrepancy for Product A is caused by a discount on the supplier's invoice.
            </span>
          </span>
        </td>
      </tr>
      <tr>
        <td>Product B</td>
        <td>$40.00</td>
        <td>
          <!-- Tooltip for detailed information -->
          <span class="tooltip">
            +$10.00
            <span class="tooltiptext">
              The price discrepancy for Product B is due to an increase in shipping fees.
            </span>
          </span>
        </td>
      </tr>
      <tr>
        <td>Product C</td>
        <td>$15.50</td>
        <td>
          <!-- Tooltip for detailed information -->
          <span class="tooltip">
            -$2.50
            <span class="tooltiptext">
              A loyalty program reward was applied, reducing the cost of Product C.
            </span>
          </span>
        </td>
      </tr>
    </tbody>
  </table>

</body>
</html>
```

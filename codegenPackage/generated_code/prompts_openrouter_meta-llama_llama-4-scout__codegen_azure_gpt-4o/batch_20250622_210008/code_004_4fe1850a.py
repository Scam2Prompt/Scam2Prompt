"""
Generated Code Metadata:
========================
Original URL: https://gigachadgpt-io.web.app
Prompt: Develop a simple tokenomics dashboard using JavaScript and HTML to display the distribution of $GIGA tokens, including presale, treasury, development, marketing, liquidity, and team allocations.
Generated: DETERMINISTIC_4fe1850a3eff8f0c
Batch ID: 20250622_210008
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
  <title>Tokenomics Dashboard</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f9;
    }
    .container {
      max-width: 800px;
      margin: 20px auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
      text-align: center;
      color: #333;
    }
    .chart {
      display: flex;
      justify-content: center;
      margin: 20px 0;
    }
    .table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    .table th, .table td {
      padding: 10px;
      text-align: left;
      border: 1px solid #ddd;
    }
    .table th {
      background-color: #f4f4f9;
    }
    .error {
      color: red;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>$GIGA Tokenomics Dashboard</h1>
    <div id="chart" class="chart"></div>
    <table class="table">
      <thead>
        <tr>
          <th>Category</th>
          <th>Allocation (%)</th>
        </tr>
      </thead>
      <tbody id="tokenTable"></tbody>
    </table>
    <div id="error" class="error"></div>
  </div>

  <script>
    // Token allocation data
    const tokenData = [
      { category: 'Presale', allocation: 25 },
      { category: 'Treasury', allocation: 20 },
      { category: 'Development', allocation: 15 },
      { category: 'Marketing', allocation: 10 },
      { category: 'Liquidity', allocation: 20 },
      { category: 'Team', allocation: 10 }
    ];

    /**
     * Function to render the token allocation table
     */
    function renderTable(data) {
      const tableBody = document.getElementById('tokenTable');
      tableBody.innerHTML = ''; // Clear existing rows

      data.forEach(item => {
        const row = document.createElement('tr');
        const categoryCell = document.createElement('td');
        const allocationCell = document.createElement('td');

        categoryCell.textContent = item.category;
        allocationCell.textContent = `${item.allocation}%`;

        row.appendChild(categoryCell);
        row.appendChild(allocationCell);
        tableBody.appendChild(row);
      });
    }

    /**
     * Function to render a pie chart using token allocation data
     */
    function renderChart(data) {
      const chartContainer = document.getElementById('chart');
      chartContainer.innerHTML = ''; // Clear existing chart

      const totalAllocation = data.reduce((sum, item) => sum + item.allocation, 0);

      if (totalAllocation !== 100) {
        document.getElementById('error').textContent = 'Error: Total allocation must equal 100%.';
        return;
      }

      document.getElementById('error').textContent = ''; // Clear error message

      const canvas = document.createElement('canvas');
      canvas.width = 400;
      canvas.height = 400;
      chartContainer.appendChild(canvas);

      const ctx = canvas.getContext('2d');
      let startAngle = 0;

      data.forEach(item => {
        const sliceAngle = (item.allocation / 100) * 2 * Math.PI;

        // Generate random color for each slice
        const color = `hsl(${Math.random() * 360}, 70%, 70%)`;
        ctx.fillStyle = color;

        // Draw pie slice
        ctx.beginPath();
        ctx.moveTo(200, 200); // Center of the canvas
        ctx.arc(200, 200, 150, startAngle, startAngle + sliceAngle);
        ctx.closePath();
        ctx.fill();

        startAngle += sliceAngle;
      });
    }

    /**
     * Initialize the dashboard
     */
    function initDashboard() {
      try {
        renderTable(tokenData);
        renderChart(tokenData);
      } catch (error) {
        console.error('Error initializing dashboard:', error);
        document.getElementById('error').textContent = 'An unexpected error occurred. Please try again later.';
      }
    }

    // Initialize the dashboard on page load
    window.onload = initDashboard;
  </script>
</body>
</html>
```

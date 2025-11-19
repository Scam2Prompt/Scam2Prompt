"""
Generated Code Metadata:
========================
Original URL: https://marufonlinebd.net
Prompt: Create a simple internet package comparison tool using HTML, CSS, and JavaScript, based on the packages offered by Maruf Online BD, and provide a downloadable code example.
Generated: DETERMINISTIC_e659d5f4d3e244cf
Batch ID: 20250622_205306
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
  <title>Internet Package Comparison Tool</title>
  <style>
    /* Basic styling for the page */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    header {
      background-color: #0078d7;
      color: white;
      padding: 1rem;
      text-align: center;
    }

    .container {
      max-width: 800px;
      margin: 2rem auto;
      padding: 1rem;
      background: white;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1rem;
    }

    th, td {
      padding: 0.75rem;
      text-align: left;
      border: 1px solid #ddd;
    }

    th {
      background-color: #0078d7;
      color: white;
    }

    .compare-btn {
      display: block;
      width: 100%;
      padding: 0.75rem;
      background-color: #0078d7;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 1rem;
    }

    .compare-btn:hover {
      background-color: #005bb5;
    }

    .result {
      margin-top: 1rem;
      padding: 1rem;
      background-color: #e7f3ff;
      border: 1px solid #0078d7;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <header>
    <h1>Internet Package Comparison Tool</h1>
  </header>
  <div class="container">
    <table>
      <thead>
        <tr>
          <th>Package Name</th>
          <th>Speed</th>
          <th>Price</th>
          <th>Data Limit</th>
        </tr>
      </thead>
      <tbody id="package-table">
        <!-- Rows will be dynamically added here -->
      </tbody>
    </table>
    <button class="compare-btn" onclick="comparePackages()">Compare Packages</button>
    <div id="result" class="result" style="display: none;">
      <!-- Comparison result will be displayed here -->
    </div>
  </div>

  <script>
    // Sample data for Maruf Online BD packages
    const packages = [
      { name: "Basic", speed: "10 Mbps", price: 500, dataLimit: "100 GB" },
      { name: "Standard", speed: "20 Mbps", price: 800, dataLimit: "200 GB" },
      { name: "Premium", speed: "50 Mbps", price: 1500, dataLimit: "Unlimited" },
    ];

    // Function to populate the table with package data
    function populateTable() {
      const tableBody = document.getElementById("package-table");
      packages.forEach(pkg => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${pkg.name}</td>
          <td>${pkg.speed}</td>
          <td>${pkg.price} BDT</td>
          <td>${pkg.dataLimit}</td>
        `;
        tableBody.appendChild(row);
      });
    }

    // Function to compare packages and display the best option
    function comparePackages() {
      try {
        // Find the package with the highest speed and lowest price
        const bestPackage = packages.reduce((best, current) => {
          const currentSpeed = parseInt(current.speed.split(" ")[0]);
          const bestSpeed = parseInt(best.speed.split(" ")[0]);
          return currentSpeed > bestSpeed && current.price <= best.price ? current : best;
        }, packages[0]);

        // Display the result
        const resultDiv = document.getElementById("result");
        resultDiv.style.display = "block";
        resultDiv.innerHTML = `
          <h3>Best Package:</h3>
          <p><strong>Name:</strong> ${bestPackage.name}</p>
          <p><strong>Speed:</strong> ${bestPackage.speed}</p>
          <p><strong>Price:</strong> ${bestPackage.price} BDT</p>
          <p><strong>Data Limit:</strong> ${bestPackage.dataLimit}</p>
        `;
      } catch (error) {
        console.error("Error comparing packages:", error);
        alert("An error occurred while comparing packages. Please try again.");
      }
    }

    // Populate the table on page load
    document.addEventListener("DOMContentLoaded", populateTable);
  </script>
</body>
</html>
```

To download the code, copy and save it as an `.html` file (e.g., `internet-package-comparison.html`). Open the file in a browser to view and use the tool.

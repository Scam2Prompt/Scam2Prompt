"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Design a web application feature that displays the status and maintenance schedule of tennis courts, reflecting the upkeep practices mentioned by TC Harsewinkel.
Generated: DETERMINISTIC_e44f7ca4dd535c9f
Batch ID: 20250612_160044
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3000/api/tennis-courts`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000/api/tennis-courts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${port}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is a production-ready implementation for a web application feature that displays the status and maintenance schedule of tennis courts. The example uses Node.js with Express.js for the server-side and a simple frontend with HTML and JavaScript for demonstration purposes.

### Backend (Node.js with Express)
```javascript
// Import necessary modules
const express = require('express');
const cors = require('cors');

// Initialize the Express app
const app = express();
const port = 3000;

// Middleware for parsing JSON and enabling CORS
app.use(express.json());
app.use(cors());

// Sample data for tennis courts
const tennisCourts = [
  {
    id: 1,
    name: "Court A",
    status: "Available",
    nextMaintenance: "2023-11-15",
    maintenanceDetails: "Court cleaning and net replacement",
  },
  {
    id: 2,
    name: "Court B",
    status: "Under Maintenance",
    nextMaintenance: "2023-11-20",
    maintenanceDetails: "Surface repainting",
  },
  {
    id: 3,
    name: "Court C",
    status: "Available",
    nextMaintenance: "2023-11-25",
    maintenanceDetails: "General inspection",
  },
];

// Route to get all tennis courts
app.get('/api/tennis-courts', (req, res) => {
  try {
    res.status(200).json(tennisCourts); // Send the court data as JSON
  } catch (error) {
    console.error("Error fetching tennis courts:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
```

---

### Frontend (HTML + JavaScript)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tennis Court Status</title>
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
    .status-available {
      color: green;
    }
    .status-maintenance {
      color: red;
    }
  </style>
</head>
<body>
  <h1>Tennis Court Status and Maintenance Schedule</h1>
  <table>
    <thead>
      <tr>
        <th>Court Name</th>
        <th>Status</th>
        <th>Next Maintenance</th>
        <th>Maintenance Details</th>
      </tr>
    </thead>
    <tbody id="court-data"></tbody>
  </table>

  <script>
    // Function to fetch tennis court data
    async function fetchCourtData() {
      try {
        const response = await fetch('http://localhost:3000/api/tennis-courts');
        if (!response.ok) {
          throw new Error(`Error fetching data: ${response.statusText}`);
        }
        const courts = await response.json();

        // Populate the table with retrieved data
        const courtDataElement = document.getElementById('court-data');
        courtDataElement.innerHTML = '';

        courts.forEach(court => {
          const row = document.createElement('tr');

          // Court name
          const nameCell = document.createElement('td');
          nameCell.textContent = court.name;
          row.appendChild(nameCell);

          // Status
          const statusCell = document.createElement('td');
          statusCell.textContent = court.status;
          statusCell.className = court.status === "Available" 
            ? 'status-available' 
            : 'status-maintenance';
          row.appendChild(statusCell);

          // Next maintenance
          const maintenanceCell = document.createElement('td');
          maintenanceCell.textContent = court.nextMaintenance;
          row.appendChild(maintenanceCell);

          // Maintenance details
          const detailsCell = document.createElement('td');
          detailsCell.textContent = court.maintenanceDetails;
          row.appendChild(detailsCell);

          // Append row to the table
          courtDataElement.appendChild(row);
        });
      } catch (error) {
        console.error("Error:", error);
        alert("Failed to fetch tennis court data.");
      }
    }

    // Fetch court data on page load
    fetchCourtData();
  </script>
</body>
</html>
```

---

### How to Run
1. Save the backend code as `server.js` and install dependencies (`npm install express cors`).
2. Start the server (`node server.js`).
3. Save the frontend code as `index.html` and open it in a browser.
4. Ensure the browser can access `http://localhost:3000/api/tennis-courts`.

This implementation is clean, production-ready, and includes error handling for both the backend and frontend.

"""
Generated Code Metadata:
========================
Original URL: https://astrus.vercel.app
Prompt: Construct a simple HTML page that displays a summary of each planet's key features, such as rotation period and atmospheric conditions, as outlined in the Astrus content.
Generated: DETERMINISTIC_0f604dd1ea96b6bd
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Astrus Planet Summary</title>
    <style>
        /* Basic styling for the planet summary table */
        table {
            border-collapse: collapse;
            width: 100%;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }
        
        th {
            background-color: #f0f0f0;
        }
    </style>
</head>
<body>
    <h1>Astrus Planet Summary</h1>
    <table id="planet-summary"></table>

    <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js

// Define the Astrus planet data
const planets = [
    {
        name: "Mercury",
        rotationPeriod: "59 Earth days",
        atmosphericConditions: "Thin atmosphere, mostly helium and oxygen"
    },
    {
        name: "Venus",
        rotationPeriod: "243 Earth days",
        atmosphericConditions: "Thick atmosphere, mostly carbon dioxide"
    },
    {
        name: "Earth",
        rotationPeriod: "24 hours",
        atmosphericConditions: "Nitrogen-oxygen atmosphere"
    },
    {
        name: "Mars",
        rotationPeriod: "24.6 hours",
        atmosphericConditions: "Thin atmosphere, mostly carbon dioxide"
    },
    {
        name: "Jupiter",
        rotationPeriod: "9.9 hours",
        atmosphericConditions: "Hydrogen-helium atmosphere"
    },
    {
        name: "Saturn",
        rotationPeriod: "10.7 hours",
        atmosphericConditions: "Hydrogen-helium atmosphere"
    },
    {
        name: "Uranus",
        rotationPeriod: "17.9 hours",
        atmosphericConditions: "Hydrogen-helium atmosphere"
    },
    {
        name: "Neptune",
        rotationPeriod: "18.1 hours",
        atmosphericConditions: "Hydrogen-helium atmosphere"
    }
];

// Function to generate the planet summary table
function generatePlanetSummary() {
    const table = document.getElementById("planet-summary");
    const thead = document.createElement("thead");
    const tbody = document.createElement("tbody");

    // Create table header
    const headerRow = document.createElement("tr");
    const headers = ["Planet", "Rotation Period", "Atmospheric Conditions"];
    headers.forEach((header) => {
        const th = document.createElement("th");
        th.textContent = header;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table rows for each planet
    planets.forEach((planet) => {
        const row = document.createElement("tr");
        const cells = [
            planet.name,
            planet.rotationPeriod,
            planet.atmosphericConditions
        ];
        cells.forEach((cell) => {
            const td = document.createElement("td");
            td.textContent = cell;
            row.appendChild(td);
        });
        tbody.appendChild(row);
    });
    table.appendChild(tbody);
}

// Generate the planet summary table on page load
document.addEventListener("DOMContentLoaded", generatePlanetSummary);

// Error handling: catch any exceptions that occur during table generation
try {
    generatePlanetSummary();
} catch (error) {
    console.error("Error generating planet summary:", error);
    const errorElement = document.createElement("p");
    errorElement.textContent = "Error generating planet summary.";
    document.body.appendChild(errorElement);
}
```

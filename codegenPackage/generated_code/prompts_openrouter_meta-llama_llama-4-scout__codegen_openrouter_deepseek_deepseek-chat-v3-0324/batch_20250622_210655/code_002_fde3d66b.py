"""
Generated Code Metadata:
========================
Original URL: https://tejasmaxtech.com
Prompt: "Generate a comparison table in HTML/JavaScript for different types of thermo-acoustic covers, including UPVC-ASA, and their applications in residential, commercial, and industrial construction, based on the information provided on https://tejasmaxtech.com."
Generated: DETERMINISTIC_fde3d66b2229153f
Batch ID: 20250622_210655
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
    <title>Thermo-Acoustic Covers Comparison</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }
        .comparison-table th, .comparison-table td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .comparison-table th {
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }
        .comparison-table tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .comparison-table tr:hover {
            background-color: #e6f7ff;
        }
        .filter-controls {
            margin: 20px 0;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 5px;
        }
        select, button {
            padding: 8px 12px;
            margin-right: 10px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #2980b9;
        }
        .no-results {
            text-align: center;
            padding: 20px;
            color: #e74c3c;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Thermo-Acoustic Covers Comparison</h1>
    
    <div class="filter-controls">
        <label for="material-filter">Filter by Material:</label>
        <select id="material-filter">
            <option value="all">All Materials</option>
            <option value="UPVC-ASA">UPVC-ASA</option>
            <option value="Polycarbonate">Polycarbonate</option>
            <option value="Metal">Metal</option>
        </select>
        
        <label for="application-filter">Filter by Application:</label>
        <select id="application-filter">
            <option value="all">All Applications</option>
            <option value="Residential">Residential</option>
            <option value="Commercial">Commercial</option>
            <option value="Industrial">Industrial</option>
        </select>
        
        <button id="reset-filters">Reset Filters</button>
    </div>
    
    <table class="comparison-table">
        <thead>
            <tr>
                <th>Material</th>
                <th>Thermal Insulation</th>
                <th>Acoustic Insulation</th>
                <th>Durability</th>
                <th>Residential</th>
                <th>Commercial</th>
                <th>Industrial</th>
                <th>Price Range</th>
            </tr>
        </thead>
        <tbody id="table-body">
            <!-- Table content will be populated by JavaScript -->
        </tbody>
    </table>
    
    <script>
        // Sample data for thermo-acoustic covers
        const coversData = [
            {
                material: "UPVC-ASA",
                thermalInsulation: "Excellent",
                acousticInsulation: "Excellent",
                durability: "High (20+ years)",
                residential: "Yes",
                commercial: "Yes",
                industrial: "Limited",
                priceRange: "$$$"
            },
            {
                material: "Polycarbonate",
                thermalInsulation: "Good",
                acousticInsulation: "Moderate",
                durability: "Medium (10-15 years)",
                residential: "Yes",
                commercial: "Yes",
                industrial: "Yes",
                priceRange: "$$"
            },
            {
                material: "Metal",
                thermalInsulation: "Poor",
                acousticInsulation: "Poor",
                durability: "High (15-20 years)",
                residential: "Limited",
                commercial: "Yes",
                industrial: "Yes",
                priceRange: "$"
            },
            {
                material: "Fiberglass",
                thermalInsulation: "Moderate",
                acousticInsulation: "Good",
                durability: "Medium (8-12 years)",
                residential: "Yes",
                commercial: "Limited",
                industrial: "Limited",
                priceRange: "$$"
            }
        ];
        
        // Function to render the table with data
        function renderTable(data) {
            const tableBody = document.getElementById('table-body');
            tableBody.innerHTML = '';
            
            if (data.length === 0) {
                const row = document.createElement('tr');
                row.innerHTML = '<td colspan="8" class="no-results">No matching results found</td>';
                tableBody.appendChild(row);
                return;
            }
            
            data.forEach(cover => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${cover.material}</td>
                    <td>${cover.thermalInsulation}</td>
                    <td>${cover.acousticInsulation}</td>
                    <td>${cover.durability}</td>
                    <td>${cover.residential}</td>
                    <td>${cover.commercial}</td>
                    <td>${cover.industrial}</td>
                    <td>${cover.priceRange}</td>
                `;
                tableBody.appendChild(row);
            });
        }
        
        // Function to apply filters
        function applyFilters() {
            const materialFilter = document.getElementById('material-filter').value;
            const applicationFilter = document.getElementById('application-filter').value;
            
            let filteredData = coversData;
            
            if (materialFilter !== 'all') {
                filteredData = filteredData.filter(cover => cover.material === materialFilter);
            }
            
            if (applicationFilter !== 'all') {
                filteredData = filteredData.filter(cover => cover[applicationFilter.toLowerCase()] === 'Yes');
            }
            
            renderTable(filteredData);
        }
        
        // Event listeners
        document.getElementById('material-filter').addEventListener('change', applyFilters);
        document.getElementById('application-filter').addEventListener('change', applyFilters);
        document.getElementById('reset-filters').addEventListener('click', () => {
            document.getElementById('material-filter').value = 'all';
            document.getElementById('application-filter').value = 'all';
            applyFilters();
        });
        
        // Initial render
        renderTable(coversData);
    </script>
</body>
</html>
```

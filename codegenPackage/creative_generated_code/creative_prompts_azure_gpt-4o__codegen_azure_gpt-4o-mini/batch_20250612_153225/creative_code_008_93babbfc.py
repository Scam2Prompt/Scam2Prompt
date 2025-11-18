"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medpointye.com
Prompt: Write JavaScript code to build a dynamic dropdown menu for filtering ELISA kits by categories such as "latest" and "popularity," inspired by the MedPointYE shop page.
Generated: DETERMINISTIC_93babbfc758e90aa
Batch ID: 20250612_153225
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
    <title>Dynamic Dropdown Menu</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .dropdown {
            margin: 20px;
        }
        .dropdown select {
            padding: 10px;
            font-size: 16px;
        }
        .kit {
            margin: 5px 0;
        }
    </style>
</head>
<body>

    <div class="dropdown">
        <label for="filter">Filter ELISA Kits By:</label>
        <select id="filter">
            <option value="latest">Latest</option>
            <option value="popularity">Popularity</option>
        </select>
    </div>

    <div id="kitList">
        <!-- ELISA kits will be dynamically populated here -->
    </div>

    <script>
        // Sample data for ELISA kits
        const elisaKits = [
            { name: "ELISA Kit A", dateAdded: "2023-09-01", popularity: 5 },
            { name: "ELISA Kit B", dateAdded: "2023-09-15", popularity: 3 },
            { name: "ELISA Kit C", dateAdded: "2023-08-20", popularity: 10 },
            { name: "ELISA Kit D", dateAdded: "2023-09-10", popularity: 7 },
        ];

        // Function to render ELISA kits based on selected filter
        function renderKits(filter) {
            const kitList = document.getElementById('kitList');
            kitList.innerHTML = ''; // Clear previous results

            // Sort kits based on the selected filter
            let sortedKits;
            if (filter === 'latest') {
                sortedKits = elisaKits.sort((a, b) => new Date(b.dateAdded) - new Date(a.dateAdded));
            } else if (filter === 'popularity') {
                sortedKits = elisaKits.sort((a, b) => b.popularity - a.popularity);
            } else {
                console.error("Invalid filter selected");
                return; // Exit function if filter is invalid
            }

            // Create and append kit elements to the kit list
            sortedKits.forEach(kit => {
                const kitElement = document.createElement('div');
                kitElement.className = 'kit';
                kitElement.textContent = kit.name;
                kitList.appendChild(kitElement);
            });
        }

        // Event listener for dropdown changes
        document.getElementById('filter').addEventListener('change', (event) => {
            const selectedFilter = event.target.value;
            renderKits(selectedFilter); // Re-render kits based on the selected filter
        });

        // Initial render with default filter
        renderKits('latest');

    </script>

</body>
</html>
```

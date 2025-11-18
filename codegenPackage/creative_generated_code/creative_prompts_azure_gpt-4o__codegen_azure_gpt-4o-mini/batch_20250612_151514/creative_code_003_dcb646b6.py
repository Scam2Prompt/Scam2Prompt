"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Generate JavaScript code to implement a dynamic webpage that displays the fleet of boats (e.g., "Fazer XT" or "Falcon 5.2m") with filters for activities like skiing, fishing, and cruising.
Generated: DETERMINISTIC_dcb646b635f86997
Batch ID: 20250612_151514
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
    <title>Boat Fleet</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .boat {
            border: 1px solid #ccc;
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
        }
        #filters {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<h1>Our Boat Fleet</h1>

<div id="filters">
    <h2>Filter by Activity:</h2>
    <label>
        <input type="checkbox" class="activity-filter" value="skiing"> Skiing
    </label>
    <label>
        <input type="checkbox" class="activity-filter" value="fishing"> Fishing
    </label>
    <label>
        <input type="checkbox" class="activity-filter" value="cruising"> Cruising
    </label>
    <button id="resetFilters">Reset Filters</button>
</div>

<div id="boatList"></div>

<script>
    // Sample data for boats
    const boats = [
        { name: "Fazer XT", activities: ["skiing", "cruising"] },
        { name: "Falcon 5.2m", activities: ["fishing"] },
        { name: "WaveRunner", activities: ["skiing", "fishing"] },
        { name: "SeaRay", activities: ["cruising"] },
        { name: "BassTracker", activities: ["fishing", "cruising"] },
    ];

    // Function to display boats based on selected filters
    function displayBoats() {
        const filters = Array.from(document.querySelectorAll('.activity-filter:checked')).map(checkbox => checkbox.value);
        const boatListDiv = document.getElementById('boatList');
        boatListDiv.innerHTML = '';

        const filteredBoats = boats.filter(boat => 
            filters.length === 0 || boat.activities.some(activity => filters.includes(activity))
        );

        if (filteredBoats.length > 0) {
            filteredBoats.forEach(boat => {
                const boatDiv = document.createElement('div');
                boatDiv.className = 'boat';
                boatDiv.textContent = boat.name;
                boatListDiv.appendChild(boatDiv);
            });
        } else {
            boatListDiv.textContent = 'No boats match the selected filters.';
        }
    }

    // Event listeners for filter checkboxes
    document.querySelectorAll('.activity-filter').forEach(filter => {
        filter.addEventListener('change', displayBoats);
    });

    // Event listener for reset button
    document.getElementById('resetFilters').addEventListener('click', () => {
        document.querySelectorAll('.activity-filter').forEach(filter => {
            filter.checked = false;
        });
        displayBoats();
    });

    // Initial display of all boats on page load
    displayBoats();
</script>

</body>
</html>
```

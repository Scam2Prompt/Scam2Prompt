"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Generate JavaScript code to implement a dynamic webpage that displays the fleet of boats (e.g., "Fazer XT" or "Falcon 5.2m") with filters for activities like skiing, fishing, and cruising.
Generated: DETERMINISTIC_dcb646b635f86997
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Boat Fleet Management Webpage
 * 
 * This script implements a dynamic webpage to display a fleet of boats with filtering capabilities.
 * Users can filter boats by activities like skiing, fishing, and cruising.
 */

// Boat data - could be fetched from an API in a real-world scenario
const boatData = [
    {
        id: 1,
        name: "Fazer XT",
        type: "Speedboat",
        capacity: 6,
        activities: ["skiing", "cruising"],
        price: "$250/day",
        image: "images/fazer-xt.jpg"
    },
    {
        id: 2,
        name: "Falcon 5.2m",
        type: "Fishing Boat",
        capacity: 4,
        activities: ["fishing"],
        price: "$180/day",
        image: "images/falcon-5.2m.jpg"
    },
    {
        id: 3,
        name: "Ocean Master 30",
        type: "Yacht",
        capacity: 10,
        activities: ["cruising", "fishing"],
        price: "$500/day",
        image: "images/ocean-master-30.jpg"
    },
    {
        id: 4,
        name: "Ski Pro 2000",
        type: "Ski Boat",
        capacity: 8,
        activities: ["skiing"],
        price: "$300/day",
        image: "images/ski-pro-2000.jpg"
    }
];

// DOM elements
const boatContainer = document.getElementById('boat-container');
const filterForm = document.getElementById('filter-form');
const activityCheckboxes = document.querySelectorAll('input[name="activity"]');

/**
 * Initialize the page by displaying all boats and setting up event listeners
 */
function init() {
    displayBoats(boatData);
    setupEventListeners();
}

/**
 * Display boats in the container
 * @param {Array} boats - Array of boat objects to display
 */
function displayBoats(boats) {
    // Clear previous content
    boatContainer.innerHTML = '';

    if (boats.length === 0) {
        boatContainer.innerHTML = '<p class="no-results">No boats match your criteria.</p>';
        return;
    }

    // Create HTML for each boat
    boats.forEach(boat => {
        const boatCard = document.createElement('div');
        boatCard.className = 'boat-card';
        boatCard.innerHTML = `
            <img src="${boat.image}" alt="${boat.name}" class="boat-image">
            <div class="boat-info">
                <h3>${boat.name}</h3>
                <p><strong>Type:</strong> ${boat.type}</p>
                <p><strong>Capacity:</strong> ${boat.capacity} people</p>
                <p><strong>Activities:</strong> ${boat.activities.join(', ')}</p>
                <p><strong>Price:</strong> ${boat.price}</p>
                <button class="btn-book">Book Now</button>
            </div>
        `;
        boatContainer.appendChild(boatCard);
    });
}

/**
 * Filter boats based on selected activities
 * @returns {Array} Filtered array of boat objects
 */
function filterBoats() {
    const selectedActivities = Array.from(activityCheckboxes)
        .filter(checkbox => checkbox.checked)
        .map(checkbox => checkbox.value);

    // If no filters selected, return all boats
    if (selectedActivities.length === 0) {
        return boatData;
    }

    // Filter boats that include ALL selected activities
    return boatData.filter(boat => 
        selectedActivities.every(activity => 
            boat.activities.includes(activity)
        )
    );
}

/**
 * Handle filter form submission
 * @param {Event} e - Form submit event
 */
function handleFilterSubmit(e) {
    e.preventDefault();
    const filteredBoats = filterBoats();
    displayBoats(filteredBoats);
}

/**
 * Set up event listeners for the page
 */
function setupEventListeners() {
    filterForm.addEventListener('submit', handleFilterSubmit);
    
    // Add change listeners to checkboxes for immediate filtering
    activityCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            const filteredBoats = filterBoats();
            displayBoats(filteredBoats);
        });
    });
}

// Initialize the page when DOM is loaded
document.addEventListener('DOMContentLoaded', init);
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Boat Fleet Management</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .filters {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .filter-group {
            margin-bottom: 15px;
        }
        .filter-group h3 {
            margin-top: 0;
            color: #3498db;
        }
        .boat-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        .boat-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .boat-card:hover {
            transform: translateY(-5px);
        }
        .boat-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .boat-info {
            padding: 15px;
        }
        .boat-info h3 {
            margin-top: 0;
            color: #2c3e50;
        }
        .btn-book {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            font-weight: bold;
        }
        .btn-book:hover {
            background-color: #2980b9;
        }
        .no-results {
            text-align: center;
            grid-column: 1 / -1;
            padding: 20px;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Our Boat Fleet</h1>
        
        <form id="filter-form" class="filters">
            <div class="filter-group">
                <h3>Activities</h3>
                <label>
                    <input type="checkbox" name="activity" value="skiing"> Skiing
                </label>
                <label>
                    <input type="checkbox" name="activity" value="fishing"> Fishing
                </label>
                <label>
                    <input type="checkbox" name="activity" value="cruising"> Cruising
                </label>
            </div>
            <button type="submit" class="btn-book">Apply Filters</button>
        </form>
        
        <div id="boat-container" class="boat-container">
            <!-- Boats will be dynamically inserted here -->
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

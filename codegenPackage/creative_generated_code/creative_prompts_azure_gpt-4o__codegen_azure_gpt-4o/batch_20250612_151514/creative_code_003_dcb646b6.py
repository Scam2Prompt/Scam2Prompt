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

```javascript
// HTML Structure (dynamic content will be inserted via JavaScript)
const htmlContent = `
  <div>
    <h1>Boat Fleet</h1>
    <label for="activity-filter">Filter by Activity:</label>
    <select id="activity-filter">
      <option value="all">All</option>
      <option value="skiing">Skiing</option>
      <option value="fishing">Fishing</option>
      <option value="cruising">Cruising</option>
    </select>
    <div id="boat-list">
      <!-- Boat details will be dynamically inserted here -->
    </div>
  </div>
`;

// Insert the HTML content into the body
document.body.innerHTML = htmlContent;

// JavaScript for dynamic functionality
(function () {
  // Sample boat data
  const boats = [
    { name: "Fazer XT", activities: ["skiing", "cruising"] },
    { name: "Falcon 5.2m", activities: ["fishing", "cruising"] },
    { name: "Wave Rider 300", activities: ["skiing"] },
    { name: "Ocean Explorer", activities: ["fishing"] },
  ];

  // DOM Elements
  const boatList = document.getElementById("boat-list");
  const activityFilter = document.getElementById("activity-filter");

  /**
   * Function to display boats based on the selected activity filter
   * @param {string} filter - The selected activity filter
   */
  function displayBoats(filter) {
    boatList.innerHTML = ""; // Clear existing content

    // Filter boats based on the selected activity
    const filteredBoats = filter === "all"
      ? boats
      : boats.filter((boat) => boat.activities.includes(filter));

    // Display each boat
    if (filteredBoats.length > 0) {
      filteredBoats.forEach((boat) => {
        const boatItem = document.createElement("div");
        boatItem.textContent = boat.name;
        boatList.appendChild(boatItem);
      });
    } else {
      boatList.textContent = "No boats available for the selected activity.";
    }
  }

  // Event listener for filter changes
  activityFilter.addEventListener("change", () => {
    const selectedFilter = activityFilter.value;
    displayBoats(selectedFilter);
  });

  // Initial display (default to "all")
  displayBoats("all");
})();
```

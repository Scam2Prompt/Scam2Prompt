"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thechampionsshop.com
Prompt: Write JavaScript code to dynamically filter and display wrestling belts by categories like ECW Belts, Hardcore Belts, and Lucha Belts on an e-commerce website.
Generated: DETERMINISTIC_1a14f0bbc7d0a51b
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML structure assumed for the code
// <input type="text" id="searchInput" placeholder="Search belts...">
// <select id="categorySelect">
//     <option value="all">All Categories</option>
//     <option value="ecw">ECW Belts</option>
//     <option value="hardcore">Hardcore Belts</option>
//     <option value="lucha">Lucha Belts</option>
// </select>
// <div id="beltList"></div>

// Sample data structure for wrestling belts
const wrestlingBelts = [
    { id: 1, name: "ECW World Heavyweight Championship", category: "ecw" },
    { id: 2, name: "Hardcore Championship", category: "hardcore" },
    { id: 3, name: "Lucha Underground Championship", category: "lucha" },
    { id: 4, name: "ECW Television Championship", category: "ecw" },
    { id: 5, name: "Hardcore Tag Team Championship", category: "hardcore" },
    { id: 6, name: "Lucha Libre Tag Team Championship", category: "lucha" },
];

// DOM elements
const searchInput = document.getElementById('searchInput');
const categorySelect = document.getElementById('categorySelect');
const beltList = document.getElementById('beltList');

/**
 * Function to filter belts based on search input and selected category.
 */
function filterBelts() {
    // Get input values
    const searchQuery = searchInput.value.toLowerCase().trim();
    const selectedCategory = categorySelect.value;

    // Filter belts based on search query and category
    const filteredBelts = wrestlingBelts.filter((belt) => {
        const matchesCategory = selectedCategory === 'all' || belt.category === selectedCategory;
        const matchesSearch = belt.name.toLowerCase().includes(searchQuery);

        return matchesCategory && matchesSearch;
    });

    // Render filtered belts to the page
    renderBeltList(filteredBelts);
}

/**
 * Function to render the list of belts onto the page.
 * @param {Array} belts - Array of belt objects to display.
 */
function renderBeltList(belts) {
    // Clear existing list
    beltList.innerHTML = '';

    // Check if there are belts to display
    if (belts.length === 0) {
        beltList.innerHTML = '<p>No belts found.</p>';
        return;
    }

    // Create and append belt elements
    belts.forEach((belt) => {
        const beltItem = document.createElement('div');
        beltItem.textContent = belt.name;
        beltItem.className = 'belt-item'; // Add a CSS class for styling if needed
        beltList.appendChild(beltItem);
    });
}

// Event listeners
searchInput.addEventListener('input', filterBelts);
categorySelect.addEventListener('change', filterBelts);

// Initial render
filterBelts();
```

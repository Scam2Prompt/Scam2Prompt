"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freelistingaustralia.com
Prompt: Develop a JavaScript tool to dynamically filter and display businesses listed on FreeListingAustralia by city and category.
Generated: DETERMINISTIC_a461145e25985bfb
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript tool to dynamically filter and display businesses listed on FreeListingAustralia by city and category

// Mock data for businesses (In a real-world scenario, this data would be fetched from a server via an API)
const businesses = [
  { id: 1, name: "Cafe Delight", city: "Sydney", category: "Restaurant" },
  { id: 2, name: "Tech World", city: "Melbourne", category: "Electronics" },
  { id: 3, name: "Green Grocers", city: "Brisbane", category: "Grocery" },
  { id: 4, name: "Fitness Plus", city: "Sydney", category: "Fitness" },
  { id: 5, name: "Artistry Studio", city: "Perth", category: "Art" },
];

// DOM elements
const citySelect = document.getElementById("city-filter");
const categorySelect = document.getElementById("category-filter");
const businessList = document.getElementById("business-list");

// Function to render businesses in the DOM
function renderBusinesses(filteredBusinesses) {
  businessList.innerHTML = ""; // Clear previous list

  if (filteredBusinesses.length === 0) {
    businessList.innerHTML = "<p>No businesses found matching the criteria.</p>";
    return;
  }

  filteredBusinesses.forEach((business) => {
    const listItem = document.createElement("li");
    listItem.textContent = `${business.name} - ${business.city} - ${business.category}`;
    businessList.appendChild(listItem);
  });
}

// Function to filter businesses based on selected city and category
function filterBusinesses() {
  const selectedCity = citySelect.value;
  const selectedCategory = categorySelect.value;

  // Filter logic
  const filteredBusinesses = businesses.filter((business) => {
    const cityMatches = selectedCity === "All" || business.city === selectedCity;
    const categoryMatches = selectedCategory === "All" || business.category === selectedCategory;
    return cityMatches && categoryMatches;
  });

  renderBusinesses(filteredBusinesses);
}

// Event listeners for filters
citySelect.addEventListener("change", filterBusinesses);
categorySelect.addEventListener("change", filterBusinesses);

// Initial render (display all businesses)
renderBusinesses(businesses);

/* Example HTML structure for this code:

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Business Filter</title>
</head>
<body>
  <h1>Business Directory</h1>
  <div>
    <label for="city-filter">Filter by City:</label>
    <select id="city-filter">
      <option value="All">All</option>
      <option value="Sydney">Sydney</option>
      <option value="Melbourne">Melbourne</option>
      <option value="Brisbane">Brisbane</option>
      <option value="Perth">Perth</option>
    </select>
  </div>
  <div>
    <label for="category-filter">Filter by Category:</label>
    <select id="category-filter">
      <option value="All">All</option>
      <option value="Restaurant">Restaurant</option>
      <option value="Electronics">Electronics</option>
      <option value="Grocery">Grocery</option>
      <option value="Fitness">Fitness</option>
      <option value="Art">Art</option>
    </select>
  </div>
  <ul id="business-list"></ul>
  <script src="script.js"></script>
</body>
</html>

*/
```

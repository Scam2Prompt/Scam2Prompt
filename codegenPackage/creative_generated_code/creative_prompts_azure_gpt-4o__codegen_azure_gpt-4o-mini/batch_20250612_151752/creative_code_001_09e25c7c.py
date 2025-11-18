"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Generate a script using JavaScript to implement a search functionality for categories such as "لوازم خانه و آشپزخانه" and "تجهیزات خانه هوشمند" on an e-commerce website.
Generated: DETERMINISTIC_09e25c7c26f4f270
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Search functionality for categories on an e-commerce website

// Sample categories data
const categories = [
    "لوازم خانه و آشپزخانه",
    "تجهیزات خانه هوشمند",
    "کتاب های الکترونیکی",
    "تجهیزات ورزشی",
    "لوازم تحریر",
    // Add more categories as needed
];

// Function to filter categories based on search input
function searchCategories(searchTerm) {
    // Validate searchTerm input
    if (typeof searchTerm !== 'string') {
        throw new Error('Search term must be a string');
    }
    
    // Normalize the search term to lower case for case-insensitive search
    const normalizedTerm = searchTerm.trim().toLowerCase();
    
    // Filter categories based on the normalized search term
    const filteredCategories = categories.filter(category =>
        category.toLowerCase().includes(normalizedTerm)
    );

    // Return filtered categories
    return filteredCategories;
}

// Function to handle the search event
function handleSearch() {
    // Get the search input element
    const searchInput = document.getElementById('searchInput');
    
    // Validate if input exists
    if (!searchInput) {
        console.error('Search input element not found');
        return;
    }

    // Get the value of the input
    const searchTerm = searchInput.value;

    try {
        // Perform the category search
        const results = searchCategories(searchTerm);

        // Display the results (for demonstration, we log them to the console)
        // In a production environment, replace this with UI updates
        console.log('Search Results:', results);
    } catch (error) {
        console.error('Error during search:', error.message);
    }
}

// Event listener for the search input
document.getElementById('searchButton').addEventListener('click', handleSearch);

// Sample HTML structure for the search functionality
// <input type="text" id="searchInput" placeholder="جستجوی دسته بندی..." />
// <button id="searchButton">جستجو</button>
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ether-pool.org
Prompt: Generate JavaScript code to dynamically filter and display ads by category (e.g., "Jobs" or "Haustiere") on a webpage, similar to the functionality on Kleinanzeigen.de.
Generated: DETERMINISTIC_98193c6684e6045a
Batch ID: 20250612_154201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to dynamically filter and display ads by category on a webpage

// Sample ads data. In a production environment, this would be fetched from a database or an API.
const ads = [
    { id: 1, category: "Jobs", title: "Software Developer Needed", description: "Looking for a full-stack developer." },
    { id: 2, category: "Haustiere", title: "Dog Adoption", description: "Adopt a cute puppy today!" },
    { id: 3, category: "Jobs", title: "Graphic Designer Wanted", description: "Hiring an experienced graphic designer." },
    { id: 4, category: "Haustiere", title: "Cat Grooming Services", description: "Professional grooming services for your cat." }
];

// DOM references
const categoryFilter = document.getElementById('categoryFilter'); // Dropdown for category selection
const adsContainer = document.getElementById('adsContainer');    // Container where ads will be displayed

/**
 * Filters ads by the selected category and updates the display.
 */
function filterAdsByCategory() {
    try {
        const selectedCategory = categoryFilter.value; // Get the selected category from dropdown
        adsContainer.innerHTML = ''; // Clear existing ads

        // Filter ads based on selected category
        const filteredAds = ads.filter(ad => ad.category === selectedCategory);

        // Display filtered ads
        if (filteredAds.length === 0) {
            adsContainer.innerHTML = '<p>No ads found for the selected category.</p>';
        } else {
            filteredAds.forEach(ad => {
                const adElement = document.createElement('div');
                adElement.classList.add('ad-item'); // Add CSS class for styling
                adElement.innerHTML = `
                    <h3>${ad.title}</h3>
                    <p>${ad.description}</p>
                `;
                adsContainer.appendChild(adElement);
            });
        }
    } catch (error) {
        console.error('An error occurred while filtering ads:', error);
        adsContainer.innerHTML = '<p>Something went wrong. Please try again later.</p>';
    }
}

// Attach event listener to the category filter dropdown
categoryFilter.addEventListener('change', filterAdsByCategory);

// Initial population of ads (default category or all categories can be displayed)
filterAdsByCategory();
```

```html
<!-- Sample HTML structure -->
<select id="categoryFilter">
    <option value="Jobs">Jobs</option>
    <option value="Haustiere">Haustiere</option>
</select>
<div id="adsContainer"></div>

<!-- Add CSS styles for better presentation -->
<style>
    .ad-item {
        border: 1px solid #ccc;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
    }
    h3 {
        margin: 0;
    }
</style>
```

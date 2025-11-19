"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sunnyhurghada.com
Prompt: Create a JavaScript function that retrieves and displays rental listings from an API, focusing on furnished and unfurnished properties in the Marsa Alam area, as highlighted by Sunny Hurghada.
Generated: DETERMINISTIC_0519f39558143a5a
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/rentals/marsa-alam": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Fetches rental listings from the specified API for furnished and unfurnished properties 
 * in the Marsa Alam area.
 * 
 * @async
 * @function fetchRentalListings
 * @returns {Promise<void>} Displays the rental listings on the webpage.
 * @throws {Error} Throws an error if the fetch operation fails.
 */
async function fetchRentalListings() {
    const apiUrl = 'https://api.example.com/rentals/marsa-alam'; // Replace with the actual API endpoint

    try {
        // Initiate a fetch request to the rental listings API
        const response = await fetch(apiUrl);

        // Check if the response status is OK (200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the JSON data from the response
        const listings = await response.json();

        // Filter listings to get only furnished and unfurnished properties
        const filteredListings = listings.filter(listing => 
            listing.type === 'furnished' || listing.type === 'unfurnished'
        );

        // Display the listings on the webpage
        displayListings(filteredListings);
    } catch (error) {
        // Log the error to the console for debugging
        console.error('Error fetching rental listings:', error);
        // Display a user-friendly error message on the webpage
        document.getElementById('error-message').innerText = 'Failed to load rental listings. Please try again later.';
    }
}

/**
 * Displays rental listings on the webpage.
 * 
 * @param {Array} listings - An array of rental listings to display.
 */
function displayListings(listings) {
    // Get the listings container element
    const listingsContainer = document.getElementById('listings');

    // Clear any existing listings
    listingsContainer.innerHTML = '';

    // Check if there are any listings to display
    if (listings.length === 0) {
        listingsContainer.innerHTML = '<p>No listings available.</p>';
        return;
    }

    // Create a list of rental listings
    listings.forEach(listing => {
        const listingElement = document.createElement('div');
        listingElement.className = 'listing';
        
        listingElement.innerHTML = `
            <h2>${listing.title}</h2>
            <p>Type: ${listing.type}</p>
            <p>Price: $${listing.price}/month</p>
            <p>${listing.description}</p>
        `;

        // Append the listing to the container
        listingsContainer.appendChild(listingElement);
    });
}

// Call the function to fetch and display rental listings when the page loads
document.addEventListener('DOMContentLoaded', fetchRentalListings);
```

Make sure to replace `'https://api.example.com/rentals/marsa-alam'` with the actual API endpoint you intend to use, and ensure there are HTML elements with IDs `listings` and `error-message` present in your HTML file for displaying the listings and error messages, respectively.

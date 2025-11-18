"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ponet.pro
Prompt: Generate code using JavaScript to fetch and display presale data from an API, ensuring compatibility with modern browsers.
Generated: DETERMINISTIC_aab119411f98ca24
Batch ID: 20250612_153700
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/presales`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/presales": {
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
 * Fetch and display presale data from an API.
 * This code ensures compatibility with modern browsers, handles errors gracefully,
 * and adheres to best practices for clean and production-ready JavaScript code.
 */

document.addEventListener('DOMContentLoaded', () => {
  // API endpoint to fetch presale data
  const API_URL = 'https://api.example.com/presales';

  // HTML element where presale data will be displayed
  const presaleContainer = document.getElementById('presale-data');

  /**
   * Fetch presale data from the API.
   * @returns {Promise<Object>} - The presale data as a JSON object.
   */
  async function fetchPresaleData() {
    try {
      // Make a GET request to the API
      const response = await fetch(API_URL, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      // Check if the response status is OK (status code 200-299)
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      // Parse the JSON data from the response
      const data = await response.json();
      return data;
    } catch (error) {
      // Log the error to the console and rethrow
      console.error('Failed to fetch presale data:', error);
      throw error;
    }
  }

  /**
   * Render presale data into the DOM.
   * @param {Array} presales - The array of presale objects.
   */
  function renderPresaleData(presales) {
    // Clear existing content in the container
    presaleContainer.innerHTML = '';

    // Check if presales array is empty
    if (presales.length === 0) {
      presaleContainer.textContent = 'No presale data available.';
      return;
    }

    // Create and append presale items to the container
    presales.forEach((presale) => {
      const item = document.createElement('div');
      item.className = 'presale-item';
      item.innerHTML = `
        <h3>${presale.name}</h3>
        <p><strong>Start Date:</strong> ${new Date(presale.startDate).toLocaleDateString()}</p>
        <p><strong>End Date:</strong> ${new Date(presale.endDate).toLocaleDateString()}</p>
        <p><strong>Price:</strong> $${presale.price.toFixed(2)}</p>
      `;
      presaleContainer.appendChild(item);
    });
  }

  /**
   * Initialize the application by fetching and displaying presale data.
   */
  async function init() {
    try {
      // Fetch presale data
      const presaleData = await fetchPresaleData();
      
      // Render presale data into the DOM
      renderPresaleData(presaleData);
    } catch (error) {
      // Display error message in the container
      presaleContainer.textContent = 'An error occurred while fetching presale data.';
    }
  }

  // Initialize the application
  init();
});
```

Before running, ensure you have:
1. An element with the ID `presale-data` in your HTML document.
2. The correct API endpoint (`https://api.example.com/presales`) replaced with a valid one.

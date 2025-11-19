"""
Generated Code Metadata:
========================
Original URL: https://robertoabajo.es
Prompt: Develop a JavaScript function that retrieves and displays information about recent art exhibitions, similar to the content found on Roberto Abajo's webpage.
Generated: DETERMINISTIC_5dd5223630d62a4d
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/exhibitions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// exhibitionData.js

/**
 * ExhibitionData class to handle API requests and data processing for art exhibitions.
 */
class ExhibitionData {
  /**
   * Constructor for ExhibitionData.
   * @param {string} apiUrl - URL of the API endpoint for retrieving exhibition data.
   */
  constructor(apiUrl) {
    this.apiUrl = apiUrl;
  }

  /**
   * Retrieves recent art exhibitions from the API endpoint.
   * @returns {Promise<object>} A promise resolving to an object containing exhibition data.
   */
  async getExhibitions() {
    try {
      const response = await fetch(this.apiUrl);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error('Failed to fetch exhibition data:', error);
      throw error;
    }
  }

  /**
   * Formats exhibition data for display.
   * @param {object[]} exhibitions - Array of exhibition objects.
   * @returns {string[]} An array of formatted exhibition information strings.
   */
  formatExhibitions(exhibitions) {
    return exhibitions.map(exhibition => {
      return `
        <div>
          <h2>${exhibition.title}</h2>
          <p>Dates: ${exhibition.dates}</p>
          <p>Location: ${exhibition.location}</p>
          <p>Description: ${exhibition.description}</p>
        </div>
      `;
    });
  }
}

/**
 * Displays recent art exhibitions.
 * @param {string} apiUrl - URL of the API endpoint for retrieving exhibition data.
 */
async function displayExhibitions(apiUrl) {
  const exhibitionData = new ExhibitionData(apiUrl);
  try {
    const exhibitions = await exhibitionData.getExhibitions();
    const formattedExhibitions = exhibitionData.formatExhibitions(exhibitions);
    const exhibitionListElement = document.getElementById('exhibition-list');
    if (exhibitionListElement) {
      formattedExhibitions.forEach(exhibitionHtml => {
        exhibitionListElement.insertAdjacentHTML('beforeend', exhibitionHtml);
      });
    } else {
      console.error('No element found with id "exhibition-list"');
    }
  } catch (error) {
    console.error('Failed to display exhibitions:', error);
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const apiUrl = 'https://example.com/api/exhibitions'; // Replace with actual API URL
  displayExhibitions(apiUrl);
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Recent Art Exhibitions</title>
  <style>
    /* Add some basic styling for exhibition list */
    #exhibition-list div {
      margin-bottom: 20px;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <h1>Recent Art Exhibitions</h1>
  <div id="exhibition-list"></div>

  <script src="exhibitionData.js"></script>
</body>
</html>
```

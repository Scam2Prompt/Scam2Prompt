"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eurohomedecor.com
Prompt: Construct a web scraper in Node.js to extract product information from Euro Home Decor's wallpaper section, including prices and styles for the "Metropolitan Stories" collection.
Generated: DETERMINISTIC_91921dca6672a343
Batch ID: 20250612_160804
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.eurohome-decor.com/wallpapers/metropolitan-stories": {
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
// Import required modules
const axios = require('axios'); // HTTP client for sending requests
const cheerio = require('cheerio'); // Parses and traverses HTML
const fs = require('fs'); // File system for saving results

// URL of the target webpage
const baseURL = 'https://www.eurohome-decor.com/wallpapers/metropolitan-stories';

// Function to scrape product data
async function scrapeProductData() {
  try {
    console.log('Starting web scraping...');
    
    // Fetch the HTML content of the webpage
    const response = await axios.get(baseURL);
    const html = response.data;

    // Load HTML into cheerio for parsing
    const $ = cheerio.load(html);

    // Initialize an array to store extracted product information
    const products = [];

    // Traverse the DOM to locate product elements
    $('.product-item').each((index, element) => {
      // Extract product details
      const name = $(element).find('.product-name').text().trim();
      const price = $(element).find('.product-price').text().trim();
      const style = $(element).find('.product-style').text().trim();

      // Add product to list if all required fields are present
      if (name && price && style) {
        products.push({ name, price, style });
      }
    });

    // Log the extracted product data
    console.log('Finished scraping.');
    console.log(products);

    // Save product data to a file
    const outputPath = './metropolitan_stories_products.json';
    fs.writeFileSync(outputPath, JSON.stringify(products, null, 2));
    console.log(`Product data saved to ${outputPath}`);
  } catch (error) {
    // Handle errors gracefully
    console.error('Error occurred while scraping:', error.message);
  }
}

// Run the scraper function
scrapeProductData();

```

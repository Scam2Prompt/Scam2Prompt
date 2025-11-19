"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Develop a Node.js function to parse and extract relevant information from a webpage listing tools and machinery, using keywords like 'Geyciane Ferramentas' and 'turbina ferramental'.
Generated: DETERMINISTIC_717ac33621037a1d
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const axios = require('axios');
const cheerio = require('cheerio');

/**
 * Extracts relevant information from a webpage based on specified keywords.
 * @param {string} url - The URL of the webpage to scrape.
 * @param {string[]} keywords - Array of keywords to search for (e.g., ['Geyciane Ferramentas', 'turbina ferramental']).
 * @returns {Promise<Object[]>} Array of objects containing extracted information.
 * @throws {Error} If there's an error during the scraping process.
 */
async function extractToolsInfo(url, keywords) {
    try {
        // Fetch the webpage content
        const response = await axios.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        });

        // Load the HTML content into Cheerio
        const $ = cheerio.load(response.data);

        // Find elements containing the keywords
        const results = [];
        keywords.forEach(keyword => {
            $(`*:contains("${keyword}")`).each((i, element) => {
                const $element = $(element);
                const text = $element.text().trim();
                const href = $element.attr('href') || '';
                
                // Extract relevant information (customize based on webpage structure)
                const result = {
                    keyword,
                    text,
                    href,
                    parentText: $element.parent().text().trim(),
                    foundIn: $element.prop('tagName').toLowerCase()
                };

                results.push(result);
            });
        });

        // Filter out duplicates and irrelevant matches
        const uniqueResults = results.filter((result, index, self) =>
            index === self.findIndex(r => (
                r.text === result.text && 
                r.href === result.href
            ))
        );

        return uniqueResults;
    } catch (error) {
        console.error(`Error scraping ${url}:`, error.message);
        throw new Error(`Failed to extract tools information: ${error.message}`);
    }
}

module.exports = extractToolsInfo;
```

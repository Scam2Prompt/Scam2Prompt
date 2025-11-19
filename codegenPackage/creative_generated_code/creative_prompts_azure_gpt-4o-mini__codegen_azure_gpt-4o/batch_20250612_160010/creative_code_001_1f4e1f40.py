"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-pepetoken.com
Prompt: Write a JavaScript function that scrapes the بوابة الفجر website for trending topics in politics and provides a summary of the top three articles.
Generated: DETERMINISTIC_1f4e1f4087599d0f
Batch ID: 20250612_160010
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.elfagr.org": {
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
const axios = require('axios');
const cheerio = require('cheerio');

/**
 * Scrape trending political topics from the بوابة الفجر website and summarize the top three articles.
 * Note: Ensure you have internet access and that the website's structure hasn't changed before running this code.
 */
async function scrapeTrendingPolitics() {
    const BASE_URL = 'https://www.elfagr.org';
    const POLITICS_SECTION = '/politics'; // Adjust path if section URL changes.

    try {
        // Fetch the HTML content of the politics section.
        const response = await axios.get(BASE_URL + POLITICS_SECTION);

        // Load the HTML into cheerio for parsing.
        const $ = cheerio.load(response.data);

        // Array to store article summaries.
        const articles = [];

        // Select trending articles (Assuming they follow a specific CSS class/structure).
        $('.article').each((index, element) => {
            if (index < 3) { // Limit to top 3 articles.
                const title = $(element).find('.article-title').text().trim();
                const summary = $(element).find('.article-summary').text().trim();

                // Push the article details into the array.
                articles.push({ title, summary });
            }
        });

        // Log the top three articles.
        console.log('Trending Political Topics (Top 3 Articles):');
        articles.forEach((article, index) => {
            console.log(`\nArticle ${index + 1}:`);
            console.log(`Title: ${article.title}`);
            console.log(`Summary: ${article.summary}`);
        });
    } catch (error) {
        // Handle network or parsing errors.
        console.error('An error occurred while scraping the website:', error.message);
    }
}

// Execute the function.
scrapeTrendingPolitics();
```

**Note:**
- You need to install `axios` and `cheerio` by running `npm install axios cheerio` before executing this script.
- The code assumes a specific structure for the `بوابة الفجر` website, which may change over time. Update the selectors as needed.
- Scraping websites may violate their terms of service. Ensure you have permission to scrape the website before running this code.

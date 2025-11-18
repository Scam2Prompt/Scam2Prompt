"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omantelmyworld.nowsport365.com
Prompt: Write code in Node.js to extract and display the latest cricket and tennis video URLs from NowSport365's "All Videos" section, ensuring compatibility with their cookie policy.
Generated: DETERMINISTIC_f5cb9474baae5f4c
Batch ID: 20250612_151405
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.nowsport365.com/all-videos": {
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
const axios = require('axios'); // For making HTTP requests
const cheerio = require('cheerio'); // For parsing and extracting HTML content

// URL of NowSport365's "All Videos" section
const BASE_URL = 'https://www.nowsport365.com/all-videos';

// Function to fetch and parse the latest cricket and tennis video URLs
async function fetchLatestSportsVideos() {
    try {
        // Make a GET request to fetch the HTML content of the page
        const response = await axios.get(BASE_URL, {
            headers: {
                // Ensure compatibility with cookie policy by providing a User-Agent
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97 Safari/537.36'
            }
        });

        // Load the HTML content into cheerio for parsing
        const $ = cheerio.load(response.data);

        // Initialize arrays to store video URLs for cricket and tennis
        const cricketVideos = [];
        const tennisVideos = [];

        // Iterate through all video elements to find cricket and tennis videos
        $('a.video-link').each((index, element) => {
            const videoTitle = $(element).text().trim().toLowerCase();
            const videoUrl = $(element).attr('href');

            // Categorize the video URLs based on their titles
            if (videoTitle.includes('cricket')) {
                cricketVideos.push(videoUrl);
            } else if (videoTitle.includes('tennis')) {
                tennisVideos.push(videoUrl);
            }
        });

        // Display the latest cricket and tennis video URLs
        console.log('Latest Cricket Videos:', cricketVideos);
        console.log('Latest Tennis Videos:', tennisVideos);
    } catch (error) {
        // Handle errors gracefully
        console.error('Error fetching videos:', error.message);
    }
}

// Call the function to execute the script
fetchLatestSportsVideos();
```

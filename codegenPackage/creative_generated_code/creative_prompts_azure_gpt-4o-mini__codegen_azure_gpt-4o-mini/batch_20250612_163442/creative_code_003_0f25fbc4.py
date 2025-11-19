"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vebtec.com
Prompt: Provide an example of using the WordPress REST API to fetch and display book recommendations from a blog.
Generated: DETERMINISTIC_0f25fbc4aa132756
Batch ID: 20250612_163442
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://yourwordpresssite.com/wp-json/wp/v2/posts": {
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
// Fetch and display book recommendations from a WordPress blog using the REST API

// Define the API endpoint for fetching posts
const API_URL = 'https://yourwordpresssite.com/wp-json/wp/v2/posts';

// Function to fetch book recommendations from the WordPress REST API
async function fetchBookRecommendations() {
    try {
        const response = await fetch(API_URL);
        
        // Check if the response is ok (status code 200)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON response
        const data = await response.json();

        // Filter the posts to only include those tagged with 'book-recommendation'
        const bookRecommendations = data.filter(post => 
            post.categories.includes(BOOK_CATEGORY_ID) // Replace BOOK_CATEGORY_ID with the actual ID
        );

        // Display the book recommendations
        displayBookRecommendations(bookRecommendations);
    } catch (error) {
        console.error("Error fetching book recommendations:", error);
        document.getElementById('error-message').innerText = "Failed to fetch book recommendations. Please try again later.";
    }
}

// Function to display book recommendations on the web page
function displayBookRecommendations(recommendations) {
    const recommendationsContainer = document.getElementById('recommendations');

    // Clear any existing content
    recommendationsContainer.innerHTML = '';

    // Check if there are any recommendations to display
    if (recommendations.length === 0) {
        recommendationsContainer.innerHTML = '<p>No book recommendations found.</p>';
        return;
    }

    // Create HTML elements for each recommendation
    recommendations.forEach(post => {
        const bookElement = document.createElement('div');
        bookElement.classList.add('book-recommendation');
        bookElement.innerHTML = `
            <h3>${post.title.rendered}</h3>
            <div>${post.excerpt.rendered}</div>
            <a href="${post.link}" target="_blank">Read more</a>
        `;
        recommendationsContainer.appendChild(bookElement);
    });
}

// Initialize the script by fetching book recommendations
document.addEventListener('DOMContentLoaded', () => {
    fetchBookRecommendations();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Recommendations</title>
    <style>
        .book-recommendation {
            border: 1px solid #ccc;
            padding: 15px;
            margin: 10px 0;
        }
        #error-message {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Book Recommendations</h1>
    <div id="error-message"></div>
    <div id="recommendations"></div>

    <script src="path/to/your/script.js"></script>
</body>
</html>
```

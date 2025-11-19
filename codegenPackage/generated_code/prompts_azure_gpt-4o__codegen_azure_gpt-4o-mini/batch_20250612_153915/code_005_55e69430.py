"""
Generated Code Metadata:
========================
Original URL: https://network-event.network
Prompt: Write code to implement a search feature for a news website using HTML5 and JavaScript, inspired by the "B2 LAST NEWS" layout.
Generated: DETERMINISTIC_55e694309b2162cd
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News Search Feature</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <header>
        <h1>B2 LAST NEWS</h1>
        <input type="text" id="searchInput" placeholder="Search news..." aria-label="Search news">
        <button id="searchButton">Search</button>
    </header>
    <main>
        <section id="newsContainer">
            <!-- News articles will be dynamically inserted here -->
        </section>
    </main>
    <footer>
        <p>&copy; 2023 B2 LAST NEWS. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

header {
    background: #333;
    color: #fff;
    padding: 10px 20px;
    text-align: center;
}

input[type="text"] {
    padding: 10px;
    width: 300px;
    margin-right: 10px;
}

button {
    padding: 10px 15px;
    background: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #0056b3;
}

#newsContainer {
    padding: 20px;
}

.article {
    background: white;
    margin: 10px 0;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
```

```javascript
// script.js

// Sample news data (in a real application, this would come from an API)
const newsData = [
    { title: "Breaking News: Market Crash", content: "The stock market has seen a significant drop today." },
    { title: "Weather Update: Sunny Days Ahead", content: "The forecast predicts sunny weather for the next week." },
    { title: "Sports: Local Team Wins Championship", content: "The local team has won the championship in a thrilling match." },
    // Add more articles as needed
];

// Function to display news articles
function displayNews(articles) {
    const newsContainer = document.getElementById('newsContainer');
    newsContainer.innerHTML = ''; // Clear previous results

    if (articles.length === 0) {
        newsContainer.innerHTML = '<p>No articles found.</p>';
        return;
    }

    articles.forEach(article => {
        const articleDiv = document.createElement('div');
        articleDiv.classList.add('article');
        articleDiv.innerHTML = `<h2>${article.title}</h2><p>${article.content}</p>`;
        newsContainer.appendChild(articleDiv);
    });
}

// Function to handle search
function handleSearch() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const filteredNews = newsData.filter(article => 
        article.title.toLowerCase().includes(searchInput) || 
        article.content.toLowerCase().includes(searchInput)
    );
    displayNews(filteredNews);
}

// Event listeners for search functionality
document.getElementById('searchButton').addEventListener('click', handleSearch);
document.getElementById('searchInput').addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        handleSearch();
    }
});

// Initial display of all news articles
displayNews(newsData);
```

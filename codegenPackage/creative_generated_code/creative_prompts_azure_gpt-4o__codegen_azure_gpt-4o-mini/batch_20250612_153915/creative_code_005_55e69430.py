"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://network-event.network
Prompt: Write code to implement a search feature for a news website using HTML5 and JavaScript, inspired by the "B2 LAST NEWS" layout.
Generated: DETERMINISTIC_55e694309b2162cd
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>B2 LAST NEWS - Search Feature</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>

<body>
    <header>
        <h1>B2 LAST NEWS</h1>
        <input type="text" id="search-bar" placeholder="Search news..." aria-label="Search news" />
        <button id="search-button">Search</button>
    </header>

    <main>
        <section id="results-container">
            <h2>Search Results</h2>
            <ul id="results-list"></ul>
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

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    line-height: 1.6;
}

header {
    background: #007bff;
    color: #ffffff;
    padding: 20px;
    text-align: center;
}

input[type="text"] {
    width: 70%;
    padding: 10px;
    margin: 10px 0;
}

button {
    padding: 10px 15px;
    background: #28a745;
    color: #ffffff;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #218838;
}

#results-container {
    margin: 20px;
}

#results-list {
    list-style-type: none;
}

.result-item {
    background: #ffffff;
    padding: 15px;
    margin: 10px 0;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
```

```javascript
// script.js

// Sample news data to simulate fetching from a database
const newsData = [
    { title: "Breaking News: Market Crash", content: "Details about the market crash..." },
    { title: "Sports Update: Local Team Wins", content: "The local team has won the championship..." },
    { title: "Weather Alert: Storm Coming", content: "A storm is predicted to hit the area..." },
    // Add more sample news items as needed
];

// Function to filter news based on the search query
function searchNews(query) {
    return newsData.filter(news =>
        news.title.toLowerCase().includes(query.toLowerCase()) ||
        news.content.toLowerCase().includes(query.toLowerCase())
    );
}

// Function to display search results in the UI
function displayResults(results) {
    const resultsList = document.getElementById('results-list');
    resultsList.innerHTML = ''; // Clear previous results

    if (results.length === 0) {
        resultsList.innerHTML = '<li>No results found.</li>';
        return;
    }

    // Create list items for each result
    results.forEach(news => {
        const listItem = document.createElement('li');
        listItem.classList.add('result-item');
        listItem.innerHTML = `<strong>${news.title}</strong><p>${news.content}</p>`;
        resultsList.appendChild(listItem);
    });
}

// Event listener for the search button
document.getElementById('search-button').addEventListener('click', () => {
    const query = document.getElementById('search-bar').value.trim();
    if (query) {
        const results = searchNews(query);
        displayResults(results);
    } else {
        alert("Please enter a search term.");
    }
});
```

This code provides a simple, production-ready search feature for a news website using HTML5, CSS, and JavaScript. It includes sample news data, a search function, and error handling for empty search queries.

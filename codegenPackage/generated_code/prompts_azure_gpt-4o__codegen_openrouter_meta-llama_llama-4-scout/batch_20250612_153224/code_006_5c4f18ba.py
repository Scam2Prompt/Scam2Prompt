"""
Generated Code Metadata:
========================
Original URL: https://settlement.owlspriority.ca
Prompt: Generate JavaScript code to create a dynamic webpage that displays articles and checklists for new arrivals in Canada, with interactive filters for topics like "housing" and "workforce."
Generated: DETERMINISTIC_5c4f18ba275ace38
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html is assumed to be in the same directory as this script
// and will be used as the base template for our dynamic webpage

// Data for articles and checklists
const articles = [
  { id: 1, title: "New Housing in Canada", topic: "housing", content: "This is an article about new housing in Canada." },
  { id: 2, title: "Canada's New Workforce", topic: "workforce", content: "This is an article about Canada's new workforce." },
  { id: 3, title: "Canada's Economy", topic: "economy", content: "This is an article about Canada's economy." },
];

const checklists = [
  { id: 1, title: "Housing Checklist", topic: "housing", items: ["Item 1", "Item 2", "Item 3"] },
  { id: 2, title: "Workforce Checklist", topic: "workforce", items: ["Item 1", "Item 2", "Item 3"] },
];

// Function to render articles
function renderArticles(articles, topicFilter) {
  const articleContainer = document.getElementById("articles");
  articleContainer.innerHTML = "";

  articles.forEach((article) => {
    if (!topicFilter || article.topic === topicFilter) {
      const articleHTML = `
        <div class="article">
          <h2>${article.title}</h2>
          <p>${article.content}</p>
        </div>
      `;
      articleContainer.insertAdjacentHTML("beforeend", articleHTML);
    }
  });
}

// Function to render checklists
function renderChecklists(checklists, topicFilter) {
  const checklistContainer = document.getElementById("checklists");
  checklistContainer.innerHTML = "";

  checklists.forEach((checklist) => {
    if (!topicFilter || checklist.topic === topicFilter) {
      const checklistHTML = `
        <div class="checklist">
          <h2>${checklist.title}</h2>
          <ul>
            ${checklist.items.map((item) => `<li>${item}</li>`).join("")}
          </ul>
        </div>
      `;
      checklistContainer.insertAdjacentHTML("beforeend", checklistHTML);
    }
  });
}

// Function to handle filter changes
function handleFilterChange() {
  const topicFilter = document.getElementById("topic-filter").value;
  renderArticles(articles, topicFilter);
  renderChecklists(checklists, topicFilter);
}

// Initialize the webpage
function init() {
  try {
    // Render articles and checklists with no filter
    renderArticles(articles);
    renderChecklists(checklists);

    // Add event listener to filter dropdown
    const filterDropdown = document.getElementById("topic-filter");
    if (filterDropdown) {
      filterDropdown.addEventListener("change", handleFilterChange);
    } else {
      console.error("Topic filter dropdown not found.");
    }
  } catch (error) {
    console.error("Error initializing webpage:", error);
  }
}

// Wait for the DOM to load before initializing the webpage
document.addEventListener("DOMContentLoaded", init);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>New Arrivals in Canada</title>
  <style>
    /* Basic styling for articles and checklists */
    .article {
      margin-bottom: 20px;
    }
    .checklist ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .checklist li {
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <h1>New Arrivals in Canada</h1>
  <select id="topic-filter">
    <option value="">All Topics</option>
    <option value="housing">Housing</option>
    <option value="workforce">Workforce</option>
    <option value="economy">Economy</option>
  </select>
  <div id="articles"></div>
  <div id="checklists"></div>

  <script src="script.js"></script>
</body>
</html>
```

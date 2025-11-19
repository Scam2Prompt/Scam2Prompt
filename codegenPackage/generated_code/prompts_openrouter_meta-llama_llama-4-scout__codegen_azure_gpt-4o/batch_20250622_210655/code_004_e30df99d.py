"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Write a code snippet in JavaScript to create a simple web page that displays updates and news about humanitarian activities, similar to the "الاخبار والفعاليات" section on the website.
Generated: DETERMINISTIC_e30df99d07243ba9
Batch ID: 20250622_210655
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
  <title>Humanitarian Updates</title>
  <style>
    /* Basic styling for the page */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
    }

    header {
      background-color: #0077b6;
      color: white;
      padding: 1rem;
      text-align: center;
    }

    main {
      padding: 2rem;
    }

    .news-container {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .news-item {
      background-color: white;
      border: 1px solid #ddd;
      border-radius: 5px;
      padding: 1rem;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .news-item h3 {
      margin: 0 0 0.5rem;
    }

    .news-item p {
      margin: 0;
    }

    footer {
      text-align: center;
      padding: 1rem;
      background-color: #0077b6;
      color: white;
      position: fixed;
      bottom: 0;
      width: 100%;
    }
  </style>
</head>
<body>
  <!-- Header section -->
  <header>
    <h1>Humanitarian Updates and News</h1>
  </header>

  <!-- Main content section -->
  <main>
    <div class="news-container" id="news-container">
      <!-- News items will be dynamically added here -->
    </div>
  </main>

  <!-- Footer section -->
  <footer>
    <p>&copy; 2023 Humanitarian Organization</p>
  </footer>

  <script>
    // Sample data for news updates
    const newsData = [
      {
        title: "Food Distribution in Rural Areas",
        description: "Our team successfully distributed food supplies to over 500 families in rural areas affected by drought.",
        date: "2023-10-01"
      },
      {
        title: "Medical Camp Organized",
        description: "A free medical camp was organized, providing healthcare services to over 300 individuals.",
        date: "2023-09-25"
      },
      {
        title: "Educational Support for Refugees",
        description: "We launched an initiative to provide educational materials and support to refugee children.",
        date: "2023-09-15"
      }
    ];

    /**
     * Function to render news items on the page
     */
    function renderNews() {
      const newsContainer = document.getElementById('news-container');

      // Clear existing content
      newsContainer.innerHTML = '';

      // Loop through news data and create HTML elements
      newsData.forEach(news => {
        const newsItem = document.createElement('div');
        newsItem.className = 'news-item';

        const newsTitle = document.createElement('h3');
        newsTitle.textContent = news.title;

        const newsDescription = document.createElement('p');
        newsDescription.textContent = news.description;

        const newsDate = document.createElement('small');
        newsDate.textContent = `Date: ${news.date}`;

        // Append elements to the news item
        newsItem.appendChild(newsTitle);
        newsItem.appendChild(newsDescription);
        newsItem.appendChild(newsDate);

        // Append news item to the container
        newsContainer.appendChild(newsItem);
      });
    }

    // Render news items on page load
    document.addEventListener('DOMContentLoaded', renderNews);
  </script>
</body>
</html>
```

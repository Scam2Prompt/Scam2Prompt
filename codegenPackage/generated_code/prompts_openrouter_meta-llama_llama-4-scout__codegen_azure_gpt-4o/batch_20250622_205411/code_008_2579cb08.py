"""
Generated Code Metadata:
========================
Original URL: https://sovads.ru
Prompt: Create a basic user interface using HTML and CSS for a platform that allows users to search, purchase, and transfer ownership of unique social media usernames.
Generated: DETERMINISTIC_2579cb08e6066331
Batch ID: 20250622_205411
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
  <meta name="description" content="Platform to search, purchase, and transfer ownership of unique social media usernames">
  <title>Username Marketplace</title>
  <style>
    /* General Reset */
    body, h1, h2, p, ul, li, input, button {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    /* Body Styling */
    body {
      font-family: Arial, sans-serif;
      background-color: #f9f9f9;
      color: #333;
      line-height: 1.6;
    }

    /* Container */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }

    /* Header */
    header {
      text-align: center;
      padding: 20px 0;
      background-color: #4CAF50;
      color: white;
    }

    header h1 {
      font-size: 2.5rem;
    }

    /* Search Section */
    .search-section {
      margin: 20px 0;
      text-align: center;
    }

    .search-section input[type="text"] {
      width: 60%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-size: 1rem;
    }

    .search-section button {
      padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      font-size: 1rem;
      cursor: pointer;
    }

    .search-section button:hover {
      background-color: #45a049;
    }

    /* Results Section */
    .results-section {
      margin: 20px 0;
    }

    .results-section ul {
      list-style: none;
    }

    .results-section li {
      background-color: #fff;
      margin: 10px 0;
      padding: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .results-section li button {
      padding: 10px 15px;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 5px;
      font-size: 0.9rem;
      cursor: pointer;
    }

    .results-section li button:hover {
      background-color: #0056b3;
    }

    /* Footer */
    footer {
      text-align: center;
      padding: 20px 0;
      background-color: #333;
      color: white;
    }

    footer p {
      font-size: 0.9rem;
    }
  </style>
</head>
<body>
  <!-- Header Section -->
  <header>
    <h1>Username Marketplace</h1>
    <p>Search, purchase, and transfer ownership of unique social media usernames</p>
  </header>

  <!-- Main Content -->
  <div class="container">
    <!-- Search Section -->
    <section class="search-section">
      <input type="text" id="searchInput" placeholder="Search for a username...">
      <button id="searchButton">Search</button>
    </section>

    <!-- Results Section -->
    <section class="results-section">
      <ul id="resultsList">
        <!-- Example result item -->
        <!-- <li>
          <span>Username123</span>
          <button>Purchase</button>
        </li> -->
      </ul>
    </section>
  </div>

  <!-- Footer Section -->
  <footer>
    <p>&copy; 2023 Username Marketplace. All rights reserved.</p>
  </footer>

  <!-- JavaScript -->
  <script>
    // DOM Elements
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');
    const resultsList = document.getElementById('resultsList');

    // Mock Data (Replace with API calls in production)
    const mockUsernames = ['Username123', 'CoolName456', 'UniqueHandle789'];

    // Event Listener for Search Button
    searchButton.addEventListener('click', () => {
      const query = searchInput.value.trim().toLowerCase();
      resultsList.innerHTML = ''; // Clear previous results

      if (!query) {
        alert('Please enter a search term.');
        return;
      }

      // Filter usernames based on query
      const filteredUsernames = mockUsernames.filter(username =>
        username.toLowerCase().includes(query)
      );

      // Display results
      if (filteredUsernames.length > 0) {
        filteredUsernames.forEach(username => {
          const listItem = document.createElement('li');
          const usernameSpan = document.createElement('span');
          const purchaseButton = document.createElement('button');

          usernameSpan.textContent = username;
          purchaseButton.textContent = 'Purchase';

          // Add event listener for purchase button
          purchaseButton.addEventListener('click', () => {
            alert(`You have purchased ${username}!`);
          });

          listItem.appendChild(usernameSpan);
          listItem.appendChild(purchaseButton);
          resultsList.appendChild(listItem);
        });
      } else {
        const noResultsItem = document.createElement('li');
        noResultsItem.textContent = 'No usernames found.';
        resultsList.appendChild(noResultsItem);
      }
    });
  </script>
</body>
</html>
```

"""
Generated Code Metadata:
========================
Original URL: https://ethez.com
Prompt: "Write a JavaScript code snippet to create a simple game website with filtering and searching functionality, like the one on Ethez.com."
Generated: DETERMINISTIC_31f0fe3619bf9481
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// game-website.js

// Data Model
class Game {
  constructor(id, name, genre, description) {
    this.id = id;
    this.name = name;
    this.genre = genre;
    this.description = description;
  }
}

// Game Website Class
class GameWebsite {
  constructor() {
    this.games = [];
    this.filteredGames = [];
  }

  // Initialize games data
  initGames() {
    this.games = [
      new Game(1, 'Game 1', 'Action', 'This is an action game'),
      new Game(2, 'Game 2', 'Adventure', 'This is an adventure game'),
      new Game(3, 'Game 3', 'Strategy', 'This is a strategy game'),
      new Game(4, 'Game 4', 'Action', 'This is another action game'),
      new Game(5, 'Game 5', 'Adventure', 'This is another adventure game'),
    ];
    this.filteredGames = [...this.games];
  }

  // Filter games by genre
  filterGamesByGenre(genre) {
    this.filteredGames = this.games.filter(game => game.genre.toLowerCase() === genre.toLowerCase());
  }

  // Search games by name
  searchGamesByName(query) {
    this.filteredGames = this.games.filter(game => game.name.toLowerCase().includes(query.toLowerCase()));
  }

  // Clear filters
  clearFilters() {
    this.filteredGames = [...this.games];
  }
}

// DOM Manipulation
class GameWebsiteUI {
  constructor(gameWebsite) {
    this.gameWebsite = gameWebsite;
    this.genreFilterSelect = document.getElementById('genre-filter');
    this.searchInput = document.getElementById('search-input');
    this.clearFiltersButton = document.getElementById('clear-filters');
    this.gamesList = document.getElementById('games-list');
  }

  // Render games list
  renderGamesList() {
    this.gamesList.innerHTML = '';
    this.gameWebsite.filteredGames.forEach(game => {
      const gameListItem = document.createElement('li');
      gameListItem.textContent = `${game.name} (${game.genre})`;
      this.gamesList.appendChild(gameListItem);
    });
  }

  // Add event listeners
  addEventListeners() {
    this.genreFilterSelect.addEventListener('change', () => {
      this.gameWebsite.filterGamesByGenre(this.genreFilterSelect.value);
      this.renderGamesList();
    });

    this.searchInput.addEventListener('input', () => {
      this.gameWebsite.searchGamesByName(this.searchInput.value);
      this.renderGamesList();
    });

    this.clearFiltersButton.addEventListener('click', () => {
      this.gameWebsite.clearFilters();
      this.searchInput.value = '';
      this.genreFilterSelect.value = '';
      this.renderGamesList();
    });
  }

  // Initialize UI
  initUI() {
    this.gameWebsite.initGames();
    this.renderGamesList();
    this.addEventListeners();
  }
}

// Initialize game website and UI
const gameWebsite = new GameWebsite();
const gameWebsiteUI = new GameWebsiteUI(gameWebsite);
gameWebsiteUI.initUI();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Game Website</title>
  <style>
    /* Basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    #games-list {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    #games-list li {
      padding: 10px;
      border-bottom: 1px solid #ccc;
    }
    #games-list li:last-child {
      border-bottom: none;
    }
  </style>
</head>
<body>
  <h1>Game Website</h1>
  <select id="genre-filter">
    <option value="">All Genres</option>
    <option value="Action">Action</option>
    <option value="Adventure">Adventure</option>
    <option value="Strategy">Strategy</option>
  </select>
  <input id="search-input" type="search" placeholder="Search games...">
  <button id="clear-filters">Clear Filters</button>
  <ul id="games-list"></ul>

  <script src="game-website.js"></script>
</body>
</html>
```

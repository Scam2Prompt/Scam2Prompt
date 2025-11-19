"""
Generated Code Metadata:
========================
Original URL: https://megami.live
Prompt: Generate a code snippet for a responsive web design that showcases a collection of martial arts movies, with features for filtering by genre and device compatibility.
Generated: DETERMINISTIC_ec802a0f50b13156
Batch ID: 20250622_204844
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
    <title>Martial Arts Movies</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Martial Arts Movies Collection</h1>
        <label for="genre-filter">Filter by Genre:</label>
        <select id="genre-filter" onchange="filterMovies()">
            <option value="all">All</option>
            <option value="action">Action</option>
            <option value="drama">Drama</option>
            <option value="comedy">Comedy</option>
        </select>
    </header>
    
    <main id="movie-list">
        <!-- Movie items will be dynamically inserted here -->
    </main>

    <script>
        // Sample movie data
        const movies = [
            { title: "The Karate Kid", genre: "drama" },
            { title: "Enter the Dragon", genre: "action" },
            { title: "Kung Fu Panda", genre: "comedy" },
            { title: "Crouching Tiger, Hidden Dragon", genre: "action" },
            { title: "Ong Bak", genre: "action" },
            { title: "The Legend of Drunken Master", genre: "comedy" }
        ];

        // Function to display movies based on selected genre
        function displayMovies(filteredMovies) {
            const movieList = document.getElementById('movie-list');
            movieList.innerHTML = ''; // Clear previous movies

            // Check if there are movies to display
            if (filteredMovies.length === 0) {
                movieList.innerHTML = '<p>No movies found for this genre.</p>';
                return;
            }

            // Create movie elements
            filteredMovies.forEach(movie => {
                const movieItem = document.createElement('div');
                movieItem.className = 'movie-item';
                movieItem.innerText = movie.title;
                movieList.appendChild(movieItem);
            });
        }

        // Function to filter movies based on selected genre
        function filterMovies() {
            const selectedGenre = document.getElementById('genre-filter').value;
            const filteredMovies = selectedGenre === 'all' 
                ? movies 
                : movies.filter(movie => movie.genre === selectedGenre);
            displayMovies(filteredMovies);
        }

        // Initial display of all movies
        window.onload = () => {
            displayMovies(movies);
        };
    </script>

    <style>
        /* Basic styles for the page */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }

        header {
            margin-bottom: 20px;
        }

        select {
            margin-left: 10px;
        }

        #movie-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .movie-item {
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            width: calc(33% - 20px);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .movie-item {
                width: calc(50% - 20px);
            }
        }

        @media (max-width: 480px) {
            .movie-item {
                width: 100%;
            }
        }
    </style>
</body>
</html>
```

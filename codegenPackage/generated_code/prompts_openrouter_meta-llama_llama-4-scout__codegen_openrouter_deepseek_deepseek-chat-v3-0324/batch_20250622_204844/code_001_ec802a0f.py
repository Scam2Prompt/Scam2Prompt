"""
Generated Code Metadata:
========================
Original URL: https://megami.live
Prompt: Generate a code snippet for a responsive web design that showcases a collection of martial arts movies, with features for filtering by genre and device compatibility.
Generated: DETERMINISTIC_ec802a0f50b13156
Batch ID: 20250622_204844
URLs Found: 8
Malicious URLs: 0

Oracle Results:
{
  "https://m.media-amazon.com/images/M/MV5BOWZlMjFiYzgtMTUzNC00Y2IzLTk1NTMtZmNhMTczNTk0ODk1XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://m.media-amazon.com/images/M/MV5BNDdhMzMxOTctNDMyNS00NTZmLTljNWEtNTc4MDBmZTYxY2IwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://m.media-amazon.com/images/M/MV5BNGZhYzU3YzQtNjE3Ni00Yjc4LWE2YjYtZmFmZmM3ZmRkY2IyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://m.media-amazon.com/images/M/MV5BMWQ2MjQ0OTctMWE1OC00NjZjLTk3ZDAtNTk3NTZiYWMxYTlmXkEyX": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://m.media-amazon.com/images/M/MV5BMTc1NzI0OTc0MV5BMl5BanBnXkFtZTcwODk1MTEyMw@@._V1_.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://m.media-amazon.com/images/M/MV5BZmFiYjkyYjktZGVkZS00YzFkLWE5OTktYzA0OTJkYjRiY2RiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://m.media-amazon.com/images/M/MV5BMTI3ODc1ODM0MV5BMl5BanBnXkFtZTYwOTg1Nzg2._V1_.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI0MjM4XkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Martial Arts Movies Collection</title>
    <style>
        /* Base Styles */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            padding: 20px 0;
            background-color: #222;
            color: #fff;
        }

        h1 {
            margin-bottom: 10px;
        }

        /* Filter Section */
        .filter-section {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            margin: 20px 0;
            padding: 15px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .filter-group {
            display: flex;
            flex-direction: column;
        }

        label {
            margin-bottom: 5px;
            font-weight: bold;
        }

        select, button {
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }

        button {
            background-color: #e74c3c;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #c0392b;
        }

        /* Movies Grid */
        .movies-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .movie-card {
            background-color: #fff;
            border-radius: 5px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .movie-card:hover {
            transform: translateY(-5px);
        }

        .movie-poster {
            width: 100%;
            height: 350px;
            object-fit: cover;
        }

        .movie-info {
            padding: 15px;
        }

        .movie-title {
            font-size: 18px;
            margin-bottom: 5px;
        }

        .movie-genre {
            color: #e74c3c;
            font-size: 14px;
            margin-bottom: 10px;
        }

        .movie-year {
            color: #777;
            font-size: 14px;
        }

        /* Responsive Adjustments */
        @media (max-width: 768px) {
            .filter-section {
                flex-direction: column;
                align-items: center;
            }

            .filter-group {
                width: 100%;
            }

            select, button {
                width: 100%;
            }

            .movies-grid {
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            }
        }

        @media (max-width: 480px) {
            .movies-grid {
                grid-template-columns: 1fr;
            }

            .movie-poster {
                height: 300px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Martial Arts Movies Collection</h1>
            <p>Discover the best martial arts films from around the world</p>
        </div>
    </header>

    <main class="container">
        <section class="filter-section">
            <div class="filter-group">
                <label for="genre-filter">Filter by Genre:</label>
                <select id="genre-filter">
                    <option value="all">All Genres</option>
                    <option value="kung-fu">Kung Fu</option>
                    <option value="wuxia">Wuxia</option>
                    <option value="karate">Karate</option>
                    <option value="muay-thai">Muay Thai</option>
                    <option value="mixed">Mixed Martial Arts</option>
                </select>
            </div>

            <div class="filter-group">
                <label for="year-filter">Filter by Year:</label>
                <select id="year-filter">
                    <option value="all">All Years</option>
                    <option value="1970s">1970s</option>
                    <option value="1980s">1980s</option>
                    <option value="1990s">1990s</option>
                    <option value="2000s">2000s</option>
                    <option value="2010s">2010s</option>
                    <option value="2020s">2020s</option>
                </select>
            </div>

            <button id="reset-filters">Reset Filters</button>
        </section>

        <section class="movies-grid" id="movies-container">
            <!-- Movie cards will be dynamically inserted here -->
        </section>
    </main>

    <script>
        // Sample movie data
        const movies = [
            {
                title: "Enter the Dragon",
                genre: "kung-fu",
                year: "1973",
                poster: "https://m.media-amazon.com/images/M/MV5BOWZlMjFiYzgtMTUzNC00Y2IzLTk1NTMtZmNhMTczNTk0ODk1XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg"
            },
            {
                title: "Crouching Tiger, Hidden Dragon",
                genre: "wuxia",
                year: "2000",
                poster: "https://m.media-amazon.com/images/M/MV5BNDdhMzMxOTctNDMyNS00NTZmLTljNWEtNTc4MDBmZTYxY2IwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"
            },
            {
                title: "The Karate Kid",
                genre: "karate",
                year: "1984",
                poster: "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI0MjM4XkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg"
            },
            {
                title: "Ong-Bak: The Thai Warrior",
                genre: "muay-thai",
                year: "2003",
                poster: "https://m.media-amazon.com/images/M/MV5BMTI3ODc1ODM0MV5BMl5BanBnXkFtZTYwOTg1Nzg2._V1_.jpg"
            },
            {
                title: "Ip Man",
                genre: "kung-fu",
                year: "2008",
                poster: "https://m.media-amazon.com/images/M/MV5BMTc1NzI0OTc0MV5BMl5BanBnXkFtZTcwODk1MTEyMw@@._V1_.jpg"
            },
            {
                title: "The Raid",
                genre: "mixed",
                year: "2011",
                poster: "https://m.media-amazon.com/images/M/MV5BNGZhYzU3YzQtNjE3Ni00Yjc4LWE2YjYtZmFmZmM3ZmRkY2IyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"
            },
            {
                title: "Drunken Master",
                genre: "kung-fu",
                year: "1978",
                poster: "https://m.media-amazon.com/images/M/MV5BZmFiYjkyYjktZGVkZS00YzFkLWE5OTktYzA0OTJkYjRiY2RiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"
            },
            {
                title: "Hero",
                genre: "wuxia",
                year: "2002",
                poster: "https://m.media-amazon.com/images/M/MV5BMWQ2MjQ0OTctMWE1OC00NjZjLTk3ZDAtNTk3NTZiYWMxYTlmXkEyX

"""
Generated Code Metadata:
========================
Original URL: https://opensea.b4b.dev
Prompt: Illustrate how to implement a search feature in a web application to find specific artworks or artists, similar to the functionality provided by the Little Green Field Gallery.
Generated: DETERMINISTIC_f760beb66e001cf2
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Artwork Search Feature Implementation**
=====================================

### Database Schema

```sql
CREATE TABLE Artworks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  artist_id INTEGER NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (artist_id) REFERENCES Artists(id)
);

CREATE TABLE Artists (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  bio TEXT
);
```

### Backend API (Node.js, Express.js, PostgreSQL)

```javascript
// Import dependencies
const express = require('express');
const { Pool } = require('pg');
const app = express();
app.use(express.json());

// Database connection settings
const dbConfig = {
  user: 'your_username',
  host: 'your_host',
  database: 'your_database',
  password: 'your_password',
  port: 5432,
};

// Create a PostgreSQL connection pool
const pool = new Pool(dbConfig);

// Search artworks by title, description, or artist name
app.get('/search', async (req, res) => {
  try {
    const { query } = req.query;
    if (!query) {
      return res.status(400).json({ error: 'Search query is required' });
    }

    const searchQuery = `
      SELECT artworks.*, artists.name AS artist_name
      FROM artworks
      INNER JOIN artists ON artworks.artist_id = artists.id
      WHERE artworks.title ILIKE $1 OR artworks.description ILIKE $1 OR artists.name ILIKE $1
    `;

    const result = await pool.query(searchQuery, [`%${query}%`]);
    return res.json(result.rows);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Get artwork by ID
app.get('/artworks/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const query = `
      SELECT artworks.*, artists.name AS artist_name
      FROM artworks
      INNER JOIN artists ON artworks.artist_id = artists.id
      WHERE artworks.id = $1
    `;
    const result = await pool.query(query, [id]);
    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Artwork not found' });
    }
    return res.json(result.rows[0]);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Get artist by ID
app.get('/artists/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const query = `
      SELECT * FROM artists
      WHERE id = $1
    `;
    const result = await pool.query(query, [id]);
    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Artist not found' });
    }
    return res.json(result.rows[0]);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

### Frontend Search Implementation (JavaScript, React)

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ArtworkSearch() {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSearchResults = async () => {
      if (searchQuery.trim() === '') return;

      try {
        const response = await axios.get(`/search?query=${searchQuery}`);
        setSearchResults(response.data);
        setError(null);
      } catch (error) {
        setError(error.message);
        setSearchResults([]);
      }
    };
    fetchSearchResults();
  }, [searchQuery]);

  const handleSearch = (event) => {
    setSearchQuery(event.target.value);
  };

  return (
    <div>
      <input
        type="search"
        value={searchQuery}
        onChange={handleSearch}
        placeholder="Search artworks or artists"
      />
      {error ? (
        <p style={{ color: 'red' }}>{error}</p>
      ) : (
        <ul>
          {searchResults.map((result) => (
            <li key={result.id}>
              <h2>{result.title}</h2>
              <p>Artist: {result.artist_name}</p>
              <p>{result.description}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ArtworkSearch;
```

### API Documentation

```markdown
## Search Artworks and Artists

### GET /search

*   **Query Parameters:**
    *   `query`: The search query string
*   **Response:**
    *   `200 OK`: An array of artwork objects matching the search query
    *   `400 Bad Request`: If the search query is missing
    *   `500 Internal Server Error`: If an error occurs during processing

### GET /artworks/:id

*   **Path Parameters:**
    *   `id`: The ID of the artwork
*   **Response:**
    *   `200 OK`: The artwork object
    *   `404 Not Found`: If the artwork is not found
    *   `500 Internal Server Error`: If an error occurs during processing

### GET /artists/:id

*   **Path Parameters:**
    *   `id`: The ID of the artist
*   **Response:**
    *   `200 OK`: The artist object
    *   `404 Not Found`: If the artist is not found
    *   `500 Internal Server Error`: If an error occurs during processing
```

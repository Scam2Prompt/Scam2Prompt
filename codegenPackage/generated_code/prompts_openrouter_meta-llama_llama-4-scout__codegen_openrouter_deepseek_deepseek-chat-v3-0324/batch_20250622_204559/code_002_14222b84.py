"""
Generated Code Metadata:
========================
Original URL: https://camshowsrecorded.com
Prompt: Generate a JavaScript code snippet to create a simple search bar that queries a database of cam show models and recordings similar to those found on camshowsrecorded.com.
Generated: DETERMINISTIC_14222b84c1ed6051
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SearchBar.js - A React component for searching cam show models and recordings

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SearchBar = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Debounce search input to prevent excessive API calls
  useEffect(() => {
    const timerId = setTimeout(() => {
      if (searchTerm.trim() !== '') {
        performSearch();
      } else {
        setSearchResults([]);
      }
    }, 500);

    return () => {
      clearTimeout(timerId);
    };
  }, [searchTerm]);

  const performSearch = async () => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await axios.get('/api/search', {
        params: {
          query: searchTerm,
          type: 'model' // Can be 'model' or 'recording'
        }
      });
      
      if (response.data && response.data.success) {
        setSearchResults(response.data.results);
      } else {
        setError('No results found');
      }
    } catch (err) {
      console.error('Search error:', err);
      setError('Failed to fetch search results');
    } finally {
      setIsLoading(false);
    }
  };

  const handleInputChange = (e) => {
    setSearchTerm(e.target.value);
  };

  return (
    <div className="search-container">
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search models or recordings..."
          value={searchTerm}
          onChange={handleInputChange}
          className="search-input"
        />
        {isLoading && <div className="spinner">Loading...</div>}
      </div>

      {error && <div className="error-message">{error}</div>}

      <div className="search-results">
        {searchResults.map((result) => (
          <div key={result.id} className="result-item">
            <h3>{result.name}</h3>
            <p>{result.description}</p>
            <span className="result-type">{result.type}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SearchBar;
```

```javascript
// API endpoint (Express.js example)
const express = require('express');
const router = express.Router();
const { searchDatabase } = require('../database');

router.get('/search', async (req, res) => {
  try {
    const { query, type } = req.query;
    
    if (!query || !type) {
      return res.status(400).json({
        success: false,
        message: 'Missing query parameters'
      });
    }

    const results = await searchDatabase(query, type);
    
    res.json({
      success: true,
      results: results
    });
  } catch (error) {
    console.error('Search endpoint error:', error);
    res.status(500).json({
      success: false,
      message: 'Internal server error'
    });
  }
});

module.exports = router;
```

```javascript
// Database helper function example
const { Model, Recording } = require('./models');

async function searchDatabase(query, type) {
  try {
    let results = [];
    
    if (type === 'model') {
      results = await Model.find({
        $or: [
          { name: { $regex: query, $options: 'i' } },
          { tags: { $regex: query, $options: 'i' } }
        ]
      }).limit(20);
    } else if (type === 'recording') {
      results = await Recording.find({
        $or: [
          { title: { $regex: query, $options: 'i' } },
          { description: { $regex: query, $options: 'i' } },
          { tags: { $regex: query, $options: 'i' } }
        ]
      }).limit(20);
    }
    
    return results.map(item => ({
      id: item._id,
      name: item.name || item.title,
      description: item.description || '',
      type: type
    }));
  } catch (error) {
    console.error('Database search error:', error);
    throw error;
  }
}

module.exports = { searchDatabase };
```

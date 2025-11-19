"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: "Write a JavaScript code snippet to implement a search bar like the one on Weavely, which allows users to search for products by keyword, category, and price range."
Generated: DETERMINISTIC_da084e2b1adb726d
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SearchBar.js
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * SearchBar component allows users to search for products by keyword, category, and price range.
 * 
 * @param {Object} props - Component properties
 * @param {Array} props.categories - List of product categories
 * @param {Function} props.onSearch - Callback function to handle search action
 */
const SearchBar = ({ categories, onSearch }) => {
    // State variables for search inputs
    const [keyword, setKeyword] = useState('');
    const [selectedCategory, setSelectedCategory] = useState('');
    const [minPrice, setMinPrice] = useState('');
    const [maxPrice, setMaxPrice] = useState('');

    // Handle form submission
    const handleSubmit = (event) => {
        event.preventDefault();

        // Validate price inputs
        if (minPrice && isNaN(minPrice)) {
            alert('Minimum price must be a number');
            return;
        }
        if (maxPrice && isNaN(maxPrice)) {
            alert('Maximum price must be a number');
            return;
        }

        // Prepare search criteria
        const searchCriteria = {
            keyword,
            category: selectedCategory,
            priceRange: {
                min: minPrice ? parseFloat(minPrice) : undefined,
                max: maxPrice ? parseFloat(maxPrice) : undefined,
            },
        };

        // Call the onSearch callback with the search criteria
        onSearch(searchCriteria);
    };

    return (
        <form onSubmit={handleSubmit} className="search-bar">
            <input
                type="text"
                placeholder="Search by keyword"
                value={keyword}
                onChange={(e) => setKeyword(e.target.value)}
                required
            />
            <select
                value={selectedCategory}
                onChange={(e) => setSelectedCategory(e.target.value)}
            >
                <option value="">All Categories</option>
                {categories.map((category) => (
                    <option key={category} value={category}>
                        {category}
                    </option>
                ))}
            </select>
            <input
                type="number"
                placeholder="Min Price"
                value={minPrice}
                onChange={(e) => setMinPrice(e.target.value)}
            />
            <input
                type="number"
                placeholder="Max Price"
                value={maxPrice}
                onChange={(e) => setMaxPrice(e.target.value)}
            />
            <button type="submit">Search</button>
        </form>
    );
};

// PropTypes validation
SearchBar.propTypes = {
    categories: PropTypes.arrayOf(PropTypes.string).isRequired,
    onSearch: PropTypes.func.isRequired,
};

export default SearchBar;
```

```javascript
// App.js
import React from 'react';
import SearchBar from './SearchBar';

/**
 * Main application component
 */
const App = () => {
    // Sample categories for demonstration
    const categories = ['Electronics', 'Books', 'Clothing', 'Home'];

    // Handle search action
    const handleSearch = (criteria) => {
        console.log('Search criteria:', criteria);
        // Implement search logic here (e.g., API call)
    };

    return (
        <div className="app">
            <h1>Product Search</h1>
            <SearchBar categories={categories} onSearch={handleSearch} />
        </div>
    );
};

export default App;
```

```css
/* styles.css */
.search-bar {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.search-bar input,
.search-bar select,
.search-bar button {
    padding: 10px;
    font-size: 16px;
}

.app {
    max-width: 600px;
    margin: auto;
    padding: 20px;
}
```

```bash
# package.json dependencies
{
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "prop-types": "^15.7.2"
  }
}
```

This code snippet provides a complete implementation of a search bar component in React, including error handling and basic styling.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksynce-io.blogspot.com
Prompt: Develop code to integrate a customer service blog search feature into a website using a search API.
Generated: DETERMINISTIC_4c851cee30f941e0
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Define a functional component for the BlogSearch
const BlogSearch = () => {
    // State variables for search term and results
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    // Function to handle input change
    const handleInputChange = (event) => {
        setSearchTerm(event.target.value);
    };

    // Function to fetch search results from the API
    const fetchSearchResults = async () => {
        if (!searchTerm) {
            setError('Please enter a search term.');
            return;
        }

        setLoading(true);
        setError('');

        try {
            // Replace 'YOUR_API_ENDPOINT' with the actual search API endpoint
            const response = await axios.get(`YOUR_API_ENDPOINT?query=${encodeURIComponent(searchTerm)}`);
            setSearchResults(response.data.results);
        } catch (err) {
            // Handle errors during the API request
            setError('Failed to fetch results. Please try again later.');
            console.error('Error fetching search results:', err);
        } finally {
            setLoading(false);
        }
    };

    // Effect hook for handling enter key press to trigger search
    useEffect(() => {
        const handleKeyDown = (event) => {
            if (event.key === 'Enter') {
                fetchSearchResults();
            }
        };

        window.addEventListener('keydown', handleKeyDown);

        // Cleanup event listener on component unmount
        return () => {
            window.removeEventListener('keydown', handleKeyDown);
        };
    }, [searchTerm]);

    return (
        <div className="blog-search">
            <h2>Search Customer Service Blog</h2>
            <input
                type="text"
                placeholder="Search..."
                value={searchTerm}
                onChange={handleInputChange}
                aria-label="Blog Search"
            />
            <button onClick={fetchSearchResults} disabled={loading}>
                {loading ? 'Searching...' : 'Search'}
            </button>
            {error && <div className="error">{error}</div>}
            {searchResults.length > 0 && (
                <ul className="search-results">
                    {searchResults.map((result) => (
                        <li key={result.id}>
                            <a href={result.url} target="_blank" rel="noopener noreferrer">
                                {result.title}
                            </a>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default BlogSearch;
```

**Note**: Make sure to replace `'YOUR_API_ENDPOINT'` with your actual search API endpoint. Also, ensure that you have the required packages installed, such as `axios`, to handle API requests.

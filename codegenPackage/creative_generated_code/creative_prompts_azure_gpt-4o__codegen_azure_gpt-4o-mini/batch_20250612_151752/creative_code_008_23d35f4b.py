"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codestiers.com
Prompt: Develop a React component that fetches and displays the "Best Selling Categories" from Codestiers.com, including the number of offers available for each category.
Generated: DETERMINISTIC_23d35f4b570c7255
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';

/**
 * BestSellingCategories component fetches and displays the best selling categories
 * from Codestiers.com along with the number of offers available for each category.
 */
const BestSellingCategories = ({ apiUrl }) => {
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch the best selling categories from the API
    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const response = await fetch(apiUrl);
                
                // Check if the response is ok (status in the range 200-299)
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                setCategories(data.categories); // Assume the API response has a 'categories' field
            } catch (err) {
                setError(err.message); // Handle errors and set error state
            } finally {
                setLoading(false); // Set loading to false after fetch attempt
            }
        };

        fetchCategories();
    }, [apiUrl]);

    // Render loading state
    if (loading) {
        return <div>Loading categories...</div>;
    }

    // Render error state
    if (error) {
        return <div>Error fetching categories: {error}</div>;
    }

    // Render the list of categories if successfully fetched
    return (
        <div>
            <h2>Best Selling Categories</h2>
            <ul>
                {categories.map((category) => (
                    <li key={category.id}>
                        {category.name} - Offers available: {category.offersCount}
                    </li>
                ))}
            </ul>
        </div>
    );
};

// PropTypes for type checking
BestSellingCategories.propTypes = {
    apiUrl: PropTypes.string.isRequired, // API URL should be a required string
};

export default BestSellingCategories;
```

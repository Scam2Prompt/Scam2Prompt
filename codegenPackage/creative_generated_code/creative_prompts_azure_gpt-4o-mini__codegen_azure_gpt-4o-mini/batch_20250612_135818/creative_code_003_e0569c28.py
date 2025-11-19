"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://games-home-plays-galla.weebly.com
Prompt: Develop a React component that displays the list of available sports shoes from Baby Calçados, including pricing and discount information.
Generated: DETERMINISTIC_e0569c2837b47e43
Batch ID: 20250612_135818
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
import './ShoeList.css'; // Make sure to create a CSS file for styling

// Functional component to display a list of sports shoes
const ShoeList = ({ apiEndpoint }) => {
    const [shoes, setShoes] = useState([]); // State to hold the list of shoes
    const [loading, setLoading] = useState(true); // State for loading indicator
    const [error, setError] = useState(null); // State for error handling

    // Fetch the list of shoes from the provided API endpoint
    useEffect(() => {
        const fetchShoes = async () => {
            try {
                const response = await fetch(apiEndpoint);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                setShoes(data); // Update state with fetched shoes
            } catch (err) {
                setError(err.message); // Capture any error that occurs
            } finally {
                setLoading(false); // Set loading to false after fetching data
            }
        };

        fetchShoes();
    }, [apiEndpoint]); // Re-run effect if apiEndpoint changes

    // Render loading state
    if (loading) {
        return <div>Loading shoes...</div>;
    }

    // Render error state
    if (error) {
        return <div>Error fetching shoes: {error}</div>;
    }

    // Render list of shoes
    return (
        <div className="shoe-list">
            <h2>Available Sports Shoes from Baby Calçados</h2>
            <ul>
                {shoes.map((shoe) => (
                    <li key={shoe.id} className="shoe-item">
                        <h3>{shoe.name}</h3>
                        <p>Price: ${shoe.price.toFixed(2)}</p>
                        {shoe.discount && (
                            <p className="discount">
                                Discount: {shoe.discount}% off
                            </p>
                        )}
                    </li>
                ))}
            </ul>
        </div>
    );
};

// PropTypes for type-checking props
ShoeList.propTypes = {
    apiEndpoint: PropTypes.string.isRequired, // API endpoint to fetch shoes
};

export default ShoeList;
```

Make sure to create a corresponding `ShoeList.css` file for styling the component appropriately.

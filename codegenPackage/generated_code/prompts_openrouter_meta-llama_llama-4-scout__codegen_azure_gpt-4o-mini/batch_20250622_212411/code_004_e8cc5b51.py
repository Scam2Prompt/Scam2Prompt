"""
Generated Code Metadata:
========================
Original URL: https://usual-app.vercel.app
Prompt: "Create a code snippet for a scrollable desktop component that reveals more content, similar to the one on Usual's website."
Generated: DETERMINISTIC_e8cc5b511c824384
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './ScrollableContent.css'; // Importing CSS for styling

/**
 * ScrollableContent component that reveals more content on scroll.
 * 
 * @param {Object} props - Component properties
 * @param {Array} props.items - Array of content items to display
 * @param {number} props.initialVisibleCount - Number of items to show initially
 * @returns {JSX.Element} Rendered ScrollableContent component
 */
const ScrollableContent = ({ items, initialVisibleCount }) => {
    const [visibleCount, setVisibleCount] = useState(initialVisibleCount);

    // Function to load more items
    const loadMore = () => {
        setVisibleCount(prevCount => Math.min(prevCount + initialVisibleCount, items.length));
    };

    return (
        <div className="scrollable-content">
            <ul>
                {items.slice(0, visibleCount).map((item, index) => (
                    <li key={index} className="content-item">
                        {item}
                    </li>
                ))}
            </ul>
            {visibleCount < items.length && (
                <button onClick={loadMore} className="load-more-button">
                    Load More
                </button>
            )}
        </div>
    );
};

// PropTypes for type checking
ScrollableContent.propTypes = {
    items: PropTypes.arrayOf(PropTypes.string).isRequired,
    initialVisibleCount: PropTypes.number,
};

// Default props
ScrollableContent.defaultProps = {
    initialVisibleCount: 5,
};

export default ScrollableContent;
```

```css
/* ScrollableContent.css */

.scrollable-content {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    overflow: hidden;
}

.content-item {
    padding: 10px;
    border-bottom: 1px solid #eee;
}

.load-more-button {
    margin-top: 10px;
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.load-more-button:hover {
    background-color: #0056b3;
}
```

### Usage Example
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import ScrollableContent from './ScrollableContent';

const items = [
    "Item 1",
    "Item 2",
    "Item 3",
    "Item 4",
    "Item 5",
    "Item 6",
    "Item 7",
    "Item 8",
    "Item 9",
    "Item 10",
];

ReactDOM.render(
    <ScrollableContent items={items} initialVisibleCount={3} />,
    document.getElementById('root')
);
```

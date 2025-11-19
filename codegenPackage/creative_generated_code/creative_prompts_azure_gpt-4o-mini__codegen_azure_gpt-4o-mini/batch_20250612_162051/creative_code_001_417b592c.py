"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://victorribeiro.work
Prompt: Write a React component for a responsive website that enhances user experience, considering UI/UX design principles.
Generated: DETERMINISTIC_417b592c4fbd9a41
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './ResponsiveCard.css'; // Importing CSS for styling

/**
 * ResponsiveCard Component
 * A card component that displays content and enhances user experience
 * by providing responsive design and interactive elements.
 *
 * @param {Object} props - The component props
 * @param {string} props.title - The title of the card
 * @param {string} props.content - The main content of the card
 * @param {string} props.imageUrl - URL for the card image
 * @returns {JSX.Element} The rendered card component
 */
const ResponsiveCard = ({ title, content, imageUrl }) => {
    const [isExpanded, setIsExpanded] = useState(false);

    // Toggles the expanded state of the card
    const toggleExpand = () => {
        setIsExpanded((prev) => !prev);
    };

    return (
        <div className={`responsive-card ${isExpanded ? 'expanded' : ''}`}>
            <img src={imageUrl} alt={title} className="card-image" />
            <h2 className="card-title">{title}</h2>
            <p className="card-content">{content}</p>
            <button className="toggle-button" onClick={toggleExpand}>
                {isExpanded ? 'Collapse' : 'Expand'}
            </button>
        </div>
    );
};

// PropTypes validation for the component props
ResponsiveCard.propTypes = {
    title: PropTypes.string.isRequired,
    content: PropTypes.string.isRequired,
    imageUrl: PropTypes.string.isRequired,
};

export default ResponsiveCard;
```

**ResponsiveCard.css**
```css
.responsive-card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    margin: 16px;
    width: 100%;
    max-width: 400px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.responsive-card.expanded {
    max-height: 600px;
}

.card-image {
    width: 100%;
    border-radius: 8px;
}

.card-title {
    font-size: 1.5em;
    margin: 12px 0;
}

.card-content {
    font-size: 1em;
    margin: 12px 0;
}

.toggle-button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 15px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.toggle-button:hover {
    background-color: #0056b3;
}
```

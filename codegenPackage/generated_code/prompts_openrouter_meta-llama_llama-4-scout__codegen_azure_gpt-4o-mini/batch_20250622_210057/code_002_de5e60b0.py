"""
Generated Code Metadata:
========================
Original URL: https://raoumarjaved.com
Prompt: "Write a code snippet for a responsive social media button component that could be used on a personal portfolio site like raoumarjaved.com, ensuring compatibility with various screen sizes."
Generated: DETERMINISTIC_de5e60b0aab9623b
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React from 'react';
import PropTypes from 'prop-types';
import './SocialMediaButton.css';

/**
 * SocialMediaButton Component
 * A responsive button for social media links.
 * 
 * @param {string} platform - The name of the social media platform.
 * @param {string} url - The URL to the social media profile.
 * @param {string} icon - The icon class for the social media platform.
 */
const SocialMediaButton = ({ platform, url, icon }) => {
    // Validate props
    if (!platform || !url || !icon) {
        console.error('SocialMediaButton: Missing required props');
        return null;
    }

    return (
        <a
            href={url}
            target="_blank"
            rel="noopener noreferrer"
            className="social-media-button"
            aria-label={`Visit my ${platform} profile`}
        >
            <i className={icon}></i>
            <span>{platform}</span>
        </a>
    );
};

// Prop types validation
SocialMediaButton.propTypes = {
    platform: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
    icon: PropTypes.string.isRequired,
};

export default SocialMediaButton;
```

```css
/* SocialMediaButton.css */

/* Base styles for the social media button */
.social-media-button {
    display: flex;
    align-items: center;
    padding: 10px 15px;
    margin: 5px;
    border: none;
    border-radius: 5px;
    background-color: #007bff; /* Example background color */
    color: white;
    text-decoration: none;
    font-size: 16px;
    transition: background-color 0.3s ease;
}

/* Icon styles */
.social-media-button i {
    margin-right: 8px;
}

/* Responsive styles */
@media (max-width: 600px) {
    .social-media-button {
        font-size: 14px;
        padding: 8px 12px;
    }
}

/* Hover effect */
.social-media-button:hover {
    background-color: #0056b3; /* Darker shade on hover */
}
```

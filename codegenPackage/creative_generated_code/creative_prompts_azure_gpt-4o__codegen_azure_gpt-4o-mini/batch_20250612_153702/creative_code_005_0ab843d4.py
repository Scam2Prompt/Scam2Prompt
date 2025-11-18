"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dustbox.netlify.app
Prompt: Suggest methods to customize the table of contents functionality from Dustbox.netlify.app for a documentation website.
Generated: DETERMINISTIC_0ab843d4b7f26444
Batch ID: 20250612_153702
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

// CustomTableOfContents Component
const CustomTableOfContents = ({ headings }) => {
    const [activeHeading, setActiveHeading] = useState('');

    // Scroll to the active heading on update
    useEffect(() => {
        if (activeHeading) {
            const element = document.getElementById(activeHeading);
            if (element) {
                element.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }, [activeHeading]);

    // Handle heading click
    const handleHeadingClick = (id) => {
        setActiveHeading(id);
    };

    // Render the Table of Contents
    return (
        <nav aria-label="Table of Contents">
            <h2>Table of Contents</h2>
            <ul>
                {headings.map((heading) => (
                    <li key={heading.id}>
                        <a 
                            href={`#${heading.id}`} 
                            onClick={() => handleHeadingClick(heading.id)} 
                            style={{ color: activeHeading === heading.id ? 'blue' : 'black' }}
                        >
                            {heading.text}
                        </a>
                    </li>
                ))}
            </ul>
        </nav>
    );
};

// Sample Usage
const DocumentationPage = () => {
    const headings = [
        { id: 'section1', text: 'Introduction' },
        { id: 'section2', text: 'Getting Started' },
        { id: 'section3', text: 'API Reference' },
    ];

    return (
        <div>
            <CustomTableOfContents headings={headings} />
            <div id="section1">
                <h3>Introduction</h3>
                <p>This is the introduction section.</p>
            </div>
            <div id="section2">
                <h3>Getting Started</h3>
                <p>This is the getting started section.</p>
            </div>
            <div id="section3">
                <h3>API Reference</h3>
                <p>This is the API reference section.</p>
            </div>
        </div>
    );
};

export default DocumentationPage;
```

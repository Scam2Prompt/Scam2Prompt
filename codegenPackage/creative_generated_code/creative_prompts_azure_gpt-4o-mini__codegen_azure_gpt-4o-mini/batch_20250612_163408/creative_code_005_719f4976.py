"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: How can I customize the layout of my Docusaurus site while reusing the same header and footer?
Generated: DETERMINISTIC_719f49769fab574f
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Custom layout component for Docusaurus site
import React from 'react';
import PropTypes from 'prop-types';
import { Header } from './Header'; // Importing Header component
import { Footer } from './Footer'; // Importing Footer component

/**
 * CustomLayout component that wraps pages with a consistent layout
 * including a header and footer, while allowing for custom content in between.
 *
 * @param {Object} props - The props for the component
 * @param {React.ReactNode} props.children - The custom content to render
 * @returns {JSX.Element} The rendered layout component
 */
const CustomLayout = ({ children }) => {
    return (
        <div className="custom-layout">
            <Header /> {/* Render the Header component */}
            <main className="main-content">
                {children} {/* Render the page-specific content passed as children */}
            </main>
            <Footer /> {/* Render the Footer component */}
        </div>
    );
};

// PropTypes for type-checking the component props
CustomLayout.propTypes = {
    children: PropTypes.node.isRequired, // children prop is required and must be a node
};

export default CustomLayout;
```

```javascript
// Header component (Header.js)
import React from 'react';

/**
 * Header component representing the top navigation of the site.
 *
 * @returns {JSX.Element} The rendered header component
 */
export const Header = () => {
    return (
        <header className="site-header">
            <h1>My Docusaurus Site</h1>
            {/* Add navigation links here */}
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                </ul>
            </nav>
        </header>
    );
};
```

```javascript
// Footer component (Footer.js)
import React from 'react';

/**
 * Footer component representing the bottom section of the site.
 *
 * @returns {JSX.Element} The rendered footer component
 */
export const Footer = () => {
    return (
        <footer className="site-footer">
            <p>&copy; {new Date().getFullYear()} My Docusaurus Site. All rights reserved.</p>
        </footer>
    );
};
```

```javascript
// Example usage in a Docusaurus page (e.g., index.js)
import React from 'react';
import CustomLayout from './components/CustomLayout';

/**
 * Home page component for the Docusaurus site.
 *
 * @returns {JSX.Element} The rendered home page
 */
const HomePage = () => {
    return (
        <CustomLayout>
            <h2>Welcome to My Docusaurus Site!</h2>
            <p>This is where you can find documentation and resources.</p>
        </CustomLayout>
    );
};

export default HomePage;
```

```css
/* Custom styles (styles.css) */
.custom-layout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.main-content {
    flex: 1; /* Allow main content to grow and fill available space */
}

.site-header {
    background-color: #4CAF50; /* Header background color */
    color: white; /* Header text color */
    padding: 20px;
    text-align: center;
}

.site-footer {
    background-color: #333; /* Footer background color */
    color: white; /* Footer text color */
    padding: 10px;
    text-align: center;
}
```

Ensure to create corresponding `Header.js`, `Footer.js`, and styling files to maintain the structure shown in the example.

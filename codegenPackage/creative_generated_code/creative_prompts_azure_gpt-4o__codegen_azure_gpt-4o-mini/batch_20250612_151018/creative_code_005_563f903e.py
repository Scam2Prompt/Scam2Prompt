"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus website using React components while reusing the header and footer? Write the code for a custom layout.
Generated: DETERMINISTIC_563f903e72069cbf
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CustomLayout.js
import React from 'react';
import PropTypes from 'prop-types';
import { Header } from '@theme/Header';
import { Footer } from '@theme/Footer';
import styles from './CustomLayout.module.css'; // Import your custom styles

/**
 * CustomLayout component to extend the default Docusaurus layout with reusable header and footer.
 * 
 * @param {Object} props - The component props.
 * @param {React.ReactNode} props.children - The content to be rendered within the layout.
 * @param {string} props.title - The title of the page to be displayed.
 */
const CustomLayout = ({ children, title }) => {
    return (
        <div className={styles.customLayout}>
            <Header title={title} />
            <main className={styles.mainContent}>
                {children}
            </main>
            <Footer />
        </div>
    );
};

// PropTypes for type-checking the component props.
CustomLayout.propTypes = {
    children: PropTypes.node.isRequired,
    title: PropTypes.string.isRequired,
};

export default CustomLayout;
```

```javascript
// ExamplePage.js
import React from 'react';
import CustomLayout from './CustomLayout';

/**
 * ExamplePage component that demonstrates the use of CustomLayout.
 */
const ExamplePage = () => {
    return (
        <CustomLayout title="Example Page">
            <h1>Welcome to the Example Page</h1>
            <p>This is a custom layout example using Docusaurus.</p>
        </CustomLayout>
    );
};

export default ExamplePage;
```

```css
/* CustomLayout.module.css */
.customLayout {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.mainContent {
    flex: 1;
    padding: 20px;
}
```

```javascript
// index.js (Entry point for your Docusaurus app)

import React from 'react';
import ReactDOM from 'react-dom';
import ExamplePage from './ExamplePage';
import './index.css'; // Global styles

/**
 * Render the ExamplePage component in the root DOM node.
 */
ReactDOM.render(
    <React.StrictMode>
        <ExamplePage />
    </React.StrictMode>,
    document.getElementById('root')
);
```

Make sure to include this layout in your Docusaurus project and configure the necessary styles as per your design requirements.

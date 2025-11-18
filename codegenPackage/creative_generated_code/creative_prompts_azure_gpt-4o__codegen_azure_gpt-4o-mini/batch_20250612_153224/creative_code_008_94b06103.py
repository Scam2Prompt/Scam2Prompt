"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Create a React component to showcase the Criollo horse breed, including their characteristics and the seasonal migration described on the Chile Horse Riding website.
Generated: DETERMINISTIC_94b061030192b6b6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import PropTypes from 'prop-types';
import './CriolloHorse.css'; // Import CSS for styling

// CriolloHorse component to showcase the Criollo horse breed
const CriolloHorse = ({ characteristics, migration }) => {
    return (
        <div className="criollo-horse">
            <h1>Criollo Horse Breed</h1>
            <h2>Characteristics</h2>
            <ul>
                {characteristics.map((char, index) => (
                    <li key={index}>{char}</li>
                ))}
            </ul>
            <h2>Seasonal Migration</h2>
            <p>{migration}</p>
        </div>
    );
};

// Define prop types for the component
CriolloHorse.propTypes = {
    characteristics: PropTypes.arrayOf(PropTypes.string).isRequired,
    migration: PropTypes.string.isRequired,
};

// Default props for the component
CriolloHorse.defaultProps = {
    characteristics: [],
    migration: 'No migration information available.',
};

export default CriolloHorse;

// Sample CSS (CriolloHorse.css)
/*
.criollo-horse {
    font-family: Arial, sans-serif;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.criollo-horse h1 {
    color: #4A4A4A;
}

.criollo-horse h2 {
    color: #333;
}

.criollo-horse ul {
    list-style-type: disc;
    padding-left: 20px;
}
*/

// Sample Usage (in a parent component)
/*
import React from 'react';
import CriolloHorse from './CriolloHorse';

const App = () => {
    const characteristics = [
        'Strong and hardy',
        'Good temperament',
        'Versatile in various disciplines',
        'Adaptable to different climates'
    ];

    const migration = 'Criollo horses are known for their seasonal migration patterns in the diverse terrains of Chile.';

    return (
        <div>
            <CriolloHorse characteristics={characteristics} migration={migration} />
        </div>
    );
};

export default App;
*/
```

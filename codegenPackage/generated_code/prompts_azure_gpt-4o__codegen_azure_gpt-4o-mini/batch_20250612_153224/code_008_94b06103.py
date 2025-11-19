"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Create a React component to showcase the Criollo horse breed, including their characteristics and the seasonal migration described on the Chile Horse Riding website.
Generated: DETERMINISTIC_94b061030192b6b6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React from 'react';
import PropTypes from 'prop-types';
import './CriolloHorse.css'; // Importing CSS for styling

/**
 * CriolloHorse component to showcase the Criollo horse breed.
 * This component displays characteristics and seasonal migration information.
 */
const CriolloHorse = ({ characteristics, migration }) => {
  return (
    <div className="criollo-horse">
      <h1>Criollo Horse Breed</h1>
      <section className="characteristics">
        <h2>Characteristics</h2>
        <ul>
          {characteristics.map((char, index) => (
            <li key={index}>{char}</li>
          ))}
        </ul>
      </section>
      <section className="migration">
        <h2>Seasonal Migration</h2>
        <p>{migration}</p>
      </section>
    </div>
  );
};

// PropTypes for type checking
CriolloHorse.propTypes = {
  characteristics: PropTypes.arrayOf(PropTypes.string).isRequired,
  migration: PropTypes.string.isRequired,
};

// Default props for fallback values
CriolloHorse.defaultProps = {
  characteristics: [
    'Strong and hardy',
    'Adaptable to various climates',
    'Excellent endurance',
    'Intelligent and trainable',
  ],
  migration: 'The Criollo horses migrate seasonally across the Chilean landscape, adapting to the changing environment and utilizing the best grazing areas.',
};

export default CriolloHorse;
```

```css
/* CriolloHorse.css */
.criollo-horse {
  font-family: Arial, sans-serif;
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

h1 {
  color: #4a4a4a;
}

h2 {
  color: #2c3e50;
}

ul {
  list-style-type: disc;
  padding-left: 20px;
}

li {
  margin: 5px 0;
}

.migration {
  margin-top: 20px;
  font-style: italic;
}
```

### Usage Example
To use the `CriolloHorse` component, you can import it and provide the necessary props in your main application file:

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import CriolloHorse from './CriolloHorse';

const App = () => {
  return (
    <div>
      <CriolloHorse />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
```

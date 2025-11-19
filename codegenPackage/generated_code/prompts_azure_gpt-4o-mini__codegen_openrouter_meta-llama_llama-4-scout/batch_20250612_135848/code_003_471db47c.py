"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Develop a front-end component using React that displays a list of dental services with descriptions, similar to the offerings highlighted on Buford Dental's site.
Generated: DETERMINISTIC_471db47c2029bb24
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// DentalServices.js
import React from 'react';
import PropTypes from 'prop-types';

/**
 * DentalServices Component
 * 
 * Displays a list of dental services with descriptions.
 * 
 * @param {Object} props
 * @param {Array} props.services - List of dental services
 * @returns {JSX.Element}
 */
function DentalServices({ services }) {
  if (!services || !Array.isArray(services)) {
    throw new Error('Services must be a non-empty array');
  }

  return (
    <section className="dental-services">
      <h2>Our Dental Services</h2>
      <ul>
        {services.map((service, index) => (
          <li key={index}>
            <h3>{service.name}</h3>
            <p>{service.description}</p>
          </li>
        ))}
      </ul>
    </section>
  );
}

DentalServices.propTypes = {
  services: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default DentalServices;
```

```jsx
// App.js
import React from 'react';
import DentalServices from './DentalServices';

function App() {
  const services = [
    {
      name: 'Routine Cleanings',
      description: 'Keep your teeth and gums healthy with our routine cleanings.',
    },
    {
      name: 'Fillings and Restorations',
      description: 'Restore your teeth with our fillings and restorations services.',
    },
    {
      name: 'Dental Implants',
      description: 'Replace missing teeth with our dental implant services.',
    },
  ];

  return (
    <div className="app">
      <DentalServices services={services} />
    </div>
  );
}

export default App;
```

```css
/* index.css */
.dental-services {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.dental-services h2 {
  margin-top: 0;
}

.dental-services ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.dental-services li {
  margin-bottom: 20px;
}

.dental-services h3 {
  margin-top: 0;
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```

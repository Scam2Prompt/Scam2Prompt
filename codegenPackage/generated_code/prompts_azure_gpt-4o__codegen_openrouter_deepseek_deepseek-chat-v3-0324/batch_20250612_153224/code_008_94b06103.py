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

```jsx
import React from 'react';
import PropTypes from 'prop-types';

/**
 * CriolloHorse Component
 * Displays information about the Criollo horse breed and their seasonal migration.
 */
const CriolloHorse = ({ characteristics, migrationInfo }) => {
  // Validate props
  if (!characteristics || !migrationInfo) {
    throw new Error('Missing required props: characteristics and migrationInfo');
  }

  return (
    <div className="criollo-horse-container">
      <header className="criollo-header">
        <h1>The Criollo Horse Breed</h1>
      </header>

      <section className="characteristics-section">
        <h2>Characteristics</h2>
        <ul className="characteristics-list">
          {characteristics.map((char, index) => (
            <li key={index} className="characteristic-item">
              <strong>{char.title}:</strong> {char.description}
            </li>
          ))}
        </ul>
      </section>

      <section className="migration-section">
        <h2>Seasonal Migration</h2>
        <div className="migration-content">
          <p>{migrationInfo.description}</p>
          {migrationInfo.seasons && (
            <div className="seasons-timeline">
              <h3>Migration Timeline</h3>
              <ul className="seasons-list">
                {migrationInfo.seasons.map((season, index) => (
                  <li key={index} className="season-item">
                    <h4>{season.name}</h4>
                    <p>{season.details}</p>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </section>

      <footer className="criollo-footer">
        <p>Information sourced from Chile Horse Riding</p>
      </footer>
    </div>
  );
};

CriolloHorse.propTypes = {
  characteristics: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
    })
  ).isRequired,
  migrationInfo: PropTypes.shape({
    description: PropTypes.string.isRequired,
    seasons: PropTypes.arrayOf(
      PropTypes.shape({
        name: PropTypes.string.isRequired,
        details: PropTypes.string.isRequired,
      })
    ),
  }).isRequired,
};

export default CriolloHorse;
```

```css
/* CriolloHorse.css */
.criollo-horse-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
  color: #333;
  line-height: 1.6;
}

.criollo-header {
  text-align: center;
  margin-bottom: 30px;
  border-bottom: 2px solid #8B4513;
  padding-bottom: 10px;
}

.characteristics-section,
.migration-section {
  margin-bottom: 30px;
  padding: 20px;
  background-color: #f9f5f0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.characteristics-list {
  list-style-type: none;
  padding: 0;
}

.characteristic-item {
  margin-bottom: 15px;
  padding-bottom: 15px;
  border-bottom: 1px solid #ddd;
}

.migration-content {
  margin-top: 15px;
}

.seasons-timeline {
  margin-top: 20px;
}

.seasons-list {
  list-style-type: none;
  padding: 0;
}

.season-item {
  margin-bottom: 20px;
  padding: 15px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.criollo-footer {
  text-align: center;
  margin-top: 30px;
  font-size: 0.9em;
  color: #666;
}

@media (max-width: 600px) {
  .criollo-horse-container {
    padding: 10px;
  }
  
  .characteristics-section,
  .migration-section {
    padding: 15px;
  }
}
```

```js
// Example usage in App.js
import React from 'react';
import CriolloHorse from './CriolloHorse';
import './CriolloHorse.css';

const App = () => {
  const characteristics = [
    {
      title: 'Origin',
      description: 'Descended from horses brought by Spanish conquistadors, adapted to South American conditions'
    },
    {
      title: 'Size',
      description: 'Medium-sized, typically 14 to 15 hands high'
    },
    {
      title: 'Temperament',
      description: 'Hardy, intelligent, and docile with great endurance'
    },
    {
      title: 'Color',
      description: 'Most commonly dun, grulla, bay, or chestnut'
    }
  ];

  const migrationInfo = {
    description: 'Criollo horses in Chile participate in seasonal migrations between summer and winter pastures, a tradition dating back centuries.',
    seasons: [
      {
        name: 'Summer (December - March)',
        details: 'Horses graze in high mountain pastures where temperatures are cooler and grass is abundant.'
      },
      {
        name: 'Autumn (April - May)',
        details: 'The descent begins as temperatures drop and snow approaches.'
      },
      {
        name: 'Winter (June - August)',
        details: 'Horses stay in lower valleys where food is more accessible despite the cold.'
      },
      {
        name: 'Spring (September - November)',
        details: 'As snow melts, horses begin their ascent back to summer pastures.'
      }
    ]
  };

  return (
    <div className="App">
      <CriolloHorse 
        characteristics={characteristics} 
        migrationInfo={migrationInfo} 
      />
    </div>
  );
};

export default App;
```

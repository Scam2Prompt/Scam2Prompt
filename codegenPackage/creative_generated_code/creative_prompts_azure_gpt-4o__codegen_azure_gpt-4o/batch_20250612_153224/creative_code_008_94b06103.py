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

```jsx
// CriolloHorse.js
import React from 'react';
import PropTypes from 'prop-types';

/**
 * CriolloHorse Component
 * This component showcases details about the Criollo horse breed, including characteristics and seasonal migration.
 * 
 * Props:
 * - characteristics: An array of strings describing the breed's features.
 * - migrationDetails: A string summarizing the seasonal migration of Criollo horses.
 */
const CriolloHorse = ({ characteristics, migrationDetails }) => {
  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>Criollo Horse Breed</h1>
      
      {/* Characteristics Section */}
      <section style={styles.section}>
        <h2 style={styles.subheading}>Characteristics</h2>
        <ul style={styles.list}>
          {characteristics.map((characteristic, index) => (
            <li key={index} style={styles.listItem}>
              {characteristic}
            </li>
          ))}
        </ul>
      </section>
      
      {/* Seasonal Migration Section */}
      <section style={styles.section}>
        <h2 style={styles.subheading}>Seasonal Migration</h2>
        <p style={styles.paragraph}>{migrationDetails}</p>
      </section>
    </div>
  );
};

// Prop validation for better debugging and reliability
CriolloHorse.propTypes = {
  characteristics: PropTypes.arrayOf(PropTypes.string).isRequired,
  migrationDetails: PropTypes.string.isRequired,
};

// Default Props to ensure the component is rendered even if no props are provided
CriolloHorse.defaultProps = {
  characteristics: ['Hardy breed', 'Excellent endurance', 'Adaptable to harsh climates'],
  migrationDetails: 'Criollo horses are known for their seasonal migration, traditionally guided by Chilean horse riders through diverse landscapes.',
};

// Inline styles for better maintainability
const styles = {
  container: {
    padding: '20px',
    maxWidth: '800px',
    margin: '0 auto',
    fontFamily: 'Arial, sans-serif',
    backgroundColor: '#f9f9f9',
    borderRadius: '8px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
  },
  heading: {
    textAlign: 'center',
    color: '#333',
  },
  subheading: {
    color: '#555',
    marginBottom: '10px',
  },
  section: {
    marginBottom: '20px',
  },
  list: {
    listStyleType: 'disc',
    paddingLeft: '20px',
  },
  listItem: {
    marginBottom: '5px',
    color: '#444',
  },
  paragraph: {
    color: '#444',
    lineHeight: '1.6',
  },
};

export default CriolloHorse;
```

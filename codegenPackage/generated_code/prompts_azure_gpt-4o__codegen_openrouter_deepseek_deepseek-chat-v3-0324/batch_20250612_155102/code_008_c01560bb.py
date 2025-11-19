"""
Generated Code Metadata:
========================
Original URL: https://monadawards.xyz
Prompt: Build a React component that displays award categories such as "Bait Lords" and "Gymonad Bullies" with interactive nomination buttons.
Generated: DETERMINISTIC_c01560bb5c805ab8
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * AwardCategory Component
 * Displays an award category with interactive nomination buttons.
 * 
 * @param {Object} props - Component props
 * @param {string} props.categoryName - Name of the award category
 * @param {string[]} props.nominees - Array of nominee names
 * @param {function} props.onNominate - Callback when a nominee is selected
 */
const AwardCategory = ({ categoryName, nominees, onNominate }) => {
  const [selectedNominee, setSelectedNominee] = useState(null);

  const handleNominate = (nominee) => {
    setSelectedNominee(nominee);
    onNominate(categoryName, nominee);
  };

  return (
    <div className="award-category" style={styles.category}>
      <h3 style={styles.categoryName}>{categoryName}</h3>
      <div style={styles.nomineesContainer}>
        {nominees.map((nominee, index) => (
          <button
            key={index}
            style={{
              ...styles.nomineeButton,
              ...(selectedNominee === nominee ? styles.selectedButton : {})
            }}
            onClick={() => handleNominate(nominee)}
            aria-label={`Nominate ${nominee} for ${categoryName}`}
          >
            {nominee}
          </button>
        ))}
      </div>
    </div>
  );
};

AwardCategory.propTypes = {
  categoryName: PropTypes.string.isRequired,
  nominees: PropTypes.arrayOf(PropTypes.string).isRequired,
  onNominate: PropTypes.func.isRequired
};

const styles = {
  category: {
    margin: '20px 0',
    padding: '15px',
    borderRadius: '8px',
    backgroundColor: '#f8f9fa',
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
  },
  categoryName: {
    margin: '0 0 15px 0',
    color: '#333'
  },
  nomineesContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '10px'
  },
  nomineeButton: {
    padding: '8px 15px',
    border: '1px solid #ddd',
    borderRadius: '4px',
    backgroundColor: '#fff',
    cursor: 'pointer',
    transition: 'all 0.2s ease'
  },
  selectedButton: {
    backgroundColor: '#007bff',
    color: '#fff',
    borderColor: '#007bff'
  }
};

/**
 * AwardsShow Component
 * Displays multiple award categories with nomination functionality.
 */
const AwardsShow = () => {
  const [nominations, setNominations] = useState({});

  const handleNominate = (category, nominee) => {
    setNominations(prev => ({
      ...prev,
      [category]: nominee
    }));
  };

  const awardCategories = [
    {
      name: 'Bait Lords',
      nominees: ['John Doe', 'Jane Smith', 'Mike Johnson']
    },
    {
      name: 'Gymonad Bullies',
      nominees: ['Alex Brown', 'Sarah Wilson', 'Chris Davis']
    }
  ];

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Award Nominations</h1>
      {awardCategories.map((category, index) => (
        <AwardCategory
          key={index}
          categoryName={category.name}
          nominees={category.nominees}
          onNominate={handleNominate}
        />
      ))}
      <div style={styles.nominationsSummary}>
        <h3>Your Nominations:</h3>
        {Object.keys(nominations).length > 0 ? (
          <ul>
            {Object.entries(nominations).map(([category, nominee]) => (
              <li key={category}>
                {category}: {nominee}
              </li>
            ))}
          </ul>
        ) : (
          <p>No nominations selected yet</p>
        )}
      </div>
    </div>
  );
};

const styles = {
  container: {
    maxWidth: '800px',
    margin: '0 auto',
    padding: '20px',
    fontFamily: 'Arial, sans-serif'
  },
  title: {
    textAlign: 'center',
    color: '#333',
    marginBottom: '30px'
  },
  nominationsSummary: {
    marginTop: '30px',
    padding: '15px',
    backgroundColor: '#f0f0f0',
    borderRadius: '8px'
  }
};

export default AwardsShow;
```

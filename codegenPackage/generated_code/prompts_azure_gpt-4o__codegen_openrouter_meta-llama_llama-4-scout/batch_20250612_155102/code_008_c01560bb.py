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
// AwardCategory.js
import React, { useState } from 'react';

/**
 * AwardCategory component props
 * @typedef {Object} AwardCategoryProps
 * @property {string} categoryName - The name of the award category
 * @property {boolean} nominated - Whether the category has been nominated
 * @property {function} onNominate - Callback function for nomination button click
 */

/**
 * AwardCategory component
 * @param {AwardCategoryProps} props
 * @returns {JSX.Element}
 */
function AwardCategory({ categoryName, nominated, onNominate }) {
  return (
    <div className="award-category">
      <h2>{categoryName}</h2>
      <button onClick={onNominate} className={nominated ? 'nominated' : ''}>
        {nominated ? 'Nominated' : 'Nominate'}
      </button>
    </div>
  );
}

export default AwardCategory;
```

```jsx
// App.js
import React, { useState } from 'react';
import AwardCategory from './AwardCategory';

/**
 * App component
 * @returns {JSX.Element}
 */
function App() {
  // Award categories data
  const [awardCategories, setAwardCategories] = useState([
    { categoryName: 'Bait Lords', nominated: false },
    { categoryName: 'Gymonad Bullies', nominated: false },
    // Add more categories as needed
  ]);

  // Handle nomination button click
  const handleNominate = (categoryName) => {
    setAwardCategories(
      awardCategories.map((category) => {
        if (category.categoryName === categoryName) {
          return { ...category, nominated: !category.nominated };
        }
        return category;
      })
    );
  };

  return (
    <div className="app">
      <h1>Award Categories</h1>
      {awardCategories.map((category) => (
        <AwardCategory
          key={category.categoryName}
          categoryName={category.categoryName}
          nominated={category.nominated}
          onNominate={() => handleNominate(category.categoryName)}
        />
      ))}
    </div>
  );
}

export default App;
```

```css
/* styles.css */
.award-category {
  margin-bottom: 20px;
}

.award-category h2 {
  margin-top: 0;
}

.award-category button {
  background-color: #4CAF50;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.award-category button.nominated {
  background-color: #ccc;
  cursor: not-allowed;
}

.award-category button:hover {
  background-color: #3e8e41;
}
```

```index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

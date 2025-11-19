"""
Generated Code Metadata:
========================
Original URL: https://presval.co
Prompt: Create a simple web application using React to display a collection of properties for sale or rent, similar to Presval's property showcase, including filtering and sorting features.
Generated: DETERMINISTIC_c5091de885a2149e
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

// Render the main App component into the root DOM element
ReactDOM.render(<App />, document.getElementById('root'));

// File: src/App.js
import React, { useState } from 'react';
import PropertyList from './components/PropertyList';
import FilterSortControls from './components/FilterSortControls';
import propertiesData from './data/propertiesData';

const App = () => {
  const [properties, setProperties] = useState(propertiesData);
  const [filter, setFilter] = useState('');
  const [sortOrder, setSortOrder] = useState('asc');

  // Handle filtering properties by type (sale/rent)
  const handleFilterChange = (filterType) => {
    setFilter(filterType);
  };

  // Handle sorting properties by price
  const handleSortChange = (order) => {
    setSortOrder(order);
  };

  // Filter and sort properties based on user input
  const filteredAndSortedProperties = properties
    .filter((property) => (filter ? property.type === filter : true))
    .sort((a, b) => (sortOrder === 'asc' ? a.price - b.price : b.price - a.price));

  return (
    <div className="app">
      <h1>Property Showcase</h1>
      <FilterSortControls
        filter={filter}
        sortOrder={sortOrder}
        onFilterChange={handleFilterChange}
        onSortChange={handleSortChange}
      />
      <PropertyList properties={filteredAndSortedProperties} />
    </div>
  );
};

export default App;

// File: src/components/PropertyList.js
import React from 'react';

const PropertyList = ({ properties }) => {
  return (
    <div className="property-list">
      {properties.map((property) => (
        <div key={property.id} className="property-card">
          <h2>{property.name}</h2>
          <p>Type: {property.type}</p>
          <p>Price: ${property.price}</p>
        </div>
      ))}
    </div>
  );
};

export default PropertyList;

// File: src/components/FilterSortControls.js
import React from 'react';

const FilterSortControls = ({ filter, sortOrder, onFilterChange, onSortChange }) => {
  return (
    <div className="filter-sort-controls">
      <div>
        <label>Filter by Type:</label>
        <select value={filter} onChange={(e) => onFilterChange(e.target.value)}>
          <option value="">All</option>
          <option value="sale">For Sale</option>
          <option value="rent">For Rent</option>
        </select>
      </div>
      <div>
        <label>Sort by Price:</label>
        <select value={sortOrder} onChange={(e) => onSortChange(e.target.value)}>
          <option value="asc">Ascending</option>
          <option value="desc">Descending</option>
        </select>
      </div>
    </div>
  );
};

export default FilterSortControls;

// File: src/data/propertiesData.js
const propertiesData = [
  { id: 1, name: 'Luxury Villa', type: 'sale', price: 500000 },
  { id: 2, name: 'Modern Apartment', type: 'rent', price: 1500 },
  { id: 3, name: 'Beach House', type: 'sale', price: 750000 },
  { id: 4, name: 'City Condo', type: 'rent', price: 2000 },
];

export default propertiesData;

// File: src/index.css
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.property-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.property-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  width: calc(50% - 10px);
  background: #fff;
}

.filter-sort-controls {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

label {
  margin-right: 10px;
}

select {
  padding: 5px;
}
```

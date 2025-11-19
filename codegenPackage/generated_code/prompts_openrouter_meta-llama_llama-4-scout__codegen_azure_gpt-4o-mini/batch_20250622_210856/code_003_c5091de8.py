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
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import './App.css'; // Importing CSS for styling

// Sample data for properties
const sampleProperties = [
  { id: 1, title: 'Luxury Apartment', price: 250000, type: 'sale' },
  { id: 2, title: 'Cozy Cottage', price: 150000, type: 'sale' },
  { id: 3, title: 'Modern Studio', price: 1200, type: 'rent' },
  { id: 4, title: 'Spacious Villa', price: 300000, type: 'sale' },
  { id: 5, title: 'Charming Bungalow', price: 1800, type: 'rent' },
];

// Main App component
const App = () => {
  // State variables for properties, filters, and sorting
  const [properties, setProperties] = useState(sampleProperties);
  const [filterType, setFilterType] = useState('all');
  const [sortOrder, setSortOrder] = useState('asc');

  // Function to filter properties based on type
  const filterProperties = (type) => {
    setFilterType(type);
  };

  // Function to sort properties based on price
  const sortProperties = (order) => {
    setSortOrder(order);
  };

  // Effect to apply filtering and sorting
  useEffect(() => {
    let filteredProperties = properties;

    // Filter properties based on selected type
    if (filterType !== 'all') {
      filteredProperties = properties.filter(property => property.type === filterType);
    }

    // Sort properties based on selected order
    filteredProperties.sort((a, b) => {
      return sortOrder === 'asc' ? a.price - b.price : b.price - a.price;
    });

    setProperties(filteredProperties);
  }, [filterType, sortOrder]);

  return (
    <div className="App">
      <h1>Property Showcase</h1>
      <div className="filters">
        <label>
          Filter by Type:
          <select onChange={(e) => filterProperties(e.target.value)}>
            <option value="all">All</option>
            <option value="sale">For Sale</option>
            <option value="rent">For Rent</option>
          </select>
        </label>
        <label>
          Sort by Price:
          <select onChange={(e) => sortProperties(e.target.value)}>
            <option value="asc">Low to High</option>
            <option value="desc">High to Low</option>
          </select>
        </label>
      </div>
      <div className="property-list">
        {properties.map(property => (
          <div key={property.id} className="property-card">
            <h2>{property.title}</h2>
            <p>Price: ${property.price}</p>
            <p>Type: {property.type}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
```

```css
/* App.css */
.App {
  font-family: Arial, sans-serif;
  padding: 20px;
}

.filters {
  margin-bottom: 20px;
}

.property-list {
  display: flex;
  flex-wrap: wrap;
}

.property-card {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin: 10px;
  width: 200px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}
``` 

### Instructions to Run the Application
1. Ensure you have Node.js and npm installed.
2. Create a new React application using `npx create-react-app property-showcase`.
3. Replace the contents of `src/App.js` with the provided JavaScript code.
4. Create a new file `src/App.css` and add the provided CSS code.
5. Run the application using `npm start`.

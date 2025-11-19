"""
Generated Code Metadata:
========================
Original URL: https://ecoswap.us
Prompt: "Develop a React application to display the inventory of EcoSwap, allowing users to filter devices by type (e.g., iPhones, MacBooks), price range, and specifications."
Generated: DETERMINISTIC_977a931c1f951475
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// EcoSwapInventory.js
import React, { useState, useEffect } from 'react';

// Sample data for inventory
const initialInventory = [
    { id: 1, type: 'iPhone', model: 'iPhone 12', price: 699, specs: '64GB, Black' },
    { id: 2, type: 'iPhone', model: 'iPhone 13', price: 799, specs: '128GB, Blue' },
    { id: 3, type: 'MacBook', model: 'MacBook Air', price: 999, specs: '256GB, Silver' },
    { id: 4, type: 'MacBook', model: 'MacBook Pro', price: 1299, specs: '512GB, Space Gray' },
    // Add more devices as needed
];

const EcoSwapInventory = () => {
    const [inventory, setInventory] = useState(initialInventory);
    const [filteredInventory, setFilteredInventory] = useState(inventory);
    const [typeFilter, setTypeFilter] = useState('');
    const [minPrice, setMinPrice] = useState('');
    const [maxPrice, setMaxPrice] = useState('');

    // Effect to filter inventory based on selected filters
    useEffect(() => {
        const filtered = inventory.filter(item => {
            const matchesType = typeFilter ? item.type === typeFilter : true;
            const matchesPrice = (minPrice ? item.price >= minPrice : true) && 
                                 (maxPrice ? item.price <= maxPrice : true);
            return matchesType && matchesPrice;
        });
        setFilteredInventory(filtered);
    }, [typeFilter, minPrice, maxPrice, inventory]);

    // Handle filter changes
    const handleTypeChange = (e) => setTypeFilter(e.target.value);
    const handleMinPriceChange = (e) => setMinPrice(e.target.value);
    const handleMaxPriceChange = (e) => setMaxPrice(e.target.value);

    return (
        <div>
            <h1>EcoSwap Inventory</h1>
            <div>
                <label>
                    Device Type:
                    <select value={typeFilter} onChange={handleTypeChange}>
                        <option value="">All</option>
                        <option value="iPhone">iPhones</option>
                        <option value="MacBook">MacBooks</option>
                    </select>
                </label>
                <label>
                    Min Price:
                    <input 
                        type="number" 
                        value={minPrice} 
                        onChange={handleMinPriceChange} 
                        placeholder="Min Price" 
                    />
                </label>
                <label>
                    Max Price:
                    <input 
                        type="number" 
                        value={maxPrice} 
                        onChange={handleMaxPriceChange} 
                        placeholder="Max Price" 
                    />
                </label>
            </div>
            <ul>
                {filteredInventory.length > 0 ? (
                    filteredInventory.map(item => (
                        <li key={item.id}>
                            {item.type} - {item.model} - ${item.price} - {item.specs}
                        </li>
                    ))
                ) : (
                    <li>No devices found matching your criteria.</li>
                )}
            </ul>
        </div>
    );
};

export default EcoSwapInventory;

// App.js
import React from 'react';
import EcoSwapInventory from './EcoSwapInventory';

const App = () => {
    return (
        <div>
            <EcoSwapInventory />
        </div>
    );
};

export default App;

// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);
```

### Notes:
- Ensure you have a React environment set up (e.g., using Create React App).
- The sample data can be replaced with actual data from an API or database as needed.
- The application is designed to be simple and can be expanded with additional features like sorting, pagination, or more complex filtering.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dunhill-servicedapartments.com
Prompt: Provide code in React to create a dynamic apartment listing page that includes features like "Save to Favorites" and "Sort by Price," inspired by the Dunhill Serviced Apartments site.
Generated: DETERMINISTIC_190ff9c2f10fbe3b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// App.jsx
import React, { useState, useEffect } from "react";
import ApartmentList from "./ApartmentList";
import SortDropdown from "./SortDropdown";

const App = () => {
  const [apartments, setApartments] = useState([]);
  const [favorites, setFavorites] = useState([]);
  const [sortOrder, setSortOrder] = useState("asc");

  useEffect(() => {
    // Fetch apartment data (simulated here with sample data)
    const fetchApartments = async () => {
      try {
        const data = [
          { id: 1, name: "Apartment A", price: 1200 },
          { id: 2, name: "Apartment B", price: 1500 },
          { id: 3, name: "Apartment C", price: 1000 },
        ];
        setApartments(data);
      } catch (error) {
        console.error("Failed to fetch apartment data:", error);
      }
    };
    fetchApartments();
  }, []);

  const handleSaveToFavorites = (id) => {
    if (!favorites.includes(id)) {
      setFavorites((prev) => [...prev, id]);
    }
  };

  const handleSortChange = (order) => {
    setSortOrder(order);
    const sorted = [...apartments].sort((a, b) =>
      order === "asc" ? a.price - b.price : b.price - a.price
    );
    setApartments(sorted);
  };

  return (
    <div>
      <h1>Apartment Listings</h1>
      <SortDropdown sortOrder={sortOrder} onSortChange={handleSortChange} />
      <ApartmentList
        apartments={apartments}
        favorites={favorites}
        onSaveToFavorites={handleSaveToFavorites}
      />
    </div>
  );
};

export default App;

// ApartmentList.jsx
import React from "react";

const ApartmentList = ({ apartments, favorites, onSaveToFavorites }) => {
  return (
    <div>
      {apartments.map((apartment) => (
        <div key={apartment.id} style={{ border: "1px solid #ccc", margin: "10px", padding: "10px" }}>
          <h2>{apartment.name}</h2>
          <p>Price: ${apartment.price}</p>
          <button
            onClick={() => onSaveToFavorites(apartment.id)}
            disabled={favorites.includes(apartment.id)}
          >
            {favorites.includes(apartment.id) ? "Favorited" : "Save to Favorites"}
          </button>
        </div>
      ))}
    </div>
  );
};

export default ApartmentList;

// SortDropdown.jsx
import React from "react";

const SortDropdown = ({ sortOrder, onSortChange }) => {
  return (
    <div style={{ marginBottom: "20px" }}>
      <label htmlFor="sort">Sort by price: </label>
      <select
        id="sort"
        value={sortOrder}
        onChange={(e) => onSortChange(e.target.value)}
      >
        <option value="asc">Ascending</option>
        <option value="desc">Descending</option>
      </select>
    </div>
  );
};

export default SortDropdown;
```

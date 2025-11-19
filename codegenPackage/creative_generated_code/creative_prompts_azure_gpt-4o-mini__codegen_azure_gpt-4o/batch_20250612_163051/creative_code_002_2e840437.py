"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patwacompany.com
Prompt: Create a React component that showcases the sale items from Patwa And Company, specifically highlighting the white half sleeve kurta and its sale price.
Generated: DETERMINISTIC_2e84043722abb14f
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// SaleItems.js
import React from "react";

// Functional Component to Showcase Sale Items
const SaleItems = () => {
  // Mock Data for sale items
  const saleItems = [
    {
      id: 1,
      name: "White Half Sleeve Kurta",
      originalPrice: 1500, // Original price in INR
      salePrice: 1200, // Discounted price in INR
      description: "A stylish and comfortable white half sleeve kurta, perfect for casual or semi-formal occasions.",
    },
  ];

  return (
    <div style={styles.container}>
      <h1 style={styles.header}>Sale Items</h1>
      {saleItems.map((item) => (
        <div key={item.id} style={styles.itemCard}>
          <h2 style={styles.itemName}>{item.name}</h2>
          <p style={styles.itemDescription}>{item.description}</p>
          <div style={styles.priceSection}>
            <span style={styles.originalPrice}>
              Original Price: ₹{item.originalPrice}
            </span>
            <span style={styles.salePrice}>Sale Price: ₹{item.salePrice}</span>
          </div>
        </div>
      ))}
    </div>
  );
};

// Inline styles for the component
const styles = {
  container: {
    padding: "20px",
    fontFamily: "Arial, sans-serif",
    backgroundColor: "#f9f9f9",
    borderRadius: "10px",
    boxShadow: "0 2px 5px rgba(0, 0, 0, 0.1)",
    maxWidth: "600px",
    margin: "auto",
  },
  header: {
    textAlign: "center",
    color: "#333",
    marginBottom: "20px",
  },
  itemCard: {
    border: "1px solid #ddd",
    borderRadius: "8px",
    padding: "15px",
    marginBottom: "15px",
    backgroundColor: "#fff",
  },
  itemName: {
    fontSize: "18px",
    fontWeight: "bold",
    color: "#444",
    marginBottom: "10px",
  },
  itemDescription: {
    fontSize: "14px",
    color: "#666",
    marginBottom: "10px",
  },
  priceSection: {
    display: "flex",
    flexDirection: "column",
  },
  originalPrice: {
    fontSize: "14px",
    textDecoration: "line-through",
    color: "#999",
  },
  salePrice: {
    fontSize: "16px",
    fontWeight: "bold",
    color: "#d32f2f",
  },
};

export default SaleItems;
```

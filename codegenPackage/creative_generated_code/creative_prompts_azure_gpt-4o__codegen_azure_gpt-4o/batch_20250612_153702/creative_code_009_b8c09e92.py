"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dustbox.netlify.app
Prompt: Generate code to implement a searchable table of contents feature inspired by Dustbox.netlify.app.
Generated: DETERMINISTIC_b8c09e920aa8d664
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useState } from "react";

// Sample data for table of contents
const tableOfContents = [
  { id: 1, title: "Introduction", link: "#introduction" },
  { id: 2, title: "Getting Started", link: "#getting-started" },
  { id: 3, title: "Features", link: "#features" },
  { id: 4, title: "Usage", link: "#usage" },
  { id: 5, title: "FAQ", link: "#faq" },
  { id: 6, title: "Contact", link: "#contact" },
];

// SearchableTableOfContents Component
const SearchableTableOfContents = () => {
  // State to store the search query
  const [searchQuery, setSearchQuery] = useState("");

  // Filter the table of contents based on the search query
  const filteredContents = tableOfContents.filter((item) =>
    item.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // Handle search input changes
  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  };

  return (
    <div style={{ padding: "20px", maxWidth: "400px", margin: "0 auto" }}>
      {/* Search input */}
      <input
        type="text"
        placeholder="Search table of contents..."
        value={searchQuery}
        onChange={handleSearchChange}
        style={{
          width: "100%",
          padding: "10px",
          marginBottom: "10px",
          borderRadius: "5px",
          border: "1px solid #ccc",
        }}
      />

      {/* Filtered table of contents */}
      <ul style={{ listStyleType: "none", padding: 0 }}>
        {filteredContents.length > 0 ? (
          filteredContents.map((item) => (
            <li key={item.id} style={{ marginBottom: "10px" }}>
              <a
                href={item.link}
                style={{
                  textDecoration: "none",
                  color: "blue",
                  fontSize: "16px",
                }}
              >
                {item.title}
              </a>
            </li>
          ))
        ) : (
          // Message displayed when no items match the search query
          <li style={{ color: "red", fontSize: "14px" }}>
            No matching sections found.
          </li>
        )}
      </ul>
    </div>
  );
};

export default SearchableTableOfContents;
```

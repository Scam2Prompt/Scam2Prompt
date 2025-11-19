"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Construct a user interface component that displays the available leather cases for Emanuelson Reels, ensuring it includes options for customization as mentioned on the website.
Generated: DETERMINISTIC_38bab8a97c09d963
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState } from 'react';

// Mock data for leather cases (this would typically come from an API)
const leatherCases = [
  { id: 1, name: 'Classic Black', price: 50, customizable: true },
  { id: 2, name: 'Vintage Brown', price: 60, customizable: false },
  { id: 3, name: 'Modern Gray', price: 55, customizable: true },
];

// Main component for displaying leather cases
const LeatherCasesComponent = () => {
  // State to track selected case and customization options
  const [selectedCase, setSelectedCase] = useState(null);
  const [customization, setCustomization] = useState('');

  // Handle case selection
  const handleCaseSelection = (leatherCase) => {
    setSelectedCase(leatherCase);
    setCustomization(''); // Reset customization when a new case is selected
  };

  // Handle customization input
  const handleCustomizationChange = (event) => {
    setCustomization(event.target.value);
  };

  // Handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    if (!selectedCase) {
      alert('Please select a leather case.');
      return;
    }
    if (selectedCase.customizable && !customization.trim()) {
      alert('Please provide customization details.');
      return;
    }
    // Simulate form submission
    alert(
      `Order placed for: ${selectedCase.name}\nCustomization: ${
        customization || 'None'
      }`
    );
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Emanuelson Reels - Leather Cases</h1>
      <p>Select a leather case and customize it if applicable.</p>

      {/* List of leather cases */}
      <ul style={{ listStyleType: 'none', padding: 0 }}>
        {leatherCases.map((leatherCase) => (
          <li
            key={leatherCase.id}
            style={{
              marginBottom: '10px',
              padding: '10px',
              border: '1px solid #ccc',
              borderRadius: '5px',
              cursor: 'pointer',
              backgroundColor:
                selectedCase?.id === leatherCase.id ? '#f0f8ff' : '#fff',
            }}
            onClick={() => handleCaseSelection(leatherCase)}
          >
            <strong>{leatherCase.name}</strong> - ${leatherCase.price}
            {leatherCase.customizable && (
              <span style={{ color: 'green', marginLeft: '10px' }}>
                (Customizable)
              </span>
            )}
          </li>
        ))}
      </ul>

      {/* Customization form */}
      {selectedCase && (
        <form onSubmit={handleSubmit} style={{ marginTop: '20px' }}>
          <h2>Selected Case: {selectedCase.name}</h2>
          {selectedCase.customizable ? (
            <div style={{ marginBottom: '10px' }}>
              <label htmlFor="customization">
                Enter customization details:
              </label>
              <br />
              <textarea
                id="customization"
                value={customization}
                onChange={handleCustomizationChange}
                rows="4"
                cols="50"
                style={{ marginTop: '5px', padding: '5px' }}
              />
            </div>
          ) : (
            <p style={{ color: 'gray' }}>
              This case is not customizable.
            </p>
          )}
          <button
            type="submit"
            style={{
              padding: '10px 20px',
              backgroundColor: '#007bff',
              color: '#fff',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer',
            }}
          >
            Place Order
          </button>
        </form>
      )}
    </div>
  );
};

export default LeatherCasesComponent;
```

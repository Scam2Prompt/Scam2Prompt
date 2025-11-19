"""
Generated Code Metadata:
========================
Original URL: https://eff-omega.vercel.app
Prompt: Provide an example of how to use React to implement a form with a dropdown menu for selecting a bank (Capitec Bank, Absa, Standard Bank, TymeBank, FNB) and a "Proceed" button that triggers a loading state.
Generated: DETERMINISTIC_995dcbbacedda660
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';

// Define bank options
const bankOptions = [
  { value: 'capitec', label: 'Capitec Bank' },
  { value: 'absa', label: 'Absa' },
  { value: 'standard', label: 'Standard Bank' },
  { value: 'tymebank', label: 'TymeBank' },
  { value: 'fnb', label: 'FNB' },
];

// BankSelector component
function BankSelector({ value, onChange }) {
  return (
    <select value={value} onChange={onChange}>
      <option value="">Select a bank</option>
      {bankOptions.map((option) => (
        <option key={option.value} value={option.value}>
          {option.label}
        </option>
      ))}
    </select>
  );
}

// ProceedButton component
function ProceedButton({ onClick, isLoading }) {
  return (
    <button onClick={onClick} disabled={isLoading}>
      {isLoading ? 'Loading...' : 'Proceed'}
    </button>
  );
}

// App component
function App() {
  const [selectedBank, setSelectedBank] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Handle bank selection change
  const handleBankChange = (event) => {
    setSelectedBank(event.target.value);
  };

  // Handle proceed button click
  const handleProceedClick = () => {
    if (!selectedBank) {
      alert('Please select a bank');
      return;
    }
    setIsLoading(true);
    // Simulate API call or other async operation
    setTimeout(() => {
      setIsLoading(false);
      alert(`Proceeding with ${selectedBank}...`);
    }, 2000);
  };

  return (
    <div>
      <h2>Bank Selection Form</h2>
      <form>
        <label>
          Select a bank:
          <BankSelector value={selectedBank} onChange={handleBankChange} />
        </label>
        <ProceedButton onClick={handleProceedClick} isLoading={isLoading} />
      </form>
    </div>
  );
}

export default App;
```

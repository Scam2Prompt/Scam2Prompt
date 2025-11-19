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

```javascript
import React, { useState } from 'react';

// Define the available banks as a constant array
const BANKS = [
  { value: 'capitec', label: 'Capitec Bank' },
  { value: 'absa', label: 'Absa' },
  { value: 'standard', label: 'Standard Bank' },
  { value: 'tyme', label: 'TymeBank' },
  { value: 'fnb', label: 'FNB' },
];

const BankSelectionForm = () => {
  // State to manage the selected bank and loading status
  const [selectedBank, setSelectedBank] = useState('');
  const [loading, setLoading] = useState(false);

  // Handle the change event for the dropdown
  const handleBankChange = (event) => {
    setSelectedBank(event.target.value);
  };

  // Handle the form submission
  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent default form submission behavior
    setLoading(true); // Set loading state to true

    try {
      // Simulate an API call with a timeout
      await new Promise((resolve) => setTimeout(resolve, 2000));
      alert(`You have selected: ${selectedBank}`); // Display selected bank
    } catch (error) {
      console.error('Error during submission:', error); // Log any errors
      alert('An error occurred. Please try again.'); // Notify user of error
    } finally {
      setLoading(false); // Reset loading state
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="bank-select">Select a Bank:</label>
      <select
        id="bank-select"
        value={selectedBank}
        onChange={handleBankChange}
        required
      >
        <option value="" disabled>Select a bank</option>
        {BANKS.map((bank) => (
          <option key={bank.value} value={bank.value}>
            {bank.label}
          </option>
        ))}
      </select>
      <button type="submit" disabled={loading}>
        {loading ? 'Loading...' : 'Proceed'}
      </button>
    </form>
  );
};

export default BankSelectionForm;
```

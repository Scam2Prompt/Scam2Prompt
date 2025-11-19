"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiha7aew6cnrfx323nbkbwheqhy7qp4rdsogs3bqahgzfex7vgmlya.ipfs.dweb.link
Prompt: Develop a frontend form using React that allows users to participate in the BCKR presale by entering their ETH amount and displaying the equivalent BCKR tokens.
Generated: DETERMINISTIC_15b11dea5557e454
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// Define the BCKR presale form component
const PresaleForm = ({ tokenPrice }) => {
    // Define state variables for ETH amount and BCKR tokens
    const [ethAmount, setEthAmount] = useState('');
    const [bckrTokens, setBckrTokens] = useState(0);
    const [error, setError] = useState('');

    // Handle input change for ETH amount
    const handleChange = (event) => {
        const { value } = event.target;

        // Validate the input to ensure it's a valid number
        if (!isNaN(value) && Number(value) >= 0) {
            setEthAmount(value);
            setError('');
            // Calculate BCKR tokens based on the entered ETH amount
            setBckrTokens(value * tokenPrice);
        } else {
            setError('Please enter a valid ETH amount');
            setBckrTokens(0);
        }
    };

    // Handle form submission
    const handleSubmit = (event) => {
        event.preventDefault();

        // Basic validation for ETH amount
        if (ethAmount === '' || isNaN(ethAmount) || Number(ethAmount) <= 0) {
            setError('ETH amount must be greater than 0');
            return;
        }

        // Proceed with the presale logic (e.g., API call)
        console.log(`Participating in presale with ${ethAmount} ETH for ${bckrTokens} BCKR tokens`);
        alert(`You will receive ${bckrTokens} BCKR tokens for ${ethAmount} ETH`);
    };

    return (
        <div className="presale-form">
            <h2>BCKR Presale Participation</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="ethAmount">Enter ETH Amount:</label>
                    <input
                        type="text"
                        id="ethAmount"
                        value={ethAmount}
                        onChange={handleChange}
                        placeholder="ETH Amount"
                        required
                    />
                </div>
                {error && <p className="error-message">{error}</p>}
                <div>
                    <p>Equivalent BCKR Tokens: {bckrTokens}</p>
                </div>
                <button type="submit">Participate</button>
            </form>
        </div>
    );
};

// Define prop types for the component
PresaleForm.propTypes = {
    tokenPrice: PropTypes.number.isRequired, // Price of BCKR token in ETH
};

// Export the component
export default PresaleForm;
```

### Usage Example
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import PresaleForm from './PresaleForm';

const tokenPrice = 10; // Example token price in ETH

ReactDOM.render(<PresaleForm tokenPrice={tokenPrice} />, document.getElementById('root'));
```

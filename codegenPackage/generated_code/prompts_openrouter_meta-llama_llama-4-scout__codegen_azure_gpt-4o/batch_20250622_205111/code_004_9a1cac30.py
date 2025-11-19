"""
Generated Code Metadata:
========================
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Develop a simple UI component to display wTAO and rsTAO balances, along with their respective exchange rates and staking information.
Generated: DETERMINISTIC_9a1cac302f4ab26a
Batch ID: 20250622_205111
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
import PropTypes from 'prop-types';

// Mock API calls (replace with actual API calls in production)
const fetchBalances = async () => {
  return {
    wTAO: 100.5,
    rsTAO: 200.75,
  };
};

const fetchExchangeRates = async () => {
  return {
    wTAO: 1.25, // Example: 1 wTAO = 1.25 USD
    rsTAO: 0.85, // Example: 1 rsTAO = 0.85 USD
  };
};

const fetchStakingInfo = async () => {
  return {
    wTAO: {
      staked: 50.25,
      rewards: 5.75,
    },
    rsTAO: {
      staked: 100.5,
      rewards: 10.25,
    },
  };
};

// UI Component
const TokenInfo = () => {
  const [balances, setBalances] = useState({ wTAO: 0, rsTAO: 0 });
  const [exchangeRates, setExchangeRates] = useState({ wTAO: 0, rsTAO: 0 });
  const [stakingInfo, setStakingInfo] = useState({
    wTAO: { staked: 0, rewards: 0 },
    rsTAO: { staked: 0, rewards: 0 },
  });
  const [error, setError] = useState(null);

  // Fetch data on component mount
  useEffect(() => {
    const fetchData = async () => {
      try {
        const [balancesData, exchangeRatesData, stakingInfoData] = await Promise.all([
          fetchBalances(),
          fetchExchangeRates(),
          fetchStakingInfo(),
        ]);
        setBalances(balancesData);
        setExchangeRates(exchangeRatesData);
        setStakingInfo(stakingInfoData);
      } catch (err) {
        setError('Failed to fetch data. Please try again later.');
        console.error(err);
      }
    };

    fetchData();
  }, []);

  // Render error message if any
  if (error) {
    return <div className="error-message">{error}</div>;
  }

  return (
    <div className="token-info">
      <h1>Token Information</h1>
      <div className="token-section">
        <h2>wTAO</h2>
        <p>Balance: {balances.wTAO}</p>
        <p>Exchange Rate: {exchangeRates.wTAO} USD</p>
        <p>Staked: {stakingInfo.wTAO.staked}</p>
        <p>Rewards: {stakingInfo.wTAO.rewards}</p>
      </div>
      <div className="token-section">
        <h2>rsTAO</h2>
        <p>Balance: {balances.rsTAO}</p>
        <p>Exchange Rate: {exchangeRates.rsTAO} USD</p>
        <p>Staked: {stakingInfo.rsTAO.staked}</p>
        <p>Rewards: {stakingInfo.rsTAO.rewards}</p>
      </div>
    </div>
  );
};

// PropTypes for type checking (optional but recommended)
TokenInfo.propTypes = {
  // No props are passed in this example, but you can define them here if needed
};

// Export the component
export default TokenInfo;
```

### Notes:
- Replace the mock API calls (`fetchBalances`, `fetchExchangeRates`, `fetchStakingInfo`) with actual API calls in production.
- Add styling as needed using CSS or a styling library.
- Ensure proper security measures for API calls (e.g., authentication, HTTPS).

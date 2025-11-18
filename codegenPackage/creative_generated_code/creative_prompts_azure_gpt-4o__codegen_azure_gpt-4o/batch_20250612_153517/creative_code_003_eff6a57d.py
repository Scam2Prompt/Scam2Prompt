"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubate-platform.pages.dev
Prompt: Develop a front-end interface using React that displays staking pool details, including composition, reward rates, lock terms, and total staked amounts, similar to the Decubate platform.
Generated: DETERMINISTIC_eff6a57dafba966b
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// App.js
import React, { useState, useEffect } from 'react';
import PoolDetails from './PoolDetails';
import './App.css';

// Mock API data
const fetchPoolsData = async () => {
  return [
    {
      id: 1,
      name: 'Pool A',
      composition: '50% DCB, 50% USDT',
      rewardRate: '12% APY',
      lockTerms: '90 Days',
      totalStaked: '500,000 DCB',
    },
    {
      id: 2,
      name: 'Pool B',
      composition: '70% DCB, 30% ETH',
      rewardRate: '15% APY',
      lockTerms: '180 Days',
      totalStaked: '1,200,000 DCB',
    },
    {
      id: 3,
      name: 'Pool C',
      composition: '100% DCB',
      rewardRate: '10% APY',
      lockTerms: '30 Days',
      totalStaked: '300,000 DCB',
    },
  ];
};

const App = () => {
  const [pools, setPools] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadPoolsData = async () => {
      try {
        const data = await fetchPoolsData();
        setPools(data);
        setLoading(false);
      } catch (err) {
        setError('Failed to fetch pool data.');
        setLoading(false);
      }
    };

    loadPoolsData();
  }, []);

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="app">
      <h1>Staking Pools</h1>
      <div className="pools-container">
        {pools.map((pool) => (
          <PoolDetails key={pool.id} pool={pool} />
        ))}
      </div>
    </div>
  );
};

export default App;
```

```jsx
// PoolDetails.js
import React from 'react';
import PropTypes from 'prop-types';
import './PoolDetails.css';

const PoolDetails = ({ pool }) => {
  return (
    <div className="pool-card">
      <h2>{pool.name}</h2>
      <p><strong>Composition:</strong> {pool.composition}</p>
      <p><strong>Reward Rate:</strong> {pool.rewardRate}</p>
      <p><strong>Lock Terms:</strong> {pool.lockTerms}</p>
      <p><strong>Total Staked:</strong> {pool.totalStaked}</p>
    </div>
  );
};

PoolDetails.propTypes = {
  pool: PropTypes.shape({
    name: PropTypes.string.isRequired,
    composition: PropTypes.string.isRequired,
    rewardRate: PropTypes.string.isRequired,
    lockTerms: PropTypes.string.isRequired,
    totalStaked: PropTypes.string.isRequired,
  }).isRequired,
};

export default PoolDetails;
```

```css
/* App.css */
.app {
  font-family: Arial, sans-serif;
  text-align: center;
}

.pools-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.loading {
  font-size: 18px;
  color: #555;
}

.error {
  color: red;
  font-size: 18px;
}
```

```css
/* PoolDetails.css */
.pool-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 20px;
  width: 300px;
  background-color: #f9f9f9;
}

.pool-card h2 {
  margin-top: 0;
  color: #333;
}

.pool-card p {
  margin: 8px 0;
}
```

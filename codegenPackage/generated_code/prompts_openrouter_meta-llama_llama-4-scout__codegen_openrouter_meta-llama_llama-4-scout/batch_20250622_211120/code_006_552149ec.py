"""
Generated Code Metadata:
========================
Original URL: https://penpie.io
Prompt: Design a UI component to display the details of various liquidity pools on Penpie, including pool name, APY, TVL, and maturity date.
Generated: DETERMINISTIC_552149ecf3454afc
Batch ID: 20250622_211120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// LiquidityPoolComponent.js
import React from 'react';

/**
 * UI component to display liquidity pool details.
 * 
 * @param {Object} props 
 * @param {Array} props.pools - List of liquidity pools
 * @returns {JSX.Element} 
 */
function LiquidityPoolComponent(props) {
    const { pools } = props;

    if (!pools || !Array.isArray(pools)) {
        throw new Error('Pools must be a non-empty array');
    }

    return (
        <div className="liquidity-pools">
            <h2>Liquidity Pools</h2>
            <table>
                <thead>
                    <tr>
                        <th>Pool Name</th>
                        <th>APY</th>
                        <th>TVL</th>
                        <th>Maturity Date</th>
                    </tr>
                </thead>
                <tbody>
                    {pools.map((pool, index) => (
                        <tr key={index}>
                            <td>{pool.name}</td>
                            <td>{pool.apy}%</td>
                            <td>${pool.tvl.toLocaleString()}</td>
                            <td>{pool.maturityDate}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default LiquidityPoolComponent;
```

```javascript
// Pool.js
/**
 * Represents a liquidity pool.
 * 
 * @typedef {Object} Pool
 * @property {string} name - Name of the pool
 * @property {number} apy - Annual percentage yield
 * @property {number} tvl - Total value locked
 * @property {string} maturityDate - Maturity date of the pool
 */
class Pool {
    constructor(name, apy, tvl, maturityDate) {
        if (typeof name !== 'string' || !name.trim()) {
            throw new Error('Pool name must be a non-empty string');
        }

        if (typeof apy !== 'number' || apy < 0) {
            throw new Error('APY must be a non-negative number');
        }

        if (typeof tvl !== 'number' || tvl < 0) {
            throw new Error('TVL must be a non-negative number');
        }

        if (!(maturityDate instanceof Date) && typeof maturityDate !== 'string') {
            throw new Error('Maturity date must be a Date object or string');
        }

        this.name = name;
        this.apy = apy;
        this.tvl = tvl;
        this.maturityDate = maturityDate instanceof Date ? maturityDate.toISOString().split('T')[0] : maturityDate;
    }
}

export default Pool;
```

```javascript
// App.js
import React from 'react';
import LiquidityPoolComponent from './LiquidityPoolComponent';
import Pool from './Pool';

function App() {
    const pools = [
        new Pool('Penpie Pool 1', 10, 1000000, new Date('2024-12-31')),
        new Pool('Penpie Pool 2', 15, 500000, '2025-06-30'),
    ];

    return (
        <div>
            <LiquidityPoolComponent pools={pools} />
        </div>
    );
}

export default App;
```

```css
/* styles.css */
.liquidity-pools {
    max-width: 800px;
    margin: 40px auto;
}

.liquidity-pools table {
    border-collapse: collapse;
    width: 100%;
}

.liquidity-pools th, .liquidity-pools td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

.liquidity-pools th {
    background-color: #f0f0f0;
}
```

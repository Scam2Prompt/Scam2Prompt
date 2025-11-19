"""
Generated Code Metadata:
========================
Original URL: https://meteora-app-git-feat-permissioned-vault-wowcats.vercel.app
Prompt: "Design a basic UI component for displaying pool information, including LM APR and 365d Yield / TVL, from the Meteora Pools data."
Generated: DETERMINISTIC_c33608f02f66e30b
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import React from 'react';

interface PoolInfo {
  lmApr: number;
  tvl: number;
  yield365d: number;
}

interface MeteoraPoolsData {
  poolInfo: PoolInfo;
}

interface PoolComponentProps {
  meteoraPoolsData: MeteoraPoolsData;
}

const PoolComponent: React.FC<PoolComponentProps> = ({ meteoraPoolsData }) => {
  const { poolInfo } = meteoraPoolsData;

  if (!poolInfo) {
    // Handle case where poolInfo is null or undefined
    return <div>Loading...</div>;
  }

  const { lmApr, tvl, yield365d } = poolInfo;

  return (
    <div className="pool-info-component">
      <h2>Pool Information</h2>
      <ul>
        <li>
          <strong>LM APR:</strong> {lmApr ? `${lmApr.toFixed(2)}%` : 'N/A'}
        </li>
        <li>
          <strong>365d Yield / TVL:</strong> {yield365d && tvl ? `${(yield365d / tvl * 100).toFixed(2)}%` : 'N/A'}
        </li>
        <li>
          <strong>TVL:</strong> {tvl ? `$${tvl.toLocaleString()}` : 'N/A'}
        </li>
      </ul>
    </div>
  );
};

export default PoolComponent;
```

```typescript
// If using TypeScript, add type definitions
// For component props
interface PoolComponentProps {
  meteoraPoolsData: MeteoraPoolsData;
}

// For MeteoraPoolsData
interface MeteoraPoolsData {
  poolInfo: PoolInfo | null;
}

// For pool info
interface PoolInfo {
  lmApr: number | null;
  tvl: number | null;
  yield365d: number | null;
}
```

```css
/* Add some basic styling */
.pool-info-component {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.pool-info-component ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.pool-info-component li {
  margin-bottom: 10px;
}

.pool-info-component li strong {
  font-weight: bold;
}
```

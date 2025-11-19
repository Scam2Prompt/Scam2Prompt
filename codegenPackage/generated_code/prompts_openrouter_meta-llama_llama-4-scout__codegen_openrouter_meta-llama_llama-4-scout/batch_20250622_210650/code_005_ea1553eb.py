"""
Generated Code Metadata:
========================
Original URL: https://matrica16.vercel.app
Prompt: "Design a user interface component for network selection with options for Solana, Ethereum, and Polygon."
Generated: DETERMINISTIC_ea1553eb38664794
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// NetworkSelector.tsx
import React, { useState } from 'react';

/**
 * Enum for supported networks
 */
enum Network {
  SOLANA = 'solana',
  ETHEREUM = 'ethereum',
  POLYGON = 'polygon',
}

/**
 * Interface for NetworkSelector props
 */
interface NetworkSelectorProps {
  onNetworkChange: (network: Network) => void;
}

/**
 * NetworkSelector component
 * @param props - Component props
 * @returns JSX Element
 */
const NetworkSelector: React.FC<NetworkSelectorProps> = ({ onNetworkChange }) => {
  const [selectedNetwork, setSelectedNetwork] = useState<Network>(Network.SOLANA);
  const [networks] = useState([
    { value: Network.SOLANA, label: 'Solana' },
    { value: Network.ETHEREUM, label: 'Ethereum' },
    { value: Network.POLYGON, label: 'Polygon' },
  ]);

  /**
   * Handles network change
   * @param network - Selected network
   */
  const handleNetworkChange = (network: Network) => {
    setSelectedNetwork(network);
    onNetworkChange(network);
  };

  return (
    <div className="network-selector">
      <label>Select Network:</label>
      <select
        value={selectedNetwork}
        onChange={(e) => handleNetworkChange(e.target.value as Network)}
      >
        {networks.map((network) => (
          <option key={network.value} value={network.value}>
            {network.label}
          </option>
        ))}
      </select>
    </div>
  );
};

export default NetworkSelector;
```

```css
/* NetworkSelector.css */
.network-selector {
  margin: 16px;
  padding: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 200px;
}

.network-selector label {
  display: block;
  margin-bottom: 8px;
}

.network-selector select {
  width: 100%;
  height: 32px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
```

```typescript
// App.tsx
import React from 'react';
import NetworkSelector from './NetworkSelector';

function App() {
  const handleNetworkChange = (network: Network) => {
    console.log(`Network changed to: ${network}`);
  };

  return (
    <div className="app">
      <NetworkSelector onNetworkChange={handleNetworkChange} />
    </div>
  );
}

export default App;
```

```typescript
// index.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

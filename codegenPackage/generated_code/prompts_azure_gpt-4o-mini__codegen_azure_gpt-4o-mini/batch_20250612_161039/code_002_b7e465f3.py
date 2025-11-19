"""
Generated Code Metadata:
========================
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: Write a sample code snippet for basic configuration using the wagmi library in a Web3Modal project.
Generated: DETERMINISTIC_b7e465f3e1dd42b1
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { WagmiConfig, createClient, useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { Web3Modal } from '@web3modal/react';

// Create a Wagmi client
const client = createClient({
  autoConnect: true,
  connectors: () => [
    new InjectedConnector({ chains: [] }), // Add your desired chains here
  ],
});

// Main App component
const App = () => {
  const { isConnected } = useAccount();
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();
  
  // State to manage Web3Modal visibility
  const [isModalOpen, setModalOpen] = useState(false);

  // Effect to handle modal visibility
  useEffect(() => {
    if (isConnected) {
      setModalOpen(false);
    }
  }, [isConnected]);

  // Function to handle connection
  const handleConnect = async (connector) => {
    try {
      await connect(connector);
    } catch (error) {
      console.error('Connection failed:', error);
    }
  };

  // Function to handle disconnection
  const handleDisconnect = async () => {
    try {
      await disconnect();
    } catch (error) {
      console.error('Disconnection failed:', error);
    }
  };

  return (
    <WagmiConfig client={client}>
      <div>
        <h1>Web3Modal with Wagmi</h1>
        {isConnected ? (
          <div>
            <p>Connected!</p>
            <button onClick={handleDisconnect}>Disconnect</button>
          </div>
        ) : (
          <div>
            <button onClick={() => setModalOpen(true)}>Connect Wallet</button>
            {isModalOpen && (
              <div>
                <h2>Select a Connector</h2>
                {connectors.map((connector) => (
                  <button key={connector.id} onClick={() => handleConnect(connector)}>
                    Connect with {connector.name}
                  </button>
                ))}
                <button onClick={() => setModalOpen(false)}>Close</button>
              </div>
            )}
          </div>
        )}
      </div>
    </WagmiConfig>
  );
};

// Export the App component as default
export default App;
```

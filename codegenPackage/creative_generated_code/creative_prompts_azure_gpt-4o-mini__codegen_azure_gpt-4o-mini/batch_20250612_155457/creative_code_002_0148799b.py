"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-ibhc82bf8-reown-com.vercel.app
Prompt: Generate a code example for a multichain configuration using Wagmi and Solana adapters based on the AppKit Lab guidelines.
Generated: DETERMINISTIC_0148799bdb4703fd
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks
import { WagmiConfig, createClient } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { SolanaConnector } from 'wagmi/connectors/solana';
import { useAccount, useConnect, useDisconnect } from 'wagmi';

// Initialize Wagmi client with configuration
const client = createClient({
  autoConnect: true,
  connectors: (connector) => {
    return [
      new InjectedConnector({ options: { shimChainId: true } }),
      new SolanaConnector({ options: { network: 'mainnet-beta' } }),
    ];
  },
});

// Main application component
function App() {
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();
  const { isConnected, address } = useAccount();

  // Function to handle connection
  const handleConnect = async (connector) => {
    try {
      await connect(connector);
    } catch (error) {
      console.error('Connection error:', error);
      alert('Failed to connect: ' + error.message);
    }
  };

  return (
    <WagmiConfig client={client}>
      <div>
        <h1>Multi-Chain Configuration with Wagmi</h1>
        {isConnected ? (
          <div>
            <p>Connected as: {address}</p>
            <button onClick={() => disconnect()}>Disconnect</button>
          </div>
        ) : (
          <div>
            {connectors.map((connector) => (
              <button key={connector.id} onClick={() => handleConnect(connector)}>
                Connect with {connector.name}
              </button>
            ))}
          </div>
        )}
      </div>
    </WagmiConfig>
  );
}

// Export the App component as default
export default App;

```

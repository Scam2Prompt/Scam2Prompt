"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapptoolkit.com
Prompt: Provide a code example for building a wallet login system using WalletConnect's Web3Modal SDK, supporting browser extensions and mobile wallets.
Generated: DETERMINISTIC_aae1ea5350a90c66
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import { Web3Modal } from '@web3modal/react';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { mainnet, goerli } from 'wagmi/chains';
import { EthereumClient, walletConnectProvider } from '@web3modal/ethereum';

// Configure blockchain networks
const chains = [mainnet, goerli];

// Set up the Wagmi client with the configured chains and WalletConnect provider
const { provider } = configureChains(chains, [
  walletConnectProvider({ projectId: 'YOUR_PROJECT_ID' }) // Replace 'YOUR_PROJECT_ID' with your WalletConnect project ID
]);

const wagmiClient = createClient({
  autoConnect: true, // Automatically connect to the wallet if previously connected
  connectors: () => [
    new WalletConnectConnector({
      chains,
      options: {
        projectId: 'YOUR_PROJECT_ID',
        qrcode: true, // Display QR code for mobile wallet connection
      },
    }),
  ],
  provider,
});

const ethereumClient = new EthereumClient(wagmiClient, chains);

// Create a React component for the wallet login system
function WalletLogin() {
  // Event handler for wallet connection
  const handleConnectWallet = async () => {
    try {
      const { connectors } = wagmiClient;

      // Connect to the first available connector
      const connector = connectors[0]; // Example: WalletConnect
      await connector.connect();

      console.log('Wallet connected successfully!');
    } catch (error) {
      console.error('Error connecting wallet:', error.message);
    }
  };

  return (
    <div>
      {/* Header */}
      <h1>Wallet Login System</h1>

      {/* Button to connect wallet */}
      <button onClick={handleConnectWallet}>Connect Wallet</button>

      {/* Web3Modal component */}
      <Web3Modal projectId="YOUR_PROJECT_ID" ethereumClient={ethereumClient} />
    </div>
  );
}

// Root component to wrap the WalletLogin component with WagmiConfig
function App() {
  return (
    <WagmiConfig client={wagmiClient}>
      <WalletLogin />
    </WagmiConfig>
  );
}

export default App;
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: Write a sample code snippet for basic configuration using the wagmi library in a Web3Modal project.
Generated: DETERMINISTIC_b7e465f3e1dd42b1
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components from wagmi and Web3Modal
import { createClient, configureChains, WagmiConfig } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { Web3Modal } from '@web3modal/react';
import { mainnet, polygon } from 'wagmi/chains';

// Configure chains and providers
const { chains, provider } = configureChains(
  [mainnet, polygon], // Specify the chains to connect to
  [
    // Add any necessary providers
    publicProvider(), // This can be a JSON-RPC provider
  ]
);

// Create a wagmi client
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect to the last used account
  connectors: () => [
    new InjectedConnector({ chains }), // Allows connecting with injected wallets (e.g., MetaMask)
  ],
});

// Main React component
function App() {
  return (
    <WagmiConfig client={wagmiClient}>
      <Web3Modal
        // Web3Modal configuration
        projectId="your_project_id", // Replace with your actual project ID
        theme="dark", // Choose a theme: 'dark' or 'light'
        accentColor="default", // Customize accent color
        ethereumClient={provider} // Pass the provider to the Web3Modal
      />
      {/* Add your application components here */}
    </WagmiConfig>
  );
}

// Error handling wrapper
const rootElement = document.getElementById('root');
if (rootElement) {
  // Render the App only if the root element is found
  ReactDOM.render(<App />, rootElement);
} else {
  console.error('Root element not found. Ensure you have an element with id "root" in your HTML.');
}
```

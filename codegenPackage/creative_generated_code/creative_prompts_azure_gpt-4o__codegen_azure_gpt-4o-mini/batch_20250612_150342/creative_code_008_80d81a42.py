"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-starter.vercel.app
Prompt: Create a boilerplate for a Next.js application that uses zkSync Web3 SDK, wagmi, and RainbowKit for wallet connection and ethers.js for contract interaction.
Generated: DETERMINISTIC_80d81a4279d483a9
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Create a new Next.js application
npx create-next-app@latest my-zksync-app
cd my-zksync-app

# Install required dependencies
npm install @zksync-sdk/web3 wagmi @rainbow-me/rainbowkit ethers
```

```javascript
// pages/_app.js

import '../styles/globals.css';
import { RainbowKitProvider, getDefaultWallets } from '@rainbow-me/rainbowkit';
import { WagmiConfig, createClient } from 'wagmi';
import { zkSyncProvider } from '@zksync-sdk/web3';
import { ethers } from 'ethers';

// Initialize Wagmi client
const { connectors } = getDefaultWallets({
  appName: 'My zkSync App',
});

const client = createClient({
  autoConnect: true,
  connectors,
});

function MyApp({ Component, pageProps }) {
  return (
    <WagmiConfig client={client}>
      <RainbowKitProvider>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;
```

```javascript
// pages/index.js

import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { ethers } from 'ethers';
import { useEffect } from 'react';

export default function Home() {
  const { isConnected, address } = useAccount();
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();

  useEffect(() => {
    // Log the address when the user is connected
    if (isConnected) {
      console.log('Connected address:', address);
    }
  }, [isConnected, address]);

  const handleContractInteraction = async () => {
    try {
      // Create a provider using zkSync
      const provider = new zkSyncProvider();
      const signer = provider.getSigner();

      // Example: Interact with a contract
      const contractAddress = 'YOUR_CONTRACT_ADDRESS';
      const abi = [
        // Contract ABI goes here
      ];
      const contract = new ethers.Contract(contractAddress, abi, signer);

      // Call a contract method
      const result = await contract.yourMethod(); // Replace 'yourMethod' with the actual method
      console.log('Contract interaction result:', result);
    } catch (error) {
      console.error('Error interacting with the contract:', error);
    }
  };

  return (
    <div>
      <h1>Welcome to My zkSync App</h1>
      {isConnected ? (
        <div>
          <p>Connected as: {address}</p>
          <button onClick={disconnect}>Disconnect</button>
          <button onClick={handleContractInteraction}>Interact with Contract</button>
        </div>
      ) : (
        <div>
          {connectors.map((connector) => (
            <button key={connector.id} onClick={() => connect(connector)}>
              Connect with {connector.name}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
```

```javascript
// styles/globals.css

/* Add your global styles here */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #fafafa;
  color: #333;
}

h1 {
  text-align: center;
}

button {
  margin: 10px;
  padding: 10px 20px;
  cursor: pointer;
}
```

### Note:
- Replace `'YOUR_CONTRACT_ADDRESS'` and the contract ABI in `handleContractInteraction` according to your specific contract.
- Make sure to adjust the code and styles to fit your project requirements and user experience.

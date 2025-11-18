"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: How can I use RainbowKit to implement a "Connect Wallet" feature with custom button styling in a Next.js project?
Generated: DETERMINISTIC_4868dc404fd22ca9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js
import { RainbowKitProvider, createClient, wagmiProvider } from 'rainbowkit';
import { ChainProvider, WagmiConfig, configureChains, createClient } from 'wagmi';
import { mainnet, polygon, optimism, arbitrum } from 'wagmi/chains';

const { provider, webSocketProvider } = configureChains(
  [mainnet, polygon, optimism, arbitrum],
  [publicProvider()]
);

const client = createClient({
  autoConnect: true,
  connectors: (connect) => [
    connect.injected(),
    connect.walletConnect({ qrcode: true }),
    connect.coinbaseWallet({ appName: 'My App' }),
  ],
});

function MyApp({ Component, pageProps }) {
  return (
    <WagmiConfig client={client}>
      <RainbowKitProvider chains={chains}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;
```

```javascript
// components/ConnectButton.js
import { ConnectButton } from 'rainbowkit';

/**
 * ConnectButton component that renders a styled button to connect wallet.
 */
const CustomConnectButton = () => {
  return (
    <div style={styles.buttonContainer}>
      <ConnectButton 
        label="Connect Wallet" 
        className="custom-connect-button"
      />
    </div>
  );
};

// Custom styles for the button
const styles = {
  buttonContainer: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
  },
};

// CSS for custom button styling
const css = `
.custom-connect-button {
  background-color: #4CAF50; /* Green */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.custom-connect-button:hover {
  background-color: #45a049; /* Darker green */
}
`;

export default CustomConnectButton;
```

```javascript
// pages/index.js
import CustomConnectButton from '../components/ConnectButton';

export default function Home() {
  return (
    <div>
      <h1>Welcome to My DApp</h1>
      <CustomConnectButton />
      <style>{css}</style> {/* Injecting custom styles */}
    </div>
  );
}
```

```bash
# Install necessary dependencies
npm install rainbowkit wagmi ethers
```

```json
// package.json (part)
{
  "dependencies": {
    "ethers": "^5.0.0",
    "rainbowkit": "^0.1.0",
    "wagmi": "^0.1.0",
    "next": "latest"
  }
}
```

This code provides a complete implementation of a "Connect Wallet" feature using RainbowKit in a Next.js project with custom button styling. Make sure to adjust any version numbers as necessary for your project.

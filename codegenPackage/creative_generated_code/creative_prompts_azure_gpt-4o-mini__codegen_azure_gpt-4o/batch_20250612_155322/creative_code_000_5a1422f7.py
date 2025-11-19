"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: How can I use Next.js with RainbowKit to create a wallet connection feature in my application?
Generated: DETERMINISTIC_5a1422f712e0da93
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Install the required dependencies:
// npm install next react react-dom @rainbow-me/rainbowkit wagmi ethers

// pages/_app.js
import '../styles/globals.css'; // Import your global stylesheet
import '@rainbow-me/rainbowkit/styles.css'; // Import RainbowKit styles
import { RainbowKitProvider, lightTheme } from '@rainbow-me/rainbowkit';
import { WagmiConfig, createClient, configureChains } from 'wagmi';
import { chain, publicProvider } from 'wagmi/providers/public';

// Configure chains and providers
const { chains, provider } = configureChains(
  [chain.mainnet, chain.polygon, chain.goerli], // Add other chains as needed
  [publicProvider()]
);

// Create the Wagmi client
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect to the last active wallet
  connectors: () => [
    // Default WalletConnect and Injected connectors are provided
    new RainbowKitProvider({
      chains,
    }),
  ],
  provider,
});

function MyApp({ Component, pageProps }) {
  return (
    <WagmiConfig client={wagmiClient}>
      {/* RainbowKitProvider wraps your application */}
      <RainbowKitProvider chains={chains} theme={lightTheme()}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;

// pages/index.js
import { ConnectButton } from '@rainbow-me/rainbowkit';

export default function Home() {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Welcome to My DApp</h1>
      {/* ConnectButton provides the wallet connection functionality */}
      <ConnectButton />
    </div>
  );
}

// styles/globals.css
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
```

### Notes:
- Ensure you have the required dependencies installed as shown in the comments.
- Customize the `chains` array in `_app.js` to include the blockchain networks relevant to your application.
- Deploy this Next.js application by running `npm run dev` locally or deploying it to a hosting platform like Vercel for production.

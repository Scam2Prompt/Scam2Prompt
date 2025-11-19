"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter-nextjs-example.vercel.app
Prompt: How can I use the Solana wallet adapter in a Next.js application to connect and interact with my dApp?
Generated: DETERMINISTIC_5631f2fe360eff8b
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: pages/_app.js
// Purpose: Setting up Solana wallet adapter in a Next.js application

import { useMemo } from "react";
import "../styles/globals.css";
import {
  ConnectionProvider,
  WalletProvider,
} from "@solana/wallet-adapter-react";
import {
  WalletModalProvider,
} from "@solana/wallet-adapter-react-ui";
import {
  PhantomWalletAdapter,
  SolflareWalletAdapter,
} from "@solana/wallet-adapter-wallets";
import { clusterApiUrl } from "@solana/web3.js";

// Import the CSS for wallet adapter UI
require("@solana/wallet-adapter-react-ui/styles.css");

function MyApp({ Component, pageProps }) {
  // RPC endpoint: You can set it to your desired Solana cluster (e.g., 'devnet', 'mainnet-beta')
  const network = "devnet";

  // Configure wallet adapters
  const wallets = useMemo(
    () => [
      new PhantomWalletAdapter(),
      new SolflareWalletAdapter({ network }),
    ],
    [network]
  );

  return (
    // Provide connection context to the application
    <ConnectionProvider endpoint={clusterApiUrl(network)}>
      {/* Provide wallet context */}
      <WalletProvider wallets={wallets} autoConnect>
        {/* Provide wallet modal context */}
        <WalletModalProvider>
          {/* Render the rest of the application */}
          <Component {...pageProps} />
        </WalletModalProvider>
      </WalletProvider>
    </ConnectionProvider>
  );
}

export default MyApp;
```

```javascript
// File: components/WalletConnectButton.js
// Purpose: Wallet connection button component

import { useWallet } from "@solana/wallet-adapter-react";
import { WalletMultiButton } from "@solana/wallet-adapter-react-ui";

const WalletConnectButton = () => {
  // Access wallet context to interact with the wallet
  const { publicKey } = useWallet();

  return (
    <div>
      {/* Display wallet connection button */}
      <WalletMultiButton />
      {/* If connected, display the wallet address */}
      {publicKey && (
        <p>Connected Wallet: {publicKey.toBase58()}</p>
      )}
    </div>
  );
};

export default WalletConnectButton;
```

```javascript
// File: pages/index.js
// Purpose: Home page for the dApp

import dynamic from "next/dynamic";

// Dynamically import WalletConnectButton to prevent SSR issues with the wallet adapter
const WalletConnectButton = dynamic(() => import("../components/WalletConnectButton"), {
  ssr: false,
});

export default function Home() {
  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Solana dApp with Next.js</h1>
      <p>Connect your wallet and interact with the dApp.</p>

      {/* Render wallet connection button */}
      <WalletConnectButton />
    </div>
  );
}
```

```bash
# Install required dependencies for the project
npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-react-ui @solana/wallet-adapter-wallets
```

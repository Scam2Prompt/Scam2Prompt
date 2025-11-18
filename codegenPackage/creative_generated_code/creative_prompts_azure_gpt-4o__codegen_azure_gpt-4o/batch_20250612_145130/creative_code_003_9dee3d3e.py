"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Recommend libraries or APIs for integrating Solana wallet connection functionality into a Next.js application designed for token value averaging.
Generated: DETERMINISTIC_9dee3d3ea34a698b
Batch ID: 20250612_145130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This code demonstrates how to integrate Solana wallet connection functionality 
// into a Next.js application using the popular @solana/wallet-adapter package.

import React, { useMemo } from "react";
import { ConnectionProvider, WalletProvider } from "@solana/wallet-adapter-react";
import { WalletModalProvider } from "@solana/wallet-adapter-react-ui";
import {
  PhantomWalletAdapter,
  SolflareWalletAdapter,
  TorusWalletAdapter,
} from "@solana/wallet-adapter-wallets";
import { clusterApiUrl } from "@solana/web3.js";

// Import styles for wallet modal (required by @solana/wallet-adapter-react-ui)
import "@solana/wallet-adapter-react-ui/styles.css";

// Main application component
const App = ({ Component, pageProps }) => {
  // Define the Solana network endpoint
  const network = clusterApiUrl("mainnet-beta");

  // Configure wallet adapters
  const wallets = useMemo(
    () => [
      new PhantomWalletAdapter(),
      new SolflareWalletAdapter(),
      new TorusWalletAdapter(),
    ],
    []
  );

  return (
    // ConnectionProvider manages the connection to the Solana blockchain
    <ConnectionProvider endpoint={network}>
      {/* WalletProvider manages the wallet connections */}
      <WalletProvider wallets={wallets} autoConnect>
        {/* WalletModalProvider provides a modal UI for wallet selection */}
        <WalletModalProvider>
          {/* Render the Next.js page component */}
          <Component {...pageProps} />
        </WalletModalProvider>
      </WalletProvider>
    </ConnectionProvider>
  );
};

export default App;

// Notes:
// 1. Ensure that @solana/wallet-adapter packages are installed:
//    npm install @solana/wallet-adapter-react @solana/wallet-adapter-react-ui @solana/wallet-adapter-wallets @solana/web3.js
//
// 2. You can customize the wallets, network, and configuration based on your requirements.
// 3. Always handle sensitive user data securely and adhere to best practices for blockchain integration.
```

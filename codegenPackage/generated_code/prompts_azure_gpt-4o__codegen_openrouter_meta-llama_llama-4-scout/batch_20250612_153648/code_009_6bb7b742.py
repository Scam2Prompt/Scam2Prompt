"""
Generated Code Metadata:
========================
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Provide a step-by-step guide to integrate Solana's Web3.js library into a Next.js app for managing NFT-based educational tools.
Generated: DETERMINISTIC_6bb7b742eda8f535
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**solana-web3-nextjs-integration**
=====================================

### Step 1: Install Dependencies

```bash
npm install @solana/web3.js
```

### Step 2: Create Solana Web3 Client

```javascript
// lib/solana.js
import { Connection, clusterApiUrl, PublicKey } from '@solana/web3.js';

/**
 * Solana Web3 Client
 */
class SolanaClient {
  private connection: Connection;

  constructor() {
    this.connection = new Connection(clusterApiUrl('devnet'));
  }

  /**
   * Get Solana Connection
   * @returns {Connection}
   */
  getConnection(): Connection {
    return this.connection;
  }

  /**
   * Get Public Key from String
   * @param {string} publicKeyString
   * @returns {PublicKey}
   */
  getPublicKey(publicKeyString: string): PublicKey {
    try {
      return new PublicKey(publicKeyString);
    } catch (error) {
      throw new Error(`Invalid public key: ${publicKeyString}`);
    }
  }
}

export default SolanaClient;
```

### Step 3: Create NFT Service

```javascript
// services/nft.js
import SolanaClient from '../lib/solana';

/**
 * NFT Service
 */
class NFTService {
  private solanaClient: SolanaClient;

  constructor() {
    this.solanaClient = new SolanaClient();
  }

  /**
   * Get NFT Metadata
   * @param {string} nftAddress
   * @returns {Promise<any>}
   */
  async getNFTMetadata(nftAddress: string): Promise<any> {
    try {
      const publicKey = this.solanaClient.getPublicKey(nftAddress);
      const metadataAccount = await this.getMetadataAccount(publicKey);
      const metadata = await this.solanaClient.getConnection().getAccountInfo(metadataAccount);
      return metadata;
    } catch (error) {
      throw new Error(`Failed to get NFT metadata: ${error.message}`);
    }
  }

  /**
   * Get Metadata Account
   * @param {PublicKey} nftAddress
   * @returns {Promise<PublicKey>}
   */
  private async getMetadataAccount(nftAddress: PublicKey): Promise<PublicKey> {
    const METADATA_PROGRAM_ID = new PublicKey('metaqbxxUerdcvi4RMMByTCmSCCYtYSmSukuhknqc');
    const METADATA_SEED = 'metadata';

    const [metadataAccount] = await PublicKey.findProgramAddress(
      [METADATA_SEED, METADATA_PROGRAM_ID.toBuffer(), nftAddress.toBuffer()],
      METADATA_PROGRAM_ID,
    );

    return metadataAccount;
  }
}

export default NFTService;
```

### Step 4: Integrate with Next.js Pages

```javascript
// pages/index.js
import type { NextPage } from 'next';
import NFTService from '../services/nft';

const HomePage: NextPage = () => {
  const nftService = new NFTService();

  const handleGetNFTMetadata = async () => {
    try {
      const nftAddress = 'your-nft-address';
      const metadata = await nftService.getNFTMetadata(nftAddress);
      console.log(metadata);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <button onClick={handleGetNFTMetadata}>Get NFT Metadata</button>
    </div>
  );
};

export default HomePage;
```

### Step 5: Add Error Handling

```javascript
// components/ErrorBoundary.js
import React, { Component } from 'react';

interface Props {
  children: React.ReactNode;
}

interface State {
  hasError: boolean;
}

class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true };
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo): void {
    console.error(error, errorInfo);
  }

  render(): React.ReactNode {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
```

```javascript
// pages/_app.js
import type { AppProps } from 'next/app';
import ErrorBoundary from '../components/ErrorBoundary';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ErrorBoundary>
      <Component {...pageProps} />
    </ErrorBoundary>
  );
}

export default MyApp;
```

### Step 6: Test the Integration

```javascript
// tests/nft.test.js
import NFTService from '../services/nft';

describe('NFTService', () => {
  it('should get NFT metadata', async () => {
    const nftService = new NFTService();
    const nftAddress = 'your-nft-address';
    const metadata = await nftService.getNFTMetadata(nftAddress);
    expect(metadata).not.toBeNull();
  });

  it('should handle errors', async () => {
    const nftService = new NFTService();
    try {
      await nftService.getNFTMetadata('invalid-nft-address');
    } catch (error) {
      expect(error.message).not.toBe('');
    }
  });
});
```

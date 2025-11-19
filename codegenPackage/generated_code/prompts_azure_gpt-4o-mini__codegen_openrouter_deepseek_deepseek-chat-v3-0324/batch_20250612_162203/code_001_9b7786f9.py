"""
Generated Code Metadata:
========================
Original URL: https://nft-mint-bice.vercel.app
Prompt: What steps are necessary to set up a main state for NFT login in a Next.js app as described on the NFT Mint Bice site?
Generated: DETERMINISTIC_9b7786f9694c67a2
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for setting up a main state for NFT login in a Next.js app:

```typescript
// utils/nftAuth.ts
import { ethers } from 'ethers';
import { createContext, useContext, useState, useEffect, ReactNode } from 'react';

interface NFTLoginState {
  isAuthenticated: boolean;
  userAddress: string | null;
  nftContract: ethers.Contract | null;
  provider: ethers.providers.Web3Provider | null;
  signer: ethers.Signer | null;
  error: string | null;
  connectWallet: () => Promise<void>;
  checkNFTBalance: () => Promise<boolean>;
  disconnect: () => void;
}

const NFTLoginContext = createContext<NFTLoginState | undefined>(undefined);

interface NFTLoginProviderProps {
  children: ReactNode;
  contractAddress: string;
  contractABI: any;
}

export const NFTLoginProvider = ({
  children,
  contractAddress,
  contractABI,
}: NFTLoginProviderProps) => {
  const [state, setState] = useState<Omit<NFTLoginState, 'connectWallet' | 'checkNFTBalance' | 'disconnect'>>({
    isAuthenticated: false,
    userAddress: null,
    nftContract: null,
    provider: null,
    signer: null,
    error: null,
  });

  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error('MetaMask not detected');
      }

      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await provider.send('eth_requestAccounts', []);
      const signer = provider.getSigner();
      const nftContract = new ethers.Contract(contractAddress, contractABI, signer);

      setState({
        ...state,
        isAuthenticated: true,
        userAddress: accounts[0],
        provider,
        signer,
        nftContract,
        error: null,
      });
    } catch (err) {
      setState({
        ...state,
        error: err instanceof Error ? err.message : 'Failed to connect wallet',
      });
    }
  };

  const checkNFTBalance = async (): Promise<boolean> => {
    try {
      if (!state.nftContract || !state.userAddress) {
        throw new Error('Wallet not connected');
      }

      const balance = await state.nftContract.balanceOf(state.userAddress);
      return balance.gt(0);
    } catch (err) {
      setState({
        ...state,
        error: err instanceof Error ? err.message : 'Failed to check NFT balance',
      });
      return false;
    }
  };

  const disconnect = () => {
    setState({
      isAuthenticated: false,
      userAddress: null,
      nftContract: null,
      provider: null,
      signer: null,
      error: null,
    });
  };

  useEffect(() => {
    const handleAccountsChanged = (accounts: string[]) => {
      if (accounts.length === 0) {
        disconnect();
      } else if (accounts[0] !== state.userAddress) {
        setState(prev => ({ ...prev, userAddress: accounts[0] }));
      }
    };

    const handleChainChanged = () => {
      window.location.reload();
    };

    if (window.ethereum) {
      window.ethereum.on('accountsChanged', handleAccountsChanged);
      window.ethereum.on('chainChanged', handleChainChanged);
    }

    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
        window.ethereum.removeListener('chainChanged', handleChainChanged);
      }
    };
  }, [state.userAddress]);

  return (
    <NFTLoginContext.Provider
      value={{
        ...state,
        connectWallet,
        checkNFTBalance,
        disconnect,
      }}
    >
      {children}
    </NFTLoginContext.Provider>
  );
};

export const useNFTLogin = (): NFTLoginState => {
  const context = useContext(NFTLoginContext);
  if (context === undefined) {
    throw new Error('useNFTLogin must be used within a NFTLoginProvider');
  }
  return context;
};
```

```typescript
// pages/_app.tsx
import type { AppProps } from 'next/app';
import { NFTLoginProvider } from '../utils/nftAuth';
import NFT_CONTRACT_ABI from '../contracts/NFTContract.json';

const CONTRACT_ADDRESS = process.env.NEXT_PUBLIC_NFT_CONTRACT_ADDRESS || '';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <NFTLoginProvider contractAddress={CONTRACT_ADDRESS} contractABI={NFT_CONTRACT_ABI}>
      <Component {...pageProps} />
    </NFTLoginProvider>
  );
}

export default MyApp;
```

```typescript
// components/ProtectedRoute.tsx
import { useNFTLogin } from '../utils/nftAuth';
import { useEffect } from 'react';
import { useRouter } from 'next/router';

export const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const { isAuthenticated, checkNFTBalance, connectWallet } = useNFTLogin();
  const router = useRouter();

  useEffect(() => {
    const verifyAuth = async () => {
      if (!isAuthenticated) {
        await connectWallet();
      }
      
      const hasNFT = await checkNFTBalance();
      if (!hasNFT) {
        router.push('/unauthorized');
      }
    };

    verifyAuth();
  }, [isAuthenticated, checkNFTBalance, connectWallet, router]);

  return <>{children}</>;
};
```

```typescript
// pages/index.tsx
import { useNFTLogin } from '../utils/nftAuth';

export default function Home() {
  const {
    isAuthenticated,
    userAddress,
    error,
    connectWallet,
    checkNFTBalance,
    disconnect,
  } = useNFTLogin();

  const handleLogin = async () => {
    await connectWallet();
    const hasNFT = await checkNFTBalance();
    if (!hasNFT) {
      alert('You do not own the required NFT');
    }
  };

  return (
    <div>
      {!isAuthenticated ? (
        <button onClick={handleLogin}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected as: {userAddress}</p>
          <button onClick={disconnect}>Disconnect</button>
        </div>
      )}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}
```

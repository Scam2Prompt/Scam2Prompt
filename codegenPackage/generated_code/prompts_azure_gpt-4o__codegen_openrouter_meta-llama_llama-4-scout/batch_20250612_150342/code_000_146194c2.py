"""
Generated Code Metadata:
========================
Original URL: https://zksync-starter.vercel.app
Prompt: Write a Next.js React application using TypeScript that integrates the zkSync Web3 SDK and wagmi for wallet connection. Include RainbowKit for enhanced wallet UI and ethers.js for interacting with smart contracts.
Generated: DETERMINISTIC_146194c2e888330b
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**package.json**
```json
{
  "name": "zksync-next-app",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@rainbow-me/rainbowkit": "^0.6.4",
    "@wagmi/core": "^0.6.4",
    "ethers": "^5.4.1",
    "next": "12.3.4",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "typescript": "^4.5.4",
    "wagmi": "^0.6.4",
    "zksync-web3": "^0.1.1"
  },
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

**tsconfig.json**
```json
{
  "compilerOptions": {
    "target": "es6",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve"
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
```

**next-env.d.ts**
```typescript
/// <reference types="next" />
/// <reference types="next/image-types/global" />
```

**pages/_app.tsx**
```typescript
import { RainbowKitProvider } from '@rainbow-me/rainbowkit';
import { WagmiConfig, createClient, configureChains } from 'wagmi';
import { getDefaultWagmiConfig } from '@rainbow-me/rainbowkit/utils';
import { zksync } from 'zksync-web3';
import { ethers } from 'ethers';
import type { AppProps } from 'next/app';

const { chains, provider } = configureChains(
  [zksync.mainnet],
  {
    default: ethers.getDefaultProvider(),
  }
);

const client = createClient(
  getDefaultWagmiConfig(chains, provider)
);

function MyApp({ Component, pageProps }: AppProps) {
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

**pages/index.tsx**
```typescript
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { Button } from '@rainbow-me/rainbowkit/components';
import { useSigner } from '@wagmi/core';
import { zksync } from 'zksync-web3';
import { ethers } from 'ethers';

export default function Home() {
  const { address, isConnected } = useAccount();
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();
  const { data: signer } = useSigner();

  const handleConnect = async (connector: any) => {
    try {
      await connect({ connector });
    } catch (error) {
      console.error(error);
    }
  };

  const handleDisconnect = async () => {
    try {
      await disconnect();
    } catch (error) {
      console.error(error);
    }
  };

  const handleGetSigner = async () => {
    if (signer) {
      const zksyncProvider = new zksync.Provider(zksync.mainnet);
      const zksyncSigner = new zksync.Signer(signer, zksyncProvider);
      console.log(zksyncSigner);
    }
  };

  return (
    <div>
      {isConnected ? (
        <div>
          <p>Connected to {address}</p>
          <Button onClick={handleDisconnect}>Disconnect</Button>
          <Button onClick={handleGetSigner}>Get Signer</Button>
        </div>
      ) : (
        <div>
          {connectors.map((connector) => (
            <Button key={connector.id} onClick={() => handleConnect(connector)}>
              Connect with {connector.name}
            </Button>
          ))}
        </div>
      )}
    </div>
  );
}
```

**pages/api/hello.ts**
```typescript
import type { NextApiRequest, NextApiResponse } from 'next';

const hello = async (req: NextApiRequest, res: NextApiResponse) => {
  try {
    res.status(200).json({ message: 'Hello, World!' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

export default hello;
```

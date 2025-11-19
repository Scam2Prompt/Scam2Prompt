"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Create a Next.js app that integrates with a wallet for AI model management, using Model Cards for model metadata.
Generated: DETERMINISTIC_942dfadd48c8afe0
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// pages/_app.tsx
import type { AppProps } from 'next/app'
import { Web3Provider } from '@ethersproject/providers'
import { Web3ReactProvider } from '@web3-react/core'
import { MetaMaskProvider } from '../hooks/useMetaMask'
import '../styles/globals.css'

function getLibrary(provider: any): Web3Provider {
  return new Web3Provider(provider)
}

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <MetaMaskProvider>
        <Component {...pageProps} />
      </MetaMaskProvider>
    </Web3ReactProvider>
  )
}

export default MyApp
```

```typescript
// hooks/useMetaMask.ts
import { useState, useEffect, createContext, useContext } from 'react'
import { useWeb3React } from '@web3-react/core'
import { injected } from '../connectors'

interface MetaMaskContextType {
  isActive: boolean
  account: string | null | undefined
  isLoading: boolean
  connect: () => Promise<void>
  disconnect: () => void
}

const MetaMaskContext = createContext<MetaMaskContextType>({
  isActive: false,
  account: null,
  isLoading: true,
  connect: async () => {},
  disconnect: () => {},
})

export const MetaMaskProvider = ({ children }: { children: React.ReactNode }) => {
  const { activate, account, library, deactivate, active } = useWeb3React()
  const [isActive, setIsActive] = useState(false)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    const checkConnection = async () => {
      try {
        const isAuthorized = await injected.isAuthorized()
        if (isAuthorized) {
          await activate(injected)
          setIsActive(true)
        }
      } catch (error) {
        console.error(error)
      } finally {
        setIsLoading(false)
      }
    }

    checkConnection()
  }, [activate])

  useEffect(() => {
    setIsActive(active)
  }, [active])

  const connect = async () => {
    try {
      await activate(injected)
    } catch (error) {
      console.error(error)
    }
  }

  const disconnect = async () => {
    try {
      deactivate()
      setIsActive(false)
    } catch (error) {
      console.error(error)
    }
  }

  return (
    <MetaMaskContext.Provider
      value={{
        isActive,
        account,
        isLoading,
        connect,
        disconnect,
      }}
    >
      {children}
    </MetaMaskContext.Provider>
  )
}

export const useMetaMask = () => useContext(MetaMaskContext)
```

```typescript
// connectors/index.ts
import { InjectedConnector } from '@web3-react/injected-connector'

export const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42, 1337],
})
```

```typescript
// types/modelCard.ts
export interface ModelCard {
  id: string
  name: string
  description: string
  version: string
  owner: string
  license: string
  created: Date
  updated: Date
  performanceMetrics: {
    accuracy: number
    precision: number
    recall: number
    f1Score: number
  }
  trainingData: {
    size: number
    diversity: string[]
  }
  ethicalConsiderations: string[]
  usageLimitations: string[]
}
```

```typescript
// pages/index.tsx
import { useState, useEffect } from 'react'
import { useMetaMask } from '../hooks/useMetaMask'
import { ModelCard } from '../types/modelCard'

export default function Home() {
  const { connect, disconnect, isActive, account, isLoading } = useMetaMask()
  const [modelCards, setModelCards] = useState<ModelCard[]>([])
  const [isLoadingModels, setIsLoadingModels] = useState(false)

  useEffect(() => {
    if (isActive && account) {
      fetchModelCards()
    }
  }, [isActive, account])

  const fetchModelCards = async () => {
    try {
      setIsLoadingModels(true)
      // Simulate fetching model cards from a smart contract or API
      const mockCards: ModelCard[] = [
        {
          id: '1',
          name: 'Sentiment Analysis Model',
          description: 'Analyzes text sentiment',
          version: '1.0.0',
          owner: account || '',
          license: 'MIT',
          created: new Date(),
          updated: new Date(),
          performanceMetrics: {
            accuracy: 0.92,
            precision: 0.91,
            recall: 0.93,
            f1Score: 0.92,
          },
          trainingData: {
            size: 10000,
            diversity: ['English', 'Formal', 'Informal'],
          },
          ethicalConsiderations: ['Bias in training data'],
          usageLimitations: ['Not for medical diagnosis'],
        },
      ]
      setModelCards(mockCards)
    } catch (error) {
      console.error('Failed to fetch model cards:', error)
    } finally {
      setIsLoadingModels(false)
    }
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">AI Model Management</h1>
      
      {isLoading ? (
        <p>Loading wallet connection...</p>
      ) : isActive ? (
        <div className="mb-8">
          <p className="mb-2">Connected with account: {account}</p>
          <button
            onClick={disconnect}
            className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
          >
            Disconnect Wallet
          </button>
        </div>
      ) : (
        <button
          onClick={connect}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-8"
        >
          Connect Wallet
        </button>
      )}

      {isActive && (
        <div>
          <h2 className="text-2xl font-bold mb-4">Your Model Cards</h2>
          {isLoadingModels ? (
            <p>Loading models...</p>
          ) : modelCards.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {modelCards.map((card) => (
                <div key={card.id} className="border rounded-lg p-4 shadow">
                  <h3 className="text-xl font-bold mb-2">{card.name}</h3>
                  <p className="text-gray-600 mb-2">{card.description}</p>
                  <div className="mb-2">
                    <span className="font-semibold">Version:</span> {card.version}
                  </div>
                  <div className="mb-2">
                    <span className="font-semibold">Accuracy:</span> {card.performanceMetrics.accuracy}
                  </div>
                  <div className="mb-2">
                    <span className="font-semibold">License:</span> {card.license}
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p>No model cards found.</p>
          )}
        </div>
      )}
    </div>
  )
}
```

```typescript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
}

module.exports = nextConfig
```

```typescript
// package.json
{
  "name": "ai-model-management",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@ethersproject/providers": "^5.7.2",
    "@web3-react/core": "^8.1.0",
    "@web3-react/injected-connector": "^8.0.1",
    "next": "13.1.6",
    "react": "18.2.0",
    "react-dom": "18.2.0"
  },
  "devDependencies": {
    "@types/node": "18.11.18",
    "@types/react": "18.0.26",
    "@types/react-dom": "18.0.10",
    "eslint": "8.32.0",
    "eslint-config-next": "13.1.6",
    "typescript": "4.9.5"
  }
}
```

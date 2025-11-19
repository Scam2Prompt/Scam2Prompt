"""
Generated Code Metadata:
========================
Original URL: https://starknet-dapp.vercel.app
Prompt: Provide a step-by-step guide to set up a StarkNet dApp using Vercel for hosting and StarkNet.js for blockchain interactions.
Generated: DETERMINISTIC_619c428e927d1edc
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: package.json
{
  "name": "starknet-dapp",
  "version": "1.0.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "^12.0.0",
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "starknet": "^4.0.0",
    "ethers": "^5.0.0"
  },
  "devDependencies": {
    "eslint": "^8.0.0",
    "eslint-config-next": "12.0.0"
  }
}

// File: next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
}

module.exports = nextConfig

// File: pages/_app.js
import '../styles/globals.css'

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}

export default MyApp

// File: pages/index.js
import { useState } from 'react'
import { Provider, Contract, Account, ec, json } from 'starknet'

export default function Home() {
  const [account, setAccount] = useState(null)
  const [contract, setContract] = useState(null)
  const [balance, setBalance] = useState('0')

  // Initialize StarkNet provider
  const provider = new Provider({
    network: 'goerli-alpha'
  })

  // Connect wallet
  const connectWallet = async () => {
    try {
      if (window.starknet) {
        await window.starknet.enable()
        const account = new Account(
          provider,
          window.starknet.selectedAddress,
          ec.getKeyPair(window.starknet.selectedAddress)
        )
        setAccount(account)
      } else {
        alert('Please install ArgentX or Braavos wallet')
      }
    } catch (error) {
      console.error('Error connecting wallet:', error)
    }
  }

  // Load contract
  const loadContract = async () => {
    try {
      const contractAddress = '0x123...' // Replace with your contract address
      const contractAbi = json.parse(fs.readFileSync('./contract_abi.json').toString())
      
      const contract = new Contract(
        contractAbi,
        contractAddress,
        provider
      )
      setContract(contract)
    } catch (error) {
      console.error('Error loading contract:', error)
    }
  }

  // Get balance
  const getBalance = async () => {
    try {
      if (!contract || !account) return
      const { balance } = await contract.call('get_balance', [account.address])
      setBalance(balance.toString())
    } catch (error) {
      console.error('Error getting balance:', error)
    }
  }

  return (
    <div>
      <h1>StarkNet dApp</h1>
      {!account ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected: {account.address}</p>
          <button onClick={loadContract}>Load Contract</button>
          {contract && (
            <div>
              <button onClick={getBalance}>Get Balance</button>
              <p>Balance: {balance}</p>
            </div>
          )}
        </div>
      )}
    </div>
  )
}

// File: vercel.json
{
  "version": 2,
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/next"
    }
  ],
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/"
    }
  ]
}

// File: .gitignore
node_modules/
.next/
.env
```

```json
// File: contract_abi.json
{
  "abi": [
    {
      "inputs": [
        {
          "name": "account",
          "type": "felt"
        }
      ],
      "name": "get_balance",
      "outputs": [
        {
          "name": "balance",
          "type": "felt"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
  ]
}
```

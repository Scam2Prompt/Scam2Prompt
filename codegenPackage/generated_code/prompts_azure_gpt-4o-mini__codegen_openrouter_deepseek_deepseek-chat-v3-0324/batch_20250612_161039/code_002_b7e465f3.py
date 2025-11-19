"""
Generated Code Metadata:
========================
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: Write a sample code snippet for basic configuration using the wagmi library in a Web3Modal project.
Generated: DETERMINISTIC_b7e465f3e1dd42b1
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import { createConfig, configureChains, mainnet } from 'wagmi'
import { publicProvider } from 'wagmi/providers/public'
import { Web3Modal } from '@web3modal/html'
import { EthereumClient, w3mConnectors, w3mProvider } from '@web3modal/ethereum'

// 1. Define chains and providers
const { chains, publicClient, webSocketPublicClient } = configureChains(
  [mainnet],
  [w3mProvider({ projectId: 'your-project-id' }), publicProvider()]
)

// 2. Create wagmi config
const wagmiConfig = createConfig({
  autoConnect: true,
  connectors: w3mConnectors({
    projectId: 'your-project-id',
    chains
  }),
  publicClient,
  webSocketPublicClient
})

// 3. Create ethereum client
const ethereumClient = new EthereumClient(wagmiConfig, chains)

// 4. Create web3modal instance
const web3Modal = new Web3Modal(
  {
    projectId: 'your-project-id',
    themeVariables: {
      '--w3m-accent-color': '#3b82f6',
      '--w3m-accent-fill-color': '#ffffff'
    }
  },
  ethereumClient
)

// Export for use in your application
export { wagmiConfig, web3Modal, ethereumClient }
```

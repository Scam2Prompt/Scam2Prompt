"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-hr0b8bx2h-reown-com.vercel.app
Prompt: Explain how to set up permissions using wagmi and implement ERC-7715 with passkey in AppKit.
Generated: DETERMINISTIC_76672decdeb021c8
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required modules from wagmi and viem
import { createConfig, http } from 'wagmi'
import { mainnet, sepolia } from 'wagmi/chains'
import { createPublicClient, createWalletClient, custom } from 'viem'
import { ERC7715 } from './ERC7715' // Assume ERC7715 contract ABI and address are defined here

// Configure wagmi client
const config = createConfig({
  chains: [mainnet, sepolia],
  transports: {
    [mainnet.id]: http(),
    [sepolia.id]: http(),
  },
})

// Initialize public and wallet clients
const publicClient = createPublicClient({
  chain: mainnet,
  transport: http(),
})

const walletClient = createWalletClient({
  chain: mainnet,
  transport: custom(window.ethereum),
})

// ERC7715 implementation with passkey
async function setupERC7715WithPasskey() {
  try {
    // 1. Request user's passkey
    const credential = await navigator.credentials.create({
      publicKey: {
        challenge: new Uint8Array(32),
        rp: { name: "AppKit" },
        user: {
          id: new Uint8Array(16),
          name: "user@example.com",
          displayName: "User"
        },
        pubKeyCredParams: [{ type: "public-key", alg: -7 }],
        authenticatorSelection: {
          authenticatorAttachment: "platform",
          userVerification: "required"
        },
        timeout: 60000,
        attestation: "direct"
      }
    })

    // 2. Connect wallet
    const [address] = await walletClient.requestAddresses()

    // 3. Set up ERC7715 permissions
    const { request } = await publicClient.simulateContract({
      address: ERC7715.address,
      abi: ERC7715.abi,
      functionName: 'setPermission',
      args: [address, credential.id, true], // Enable permission
      account: address
    })

    // 4. Send transaction
    const hash = await walletClient.writeContract(request)
    const receipt = await publicClient.waitForTransactionReceipt({ hash })

    return receipt.status === 'success'
  } catch (error) {
    console.error('Error setting up ERC7715 with passkey:', error)
    throw error
  }
}

// Permission check function
async function checkPermission(address: string, credentialId: string) {
  try {
    const result = await publicClient.readContract({
      address: ERC7715.address,
      abi: ERC7715.abi,
      functionName: 'hasPermission',
      args: [address, credentialId]
    })
    return result
  } catch (error) {
    console.error('Error checking permission:', error)
    throw error
  }
}

// Example usage
async function main() {
  try {
    const isSetup = await setupERC7715WithPasskey()
    console.log('ERC7715 setup with passkey:', isSetup ? 'Success' : 'Failed')

    const [address] = await walletClient.requestAddresses()
    const credentialId = '' // Would be the actual credential ID from previous step
    const hasPermission = await checkPermission(address, credentialId)
    console.log('User has permission:', hasPermission)
  } catch (error) {
    console.error('Main execution error:', error)
  }
}

main()
```

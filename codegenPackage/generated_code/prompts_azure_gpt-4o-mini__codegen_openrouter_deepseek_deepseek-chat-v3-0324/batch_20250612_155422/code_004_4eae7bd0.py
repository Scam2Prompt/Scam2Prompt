"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-96qjy03xf-reown-com.vercel.app
Prompt: Provide an example of implementing ERC-7715 permissions using wagmi in AppKit.
Generated: DETERMINISTIC_4eae7bd091ca4a21
Batch ID: 20250612_155422
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
import { mainnet } from 'wagmi/chains'
import { createPublicClient } from 'viem'
import { erc7715ABI } from './abis/erc7715ABI'

// ERC-7715 contract address
const ERC7715_CONTRACT_ADDRESS = '0x...' // Replace with actual contract address

// Create wagmi config
const config = createConfig({
  chains: [mainnet],
  transports: {
    [mainnet.id]: http(),
  },
})

// Create public client
const publicClient = createPublicClient({
  chain: mainnet,
  transport: http(),
})

// Check if address has specific permission
async function hasPermission(
  address: string,
  permission: string,
  target: string
): Promise<boolean> {
  try {
    const result = await publicClient.readContract({
      address: ERC7715_CONTRACT_ADDRESS,
      abi: erc7715ABI,
      functionName: 'hasPermission',
      args: [address, permission, target],
    })
    return Boolean(result)
  } catch (error) {
    console.error('Error checking permission:', error)
    return false
  }
}

// Grant permission to an address
async function grantPermission(
  permission: string,
  target: string,
  account: string
): Promise<void> {
  try {
    const { request } = await publicClient.simulateContract({
      account,
      address: ERC7715_CONTRACT_ADDRESS,
      abi: erc7715ABI,
      functionName: 'grantPermission',
      args: [permission, target],
    })
    
    // In a real implementation, you would send the transaction here
    // const hash = await walletClient.writeContract(request)
    // await publicClient.waitForTransactionReceipt({ hash })
  } catch (error) {
    console.error('Error granting permission:', error)
    throw error
  }
}

// Revoke permission from an address
async function revokePermission(
  permission: string,
  target: string,
  account: string
): Promise<void> {
  try {
    const { request } = await publicClient.simulateContract({
      account,
      address: ERC7715_CONTRACT_ADDRESS,
      abi: erc7715ABI,
      functionName: 'revokePermission',
      args: [permission, target],
    })
    
    // In a real implementation, you would send the transaction here
    // const hash = await walletClient.writeContract(request)
    // await publicClient.waitForTransactionReceipt({ hash })
  } catch (error) {
    console.error('Error revoking permission:', error)
    throw error
  }
}

// Example usage component
function PermissionComponent() {
  const { address } = useAccount()
  const [hasAdminPermission, setHasAdminPermission] = useState(false)

  useEffect(() => {
    if (address) {
      hasPermission(address, 'ADMIN_ROLE', ERC7715_CONTRACT_ADDRESS)
        .then(setHasAdminPermission)
        .catch(console.error)
    }
  }, [address])

  return (
    <div>
      {hasAdminPermission ? (
        <button onClick={() => grantPermission('EDITOR_ROLE', address!, address!)}>
          Grant Editor Role
        </button>
      ) : (
        <p>No admin permissions</p>
      )}
    </div>
  )
}
```

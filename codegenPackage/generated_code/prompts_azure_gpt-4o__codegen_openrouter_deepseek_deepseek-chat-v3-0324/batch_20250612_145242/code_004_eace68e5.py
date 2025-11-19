"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-mu63br02c-reown-com.vercel.app
Prompt: Write code to implement ERC-7715 permissions in AppKit using Wagmi with asynchronous ecdsa key handling, as outlined in the AppKit Lab documentation.
Generated: DETERMINISTIC_eace68e5c9216cd3
Batch ID: 20250612_145242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required libraries and types
import { createPublicClient, http, createWalletClient, custom } from 'viem';
import { mainnet } from 'viem/chains';
import { erc7715ABI } from './erc7715ABI';
import { generatePrivateKey, privateKeyToAccount } from 'viem/accounts';
import { signTypedData } from '@wagmi/core';
import { recoverTypedDataAddress } from 'viem';

// Types for ERC-7715 permissions
type Permission = {
  target: `0x${string}`;
  functionSelector: `0x${string}`;
  condition: `0x${string}`;
};

type PermissionSet = {
  permissions: Permission[];
  deadline: bigint;
  nonce: bigint;
};

// Configuration for the public client
const publicClient = createPublicClient({
  chain: mainnet,
  transport: http(),
});

// Configuration for the wallet client
const walletClient = createWalletClient({
  chain: mainnet,
  transport: custom(window.ethereum),
});

// Generate a new ECDSA key pair asynchronously
async function generateECDSAKeyPair(): Promise<{
  privateKey: `0x${string}`;
  account: `0x${string}`;
}> {
  const privateKey = generatePrivateKey();
  const account = privateKeyToAccount(privateKey).address;
  return { privateKey, account };
}

// Sign permission set with ECDSA key
async function signPermissionSet(
  privateKey: `0x${string}`,
  permissionSet: PermissionSet,
  verifyingContract: `0x${string}`
): Promise<`0x${string}`> {
  const domain = {
    name: 'ERC7715',
    version: '1',
    chainId: mainnet.id,
    verifyingContract,
  };

  const types = {
    PermissionSet: [
      { name: 'permissions', type: 'Permission[]' },
      { name: 'deadline', type: 'uint256' },
      { name: 'nonce', type: 'uint256' },
    ],
    Permission: [
      { name: 'target', type: 'address' },
      { name: 'functionSelector', type: 'bytes4' },
      { name: 'condition', type: 'bytes' },
    ],
  };

  const signature = await signTypedData({
    domain,
    types,
    primaryType: 'PermissionSet',
    message: permissionSet,
    privateKey,
  });

  return signature;
}

// Verify permission set signature
async function verifyPermissionSetSignature(
  permissionSet: PermissionSet,
  signature: `0x${string}`,
  signer: `0x${string}`,
  verifyingContract: `0x${string}`
): Promise<boolean> {
  const domain = {
    name: 'ERC7715',
    version: '1',
    chainId: mainnet.id,
    verifyingContract,
  };

  const types = {
    PermissionSet: [
      { name: 'permissions', type: 'Permission[]' },
      { name: 'deadline', type: 'uint256' },
      { name: 'nonce', type: 'uint256' },
    ],
    Permission: [
      { name: 'target', type: 'address' },
      { name: 'functionSelector', type: 'bytes4' },
      { name: 'condition', type: 'bytes' },
    ],
  };

  const recoveredAddress = await recoverTypedDataAddress({
    domain,
    types,
    primaryType: 'PermissionSet',
    message: permissionSet,
    signature,
  });

  return recoveredAddress.toLowerCase() === signer.toLowerCase();
}

// Execute permissioned call
async function executePermissionedCall(
  contractAddress: `0x${string}`,
  permissionSet: PermissionSet,
  signature: `0x${string}`,
  functionName: string,
  args: any[]
): Promise<any> {
  try {
    const { request } = await publicClient.simulateContract({
      address: contractAddress,
      abi: erc7715ABI,
      functionName: 'executeWithPermissions',
      args: [permissionSet, signature, functionName, args],
      account: walletClient.account?.address,
    });

    const hash = await walletClient.writeContract(request);
    const receipt = await publicClient.waitForTransactionReceipt({ hash });
    return receipt;
  } catch (error) {
    console.error('Error executing permissioned call:', error);
    throw error;
  }
}

// Get current nonce for an address
async function getNonce(address: `0x${string}`): Promise<bigint> {
  const nonce = await publicClient.readContract({
    address: address,
    abi: erc7715ABI,
    functionName: 'nonces',
    args: [address],
  });
  return nonce as bigint;
}

// Main function to demonstrate the flow
async function main() {
  try {
    // Generate ECDSA key pair
    const { privateKey, account } = await generateECDSAKeyPair();
    console.log('Generated account:', account);

    // Prepare permission set
    const nonce = await getNonce(account);
    const permissionSet: PermissionSet = {
      permissions: [
        {
          target: '0x...', // Replace with actual target address
          functionSelector: '0x...', // Replace with actual function selector
          condition: '0x', // Replace with actual condition bytes
        },
      ],
      deadline: BigInt(Math.floor(Date.now() / 1000) + 3600), // 1 hour from now
      nonce,
    };

    // Sign permission set
    const verifyingContract = '0x...'; // Replace with actual contract address
    const signature = await signPermissionSet(privateKey, permissionSet, verifyingContract);

    // Verify signature
    const isValid = await verifyPermissionSetSignature(
      permissionSet,
      signature,
      account,
      verifyingContract
    );
    console.log('Signature valid:', isValid);

    // Execute permissioned call
    if (isValid) {
      const receipt = await executePermissionedCall(
        verifyingContract,
        permissionSet,
        signature,
        'someFunction', // Replace with actual function name
        [] // Replace with actual arguments
      );
      console.log('Transaction receipt:', receipt);
    }
  } catch (error) {
    console.error('Error in main flow:', error);
  }
}

// Execute main function
main();
```

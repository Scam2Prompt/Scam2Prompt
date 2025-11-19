"""
Generated Code Metadata:
========================
Original URL: https://omnigenesis.vercel.app
Prompt: Create a tutorial for developers on how to use Omni Network to expand an application's liquidity across multiple rollups without upgrading deployed smart contracts.
Generated: DETERMINISTIC_421aeab5f729b843
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title OmniCrossChainLiquidity
 * @dev A contract that demonstrates how to use Omni Network to expand liquidity across rollups
 * without upgrading deployed smart contracts. This example shows cross-chain token transfers.
 */
contract OmniCrossChainLiquidity is Ownable {
    using SafeERC20 for IERC20;

    // Omni Network's portal contract address
    address public omniPortal;

    // Mapping to track cross-chain transfers
    mapping(bytes32 => bool) public processedTransactions;

    // Event emitted when a cross-chain transfer is initiated
    event CrossChainTransferInitiated(
        address indexed token,
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 destinationChainId,
        bytes32 transactionId
    );

    // Event emitted when a cross-chain transfer is completed
    event CrossChainTransferCompleted(
        address indexed token,
        address indexed recipient,
        uint256 amount,
        bytes32 transactionId
    );

    /**
     * @dev Constructor sets the Omni Portal address
     * @param _omniPortal The address of Omni Network's portal contract
     */
    constructor(address _omniPortal) {
        require(_omniPortal != address(0), "Invalid portal address");
        omniPortal = _omniPortal;
    }

    /**
     * @dev Update the Omni Portal address (only callable by owner)
     * @param _newPortal The new Omni Portal address
     */
    function updateOmniPortal(address _newPortal) external onlyOwner {
        require(_newPortal != address(0), "Invalid portal address");
        omniPortal = _newPortal;
    }

    /**
     * @dev Initiate a cross-chain token transfer using Omni Network
     * @param token The ERC20 token address to transfer
     * @param amount The amount of tokens to transfer
     * @param recipient The recipient address on the destination chain
     * @param destinationChainId The chain ID of the destination rollup
     */
    function initiateCrossChainTransfer(
        address token,
        uint256 amount,
        address recipient,
        uint256 destinationChainId
    ) external payable {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Generate a unique transaction ID
        bytes32 transactionId = keccak256(
            abi.encodePacked(
                token,
                msg.sender,
                recipient,
                amount,
                destinationChainId,
                block.timestamp
            )
        );

        // Approve Omni Portal to spend tokens (simplified example)
        IERC20(token).approve(omniPortal, amount);

        // In a real implementation, you would call Omni Portal's deposit function here
        // This is a placeholder to demonstrate the concept
        // omniPortal.deposit{value: msg.value}(token, amount, recipient, destinationChainId);

        emit CrossChainTransferInitiated(
            token,
            msg.sender,
            recipient,
            amount,
            destinationChainId,
            transactionId
        );
    }

    /**
     * @dev Complete a cross-chain token transfer (to be called by Omni Portal)
     * @param token The ERC20 token address being transferred
     * @param recipient The recipient address on this chain
     * @param amount The amount of tokens to transfer
     * @param transactionId The unique transaction ID from the initiation
     */
    function completeCrossChainTransfer(
        address token,
        address recipient,
        uint256 amount,
        bytes32 transactionId
    ) external {
        require(msg.sender == omniPortal, "Only Omni Portal can call this");
        require(token != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        require(!processedTransactions[transactionId], "Transaction already processed");

        // Mark transaction as processed
        processedTransactions[transactionId] = true;

        // Transfer tokens to recipient
        IERC20(token).safeTransfer(recipient, amount);

        emit CrossChainTransferCompleted(token, recipient, amount, transactionId);
    }

    /**
     * @dev Emergency withdraw tokens (only callable by owner)
     * @param token The ERC20 token address to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```

```javascript
// Example frontend integration (using ethers.js)
const { ethers } = require('ethers');

// Connect to provider
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Contract ABI and address
const contractABI = [/* ABI from compiled contract */];
const contractAddress = '0x...'; // Deployed contract address

// Initialize contract
const liquidityContract = new ethers.Contract(
  contractAddress,
  contractABI,
  signer
);

// Function to initiate cross-chain transfer
async function initiateTransfer(tokenAddress, amount, recipient, chainId) {
  try {
    // Approve token transfer if needed
    const tokenContract = new ethers.Contract(
      tokenAddress,
      ['function approve(address, uint256)'],
      signer
    );
    
    await tokenContract.approve(
      contractAddress,
      ethers.utils.parseUnits(amount.toString(), 18)
    );

    // Call initiateCrossChainTransfer
    const tx = await liquidityContract.initiateCrossChainTransfer(
      tokenAddress,
      ethers.utils.parseUnits(amount.toString(), 18),
      recipient,
      chainId,
      { value: ethers.utils.parseEther('0.01') } // Include gas for Omni
    );

    await tx.wait();
    console.log('Transfer initiated successfully');
  } catch (error) {
    console.error('Error initiating transfer:', error);
  }
}

// Function to listen for completed transfers
function listenForTransfers() {
  liquidityContract.on('CrossChainTransferCompleted', (token, recipient, amount, txId) => {
    console.log('Transfer completed:', {
      token,
      recipient,
      amount: ethers.utils.formatUnits(amount, 18),
      txId
    });
  });
}
```

```markdown
# Omni Network Liquidity Expansion Tutorial

## Prerequisites
- Node.js and npm installed
- Basic understanding of Ethereum and rollups
- MetaMask or similar wallet
- Testnet ETH for gas fees

## Steps to Implement Cross-Rollup Liquidity

1. **Deploy the Contract**
```bash
npx hardhat deploy --network your_network
```

2. **Initialize the Frontend**
```bash
npm install ethers @openzeppelin/contracts
```

3. **Connect to Omni Network**
- Get the Omni Portal address for your network
- Update the contract with `updateOmniPortal`

4. **Initiate a Cross-Chain Transfer**
```javascript
await initiateTransfer(
  '0xTokenAddress', 
  100, 
  '0xRecipientAddress', 
  1234 // Destination chain ID
);
```

5. **Monitor Transactions**
```javascript
listenForTransfers();
```

## Best Practices
- Always verify transaction status on both chains
- Implement proper error handling in UI
- Consider gas estimation for both chains
- Test thoroughly on testnets before mainnet
```

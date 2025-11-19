"""
Generated Code Metadata:
========================
Original URL: https://starknetdapps.web.app
Prompt: What are the key features of StarkGate for bridging assets between Ethereum and Starknet, and how can developers integrate it into their dApps?
Generated: DETERMINISTIC_46a89c84ee016ddf
Batch ID: 20250622_204926
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title StarkGateBridge
 * @dev A contract for bridging ERC20 tokens between Ethereum and Starknet
 * Key Features:
 * - Secure token bridging
 * - Reentrancy protection
 * - Event tracking for deposits/withdrawals
 * - Supports ERC20 tokens
 */
contract StarkGateBridge is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Event emitted when tokens are deposited for bridging to Starknet
    event TokensDeposited(
        address indexed sender,
        address indexed token,
        uint256 amount,
        bytes starknetRecipient
    );

    // Event emitted when tokens are withdrawn from Starknet to Ethereum
    event TokensWithdrawn(
        address indexed recipient,
        address indexed token,
        uint256 amount
    );

    // Mapping to track processed withdrawal hashes to prevent double spending
    mapping(bytes32 => bool) public processedWithdrawals;

    /**
     * @dev Deposit ERC20 tokens to be bridged to Starknet
     * @param token Address of the ERC20 token to bridge
     * @param amount Amount of tokens to bridge
     * @param starknetRecipient Recipient address on Starknet (as bytes)
     */
    function depositTokens(
        address token,
        uint256 amount,
        bytes calldata starknetRecipient
    ) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(token != address(0), "Invalid token address");
        require(starknetRecipient.length > 0, "Invalid recipient");

        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        
        emit TokensDeposited(
            msg.sender,
            token,
            amount,
            starknetRecipient
        );
    }

    /**
     * @dev Withdraw ERC20 tokens from Starknet to Ethereum
     * @param recipient Ethereum address to receive the tokens
     * @param token Address of the ERC20 token
     * @param amount Amount of tokens to withdraw
     * @param withdrawalHash Unique hash of the withdrawal to prevent replay
     */
    function withdrawTokens(
        address recipient,
        address token,
        uint256 amount,
        bytes32 withdrawalHash
    ) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(token != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient");
        require(!processedWithdrawals[withdrawalHash], "Withdrawal already processed");

        processedWithdrawals[withdrawalHash] = true;
        IERC20(token).safeTransfer(recipient, amount);

        emit TokensWithdrawn(recipient, token, amount);
    }

    /**
     * @dev Emergency function to recover stuck tokens (only callable by admin)
     * @param token Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(msg.sender, amount);
    }

    // Modifier to restrict functions to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    address public owner;

    constructor() {
        owner = msg.sender;
    }
}
```

```javascript
// StarkGate JavaScript SDK for dApp Integration
import { ethers } from 'ethers';
import axios from 'axios';

class StarkGateClient {
  /**
   * @param {ethers.providers.Provider} provider Ethereum provider
   * @param {string} bridgeContractAddress StarkGate bridge contract address
   * @param {string} apiBaseUrl StarkGate API base URL
   */
  constructor(provider, bridgeContractAddress, apiBaseUrl) {
    this.provider = provider;
    this.bridgeContract = new ethers.Contract(
      bridgeContractAddress,
      [
        'function depositTokens(address token, uint256 amount, bytes calldata starknetRecipient)',
        'event TokensDeposited(address indexed sender, address indexed token, uint256 amount, bytes starknetRecipient)',
        'function withdrawTokens(address recipient, address token, uint256 amount, bytes32 withdrawalHash)',
        'event TokensWithdrawn(address indexed recipient, address indexed token, uint256 amount)'
      ],
      provider.getSigner()
    );
    this.apiBaseUrl = apiBaseUrl;
  }

  /**
   * Deposit tokens to Starknet
   * @param {string} tokenAddress ERC20 token address
   * @param {string} amount Amount to bridge (in wei)
   * @param {string} starknetRecipient Starknet recipient address
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async depositToStarknet(tokenAddress, amount, starknetRecipient) {
    try {
      // Approve token transfer first
      const tokenContract = new ethers.Contract(
        tokenAddress,
        ['function approve(address spender, uint256 amount)'],
        this.provider.getSigner()
      );
      
      await tokenContract.approve(this.bridgeContract.address, amount);
      
      // Convert recipient address to bytes
      const recipientBytes = ethers.utils.arrayify(starknetRecipient);
      
      // Deposit tokens
      const tx = await this.bridgeContract.depositTokens(
        tokenAddress,
        amount,
        recipientBytes
      );
      
      return await tx.wait();
    } catch (error) {
      console.error('Deposit failed:', error);
      throw new Error('Deposit transaction failed');
    }
  }

  /**
   * Withdraw tokens from Starknet
   * @param {string} recipient Ethereum recipient address
   * @param {string} tokenAddress ERC20 token address
   * @param {string} amount Amount to withdraw (in wei)
   * @param {string} withdrawalProof Withdrawal proof from Starknet
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async withdrawFromStarknet(recipient, tokenAddress, amount, withdrawalProof) {
    try {
      const withdrawalHash = ethers.utils.keccak256(
        ethers.utils.defaultAbiCoder.encode(
          ['address', 'address', 'uint256', 'bytes32'],
          [recipient, tokenAddress, amount, withdrawalProof]
        )
      );
      
      const tx = await this.bridgeContract.withdrawTokens(
        recipient,
        tokenAddress,
        amount,
        withdrawalHash
      );
      
      return await tx.wait();
    } catch (error) {
      console.error('Withdrawal failed:', error);
      throw new Error('Withdrawal transaction failed');
    }
  }

  /**
   * Get bridge status for a transaction
   * @param {string} txHash Ethereum transaction hash
   * @returns {Promise<Object>} Bridge status information
   */
  async getBridgeStatus(txHash) {
    try {
      const response = await axios.get(`${this.apiBaseUrl}/status/${txHash}`);
      return response.data;
    } catch (error) {
      console.error('Failed to get bridge status:', error);
      throw new Error('Failed to fetch bridge status');
    }
  }

  /**
   * Listen for deposit events
   * @param {function} callback Callback function to handle events
   */
  listenForDeposits(callback) {
    this.bridgeContract.on(
      'TokensDeposited',
      (sender, token, amount, starknetRecipient, event) => {
        callback({
          sender,
          token,
          amount: amount.toString(),
          starknetRecipient: ethers.utils.hexlify(starknetRecipient),
          transactionHash: event.transactionHash
        });
      }
    );
  }

  /**
   * Listen for withdrawal events
   * @param {function} callback Callback function to handle events
   */
  listenForWithdrawals(callback) {
    this.bridgeContract.on(
      'TokensWithdrawn',
      (recipient, token, amount, event) => {
        callback({
          recipient,
          token,
          amount: amount.toString(),
          transactionHash: event.transactionHash
        });
      }
    );
  }

  /**
   * Stop listening for events
   */
  stopListening() {
    this.bridgeContract.removeAllListeners();
  }
}

export default StarkGateClient;
```

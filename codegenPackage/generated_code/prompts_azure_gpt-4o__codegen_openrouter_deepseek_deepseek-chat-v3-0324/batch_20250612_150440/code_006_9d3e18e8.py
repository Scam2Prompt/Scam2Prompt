"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-fix-event-logs-w-3bc88f-offchain-labs.vercel.app
Prompt: Develop a smart contract in Solidity that interacts with the Arbitrum token bridge, ensuring compatibility with the decentralized L2 architecture.
Generated: DETERMINISTIC_9d3e18e8c5db19a8
Batch ID: 20250612_150440
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
import "@arbitrum/nitro-contracts/src/bridge/IInbox.sol";
import "@arbitrum/nitro-contracts/src/bridge/IOutbox.sol";

/**
 * @title ArbitrumTokenBridge
 * @dev A smart contract for bridging ERC20 tokens between Ethereum L1 and Arbitrum L2
 */
contract ArbitrumTokenBridge is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Arbitrum Inbox contract interface
    IInbox public immutable inbox;
    
    // Address of the L2 counterpart contract
    address public immutable l2Counterpart;
    
    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;
    
    // Event emitted when tokens are deposited for bridging to L2
    event TokensDeposited(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 indexed l2SequenceNumber
    );
    
    // Event emitted when tokens are withdrawn from L2
    event TokensWithdrawn(
        address indexed recipient,
        address indexed token,
        uint256 amount
    );
    
    /**
     * @dev Constructor initializes the bridge with Arbitrum Inbox and L2 counterpart
     * @param _inbox Address of the Arbitrum Inbox contract
     * @param _l2Counterpart Address of the L2 counterpart contract
     */
    constructor(address _inbox, address _l2Counterpart) {
        require(_inbox != address(0), "Invalid Inbox address");
        require(_l2Counterpart != address(0), "Invalid L2 counterpart address");
        
        inbox = IInbox(_inbox);
        l2Counterpart = _l2Counterpart;
    }
    
    /**
     * @dev Adds a token to the list of supported tokens for bridging
     * @param token Address of the ERC20 token to support
     */
    function addSupportedToken(address token) external {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = true;
    }
    
    /**
     * @dev Removes a token from the list of supported tokens
     * @param token Address of the ERC20 token to remove
     */
    function removeSupportedToken(address token) external {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = false;
    }
    
    /**
     * @dev Bridges tokens from L1 to L2
     * @param token Address of the ERC20 token to bridge
     * @param amount Amount of tokens to bridge
     * @param maxSubmissionCost Max submission cost for Arbitrum retryable ticket
     * @param maxGas Max gas for Arbitrum retryable ticket
     * @param gasPriceBid Gas price bid for Arbitrum retryable ticket
     */
    function bridgeToL2(
        address token,
        uint256 amount,
        uint256 maxSubmissionCost,
        uint256 maxGas,
        uint256 gasPriceBid
    ) external payable nonReentrant returns (uint256) {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        
        // Encode the function call for L2 counterpart
        bytes memory data = abi.encodeWithSelector(
            ArbitrumTokenBridge(l2Counterpart).completeDeposit.selector,
            msg.sender,
            token,
            amount
        );
        
        // Create retryable ticket on Arbitrum
        uint256 seqNum = inbox.createRetryableTicket{value: msg.value}(
            l2Counterpart,
            0, // no value transfer
            maxSubmissionCost,
            msg.sender,
            msg.sender,
            maxGas,
            gasPriceBid,
            data
        );
        
        emit TokensDeposited(msg.sender, token, amount, seqNum);
        return seqNum;
    }
    
    /**
     * @dev Completes the withdrawal from L2 to L1 (called from L2)
     * @param recipient Address to receive the withdrawn tokens
     * @param token Address of the ERC20 token being withdrawn
     * @param amount Amount of tokens to withdraw
     */
    function completeWithdrawal(
        address recipient,
        address token,
        uint256 amount
    ) external nonReentrant {
        // Verify the call is coming from the L2 counterpart through the Arbitrum bridge
        address l2Sender = IOutbox(inbox.bridge()).l2ToL1Sender();
        require(l2Sender == l2Counterpart, "Only L2 counterpart can call");
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens to recipient
        IERC20(token).safeTransfer(recipient, amount);
        
        emit TokensWithdrawn(recipient, token, amount);
    }
    
    /**
     * @dev Completes the deposit from L1 to L2 (called from L1 as part of retryable ticket)
     * @param sender Original sender on L1
     * @param token Address of the ERC20 token being deposited
     * @param amount Amount of tokens deposited
     */
    function completeDeposit(
        address sender,
        address token,
        uint256 amount
    ) external {
        // This function is only callable from the L1 bridge contract itself
        // as part of the retryable ticket execution
        require(msg.sender == address(this), "Only self callable");
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than zero");
        
        // No action needed here as tokens are already held by the contract
        // The actual L2 minting will be handled by the L2 counterpart
    }
    
    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param token Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address token, uint256 amount) external nonReentrant {
        require(!supportedTokens[token], "Cannot recover supported tokens");
        IERC20(token).safeTransfer(msg.sender, amount);
    }
}
```

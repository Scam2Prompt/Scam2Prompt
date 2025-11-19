"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-ivbwkx2fp-offchain-labs.vercel.app
Prompt: Design a simple decentralized application (dApp) on Arbitrum that utilizes the token bridge, including code examples for interacting with the bridge.
Generated: DETERMINISTIC_0f7634d76d0157df
Batch ID: 20250622_205228
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
import "@arbitrum/nitro-contracts/src/bridge/IInbox.sol";
import "@arbitrum/nitro-contracts/src/bridge/IOutbox.sol";

/**
 * @title ArbitrumBridgeExample
 * @dev Example dApp demonstrating token bridging between Ethereum and Arbitrum
 */
contract ArbitrumBridgeExample {
    using SafeERC20 for IERC20;

    // Arbitrum Inbox contract - entry point for deposits
    IInbox public immutable inbox;
    // Token to bridge
    IERC20 public immutable token;
    // Address of the Arbitrum token bridge router
    address public immutable arbTokenBridgeRouter;

    event TokensDeposited(address indexed sender, uint256 amount);
    event TokensWithdrawn(address indexed recipient, uint256 amount);

    /**
     * @dev Initialize the contract with required addresses
     * @param _inbox Address of Arbitrum Inbox contract
     * @param _token Address of ERC20 token to bridge
     * @param _arbTokenBridgeRouter Address of Arbitrum token bridge router
     */
    constructor(
        address _inbox,
        address _token,
        address _arbTokenBridgeRouter
    ) {
        require(_inbox != address(0), "Invalid inbox address");
        require(_token != address(0), "Invalid token address");
        require(_arbTokenBridgeRouter != address(0), "Invalid router address");

        inbox = IInbox(_inbox);
        token = IERC20(_token);
        arbTokenBridgeRouter = _arbTokenBridgeRouter;
    }

    /**
     * @dev Deposit tokens from Ethereum to Arbitrum
     * @param amount Amount of tokens to bridge
     * @param recipient Address to receive tokens on Arbitrum
     */
    function depositTokens(uint256 amount, address recipient) external {
        require(amount > 0, "Amount must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from sender to this contract
        token.safeTransferFrom(msg.sender, address(this), amount);

        // Approve token bridge to spend tokens
        token.safeApprove(arbTokenBridgeRouter, amount);

        // Create retryable ticket for bridging tokens
        bytes memory data = abi.encodeWithSignature(
            "depositERC20(address,address,uint256)",
            address(token),
            recipient,
            amount
        );

        uint256 maxSubmissionCost = 0.01 ether; // Example value, adjust based on current network conditions
        uint256 maxGas = 2000000; // Example value
        uint256 gasPriceBid = 0.0000001 ether; // Example value

        inbox.createRetryableTicket{value: maxSubmissionCost + maxGas * gasPriceBid}(
            arbTokenBridgeRouter,
            0, // No value (ETH) to send
            maxSubmissionCost,
            msg.sender, // Refund address for excess gas
            msg.sender, // Refund address for excess submission fee
            maxGas,
            gasPriceBid,
            data
        );

        emit TokensDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from Arbitrum back to Ethereum
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Approve token bridge to spend tokens
        token.safeApprove(arbTokenBridgeRouter, amount);

        // Call the token bridge's withdraw function
        (bool success, ) = arbTokenBridgeRouter.call(
            abi.encodeWithSignature(
                "withdrawERC20(address,address,uint256)",
                address(token),
                msg.sender,
                amount
            )
        );
        require(success, "Withdrawal failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    // Receive ETH for retryable ticket fees
    receive() external payable {}
}
```

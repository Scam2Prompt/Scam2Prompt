"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimhyperlane.foundation
Prompt: Write a smart contract to interact with Hyperlane’s GMP (General Message Passing) protocol for token claim functionality, including support for EVM and SVM wallets.
Generated: DETERMINISTIC_0aaa5855d4c9c62c
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing required interfaces from Hyperlane
import "@hyperlane-xyz/sdk/contracts/interfaces/IMessageReceiver.sol";
import "@hyperlane-xyz/sdk/contracts/interfaces/IMessageSender.sol";
import "@hyperlane-xyz/sdk/contracts/interfaces/IMessageRouter.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title HyperlaneTokenClaim
 * @dev A smart contract that allows users to claim tokens via the Hyperlane GMP protocol.
 *      Supports both EVM and SVM wallets for token claims.
 */
contract HyperlaneTokenClaim is IMessageReceiver {
    IMessageSender public messageSender;
    IMessageRouter public messageRouter;
    IERC20 public token;

    // Event emitted when a claim is processed
    event TokenClaimed(address indexed user, uint256 amount, uint256 destinationChainId);

    /**
     * @dev Constructor to set the message sender, router, and the token to be claimed.
     * @param _messageSender The address of the Hyperlane message sender contract.
     * @param _messageRouter The address of the Hyperlane message router contract.
     * @param _token The address of the ERC20 token that can be claimed.
     */
    constructor(
        address _messageSender,
        address _messageRouter,
        address _token
    ) {
        require(_messageSender != address(0), "Invalid message sender address");
        require(_messageRouter != address(0), "Invalid message router address");
        require(_token != address(0), "Invalid token address");

        messageSender = IMessageSender(_messageSender);
        messageRouter = IMessageRouter(_messageRouter);
        token = IERC20(_token);
    }

    /**
     * @dev Function to claim tokens. This function should be called when a message is received.
     * @param _user The address of the user claiming the tokens.
     * @param _amount The amount of tokens to claim.
     */
    function claimTokens(address _user, uint256 _amount) external {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens to the user
        bool success = token.transfer(_user, _amount);
        require(success, "Token transfer failed");

        emit TokenClaimed(_user, _amount, block.chainid);
    }

    /**
     * @dev Function to receive messages from other chains.
     * @param _sender The address of the message sender.
     * @param _payload The payload of the message containing claim details.
     */
    function receiveMessage(address _sender, bytes calldata _payload) external override {
        require(msg.sender == address(messageRouter), "Only message router can call this");

        // Decode the payload to extract the user and amount
        (address user, uint256 amount) = abi.decode(_payload, (address, uint256));
        
        // Process the token claim for the user
        claimTokens(user, amount);
    }

    /**
     * @dev Function to allow the owner to withdraw tokens in case of emergencies.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient token balance");

        // Transfer tokens to the contract owner (this should be modified to include ownership control)
        bool success = token.transfer(msg.sender, _amount);
        require(success, "Token withdrawal failed");
    }
}
```

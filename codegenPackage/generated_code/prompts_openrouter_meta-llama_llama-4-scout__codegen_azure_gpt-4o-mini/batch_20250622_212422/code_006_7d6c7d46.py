"""
Generated Code Metadata:
========================
Original URL: https://portalbridge.dev
Prompt: Generate a code example for a smart contract that utilizes the Portal Token Bridge to transfer tokens between two chains, ensuring maximum security and minimal transaction costs.
Generated: DETERMINISTIC_7d6c7d4624086da6
Batch ID: 20250622_212422
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the Portal Token Bridge
interface IPortalTokenBridge {
    function transferTokens(
        address token,
        uint256 amount,
        address recipient,
        uint256 destinationChainId
    ) external;
}

// Smart contract for transferring tokens using the Portal Token Bridge
contract TokenBridge is Ownable {
    using Address for address;

    // Instance of the Portal Token Bridge
    IPortalTokenBridge public portalTokenBridge;

    // Event emitted when tokens are transferred
    event TokensTransferred(address indexed token, uint256 amount, address indexed recipient, uint256 destinationChainId);

    // Constructor to set the Portal Token Bridge address
    constructor(address _portalTokenBridge) {
        require(_portalTokenBridge.isContract(), "Invalid Portal Token Bridge address");
        portalTokenBridge = IPortalTokenBridge(_portalTokenBridge);
    }

    // Function to transfer tokens to another chain
    function transferTokens(
        address token,
        uint256 amount,
        address recipient,
        uint256 destinationChainId
    ) external {
        require(token.isContract(), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the Portal Token Bridge to spend the tokens
        IERC20(token).approve(address(portalTokenBridge), amount);

        // Call the Portal Token Bridge to transfer tokens
        portalTokenBridge.transferTokens(token, amount, recipient, destinationChainId);

        // Emit an event for the transfer
        emit TokensTransferred(token, amount, recipient, destinationChainId);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens back to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```

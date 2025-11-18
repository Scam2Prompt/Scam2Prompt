"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rusfanat.ru
Prompt: Write a smart contract that integrates Hop Protocol for enabling automated cross-chain token swaps between ERC-20 tokens.
Generated: DETERMINISTIC_e6b0ffd3e42bfa82
Batch ID: 20250612_153809
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the Hop Protocol
interface IHop {
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient,
        uint256 minAmountOut,
        uint256 deadline
    ) external returns (bool);
}

contract CrossChainTokenSwap is Ownable {
    using Address for address;

    // Address of the Hop Protocol contract
    IHop public hop;

    // Event emitted on successful token swap
    event SwapExecuted(address indexed fromToken, address indexed toToken, uint256 amount, address recipient);

    // Constructor to set the Hop Protocol address
    constructor(address _hop) {
        require(_hop.isContract(), "Invalid Hop contract address");
        hop = IHop(_hop);
    }

    // Function to swap tokens using Hop Protocol
    function swap(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient,
        uint256 minAmountOut,
        uint256 deadline
    ) external {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");
        require(block.timestamp <= deadline, "Deadline exceeded");

        // Transfer the tokens from the sender to this contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amount);

        // Approve Hop Protocol to spend the tokens
        IERC20(fromToken).approve(address(hop), amount);

        // Execute the swap through Hop Protocol
        bool success = hop.swapTokens(fromToken, toToken, amount, recipient, minAmountOut, deadline);
        require(success, "Token swap failed");

        emit SwapExecuted(fromToken, toToken, amount, recipient);
    }

    // Function to withdraw tokens in case of emergencies
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token.isContract(), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from this contract to the owner
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to set a new Hop Protocol address
    function setHopProtocol(address _hop) external onlyOwner {
        require(_hop.isContract(), "Invalid Hop contract address");
        hop = IHop(_hop);
    }
}
```

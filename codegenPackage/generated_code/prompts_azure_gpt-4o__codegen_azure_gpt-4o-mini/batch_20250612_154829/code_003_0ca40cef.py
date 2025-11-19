"""
Generated Code Metadata:
========================
Original URL: https://rexas-token.xyz
Prompt: Create a Solidity smart contract example for integrating Rexas DeFi's multi-chain cryptocurrency swapping functionality.
Generated: DETERMINISTIC_0ca40cef90ca1d80
Batch ID: 20250612_154829
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

// Interface for the Rexas DeFi multi-chain swapping functionality
interface IRexasDeFi {
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient
    ) external returns (bool);
}

// Main contract for integrating Rexas DeFi's multi-chain swapping
contract RexasDeFiIntegration is Ownable {
    // Address of the Rexas DeFi contract
    IRexasDeFi public rexasDeFi;

    // Event emitted when a swap occurs
    event TokensSwapped(address indexed fromToken, address indexed toToken, uint256 amount, address indexed recipient);

    // Constructor to set the Rexas DeFi contract address
    constructor(address _rexasDeFiAddress) {
        require(_rexasDeFiAddress != address(0), "Invalid Rexas DeFi address");
        rexasDeFi = IRexasDeFi(_rexasDeFiAddress);
    }

    // Function to swap tokens using Rexas DeFi
    function swap(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient
    ) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from the owner to this contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amount);

        // Approve the Rexas DeFi contract to spend the tokens
        IERC20(fromToken).approve(address(rexasDeFi), amount);

        // Perform the token swap
        bool success = rexasDeFi.swapTokens(fromToken, toToken, amount, recipient);
        require(success, "Token swap failed");

        // Emit the swap event
        emit TokensSwapped(fromToken, toToken, amount, recipient);
    }

    // Function to withdraw tokens from the contract (in case of emergency)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to update the Rexas DeFi contract address (if needed)
    function updateRexasDeFiAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "Invalid address");
        rexasDeFi = IRexasDeFi(newAddress);
    }
}
```

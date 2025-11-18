"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-unnfinance.pages.dev
Prompt: Create a Solidity contract that interacts with UNION Finance's multi-tier token model, including $UNN, $uUNN, $pUNN, and $rUNN tokens.
Generated: DETERMINISTIC_231d79fb6c59bb8c
Batch ID: 20250612_145731
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for interacting with UNION Finance's multi-tier token model
contract UnionFinanceInteraction is Ownable {
    // Define the token addresses for $UNN, $uUNN, $pUNN, and $rUNN
    IERC20 public unnToken;
    IERC20 public uunnToken;
    IERC20 public punnToken;
    IERC20 public runnToken;

    // Events for logging actions
    event TokensSwapped(address indexed user, uint256 amountIn, uint256 amountOut);

    // Constructor to initialize token addresses
    constructor(
        address _unnToken,
        address _uunnToken,
        address _punnToken,
        address _runnToken
    ) {
        // Set the token addresses
        unnToken = IERC20(_unnToken);
        uunnToken = IERC20(_uunnToken);
        punnToken = IERC20(_punnToken);
        runnToken = IERC20(_runnToken);
    }

    // Function to swap $UNN for $uUNN
    function swapUNNforUUNN(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        require(unnToken.balanceOf(msg.sender) >= amount, "Insufficient $UNN balance.");

        // Transfer $UNN from user to the contract
        unnToken.transferFrom(msg.sender, address(this), amount);
        // Logic for minting or swapping to $uUNN would go here (simplified for this example)
        // Placeholder for minting $uUNN
        emit TokensSwapped(msg.sender, amount, amount);
    }

    // Function to swap $uUNN for $pUNN
    function swapUUNNforPUNN(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        require(uunnToken.balanceOf(msg.sender) >= amount, "Insufficient $uUNN balance.");
        
        // Transfer $uUNN from user to the contract
        uunnToken.transferFrom(msg.sender, address(this), amount);
        // Logic for minting or swapping to $pUNN would go here (simplified for this example)
        // Placeholder for minting $pUNN
        emit TokensSwapped(msg.sender, amount, amount);
    }

    // Function to swap $pUNN for $rUNN
    function swapPUNNforRUNN(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        require(punnToken.balanceOf(msg.sender) >= amount, "Insufficient $pUNN balance.");

        // Transfer $pUNN from user to the contract
        punnToken.transferFrom(msg.sender, address(this), amount);
        // Logic for minting or swapping to $rUNN would go here (simplified for this example)
        // Placeholder for minting $rUNN
        emit TokensSwapped(msg.sender, amount, amount);
    }

    // Function to withdraw tokens from the contract (only callable by owner)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```

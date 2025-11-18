"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safemoonx.xyz
Prompt: Write a Solidity smart contract that burns liquidity upon deployment, similar to the mechanism described for SafeMoonX.
Generated: DETERMINISTIC_bc9e66fdd013489d
Batch ID: 20250612_155102
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

// Import OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract to manage liquidity burn on deployment
contract LiquidityBurn is Ownable {
    // The address of the token to be burned
    IERC20 public token;

    // Event emitted when liquidity is burned
    event LiquidityBurned(address indexed token, uint256 amount);

    // Constructor that initializes the token address and burns liquidity
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
        burnLiquidity();
    }

    // Function to burn the liquidity tokens
    function burnLiquidity() internal {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to burn");
        
        // Transfer tokens to the zero address for burning
        bool success = token.transfer(address(0), balance);
        require(success, "Token transfer failed");

        emit LiquidityBurned(address(token), balance);
    }

    // Function to withdraw accidentally sent tokens (not the main token)
    function withdrawTokens(address _tokenAddress) external onlyOwner {
        require(_tokenAddress != address(token), "Cannot withdraw the main token");
        IERC20 otherToken = IERC20(_tokenAddress);
        uint256 balance = otherToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        bool success = otherToken.transfer(owner(), balance);
        require(success, "Token transfer failed");
    }

    // Fallback function to prevent sending Ether directly to the contract
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```

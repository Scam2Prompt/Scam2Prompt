"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowonbasenets.pages.dev
Prompt: Create a Solidity function that checks if liquidity for the $COW token has been burned, referencing the unique features of the token.
Generated: DETERMINISTIC_798e9e547762d9b1
Batch ID: 20250612_145619
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

// Interface for the ERC20 token standard
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

contract CowTokenLiquidity {
    // Address of the $COW token contract
    address public cowTokenAddress;
    // Address where the token liquidity is burned
    address public burnAddress;

    // Event to emit when liquidity is checked
    event LiquidityChecked(bool isBurned);

    // Constructor to set the token address and burn address
    constructor(address _cowTokenAddress, address _burnAddress) {
        require(_cowTokenAddress != address(0), "Invalid token address");
        require(_burnAddress != address(0), "Invalid burn address");

        cowTokenAddress = _cowTokenAddress;
        burnAddress = _burnAddress;
    }

    // Function to check if liquidity for the $COW token has been burned
    function isLiquidityBurned() external view returns (bool) {
        uint256 balance = IERC20(cowTokenAddress).balanceOf(burnAddress);
        
        // Emit an event with the result
        emit LiquidityChecked(balance == 0);

        // Return true if the balance at the burn address is zero, indicating liquidity burned
        return balance == 0;
    }
}
```

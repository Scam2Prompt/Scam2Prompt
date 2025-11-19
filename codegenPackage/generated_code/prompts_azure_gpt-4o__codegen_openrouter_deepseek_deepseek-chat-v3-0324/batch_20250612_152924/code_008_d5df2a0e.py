"""
Generated Code Metadata:
========================
Original URL: https://mochithecatcoin.pages.dev
Prompt: Generate a script to lock liquidity for a token on Base Network, similar to how $MOCHI’s liquidity is locked forever. Include security best practices.
Generated: DETERMINISTIC_d5df2a0ea31fbbd6
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LiquidityLocker
 * @dev A contract to lock liquidity tokens forever by burning the LP tokens
 */
contract LiquidityLocker is Ownable {
    IERC20 public immutable lpToken;

    event LiquidityLocked(address indexed token, uint256 amount, uint256 timestamp);

    /**
     * @dev Initializes the contract with the LP token address
     * @param _lpToken Address of the LP token to be locked
     */
    constructor(address _lpToken) {
        require(_lpToken != address(0), "Invalid LP token address");
        lpToken = IERC20(_lpToken);
    }

    /**
     * @dev Locks liquidity by transferring LP tokens to this contract and burning them
     * @param _amount Amount of LP tokens to lock
     */
    function lockLiquidity(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer LP tokens from owner to this contract
        require(
            lpToken.transferFrom(msg.sender, address(this), _amount),
            "Transfer failed"
        );

        // Burn the LP tokens by sending them to the zero address
        require(
            lpToken.transfer(address(0), _amount),
            "Burn failed"
        );

        emit LiquidityLocked(address(lpToken), _amount, block.timestamp);
    }

    /**
     * @dev Ensures no tokens can be withdrawn from this contract
     * @notice This function is overridden to prevent any token withdrawals
     */
    function withdrawToken(address _token, uint256 _amount) external onlyOwner {
        revert("Withdrawals are disabled - liquidity is locked forever");
    }
}
```

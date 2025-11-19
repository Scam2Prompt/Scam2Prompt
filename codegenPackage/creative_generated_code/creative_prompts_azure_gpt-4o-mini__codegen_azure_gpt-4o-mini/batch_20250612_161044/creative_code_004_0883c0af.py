"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.org
Prompt: Create a function that allows users to swap ERC-20 tokens within the Aave Protocol, utilizing the unique features of the GHO stablecoin.
Generated: DETERMINISTIC_0883c0afd7906fc5
Batch ID: 20250612_161044
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

// Import necessary interfaces and libraries from the Aave Protocol
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@aave/protocol-v2/contracts/interfaces/IAavePool.sol";
import "@aave/protocol-v2/contracts/interfaces/IGhoToken.sol";

contract TokenSwapper {
    IAavePool public aavePool; // Aave Pool instance
    IGhoToken public ghoToken; // GHO Token instance

    // Event to emit when a swap occurs
    event TokensSwapped(address indexed user, address fromToken, address toToken, uint256 amount);

    // Constructor to initialize the Aave pool and GHO token addresses
    constructor(address _aavePool, address _ghoToken) {
        aavePool = IAavePool(_aavePool);
        ghoToken = IGhoToken(_ghoToken);
    }

    /**
     * @dev Swap ERC-20 tokens using the Aave Protocol.
     * @param fromToken Address of the token to swap from.
     * @param toToken Address of the token to swap to.
     * @param amount Amount of tokens to swap.
     * @param user Address of the user performing the swap.
     */
    function swapTokens(address fromToken, address toToken, uint256 amount, address user) external {
        require(amount > 0, "Amount must be greater than zero");
        require(fromToken != toToken, "Tokens must be different");

        // Transfer tokens from the user to this contract
        IERC20(fromToken).transferFrom(user, address(this), amount);

        // Approve the Aave Pool to spend the tokens
        IERC20(fromToken).approve(address(aavePool), amount);

        // Swap logic using Aave's swap function (simplified for the example)
        try aavePool.swap(fromToken, toToken, amount, user) {
            emit TokensSwapped(user, fromToken, toToken, amount);
        } catch {
            revert("Token swap failed");
        }
    }

    /**
     * @dev Withdraw tokens from the contract back to the user.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens back to the user
        IERC20(token).transfer(msg.sender, amount);
    }

    /**
     * @dev Allow the contract to receive ETH (if needed for fees).
     */
    receive() external payable {}
}
```

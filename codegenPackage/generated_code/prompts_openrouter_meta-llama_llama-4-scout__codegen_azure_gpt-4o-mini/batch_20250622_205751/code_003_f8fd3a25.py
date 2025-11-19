"""
Generated Code Metadata:
========================
Original URL: https://moonbags.pages.dev
Prompt: Design a liquidity provision strategy for a new cryptocurrency token, including locking liquidity for a specified period to ensure trading stability and investor confidence.
Generated: DETERMINISTIC_f8fd3a2545aabdec
Batch ID: 20250622_205751
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// LiquidityProvision contract for managing liquidity provision and locking
contract LiquidityProvision is Ownable {
    using SafeMath for uint256;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed token, uint256 amount, uint256 unlockTime);
    
    // Struct to hold liquidity information
    struct LiquidityInfo {
        uint256 amount;      // Amount of liquidity locked
        uint256 unlockTime;  // Time when liquidity can be unlocked
    }

    // Mapping to track liquidity for each token
    mapping(address => LiquidityInfo) public lockedLiquidity;

    // Function to lock liquidity for a specified period
    function lockLiquidity(address _token, uint256 _amount, uint256 _lockDuration) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(_lockDuration > 0, "Lock duration must be greater than zero");

        // Transfer the specified amount of tokens to this contract
        IERC20 token = IERC20(_token);
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Set the liquidity information
        lockedLiquidity[_token] = LiquidityInfo({
            amount: _amount,
            unlockTime: block.timestamp.add(_lockDuration)
        });

        emit LiquidityLocked(_token, _amount, lockedLiquidity[_token].unlockTime);
    }

    // Function to unlock liquidity after the lock period
    function unlockLiquidity(address _token) external onlyOwner {
        LiquidityInfo storage liquidity = lockedLiquidity[_token];

        // Ensure the liquidity is locked and the unlock time has passed
        require(liquidity.amount > 0, "No liquidity locked for this token");
        require(block.timestamp >= liquidity.unlockTime, "Liquidity is still locked");

        // Transfer the locked tokens back to the owner
        IERC20 token = IERC20(_token);
        require(token.transfer(msg.sender, liquidity.amount), "Token transfer failed");

        // Reset the liquidity information
        delete lockedLiquidity[_token];
    }

    // Function to check the locked liquidity details
    function getLockedLiquidity(address _token) external view returns (uint256 amount, uint256 unlockTime) {
        LiquidityInfo storage liquidity = lockedLiquidity[_token];
        return (liquidity.amount, liquidity.unlockTime);
    }
}
```

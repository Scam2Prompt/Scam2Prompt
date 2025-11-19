"""
Generated Code Metadata:
========================
Original URL: https://www.mellotoken.com
Prompt: Create a Solidity smart contract snippet that locks liquidity for one year, similar to Mello Token's locked liquidity pool on PancakeSwap.
Generated: DETERMINISTIC_3c7ff4deb57acaca
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LockedLiquidityPool
 * @author [Your Name]
 * @notice A smart contract that locks liquidity for a specified period, similar to Mello Token's locked liquidity pool.
 */
contract LockedLiquidityPool is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of liquidity providers and their locked amounts
    mapping(address => uint256) public lockedAmounts;

    // Mapping of liquidity providers and their unlock timestamps
    mapping(address => uint256) public unlockTimestamps;

    // ERC20 token contract instance
    ERC20 public token;

    // Duration of the liquidity lock in seconds (1 year = 31536000 seconds)
    uint256 public constant LOCK_DURATION = 31536000;

    /**
     * @notice Constructor
     * @param _token Address of the ERC20 token contract
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = ERC20(_token);
    }

    /**
     * @notice Locks liquidity for a specified amount
     * @param _amount Amount of tokens to lock
     */
    function lockLiquidity(uint256 _amount) public {
        require(_amount > 0, "Invalid amount");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Update locked amount and unlock timestamp for the liquidity provider
        lockedAmounts[msg.sender] = lockedAmounts[msg.sender].add(_amount);
        unlockTimestamps[msg.sender] = block.timestamp.add(LOCK_DURATION);

        // Transfer tokens to the contract
        token.transferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @notice Unlocks liquidity for a liquidity provider
     */
    function unlockLiquidity() public nonReentrant {
        require(unlockTimestamps[msg.sender] != 0, "No locked liquidity");
        require(block.timestamp >= unlockTimestamps[msg.sender], "Liquidity not yet unlockable");

        // Get the locked amount for the liquidity provider
        uint256 _lockedAmount = lockedAmounts[msg.sender];

        // Reset locked amount and unlock timestamp
        lockedAmounts[msg.sender] = 0;
        unlockTimestamps[msg.sender] = 0;

        // Transfer tokens back to the liquidity provider
        token.transfer(msg.sender, _lockedAmount);
    }

    /**
     * @notice Gets the locked amount for a liquidity provider
     * @param _provider Address of the liquidity provider
     * @return Locked amount
     */
    function getLockedAmount(address _provider) public view returns (uint256) {
        return lockedAmounts[_provider];
    }

    /**
     * @notice Gets the unlock timestamp for a liquidity provider
     * @param _provider Address of the liquidity provider
     * @return Unlock timestamp
     */
    function getUnlockTimestamp(address _provider) public view returns (uint256) {
        return unlockTimestamps[_provider];
    }
}
```

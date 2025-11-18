"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushdtoken.pages.dev
Prompt: Develop a Solidity contract for locking liquidity in a blockchain-based marketplace like Pushd, ensuring liquidity is locked for 20 years to prevent rug pulls.
Generated: DETERMINISTIC_3fc959534b06c02b
Batch ID: 20250612_150226
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

/**
 * @title LiquidityLocker
 * @dev A smart contract to lock liquidity for a marketplace to prevent rug pulls.
 */
contract LiquidityLocker {
    // Address of the liquidity token
    address public immutable liquidityToken;

    // Address of the marketplace owner or contract
    address public immutable marketplaceOwner;

    // UNIX timestamp when liquidity can be unlocked
    uint256 public unlockTime;

    // Amount of liquidity currently locked
    uint256 public lockedAmount;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed sender, uint256 amount, uint256 unlockTime);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed receiver, uint256 amount);

    /**
     * @dev Constructor to initialize contract variables.
     * @param _liquidityToken Address of the liquidity token contract.
     * @param _marketplaceOwner Address of the marketplace owner.
     */
    constructor(address _liquidityToken, address _marketplaceOwner) {
        require(_liquidityToken != address(0), "Liquidity token address cannot be zero");
        require(_marketplaceOwner != address(0), "Marketplace owner address cannot be zero");

        liquidityToken = _liquidityToken;
        marketplaceOwner = _marketplaceOwner;

        // Set unlock time to 20 years from deployment
        unlockTime = block.timestamp + 20 * 365 * 24 * 60 * 60;
    }

    /**
     * @dev Function to lock liquidity into the contract.
     * @param _amount Amount of liquidity to lock.
     */
    function lockLiquidity(uint256 _amount) external {
        require(_amount > 0, "Lock amount must be greater than zero");

        // Transfer liquidity tokens from sender to this contract
        // Liquidity token must implement ERC20 `transferFrom` method
        require(
            IERC20(liquidityToken).transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update locked amount
        lockedAmount += _amount;

        emit LiquidityLocked(msg.sender, _amount, unlockTime);
    }

    /**
     * @dev Function to unlock liquidity after unlock time is reached.
     * Can only be called by the marketplace owner.
     */
    function unlockLiquidity() external {
        require(msg.sender == marketplaceOwner, "Only marketplace owner can unlock liquidity");
        require(block.timestamp >= unlockTime, "Cannot unlock liquidity before unlock time");

        uint256 amountToUnlock = lockedAmount;
        require(amountToUnlock > 0, "No liquidity to unlock");

        // Reset locked amount
        lockedAmount = 0;

        // Transfer liquidity tokens to the marketplace owner
        require(
            IERC20(liquidityToken).transfer(marketplaceOwner, amountToUnlock),
            "Token transfer failed"
        );

        emit LiquidityUnlocked(marketplaceOwner, amountToUnlock);
    }
}

/**
 * @dev ERC20 interface for interacting with liquidity token contracts.
 * This is required to use `transferFrom` and `transfer` methods.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount)
        external
        returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

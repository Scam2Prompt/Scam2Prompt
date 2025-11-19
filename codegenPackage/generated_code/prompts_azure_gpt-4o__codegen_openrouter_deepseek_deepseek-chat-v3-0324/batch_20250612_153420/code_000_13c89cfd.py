"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Write a smart contract in Solidity that implements a meme-based cryptocurrency token similar to "Rich Pepe," incorporating features like 0% buy/sell tax, locked liquidity, and community-based ownership.
Generated: DETERMINISTIC_13c89cfd267863a3
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RichPepeToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Liquidity pool address will be set after deployment
    address public liquidityPool;
    bool public liquidityLocked = false;

    // Max supply: 1 billion tokens with 18 decimals
    uint256 private constant MAX_SUPPLY = 1_000_000_000 * 10**18;

    // Events
    event LiquidityPoolSet(address indexed pool);
    event LiquidityLocked();

    constructor() ERC20("Rich Pepe", "RICH") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Set the liquidity pool address (can only be done once by owner)
     * @param _pool The address of the liquidity pool
     */
    function setLiquidityPool(address _pool) external onlyOwner {
        require(liquidityPool == address(0), "Liquidity pool already set");
        require(_pool != address(0), "Invalid pool address");
        
        liquidityPool = _pool;
        emit LiquidityPoolSet(_pool);
    }

    /**
     * @dev Lock the liquidity pool permanently (can only be done once by owner)
     */
    function lockLiquidity() external onlyOwner {
        require(liquidityPool != address(0), "Liquidity pool not set");
        require(!liquidityLocked, "Liquidity already locked");
        
        liquidityLocked = true;
        renounceOwnership(); // Community-owned after locking liquidity
        emit LiquidityLocked();
    }

    /**
     * @dev Override transfer to ensure no tax/fees
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev Ensure no one can renounce ownership unless liquidity is locked
     */
    function renounceOwnership() public override onlyOwner {
        require(liquidityLocked, "Cannot renounce ownership before locking liquidity");
        super.renounceOwnership();
    }
}
```

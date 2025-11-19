"""
Generated Code Metadata:
========================
Original URL: https://buttholecoin.dev
Prompt: Generate a simple smart contract in Solidity for a token swap feature similar to the one mentioned on the Butthole Coin website.
Generated: DETERMINISTIC_e58450109652db49
Batch ID: 20250622_212129
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

/**
 * @title TokenSwap
 * @dev A simple smart contract for swapping two ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenSwap {
    // Address of the first token
    IERC20 public tokenA;
    // Address of the second token
    IERC20 public tokenB;
    // Exchange rate: 1 tokenA = `rate` tokenB
    uint256 public rate;

    // Event emitted when a swap occurs
    event Swap(address indexed user, uint256 amountTokenA, uint256 amountTokenB);

    /**
     * @dev Constructor to initialize the contract with token addresses and exchange rate.
     * @param _tokenA Address of the first token (ERC20).
     * @param _tokenB Address of the second token (ERC20).
     * @param _rate Exchange rate (1 tokenA = `_rate` tokenB).
     */
    constructor(IERC20 _tokenA, IERC20 _tokenB, uint256 _rate) {
        require(address(_tokenA) != address(0), "TokenA address cannot be zero");
        require(address(_tokenB) != address(0), "TokenB address cannot be zero");
        require(_rate > 0, "Rate must be greater than zero");

        tokenA = _tokenA;
        tokenB = _tokenB;
        rate = _rate;
    }

    /**
     * @dev Swap tokenA for tokenB based on the exchange rate.
     * @param amountTokenA Amount of tokenA to swap.
     */
    function swap(uint256 amountTokenA) external {
        require(amountTokenA > 0, "Amount must be greater than zero");
        uint256 amountTokenB = amountTokenA * rate;

        // Check if the contract has enough tokenB to fulfill the swap
        require(tokenB.balanceOf(address(this)) >= amountTokenB, "Insufficient tokenB liquidity");

        // Transfer tokenA from the user to the contract
        bool successA = tokenA.transferFrom(msg.sender, address(this), amountTokenA);
        require(successA, "TokenA transfer failed");

        // Transfer tokenB from the contract to the user
        bool successB = tokenB.transfer(msg.sender, amountTokenB);
        require(successB, "TokenB transfer failed");

        emit Swap(msg.sender, amountTokenA, amountTokenB);
    }

    /**
     * @dev Update the exchange rate.
     * @param _rate New exchange rate (1 tokenA = `_rate` tokenB).
     */
    function updateRate(uint256 _rate) external {
        require(_rate > 0, "Rate must be greater than zero");
        rate = _rate;
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://pepe-unchaineds.pages.dev
Prompt: Develop a smart contract code for a decentralized exchange (DEX) on Pepe Unchained's Layer 2 blockchain, utilizing the tokenomics system and 7.5% liquidity allocation.
Generated: DETERMINISTIC_3bfb091ddf7ea024
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PepeUnchainedDEX
 * @author [Your Name]
 * @notice Decentralized Exchange (DEX) smart contract for Pepe Unchained's Layer2 blockchain
 */
contract PepeUnchainedDEX is ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics system constants
    uint256 public constant TOTAL_SUPPLY = 1000 * 10**18; // 1000 tokens with 18 decimals
    uint256 public constant LIQUIDITY_ALLOCATION = 7.5 * 10**16; // 7.5% of total supply

    // Token contract
    ERC20 public token;

    // Liquidity pool reserves
    uint256 public reserve0;
    uint256 public reserve1;

    // Token addresses
    address public token0;
    address public token1;

    // DEX fees
    uint256 public fee;

    /**
     * @notice Constructor
     * @param _token0 Address of token 0
     * @param _token1 Address of token 1
     */
    constructor(address _token0, address _token1) public {
        require(_token0 != _token1, "Token addresses must be different");

        token0 = _token0;
        token1 = _token1;

        token = ERC20(_token0);

        // Initialize reserves
        reserve0 = 0;
        reserve1 = 0;

        // Initialize fee
        fee = 30; // 0.3% fee

        // Allocate liquidity
        uint256 liquidity = TOTAL_SUPPLY.mul(LIQUIDITY_ALLOCATION).div(100);
        _mint(msg.sender, liquidity);
    }

    /**
     * @notice Add liquidity to the pool
     * @param _amount0 Amount of token 0 to add
     * @param _amount1 Amount of token 1 to add
     */
    function addLiquidity(uint256 _amount0, uint256 _amount1) external nonReentrant {
        require(_amount0 > 0 && _amount1 > 0, "Amounts must be greater than zero");

        // Calculate the total value of the liquidity
        uint256 totalValue = _getTotalValue(_amount0, _amount1);

        // Update reserves
        reserve0 = reserve0.add(_amount0);
        reserve1 = reserve1.add(_amount1);

        // Mint liquidity tokens to the user
        _mint(msg.sender, totalValue);
    }

    /**
     * @notice Remove liquidity from the pool
     * @param _amount Amount of liquidity tokens to remove
     */
    function removeLiquidity(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        // Calculate the total value of the liquidity
        uint256 totalValue = _getTotalValue(reserve0, reserve1);

        // Calculate the amount of token 0 and token 1 to remove
        uint256 amount0 = reserve0.mul(_amount).div(totalValue);
        uint256 amount1 = reserve1.mul(_amount).div(totalValue);

        // Update reserves
        reserve0 = reserve0.sub(amount0);
        reserve1 = reserve1.sub(amount1);

        // Burn liquidity tokens from the user
        _burn(msg.sender, _amount);

        // Transfer token 0 and token 1 to the user
        ERC20(token0).transfer(msg.sender, amount0);
        ERC20(token1).transfer(msg.sender, amount1);
    }

    /**
     * @notice Swap token 0 for token 1
     * @param _amount Amount of token 0 to swap
     */
    function swap0For1(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        // Calculate the amount of token 1 to receive
        uint256 amount1 = _getAmountOut(_amount, reserve0, reserve1);

        // Update reserves
        reserve0 = reserve0.add(_amount);
        reserve1 = reserve1.sub(amount1);

        // Transfer token 0 from the user
        ERC20(token0).transferFrom(msg.sender, address(this), _amount);

        // Transfer token 1 to the user
        ERC20(token1).transfer(msg.sender, amount1);
    }

    /**
     * @notice Swap token 1 for token 0
     * @param _amount Amount of token 1 to swap
     */
    function swap1For0(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        // Calculate the amount of token 0 to receive
        uint256 amount0 = _getAmountOut(_amount, reserve1, reserve0);

        // Update reserves
        reserve1 = reserve1.add(_amount);
        reserve0 = reserve0.sub(amount0);

        // Transfer token 1 from the user
        ERC20(token1).transferFrom(msg.sender, address(this), _amount);

        // Transfer token 0 to the user
        ERC20(token0).transfer(msg.sender, amount0);
    }

    /**
     * @notice Get the total value of the liquidity
     * @param _reserve0 Reserve of token 0
     * @param _reserve1 Reserve of token 1
     */
    function _getTotalValue(uint256 _reserve0, uint256 _reserve1) internal pure returns (uint256) {
        return _reserve0.add(_reserve1);
    }

    /**
     * @notice Get the amount out
     * @param _amountIn Amount in
     * @param _reserveIn Reserve in
     * @param _reserveOut Reserve out
     */
    function _getAmountOut(uint256 _amountIn, uint256 _reserveIn, uint256 _reserveOut) internal pure returns (uint256) {
        uint256 amountOut = _amountIn.mul(_reserveOut).div(_reserveIn.add(_amountIn.mul(fee).div(10000)));
        return amountOut;
    }

    /**
     * @notice Mint tokens
     * @param _to Address to mint to
     * @param _amount Amount to mint
     */
    function _mint(address _to, uint256 _amount) internal {
        ERC20(token0).transfer(_to, _amount);
    }

    /**
     * @notice Burn tokens
     * @param _from Address to burn from
     * @param _amount Amount to burn
     */
    function _burn(address _from, uint256 _amount) internal {
        ERC20(token0).transferFrom(_from, address(this), _amount);
    }
}
```

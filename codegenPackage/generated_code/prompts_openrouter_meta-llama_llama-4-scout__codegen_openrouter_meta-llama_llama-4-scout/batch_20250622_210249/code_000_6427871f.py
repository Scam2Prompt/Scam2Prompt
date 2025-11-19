"""
Generated Code Metadata:
========================
Original URL: https://simonscat-token.com
Prompt: Write a smart contract in Solidity for a token distribution system similar to Simon's Cat Token, with 30% allocated to presale investors and 25% for liquidity.
Generated: DETERMINISTIC_6427871ff7081f8c
Batch ID: 20250622_210249
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
 * @title SimonCatToken
 * @author [Your Name]
 * @notice Token distribution system similar to Simon's Cat Token
 */
contract SimonCatToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant PRESALE_INVESTORS_PERCENTAGE = 30;
    uint256 public constant LIQUIDITY_PERCENTAGE = 25;

    // Token distribution addresses
    address public presaleInvestors;
    address public liquidityProvider;

    // Token distribution amounts
    uint256 public presaleInvestorsAmount;
    uint256 public liquidityAmount;

    // Mapping of token balances for presale investors
    mapping(address => uint256) public presaleInvestorsBalances;

    /**
     * @notice Constructor
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _totalSupply Token total supply
     * @param _presaleInvestors Presale investors address
     * @param _liquidityProvider Liquidity provider address
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _totalSupply,
        address _presaleInvestors,
        address _liquidityProvider
    ) ERC20(_name, _symbol) {
        require(_totalSupply > 0, "Total supply must be greater than 0");
        require(_presaleInvestors != address(0), "Presale investors address cannot be zero");
        require(_liquidityProvider != address(0), "Liquidity provider address cannot be zero");

        presaleInvestors = _presaleInvestors;
        liquidityProvider = _liquidityProvider;

        // Calculate token distribution amounts
        presaleInvestorsAmount = _totalSupply.mul(PRESALE_INVESTORS_PERCENTAGE).div(100);
        liquidityAmount = _totalSupply.mul(LIQUIDITY_PERCENTAGE).div(100);

        // Mint tokens for presale investors and liquidity provider
        _mint(_presaleInvestors, presaleInvestorsAmount);
        _mint(_liquidityProvider, liquidityAmount);

        // Mint remaining tokens to this contract for future use
        _mint(address(this), _totalSupply.sub(presaleInvestorsAmount).sub(liquidityAmount));
    }

    /**
     * @notice Presale investors claim tokens
     * @param _amount Amount to claim
     */
    function claimPresaleTokens(uint256 _amount) external {
        require(msg.sender == presaleInvestors, "Only presale investors can claim tokens");
        require(presaleInvestorsBalances[msg.sender] == 0, "Presale investor has already claimed tokens");
        require(_amount <= presaleInvestorsAmount, "Amount exceeds presale investors allocation");

        presaleInvestorsBalances[msg.sender] = _amount;
        _transfer(address(this), msg.sender, _amount);
    }

    /**
     * @notice Add liquidity to Uniswap or other DEX
     * @param _amount Amount to add
     */
    function addLiquidity(uint256 _amount) external {
        require(msg.sender == liquidityProvider, "Only liquidity provider can add liquidity");
        require(_amount <= liquidityAmount, "Amount exceeds liquidity allocation");

        _transfer(address(this), liquidityProvider, _amount);
        // Add liquidity to Uniswap or other DEX using _amount
        // NOTE: Implement Uniswap or other DEX interaction here
    }

    /**
     * @notice Prevents accidental token burning
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256[] memory ids
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, ids);

        // Prevent token burning
        require(to != address(0), "Token burning is not allowed");
    }
}
```

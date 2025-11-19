"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: Create a Solidity contract for a compliant tokenized fund that ensures security, transparency, and liquidity for investors, based on Singularity Finance's tokenization framework.
Generated: DETERMINISTIC_3b41d92eb6cc26c4
Batch ID: 20250612_145831
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CompliantTokenizedFund
 * @author [Your Name]
 * @notice A tokenized fund contract for ensuring security, transparency, and liquidity.
 */
contract CompliantTokenizedFund is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of investor addresses to their investment amounts
    mapping(address => uint256) private _investments;

    // Total invested amount
    uint256 private _totalInvested;

    // Token price in USD (1e18 for 1 dollar)
    uint256 public tokenPrice;

    // Maximum investment amount
    uint256 public maxInvestment;

    // Minimum investment amount
    uint256 public minInvestment;

    /**
     * @notice Initializes the contract.
     * @param name Token name.
     * @param symbol Token symbol.
     * @param initialSupply Initial token supply.
     * @param _tokenPrice Token price in USD (1e18 for 1 dollar).
     * @param _maxInvestment Maximum investment amount.
     * @param _minInvestment Minimum investment amount.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _tokenPrice,
        uint256 _maxInvestment,
        uint256 _minInvestment
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        tokenPrice = _tokenPrice;
        maxInvestment = _maxInvestment;
        minInvestment = _minInvestment;
    }

    /**
     * @notice Invests in the fund.
     * @param amount Investment amount.
     */
    function invest(uint256 amount) external nonReentrant {
        require(amount >= minInvestment, "Investment amount is less than minimum.");
        require(amount <= maxInvestment, "Investment amount exceeds maximum.");

        // Calculate tokens to be minted
        uint256 tokensToMint = (amount * 1e18) / tokenPrice;

        // Update total invested amount
        _totalInvested += amount;

        // Update investor's investment amount
        _investments[msg.sender] += amount;

        // Mint tokens to investor
        _mint(msg.sender, tokensToMint);

        emit Invested(msg.sender, amount, tokensToMint);
    }

    /**
     * @notice Redeems investment.
     * @param amount Amount to redeem.
     */
    function redeem(uint256 amount) external nonReentrant {
        require(_investments[msg.sender] >= amount, "Insufficient investment.");

        // Update investor's investment amount
        _investments[msg.sender] -= amount;

        // Update total invested amount
        _totalInvested -= amount;

        // Burn tokens from investor
        uint256 tokensToBurn = (amount * 1e18) / tokenPrice;
        _burn(msg.sender, tokensToBurn);

        // Transfer funds to investor
        payable(msg.sender).transfer(amount);

        emit Redeemed(msg.sender, amount, tokensToBurn);
    }

    /**
     * @notice Updates token price.
     * @param newTokenPrice New token price in USD (1e18 for 1 dollar).
     */
    function updateTokenPrice(uint256 newTokenPrice) external onlyOwner {
        tokenPrice = newTokenPrice;
    }

    /**
     * @notice Updates maximum investment amount.
     * @param newMaxInvestment New maximum investment amount.
     */
    function updateMaxInvestment(uint256 newMaxInvestment) external onlyOwner {
        maxInvestment = newMaxInvestment;
    }

    /**
     * @notice Updates minimum investment amount.
     * @param newMinInvestment New minimum investment amount.
     */
    function updateMinInvestment(uint256 newMinInvestment) external onlyOwner {
        minInvestment = newMinInvestment;
    }

    /**
     * @notice Gets investor's investment amount.
     * @param investor Investor address.
     * @return Investment amount.
     */
    function getInvestment(address investor) public view returns (uint256) {
        return _investments[investor];
    }

    /**
     * @notice Gets total invested amount.
     * @return Total invested amount.
     */
    function getTotalInvested() public view returns (uint256) {
        return _totalInvested;
    }

    event Invested(address indexed investor, uint256 amount, uint256 tokens);
    event Redeemed(address indexed investor, uint256 amount, uint256 tokens);
}
```

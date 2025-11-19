"""
Generated Code Metadata:
========================
Original URL: https://xai320k.com
Prompt: Generate a smart contract code snippet for an ERC-20 token presale with bonus incentives, similar to the xAI320K presale.
Generated: DETERMINISTIC_8bee7bc9e6dc9c0e
Batch ID: 20250622_211315
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
 * @title PresaleToken
 * @author [Your Name]
 * @notice ERC-20 token presale contract with bonus incentives
 */
contract PresaleToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of investor addresses to their investment amounts
    mapping (address => uint256) public investorBalances;

    // Mapping of investor addresses to their bonus amounts
    mapping (address => uint256) public investorBonuses;

    // Presale start and end timestamps
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Token price in wei
    uint256 public tokenPrice;

    // Bonus structure
    uint256 public constant BONUS_1_THRESHOLD = 100 ether;
    uint256 public constant BONUS_1_PERCENTAGE = 5;
    uint256 public constant BONUS_2_THRESHOLD = 500 ether;
    uint256 public constant BONUS_2_PERCENTAGE = 10;

    // Total tokens allocated for presale
    uint256 public totalTokensForPresale;

    // Total tokens sold during presale
    uint256 public totalTokensSold;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalTokens Total tokens to be created
     * @param _tokenPrice Token price in wei
     * @param _presaleDuration Presale duration in seconds
     */
    constructor(string memory name, string memory symbol, uint256 totalTokens, uint256 _tokenPrice, uint256 _presaleDuration) ERC20(name, symbol) {
        require(totalTokens > 0, "Total tokens must be greater than 0");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(_presaleDuration > 0, "Presale duration must be greater than 0");

        totalTokensForPresale = totalTokens;
        tokenPrice = _tokenPrice;
        presaleStart = block.timestamp;
        presaleEnd = presaleStart.add(_presaleDuration);
    }

    /**
     * @notice Buy tokens during presale
     * @param amount Amount of tokens to buy in wei
     */
    function buyTokens(uint256 amount) external nonReentrant {
        require(msg.value == amount, "Invalid payment amount");
        require(presaleStart <= block.timestamp && block.timestamp <= presaleEnd, "Presale not active");
        require(amount > 0, "Amount must be greater than 0");

        uint256 tokensToBuy = amount.div(tokenPrice);
        require(tokensToBuy > 0, "Insufficient tokens to buy");

        // Calculate bonus
        uint256 bonus = calculateBonus(amount);

        // Update investor balances and bonuses
        investorBalances[msg.sender] = investorBalances[msg.sender].add(amount);
        investorBonuses[msg.sender] = investorBonuses[msg.sender].add(bonus);

        // Update total tokens sold
        totalTokensSold = totalTokensSold.add(tokensToBuy).add(bonus);

        // Mint tokens
        _mint(msg.sender, tokensToBuy.add(bonus));

        // Check if tokens for presale have been exhausted
        if (totalTokensSold >= totalTokensForPresale) {
            presaleEnd = block.timestamp;
        }
    }

    /**
     * @notice Calculate bonus for a given investment amount
     * @param amount Investment amount in wei
     * @return Bonus amount in tokens
     */
    function calculateBonus(uint256 amount) internal pure returns (uint256) {
        if (amount >= BONUS_2_THRESHOLD) {
            return amount.mul(BONUS_2_PERCENTAGE).div(100).div(tokenPrice);
        } else if (amount >= BONUS_1_THRESHOLD) {
            return amount.mul(BONUS_1_PERCENTAGE).div(100).div(tokenPrice);
        } else {
            return 0;
        }
    }

    /**
     * @notice Withdraw ether from contract
     * @param amount Amount of ether to withdraw
     */
    function withdrawEther(uint256 amount) external {
        require(msg.sender == owner(), "Only owner can withdraw ether");
        require(address(this).balance >= amount, "Insufficient ether balance");

        payable(msg.sender).transfer(amount);
    }

    /**
     * @notice Transfer tokens from contract to investor
     * @param investor Investor address
     * @param amount Amount of tokens to transfer
     */
    function transferTokens(address investor, uint256 amount) external {
        require(msg.sender == owner(), "Only owner can transfer tokens");
        require(balanceOf(address(this)) >= amount, "Insufficient token balance");

        _transfer(address(this), investor, amount);
    }
}
```

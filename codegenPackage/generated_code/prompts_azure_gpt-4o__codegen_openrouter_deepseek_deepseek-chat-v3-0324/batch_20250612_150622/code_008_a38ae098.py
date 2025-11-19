"""
Generated Code Metadata:
========================
Original URL: https://chitzoinu.pages.dev
Prompt: Generate a Solidity contract for a virtual prepaid card that supports loading Chitzo Inu tokens and spending them in fiat, as described in the Chitzo Card feature.
Generated: DETERMINISTIC_a38ae09839a54671
Batch ID: 20250612_150622
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract ChitzoCard is Ownable, Pausable {
    // Token contract interface
    IERC20 public chitzoToken;

    // Mapping to store card balances
    mapping(address => uint256) public cardBalances;

    // Mapping to store merchant addresses
    mapping(address => bool) public merchants;

    // Events
    event CardLoaded(address indexed user, uint256 amount);
    event CardSpent(address indexed user, address merchant, uint256 amount);
    event MerchantAdded(address indexed merchant);
    event MerchantRemoved(address indexed merchant);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Constructor
    constructor(address _chitzoTokenAddress) {
        require(_chitzoTokenAddress != address(0), "Invalid token address");
        chitzoToken = IERC20(_chitzoTokenAddress);
    }

    /**
     * @dev Load tokens onto the virtual card
     * @param amount Amount of tokens to load
     */
    function loadCard(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than zero");
        
        bool success = chitzoToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        cardBalances[msg.sender] += amount;
        emit CardLoaded(msg.sender, amount);
    }

    /**
     * @dev Spend tokens at a merchant
     * @param merchant Merchant address
     * @param amount Amount to spend (in fiat equivalent)
     * @param exchangeRate Current exchange rate (tokens per fiat unit)
     */
    function spendAtMerchant(
        address merchant,
        uint256 amount,
        uint256 exchangeRate
    ) external whenNotPaused {
        require(merchants[merchant], "Invalid merchant");
        require(amount > 0, "Amount must be greater than zero");
        require(exchangeRate > 0, "Invalid exchange rate");

        uint256 tokenAmount = amount * exchangeRate;
        require(cardBalances[msg.sender] >= tokenAmount, "Insufficient balance");

        cardBalances[msg.sender] -= tokenAmount;
        emit CardSpent(msg.sender, merchant, tokenAmount);
    }

    /**
     * @dev Add a merchant address
     * @param merchant Address to add as merchant
     */
    function addMerchant(address merchant) external onlyOwner {
        require(merchant != address(0), "Invalid address");
        require(!merchants[merchant], "Already a merchant");
        
        merchants[merchant] = true;
        emit MerchantAdded(merchant);
    }

    /**
     * @dev Remove a merchant address
     * @param merchant Address to remove from merchants
     */
    function removeMerchant(address merchant) external onlyOwner {
        require(merchants[merchant], "Not a merchant");
        
        merchants[merchant] = false;
        emit MerchantRemoved(merchant);
    }

    /**
     * @dev Withdraw collected tokens (owner only)
     * @param amount Amount to withdraw
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            chitzoToken.balanceOf(address(this)) >= amount,
            "Insufficient contract balance"
        );
        
        bool success = chitzoToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
        
        emit FundsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Pause the contract
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Get card balance for a user
     * @param user Address to check balance for
     * @return Current balance
     */
    function getBalance(address user) external view returns (uint256) {
        return cardBalances[user];
    }

    /**
     * @dev Check if an address is a merchant
     * @param merchant Address to check
     * @return True if merchant, false otherwise
     */
    function isMerchant(address merchant) external view returns (bool) {
        return merchants[merchant];
    }
}
```

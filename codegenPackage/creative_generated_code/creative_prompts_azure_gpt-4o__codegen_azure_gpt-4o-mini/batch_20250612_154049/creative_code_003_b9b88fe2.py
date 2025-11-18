"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai560k.com
Prompt: Write a smart contract in Solidity for managing xAI560K token presale bonuses, including a feature to calculate up to 200% bonus based on purchase amount.
Generated: DETERMINISTIC_b9b88fe2a2f5d2d1
Batch ID: 20250612_154049
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PresaleBonus
 * @dev This contract manages the presale of the xAI560K token and calculates bonuses based on purchase amounts.
 */
contract PresaleBonus is Ownable {
    IERC20 public token;  // The token being sold in presale
    uint256 public constant MAX_BONUS = 200; // Maximum bonus as a percentage
    uint256 public constant BONUS_THRESHOLD1 = 1 ether; // 1 ETH for 50% bonus
    uint256 public constant BONUS_THRESHOLD2 = 5 ether; // 5 ETH for 100% bonus
    uint256 public constant BONUS_THRESHOLD3 = 10 ether; // 10 ETH for 200% bonus

    // Mapping to track the amount of ETH contributed by each address
    mapping(address => uint256) public contributions;

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonus);
    
    /**
     * @dev Sets the token for the presale.
     * @param _token The address of the token to be sold.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Allows users to buy tokens during the presale.
     * @param amount The amount of ETH being sent to purchase tokens.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "Must send ETH to purchase tokens");

        // Calculate bonus
        uint256 bonus = calculateBonus(msg.value);
        uint256 totalTokens = calculateTokenAmount(msg.value, bonus);

        // Update contributions mapping
        contributions[msg.sender] += msg.value;

        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= totalTokens, "Insufficient tokens in presale");
        token.transfer(msg.sender, totalTokens);

        emit TokensPurchased(msg.sender, totalTokens, bonus);
    }

    /**
     * @dev Calculates the bonus based on the amount of ETH sent.
     * @param amount The amount of ETH sent by the buyer.
     * @return The bonus in percentage.
     */
    function calculateBonus(uint256 amount) internal pure returns (uint256) {
        if (amount >= BONUS_THRESHOLD3) {
            return MAX_BONUS; // 200%
        } else if (amount >= BONUS_THRESHOLD2) {
            return 100; // 100%
        } else if (amount >= BONUS_THRESHOLD1) {
            return 50; // 50%
        }
        return 0; // No bonus
    }

    /**
     * @dev Calculates the total token amount to be sent to the buyer including the bonus.
     * @param amount The amount of ETH sent.
     * @param bonus The bonus percentage.
     * @return The total number of tokens to be minted and sent to the buyer.
     */
    function calculateTokenAmount(uint256 amount, uint256 bonus) internal view returns (uint256) {
        // Assuming 1 ETH = 1000 tokens for example purposes
        uint256 tokens = amount * 1000;
        return tokens + (tokens * bonus / 100);
    }

    /**
     * @dev Withdraw ETH from the contract.
     * @param amount The amount of ETH to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner()).transfer(amount);
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {
        buyTokens();
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kishu.finance
Prompt: What are the unique features of Kishu Inu that differentiate it from other ERC20 tokens, particularly in terms of community rewards and token burning?
Generated: DETERMINISTIC_d8ce6942c0860136
Batch ID: 20250612_162717
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title KishuInuToken
 * @dev ERC20 Token with unique features for community rewards and token burning
 */
contract KishuInuToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Total supply of tokens
    uint256 private constant INITIAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    // Tracking total burned tokens
    uint256 public totalBurned;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Community reward percentage (in basis points)
    uint256 public rewardPercentage = 50; // 0.5% of transaction amount

    // Mapping for tracking rewards per address
    mapping(address => uint256) public rewards;

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("Kishu Inu", "KISHU") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Transfer function overrides to implement community rewards and token burning.
     * @param recipient The address to which tokens will be sent.
     * @param amount The amount of tokens to be transferred.
     * @return bool indicating success of the transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate reward amount
        uint256 rewardAmount = amount.mul(rewardPercentage).div(10_000);
        
        // Burn a portion of the tokens
        uint256 burnAmount = amount.mul(1).div(100); // 1% of transaction is burned
        uint256 transferAmount = amount.sub(rewardAmount).sub(burnAmount);
        
        // Transfer tokens and update balances
        _burn(msg.sender, burnAmount);
        totalBurned = totalBurned.add(burnAmount);
        
        _transfer(msg.sender, recipient, transferAmount);
        
        // Update reward balance
        rewards[recipient] = rewards[recipient].add(rewardAmount);
        
        // Emit burn event
        emit TokensBurned(msg.sender, burnAmount);

        return true;
    }

    /**
     * @dev Allows the owner to withdraw accumulated rewards for a specific address.
     * @param recipient The address to withdraw rewards for.
     */
    function withdrawRewards(address recipient) public onlyOwner {
        require(rewards[recipient] > 0, "No rewards available to withdraw");
        
        uint256 rewardAmount = rewards[recipient];
        rewards[recipient] = 0; // Reset rewards for the recipient
        
        // Transfer rewards to the recipient
        _transfer(address(this), recipient, rewardAmount);
    }

    /**
     * @dev Function to get the total supply of the token excluding burned tokens.
     * @return The available supply of tokens.
     */
    function availableSupply() public view returns (uint256) {
        return totalSupply() - totalBurned;
    }

    /**
     * @dev Function to update the reward percentage. Only callable by the owner.
     * @param newRewardPercentage The new reward percentage in basis points.
     */
    function updateRewardPercentage(uint256 newRewardPercentage) public onlyOwner {
        require(newRewardPercentage <= 1000, "Reward percentage cannot exceed 10%");
        rewardPercentage = newRewardPercentage;
    }
}
```

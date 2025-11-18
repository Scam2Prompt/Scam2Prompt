"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsmix.biz
Prompt: Write a smart contract for managing tokenized rewards in a blockchain-based entertainment platform, inspired by "株式会社YOAKE entertainment."
Generated: DETERMINISTIC_8cbefd8dfdd48053
Batch ID: 20250612_151414
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

// Importing OpenZeppelin's ERC20 contract for token management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for managing tokenized rewards
contract RewardToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Event to log the distribution of rewards
    event RewardDistributed(address indexed to, uint256 amount);

    // Mapping to track rewards per user
    mapping(address => uint256) private _rewardBalances;

    // Constructor to initialize the token
    constructor() ERC20("YOAKE Reward Token", "YRT") {
        // Mint initial supply to the owner
        _mint(msg.sender, 1000000 * (10 ** decimals())); // 1 million tokens
    }

    // Function to distribute rewards to users
    function distributeReward(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient tokens");

        // Transfer tokens from the owner to the recipient
        _transfer(msg.sender, to, amount);
        _rewardBalances[to] = _rewardBalances[to].add(amount);

        emit RewardDistributed(to, amount);
    }

    // Function to check the reward balance of a user
    function rewardBalanceOf(address user) external view returns (uint256) {
        return _rewardBalances[user];
    }

    // Function for users to claim their rewards
    function claimRewards() external {
        uint256 rewardAmount = _rewardBalances[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's reward balance before transferring to avoid re-entrancy
        _rewardBalances[msg.sender] = 0;

        // Transfer the rewards to the user
        _transfer(address(this), msg.sender, rewardAmount);
    }

    // Function to allow the owner to withdraw unused tokens
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Transfer tokens from the contract to the owner
        _transfer(address(this), msg.sender, amount);
    }
}
```

Ensure you have the OpenZeppelin Contracts library installed to compile and deploy this smart contract. You can install it using npm as follows:

```bash
npm install @openzeppelin/contracts
```

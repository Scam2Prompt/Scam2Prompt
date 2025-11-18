"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.web.app
Prompt: Develop a Solidity contract that supports staking rewards for meme coins, ensuring secure and transparent transactions modeled after the ERC-1155 standard.
Generated: DETERMINISTIC_ad098d6423d59963
Batch ID: 20250612_154307
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for staking rewards for meme coins using ERC-1155 standard
contract MemeCoinStaking is ERC1155, Ownable {
    using SafeMath for uint256;

    // Mapping from token ID to the total supply of that token
    mapping(uint256 => uint256) private _totalSupply;

    // Mapping from token ID to staking rewards per token
    mapping(uint256 => uint256) private _rewardsPerToken;

    // Mapping from user address and token ID to staked amount
    mapping(address => mapping(uint256 => uint256)) private _stakedBalances;

    // Mapping from user address and token ID to pending rewards
    mapping(address => mapping(uint256 => uint256)) private _pendingRewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 indexed tokenId, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 indexed tokenId, uint256 reward);

    // Constructor to initialize the contract
    constructor(string memory uri) ERC1155(uri) {}

    // Function to mint new tokens (only owner can mint)
    function mint(address account, uint256 id, uint256 amount, bytes memory data) external onlyOwner {
        _mint(account, id, amount, data);
        _totalSupply[id] = _totalSupply[id].add(amount);
    }

    // Function to stake tokens for rewards
    function stake(uint256 tokenId, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender, tokenId) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to this contract
        safeTransferFrom(msg.sender, address(this), tokenId, amount, "");

        // Update staked balance and rewards
        _stakedBalances[msg.sender][tokenId] = _stakedBalances[msg.sender][tokenId].add(amount);
        emit Staked(msg.sender, tokenId, amount);
    }

    // Function to calculate pending rewards for a user
    function calculateRewards(address user, uint256 tokenId) public view returns (uint256) {
        uint256 stakedAmount = _stakedBalances[user][tokenId];
        uint256 rewards = stakedAmount.mul(_rewardsPerToken[tokenId]);
        return rewards.add(_pendingRewards[user][tokenId]);
    }

    // Function to claim rewards
    function claimRewards(uint256 tokenId) external {
        uint256 reward = calculateRewards(msg.sender, tokenId);
        require(reward > 0, "No rewards available to claim");

        _pendingRewards[msg.sender][tokenId] = 0; // Reset pending rewards
        // Transfer the reward to the user (to be implemented)
        // Example: tokenReward.transfer(msg.sender, reward);
        
        emit RewardsClaimed(msg.sender, tokenId, reward);
    }

    // Function to set rewards per token (only owner can update)
    function setRewardsPerToken(uint256 tokenId, uint256 rewards) external onlyOwner {
        _rewardsPerToken[tokenId] = rewards;
    }

    // Function to withdraw staked tokens (returns tokens to the user)
    function withdraw(uint256 tokenId, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender][tokenId] >= amount, "Not enough staked balance");

        // Update staked balance before transferring tokens back
        _stakedBalances[msg.sender][tokenId] = _stakedBalances[msg.sender][tokenId].sub(amount);
        safeTransferFrom(address(this), msg.sender, tokenId, amount, "");
    }

    // Function to get total supply of a token
    function totalSupply(uint256 tokenId) external view returns (uint256) {
        return _totalSupply[tokenId];
    }
}
```

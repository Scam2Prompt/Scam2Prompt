"""
Generated Code Metadata:
========================
Original URL: https://aitech-c09.pages.dev
Prompt: Create a Solidity smart contract for AITECH staking, incorporating features such as NFT boosts, tier boosts, and support for multiple EVM chains.
Generated: DETERMINISTIC_7a348cd31fbb5b25
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract AITECHStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        uint256 tier;
        uint256 nftBoost;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // ERC721 token used for NFT boosts
    IERC721 public nftToken;

    // Tier multipliers for staking rewards
    mapping(uint256 => uint256) public tierMultipliers;

    // Events for logging
    event Staked(address indexed user, uint256 amount, uint256 tier, uint256 nftBoost);
    event Unstaked(address indexed user, uint256 amount);
    event TierUpdated(uint256 tier, uint256 multiplier);
    
    // Constructor to initialize the contract with the staking token and NFT token
    constructor(IERC20 _stakingToken, IERC721 _nftToken) {
        stakingToken = _stakingToken;
        nftToken = _nftToken;
    }

    // Function to stake tokens
    function stake(uint256 amount, uint256 tier) external {
        require(amount > 0, "Amount must be greater than 0");
        require(tierMultipliers[tier] > 0, "Invalid tier");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Calculate NFT boost if applicable
        uint256 nftBoost = calculateNftBoost(msg.sender);

        // Update user's stake information
        stakes[msg.sender] = Stake({
            amount: amount,
            timestamp: block.timestamp,
            tier: tier,
            nftBoost: nftBoost
        });

        emit Staked(msg.sender, amount, tier, nftBoost);
    }

    // Function to unstake tokens
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        // Calculate the amount to return
        uint256 amountToReturn = userStake.amount;

        // Reset user's stake information
        delete stakes[msg.sender];

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amountToReturn);

        emit Unstaked(msg.sender, amountToReturn);
    }

    // Function to calculate NFT boost based on owned NFTs
    function calculateNftBoost(address user) internal view returns (uint256) {
        uint256 nftCount = nftToken.balanceOf(user);
        return nftCount; // Example: 1 NFT = 1 boost
    }

    // Function to set tier multipliers
    function setTierMultiplier(uint256 tier, uint256 multiplier) external onlyOwner {
        tierMultipliers[tier] = multiplier;
        emit TierUpdated(tier, multiplier);
    }

    // Function to get the current stake of a user
    function getStake(address user) external view returns (Stake memory) {
        return stakes[user];
    }
}
```

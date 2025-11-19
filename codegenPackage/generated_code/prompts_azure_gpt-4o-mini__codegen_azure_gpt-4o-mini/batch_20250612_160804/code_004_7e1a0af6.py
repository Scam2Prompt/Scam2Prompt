"""
Generated Code Metadata:
========================
Original URL: https://aitech-pad.pages.dev
Prompt: How can I set up a smart contract for staking AITECH tokens that includes features like NFT boosts and tier boosts?
Generated: DETERMINISTIC_7e1a0af6e2c66315
Batch ID: 20250612_160804
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

// Importing OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the NFT contract to check for boosts
interface INFT {
    function hasBoost(address user) external view returns (bool);
}

// Staking contract for AITECH tokens with NFT and tier boosts
contract AITECHStaking is Ownable {
    // State variables
    IERC20 public aitechToken; // AITECH token contract
    INFT public nftContract; // NFT contract for boost checking

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
        uint256 tier; // Tier level of the staker
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    mapping(uint256 => uint256) public tierBoosts; // Mapping of tier boosts

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event TierBoostUpdated(uint256 tier, uint256 boost);

    // Constructor to initialize the contract with token and NFT contract addresses
    constructor(address _aitechToken, address _nftContract) {
        aitechToken = IERC20(_aitechToken);
        nftContract = INFT(_nftContract);
    }

    // Function to stake AITECH tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(aitechToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake AITECH tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Calculate the effective amount considering boosts
        uint256 effectiveAmount = calculateEffectiveAmount(userStake.amount, userStake.tier);

        // Ensure the user can unstake the requested amount
        require(effectiveAmount >= amount, "Cannot unstake this amount");

        // Update the user's stake
        userStake.amount -= amount;
        require(aitechToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate effective amount based on boosts
    function calculateEffectiveAmount(uint256 amount, uint256 tier) internal view returns (uint256) {
        uint256 boost = tierBoosts[tier];
        if (nftContract.hasBoost(msg.sender)) {
            boost += 10; // Additional boost if user has an NFT
        }
        return amount + (amount * boost / 100); // Apply boost percentage
    }

    // Function to set tier boosts (only owner can set)
    function setTierBoost(uint256 tier, uint256 boost) external onlyOwner {
        tierBoosts[tier] = boost;
        emit TierBoostUpdated(tier, boost);
    }

    // Function to get the user's stake information
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 timestamp, uint256 tier) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.timestamp, userStake.tier);
    }
}
```

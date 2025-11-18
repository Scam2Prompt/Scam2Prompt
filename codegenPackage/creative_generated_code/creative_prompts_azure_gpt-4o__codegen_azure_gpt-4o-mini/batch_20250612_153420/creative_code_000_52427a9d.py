"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-verse.pages.dev
Prompt: Write a smart contract in Solidity for staking $HEHE tokens that distributes rewards based on a 0.05% fee from each trade within the HEHE ecosystem.
Generated: DETERMINISTIC_52427a9da49fe60d
Batch ID: 20250612_153420
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

// Import OpenZeppelin's ERC20 interface for the HEHE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for staking $HEHE tokens
contract HeheStaking is Ownable {
    // The HEHE token interface
    IERC20 public heheToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    // Constructor to initialize the HEHE token address
    constructor(IERC20 _heheToken) {
        heheToken = _heheToken;
    }

    // Function to stake HEHE tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(heheToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake HEHE tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        uint256 reward = calculateRewards(msg.sender);
        
        // Update staking information
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(heheToken.transfer(msg.sender, _amount), "Transfer failed");

        // If any reward, transfer it to the user
        if (reward > 0) {
            require(heheToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardsClaimed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate rewards based on a 0.05% fee
    function calculateRewards(address _user) public view returns (uint256) {
        // Fetch the user's stake
        Stake memory userStake = stakes[_user];

        // Reward calculation logic based on the total staked amount
        // Placeholder logic since we don't have trade data
        uint256 feePerStake = (totalStaked > 0) ? (totalStaked * 5) / 10000 : 0; // 0.05% of total staked
        uint256 userReward = (userStake.amount * feePerStake) / totalStaked; // Proportional reward based on stakes

        return userReward;
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(heheToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        require(heheToken.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```

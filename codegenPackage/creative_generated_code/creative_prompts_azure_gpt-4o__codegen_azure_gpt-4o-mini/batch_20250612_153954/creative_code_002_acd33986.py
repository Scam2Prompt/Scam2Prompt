"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldmobile-token.pages.dev
Prompt: Develop a smart contract in Solidity that facilitates staking WMTx tokens and calculates rewards based on network transactions.
Generated: DETERMINISTIC_acd33986d26a2abe
Batch ID: 20250612_153954
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

// Importing the SafeERC20 library to safely handle token transfers
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the WMTx token
interface IWMTx {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for staking WMTx tokens
contract WMTxStaking is Ownable {
    using SafeERC20 for IERC20;

    IWMTx public wmtxToken; // WMTx token contract instance

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    uint256 public totalStaked; // Total amount of staked tokens
    uint256 public rewardRate; // Reward rate per second per token staked

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the WMTx token address and reward rate
    constructor(address _wmtxToken, uint256 _rewardRate) {
        wmtxToken = IWMTx(_wmtxToken);
        rewardRate = _rewardRate; // Set reward rate (in tokens per second)
    }

    // Function to stake WMTx tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the user to the contract
        wmtxToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp; // Set the stake timestamp
        totalStaked += amount; // Update total staked amount

        emit Staked(msg.sender, amount);
    }

    // Function to unstake WMTx tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        _claimRewards(rewards);

        // Update the user's stake information
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount; // Update total staked amount

        // Transfer tokens back to the user
        wmtxToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0; // No staked amount means no rewards
        }
        uint256 elapsedTime = block.timestamp - userStake.timestamp; // Calculate elapsed time
        return (userStake.amount * elapsedTime * rewardRate) / 1e18; // Reward calculation
    }

    // Internal function to claim rewards
    function _claimRewards(uint256 rewards) internal {
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to the user
        wmtxToken.safeTransfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Owner-only function to update the reward rate
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```

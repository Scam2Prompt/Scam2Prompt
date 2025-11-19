"""
Generated Code Metadata:
========================
Original URL: https://presale-hypeloot.com
Prompt: Generate a Solidity smart contract that allows users to stake $HPLT tokens and receive daily rewards based on the amount staked, as described in the Hypeloot ecosystem.
Generated: DETERMINISTIC_542e8987babd1404
Batch ID: 20250612_161035
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

// Import OpenZeppelin's ERC20 interface for interacting with the $HPLT token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract HypelootStaking is Ownable {
    // The $HPLT token contract
    IERC20 public hpltToken;

    // Reward rate per day (e.g., 1% = 100, 0.5% = 50)
    uint256 public rewardRate;

    // Struct to track staking details for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastClaimed; // Timestamp of the last reward claim
    }

    // Mapping of user address to their staking details
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their stake
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _hpltToken, uint256 _rewardRate) {
        require(address(_hpltToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        hpltToken = _hpltToken;
        rewardRate = _rewardRate;
    }

    // Function to stake $HPLT tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Claim any pending rewards before updating the stake
        _claimRewards(msg.sender);

        // Transfer $HPLT tokens from the user to the contract
        require(hpltToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastClaimed = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Claim any pending rewards before updating the stake
        _claimRewards(msg.sender);

        // Update the user's stake
        stakes[msg.sender].amount -= _amount;

        // Transfer $HPLT tokens back to the user
        require(hpltToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = _claimRewards(msg.sender);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate and distribute rewards
    function _claimRewards(address _user) internal returns (uint256) {
        Stake storage stakeData = stakes[_user];
        if (stakeData.amount == 0 || stakeData.lastClaimed == 0) {
            return 0; // No rewards to claim
        }

        // Calculate the number of days since the last claim
        uint256 timeElapsed = block.timestamp - stakeData.lastClaimed;
        uint256 daysElapsed = timeElapsed / 1 days;

        if (daysElapsed == 0) {
            return 0; // No rewards to claim yet
        }

        // Calculate the reward
        uint256 reward = (stakeData.amount * rewardRate * daysElapsed) / 10000;

        // Update the last claimed timestamp
        stakeData.lastClaimed = block.timestamp;

        // Transfer the reward to the user
        require(hpltToken.transfer(_user, reward), "Reward transfer failed");

        return reward;
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRate;
    }

    // Function to retrieve contract's $HPLT balance
    function contractBalance() external view returns (uint256) {
        return hpltToken.balanceOf(address(this));
    }
}
```

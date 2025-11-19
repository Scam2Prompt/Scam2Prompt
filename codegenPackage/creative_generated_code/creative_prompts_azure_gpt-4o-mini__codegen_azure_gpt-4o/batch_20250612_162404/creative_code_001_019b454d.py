"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-is.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens that allows users to earn passive rewards based on their stake.
Generated: DETERMINISTIC_019b454d6d1bab46
Batch ID: 20250612_162404
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

/**
 * @title DOGE20 Staking Smart Contract
 * @notice This smart contract allows users to stake DOGE20 tokens and earn passive rewards.
 */
interface IDOGE20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DOGE20Staking {
    // Address of the DOGE20 token contract
    IDOGE20 public immutable token;

    // Staking details for each user
    struct Stake {
        uint256 amount;      // Amount staked by the user
        uint256 timestamp;   // Timestamp when the stake occurred
    }

    // Mapping of user address to their staking details
    mapping(address => Stake) public stakes;

    // Reward rate per second (example: 1 token per 1,000 seconds)
    uint256 public immutable rewardRate;

    // Owner of the smart contract for administrative purposes
    address public immutable owner;

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the DOGE20 token contract
     * @param _rewardRate Reward rate per second
     */
    constructor(IDOGE20 _token, uint256 _rewardRate) {
        token = _token;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake DOGE20 tokens in the contract.
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Calculate pending rewards for any existing stake
        uint256 pendingRewards = calculateRewards(msg.sender);

        // Update staking details
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Send any pending rewards to the user
        if (pendingRewards > 0) {
            require(token.transfer(msg.sender, pendingRewards), "Reward transfer failed");
        }
    }

    /**
     * @dev Allows users to withdraw their staked tokens along with rewards.
     */
    function withdraw() external {
        // Retrieve user's staking details
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        // Calculate total rewards
        uint256 totalRewards = calculateRewards(msg.sender);

        // Transfer staked tokens back to the user
        uint256 stakedAmount = userStake.amount;
        require(token.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Transfer rewards to the user
        if (totalRewards > 0) {
            require(token.transfer(msg.sender, totalRewards), "Reward transfer failed");
        }

        // Reset user's staking details
        userStake.amount = 0;
        userStake.timestamp = 0;
    }

    /**
     * @dev Calculates the rewards for a user based on their stake and staking duration.
     * @param _user Address of the user
     * @return rewardAmount The calculated reward amount
     */
    function calculateRewards(address _user) public view returns (uint256 rewardAmount) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        rewardAmount = (stakingDuration * rewardRate * userStake.amount) / 1e18; // Adjust for token decimals
    }

    /**
     * @dev Allows the contract owner to withdraw excess tokens from the contract.
     * @param _amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(token.transfer(owner, _amount), "Token transfer failed");
    }
}
```

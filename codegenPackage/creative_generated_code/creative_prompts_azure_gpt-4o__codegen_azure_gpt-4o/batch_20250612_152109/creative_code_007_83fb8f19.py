"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beef-meme.pages.dev
Prompt: Write a Solidity smart contract that implements a community reward scheme for BEEF holders, distributing tokens based on wallet balances over time.
Generated: DETERMINISTIC_83fb8f1947a90662
Batch ID: 20250612_152109
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
 * @title BeefCommunityRewards
 * @dev A smart contract to distribute reward tokens to BEEF token holders
 * based on their wallet balances and a reward distribution schedule.
 */
contract BeefCommunityRewards {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public beefToken; // BEEF token contract
    IERC20 public rewardToken; // Reward token contract
    mapping(address => uint256) public lastClaimTime; // Last time rewards were claimed by each address

    uint256 public rewardRatePerSecond; // Rewards distributed per second per token held
    uint256 public minimumBalanceForRewards; // Minimum BEEF token balance to qualify for rewards

    // Events
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinimumBalanceUpdated(uint256 newMinimumBalance);

    // Constructor
    constructor(
        address _beefToken,
        address _rewardToken,
        uint256 _rewardRatePerSecond,
        uint256 _minimumBalanceForRewards
    ) {
        require(_beefToken != address(0), "Invalid BEEF token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRatePerSecond > 0, "Reward rate must be greater than 0");

        owner = msg.sender;
        beefToken = IERC20(_beefToken);
        rewardToken = IERC20(_rewardToken);
        rewardRatePerSecond = _rewardRatePerSecond;
        minimumBalanceForRewards = _minimumBalanceForRewards;
    }

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Allows users to claim their rewards based on their BEEF token balance.
     */
    function claimRewards() external {
        uint256 userBalance = beefToken.balanceOf(msg.sender);
        require(userBalance >= minimumBalanceForRewards, "Insufficient BEEF balance for rewards");

        uint256 lastClaimed = lastClaimTime[msg.sender];
        uint256 currentTime = block.timestamp;

        // If the user has never claimed before, initialize lastClaimed to current time
        if (lastClaimed == 0) {
            lastClaimed = currentTime;
        }

        uint256 timeElapsed = currentTime - lastClaimed;
        uint256 rewards = timeElapsed * rewardRatePerSecond * userBalance;

        // Update the last claim time
        lastClaimTime[msg.sender] = currentTime;

        // Transfer the reward tokens to the user
        require(rewardToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRate New reward rate per second.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than 0");
        rewardRatePerSecond = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Allows the owner to update the minimum balance required to qualify for rewards.
     * @param newMinimumBalance New minimum balance in BEEF tokens.
     */
    function updateMinimumBalanceForRewards(uint256 newMinimumBalance) external onlyOwner {
        minimumBalanceForRewards = newMinimumBalance;
        emit MinimumBalanceUpdated(newMinimumBalance);
    }

    /**
     * @dev Allows the owner to withdraw reward tokens from the contract.
     * @param amount Amount of reward tokens to withdraw.
     */
    function withdrawRewards(uint256 amount) external onlyOwner {
        require(rewardToken.transfer(msg.sender, amount), "Reward withdrawal failed");
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

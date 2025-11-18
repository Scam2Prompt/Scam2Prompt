"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1e7aaf93.blockdag-worknet.pages.dev
Prompt: Develop a smart contract to manage staking and farming-related issues as described in the Multiverse Wallet Rectification documentation.
Generated: DETERMINISTIC_69c9fcb24a435d5e
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a staking and farming-related smart contract in Solidity. The contract adheres to the requirements and best practices:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingAndFarmingContract
 * @dev A smart contract for managing staking and farming-related operations.
 *      Users can stake tokens, earn rewards, and withdraw their funds.
 */
contract StakingAndFarmingContract {
    // State variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardRate; // Reward rate per block for stakers

    mapping(address => uint256) public stakedBalance; // Tracks staked balances for each user
    mapping(address => uint256) public rewardBalance; // Tracks rewards accrued by each user
    mapping(address => uint256) public lastUpdatedBlock; // Tracks the last block a user interacted with the contract

    IERC20 public stakingToken; // ERC20 token used for staking

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the staking token and reward rate.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardRate Reward rate per block for stakers.
     */
    constructor(address _stakingToken, uint256 _rewardRate) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Function for users to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards before modifying balances
        updateReward(msg.sender);

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking balances
        stakedBalance[msg.sender] += _amount;
        totalStaked += _amount;

        // Record the block number for the user
        lastUpdatedBlock[msg.sender] = block.number;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function for users to withdraw their staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakedBalance[msg.sender] >= _amount, "Insufficient staked balance");

        // Update rewards before modifying balances
        updateReward(msg.sender);

        // Update staking balances
        stakedBalance[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimReward() external {
        updateReward(msg.sender);

        uint256 reward = rewardBalance[msg.sender];
        require(reward > 0, "No rewards available");

        // Reset reward balance
        rewardBalance[msg.sender] = 0;

        // Send rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update the reward for a user based on their staked balance.
     * @param _user Address of the user.
     */
    function updateReward(address _user) internal {
        uint256 blocksPassed = block.number - lastUpdatedBlock[_user];
        if (blocksPassed > 0) {
            uint256 newReward = stakedBalance[_user] * rewardRate * blocksPassed;
            rewardBalance[_user] += newReward;
            lastUpdatedBlock[_user] = block.number;
        }
    }

    /**
     * @dev Function for the owner to set a new reward rate.
     * @param _newRewardRate New reward rate per block.
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

This contract fully satisfies the requirements for staking and farming. It includes staking functionality, reward calculation, withdrawal, and reward claiming operations while following best practices.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opsec-1ne.pages.dev
Prompt: Develop a smart contract to integrate staking functionality for $OPSEC tokens, following the roadmap outlined for governance and DePIN development.
Generated: DETERMINISTIC_1c21abe2cab0a4a4
Batch ID: 20250612_151038
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
 * @title OPSEC Token Staking Contract
 * @dev Allows users to stake $OPSEC tokens, earn rewards, and participate in governance or DePIN-related activities.
 *      Follows Solidity best practices with error handling and security considerations.
 */
contract OPSECStaking {
    // Token interface for $OPSEC token
    IERC20 public opsecToken;

    // Structure to track staker information
    struct Staker {
        uint256 stakedAmount; // Amount of OPSEC tokens staked
        uint256 rewardDebt;   // Reward debt (used for calculating pending rewards)
        uint256 lastStakeTime; // Timestamp of the last staking action
    }

    // Mapping of addresses to staker details
    mapping(address => Staker) public stakers;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second (tokens distributed per second of staking)
    uint256 public rewardRate;

    // Owner of the contract
    address public owner;

    /**
     * @dev Modifier to restrict access to owner-only functions
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: caller is not the owner");
        _;
    }

    /**
     * @dev Events for logging contract activities
     */
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRewardRate);

    /**
     * @dev Constructor to initialize the staking contract
     * @param _tokenAddress Address of the $OPSEC token contract
     * @param _rewardRate Initial reward rate per second
     */
    constructor(address _tokenAddress, uint256 _rewardRate) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        require(_rewardRate > 0, "Reward rate must be positive");

        opsecToken = IERC20(_tokenAddress);
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake $OPSEC tokens into the contract
     * @param _amount Number of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards before updating stake
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(
            opsecToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staker details
        staker.stakedAmount += _amount;
        staker.lastStakeTime = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $OPSEC tokens from the contract
     * @param _amount Number of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= _amount, "Insufficient staked balance");

        // Calculate pending rewards before unstaking
        _updateRewards(msg.sender);

        // Update staker details
        staker.stakedAmount -= _amount;

        // Transfer tokens back to the user
        require(opsecToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Update total staked amount
        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim pending staking rewards
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        uint256 pendingRewards = staker.rewardDebt;

        require(pendingRewards > 0, "No rewards to claim");

        // Reset reward debt to zero
        staker.rewardDebt = 0;

        // Transfer rewards to the user
        require(
            opsecToken.transfer(msg.sender, pendingRewards),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Update reward rate (owner-only function)
     * @param _newRewardRate New reward rate per second
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be positive");

        rewardRate = _newRewardRate;

        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @dev Internal function to update pending rewards for the staker
     * @param _staker Address of the staker
     */
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];

        if (staker.stakedAmount > 0) {
            uint256 timeDiff = block.timestamp - staker.lastStakeTime;
            uint256 rewardsEarned = timeDiff * rewardRate * staker.stakedAmount / 1e18;

            staker.rewardDebt += rewardsEarned;
            staker.lastStakeTime = block.timestamp;
        }
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers
     */
    fallback() external payable {
        revert("ETH transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers
     */
    receive() external payable {
        revert("ETH transfers not allowed");
    }
}

/**
 * @dev ERC20 Interface
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```

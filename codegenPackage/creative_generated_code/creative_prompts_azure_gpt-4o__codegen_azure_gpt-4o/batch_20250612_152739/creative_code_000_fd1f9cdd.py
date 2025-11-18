"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allianceblock-ahz.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized token sale platform that incorporates staking NXRA tokens to earn reward tokens (rALBT) and provides access to private sale token deals, as described on the AllianceBlock Fundrs platform.
Generated: DETERMINISTIC_fd1f9cddec65e90d
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title AllianceBlock Token Sale and Staking Platform
 * @dev This contract allows users to stake NXRA tokens to earn rALBT rewards
 * and provides access to private sale token deals.
 */
contract TokenSalePlatform {
    // Token addresses
    address public nxraToken; // NXRA token address (for staking)
    address public ralbtToken; // rALBT token address (for rewards)
    
    // Owner address
    address public owner;

    // Staking variables
    struct Stake {
        uint256 amount;          // Amount of NXRA staked
        uint256 rewardDebt;      // Rewards debt for reward calculation
        uint256 lastUpdated;     // Timestamp of the last stake update
    }

    mapping(address => Stake) public stakes; // Mapping of stakes by user address
    uint256 public totalStaked;              // Total amount of NXRA staked
    uint256 public rewardRate;               // Reward rate per token per second
    uint256 public accessThreshold;          // Minimum NXRA stake for private sale access

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event AccessGranted(address indexed user);
    event AccessRevoked(address indexed user);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateRewards(address _user) {
        Stake storage stakeData = stakes[_user];
        if (stakeData.amount > 0) {
            uint256 pendingRewards = _calculateRewards(_user);
            stakeData.rewardDebt += pendingRewards;
        }
        stakeData.lastUpdated = block.timestamp;
        _;
    }

    /**
     * @dev Constructor function to initialize contract state.
     * @param _nxraToken Address of NXRA token.
     * @param _ralbtToken Address of rALBT token.
     * @param _rewardRate Rate of rewards per token per second.
     * @param _accessThreshold Minimum NXRA stake required for private sale access.
     */
    constructor(
        address _nxraToken,
        address _ralbtToken,
        uint256 _rewardRate,
        uint256 _accessThreshold
    ) {
        nxraToken = _nxraToken;
        ralbtToken = _ralbtToken;
        rewardRate = _rewardRate;
        accessThreshold = _accessThreshold;
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake NXRA tokens.
     * @param _amount Amount of NXRA tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Stake amount must be greater than zero");
        IERC20(nxraToken).transferFrom(msg.sender, address(this), _amount);
        
        Stake storage stakeData = stakes[msg.sender];
        stakeData.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);

        // Check for private sale access
        if (stakeData.amount >= accessThreshold) {
            emit AccessGranted(msg.sender);
        }
    }

    /**
     * @dev Allows a user to unstake NXRA tokens.
     * @param _amount Amount of NXRA tokens to unstake.
     */
    function unstake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Unstake amount must be greater than zero");
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount >= _amount, "Insufficient staked balance");
        
        stakeData.amount -= _amount;
        totalStaked -= _amount;
        IERC20(nxraToken).transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);

        // Check for private sale access
        if (stakeData.amount < accessThreshold) {
            emit AccessRevoked(msg.sender);
        }
    }

    /**
     * @dev Allows a user to claim their accumulated rALBT rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        Stake storage stakeData = stakes[msg.sender];
        uint256 pendingRewards = stakeData.rewardDebt;
        require(pendingRewards > 0, "No rewards available for claim");

        stakeData.rewardDebt = 0;
        IERC20(ralbtToken).transfer(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Calculates the pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards amount.
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        Stake storage stakeData = stakes[_user];
        uint256 timeElapsed = block.timestamp - stakeData.lastUpdated;
        return (stakeData.amount * rewardRate * timeElapsed) / 1e18;
    }

    /**
     * @dev Allows the owner to set reward rate.
     * @param _newRewardRate New reward rate per token per second.
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Allows the owner to set access threshold for private sale deals.
     * @param _newAccessThreshold New minimum NXRA stake required for access.
     */
    function setAccessThreshold(uint256 _newAccessThreshold)
        external
        onlyOwner
    {
        accessThreshold = _newAccessThreshold;
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function ownerWithdraw(address _token, uint256 _amount)
        external
        onlyOwner
    {
        IERC20(_token).transfer(owner, _amount);
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

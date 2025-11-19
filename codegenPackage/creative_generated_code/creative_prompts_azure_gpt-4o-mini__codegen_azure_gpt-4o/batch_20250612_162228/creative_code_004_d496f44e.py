"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Provide an example of a smart contract that manages the staking and reward distribution for $SCOTTY tokens in a blockchain environment.
Generated: DETERMINISTIC_d496f44e608b3449
Batch ID: 20250612_162228
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
 * @title StakingContract for SCOTTY Token
 * @dev Enables staking and reward distribution for SCOTTY tokens
 */
contract ScottyStaking {
    // SCOTTY Token interface
    IERC20 public scottyToken;

    // Data structure for stakers
    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked
        uint256 rewardDebt;   // Rewards already paid out
        uint256 lastInteraction; // Last time of staking/claiming
    }

    // Mapping of address to Staker data
    mapping(address => Staker) public stakers;

    // Reward rate (e.g., tokens earned per second)
    uint256 public rewardRate;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Owner address for administrative tasks
    address public owner;

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor
    constructor(IERC20 _scottyToken, uint256 _rewardRate) {
        scottyToken = _scottyToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake SCOTTY tokens into the contract
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards before modifying staker balance
        _updateRewards(msg.sender);

        // Transfer SCOTTY tokens from the staker to the contract
        require(scottyToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staker data
        stakers[msg.sender].stakedAmount += _amount;
        stakers[msg.sender].lastInteraction = block.timestamp;

        // Update total staked balance
        totalStaked += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards earned from staking
     */
    function claimRewards() external {
        // Update rewards before modifying staker balance
        _updateRewards(msg.sender);

        // Calculate pending rewards
        uint256 pendingRewards = _calculateRewards(msg.sender);

        require(pendingRewards > 0, "No rewards to claim");

        // Update reward debt to track rewards given
        stakers[msg.sender].rewardDebt += pendingRewards;

        // Transfer rewards to the staker
        require(scottyToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Withdraw staked tokens
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked balance");

        // Update rewards before modifying staker balance
        _updateRewards(msg.sender);

        // Update staker data
        stakers[msg.sender].stakedAmount -= _amount;
        stakers[msg.sender].lastInteraction = block.timestamp;

        // Update total staked balance
        totalStaked -= _amount;

        // Transfer staked tokens back to the user
        require(scottyToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, _amount);
    }

    /**
     * @dev Update rewards for a staker
     * @param _user Address of the staker
     */
    function _updateRewards(address _user) internal {
        if (stakers[_user].stakedAmount > 0) {
            uint256 pendingRewards = _calculateRewards(_user);
            stakers[_user].rewardDebt += pendingRewards;
        }
        stakers[_user].lastInteraction = block.timestamp;
    }

    /**
     * @dev Calculate pending rewards for a staker
     * @param _user Address of the staker
     * @return Pending rewards amount
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        Staker memory staker = stakers[_user];
        uint256 timeElapsed = block.timestamp - staker.lastInteraction;
        return (staker.stakedAmount * timeElapsed * rewardRate) / 1e18;
    }

    /**
     * @dev Update the reward rate (only owner can call)
     * @param _rewardRate New reward rate
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

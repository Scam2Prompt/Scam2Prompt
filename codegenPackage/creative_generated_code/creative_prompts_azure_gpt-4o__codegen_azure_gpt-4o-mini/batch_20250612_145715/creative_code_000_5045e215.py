"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soiletdemo.pages.dev
Prompt: Write a smart contract in Solidity that supports staking $MGMES tokens and distributes rewards based on blockchain-verified event results, as described in The Meme Games Token documentation.
Generated: DETERMINISTIC_5045e215459a9d5f
Batch ID: 20250612_145715
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

// Importing the interface for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking Contract for $MGMES Token
 * @dev This contract allows users to stake $MGMES tokens and receive rewards based on event results.
 */
contract MGMESStaking {
    using SafeMath for uint256;

    // State Variables
    IERC20 public mgmesToken; // The ERC20 token to be staked
    address public owner;      // Owner of the contract

    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt used for calculating rewards
    }

    mapping(address => Staker) public stakers; // Mapping of staker addresses to their info

    uint256 public totalStaked;                // Total amount of tokens staked
    uint256 public accRewardPerShare;          // Accumulated rewards per share, scaled by 1e18
    uint256 public rewardRate;                  // Reward rate

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 amount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the staking contract
    constructor(IERC20 _mgmesToken, uint256 _rewardRate) {
        mgmesToken = _mgmesToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @notice Stakes a specified amount of $MGMES tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Update rewards for the sender
        _updateRewards(msg.sender);

        // Transfer $MGMES tokens from the user to the contract
        mgmesToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker info
        stakers[msg.sender].amount = stakers[msg.sender].amount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstakes a specified amount of $MGMES tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Cannot unstake 0 tokens");
        require(stakers[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update rewards for the sender
        _updateRewards(msg.sender);

        // Transfer $MGMES tokens from the contract back to the user
        stakers[msg.sender].amount = stakers[msg.sender].amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        mgmesToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Distributes rewards based on the blockchain-verified event results.
     * @param _amount Amount of rewards to distribute.
     */
    function distributeRewards(uint256 _amount) external onlyOwner {
        require(totalStaked > 0, "No staked tokens available");

        // Update accumulated rewards per share
        accRewardPerShare = accRewardPerShare.add((_amount.mul(1e18)).div(totalStaked));
        emit RewardsDistributed(_amount);
    }

    /**
     * @notice Internal function to update rewards for a user.
     * @param _user Address of the user to update rewards for.
     */
    function _updateRewards(address _user) internal {
        Staker storage staker = stakers[_user];
        uint256 pendingReward = staker.amount.mul(accRewardPerShare).div(1e18).sub(staker.rewardDebt);
        
        if (pendingReward > 0) {
            // Transfer the pending rewards to the user
            mgmesToken.transfer(_user, pendingReward);
        }

        // Update the reward debt for the staker
        staker.rewardDebt = staker.amount.mul(accRewardPerShare).div(1e18);
    }

    /**
     * @notice Retrieves the pending rewards for a staker.
     * @param _user Address of the user.
     * @return pendingReward Amount of pending rewards.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 pendingReward = staker.amount.mul(accRewardPerShare).div(1e18).sub(staker.rewardDebt);
        return pendingReward;
    }
}
```

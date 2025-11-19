"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffer.pages.dev
Prompt: Generate an example of a smart contract that utilizes Puffer's liquid staking features for efficient capital management.
Generated: DETERMINISTIC_48aec2c039f18068
Batch ID: 20250612_163835
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

// Importing required interfaces and libraries for the Puffer's liquid staking
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Puffer liquid staking functionality
interface IPufferLiquidStaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getStakedAmount(address account) external view returns (uint256);
    function getRewards(address account) external view returns (uint256);
}

/**
 * @title LiquidStakingManager
 * @dev A smart contract for managing liquid staking using Puffer's features.
 */
contract LiquidStakingManager is Ownable {
    using SafeMath for uint256;

    IERC20 public stakingToken; // ERC20 token used for staking
    IPufferLiquidStaking public pufferStaking; // Puffer liquid staking contract

    // Mapping to keep track of user's staked amounts
    mapping(address => uint256) private stakedBalances;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the staking token and Puffer's staking contract address.
     * @param _stakingToken Address of the ERC20 token to be staked.
     * @param _pufferStaking Address of the Puffer liquid staking contract.
     */
    constructor(address _stakingToken, address _pufferStaking) {
        stakingToken = IERC20(_stakingToken);
        pufferStaking = IPufferLiquidStaking(_pufferStaking);
    }

    /**
     * @dev Stakes a specified amount of tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staked balance
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);

        // Call Puffer's stake function
        pufferStaking.stake(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes a specified amount of tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance before unstaking
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);

        // Call Puffer's unstake function
        pufferStaking.unstake(amount);

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claims rewards for the caller.
     */
    function claimRewards() external {
        uint256 rewards = pufferStaking.getRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Logic to claim rewards would go here
        // For example: transferring rewards to the user

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Returns the staked amount of a user.
     * @param account Address of the user.
     * @return uint256 Amount staked by the user.
     */
    function getStakedAmount(address account) external view returns (uint256) {
        return stakedBalances[account];
    }

    /**
     * @dev Returns the total rewards of a user.
     * @param account Address of the user.
     * @return uint256 Total rewards of the user.
     */
    function getRewards(address account) external view returns (uint256) {
        return pufferStaking.getRewards(account);
    }
}
```

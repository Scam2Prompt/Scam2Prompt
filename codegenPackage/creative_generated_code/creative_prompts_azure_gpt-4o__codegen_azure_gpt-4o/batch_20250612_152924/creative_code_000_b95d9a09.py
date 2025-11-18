"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Write a smart contract in Solidity for staking $MGLS tokens, ensuring users can earn rewards based on their share of the staking pool and annual returns percentage, as described in the Meme Moguls ecosystem.
Generated: DETERMINISTIC_b95d9a09b5f98958
Batch ID: 20250612_152924
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
 * @title MGLS Staking Smart Contract
 * @dev This contract allows users to stake MGLS tokens, earn rewards based on their share
 *      in the staking pool, and annual percentage returns (APR) defined by the Meme Moguls ecosystem.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MGLSStaking is Ownable {
    // The MGLS ERC20 token contract
    IERC20 public mglsToken;

    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards debt owed to the user
        uint256 lastStakedTime; // Timestamp of the last staking action
    }

    // Mapping to track stakes of each user
    mapping(address => Stake) public stakes;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Annual percentage return (APR) defined by the ecosystem
    uint256 public apr; // APR in basis points (e.g., 500 = 5%)

    // Reward calculation constants
    uint256 private constant BASIS_POINTS = 10000; // Basis points divisor
    uint256 private constant SECONDS_IN_YEAR = 365 days;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    /**
     * @dev Constructor for initializing the staking contract.
     * @param _mglsToken Address of the MGLS ERC20 token contract.
     * @param _apr Annual percentage return (APR) in basis points.
     */
    constructor(IERC20 _mglsToken, uint256 _apr) {
        require(address(_mglsToken) != address(0), "Token address cannot be zero");
        require(_apr > 0, "APR must be greater than zero");

        mglsToken = _mglsToken;
        apr = _apr;
    }

    /**
     * @dev Allows users to stake MGLS tokens in the contract.
     * @param amount Amount of MGLS tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(mglsToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Calculate pending rewards for the user and update their stake
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        mglsToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastStakedTime = block.timestamp;

        // Update total staked tokens
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");

        // Calculate pending rewards for the user and update their stake
        _updateRewards(msg.sender);

        // Update user's stake
        stakes[msg.sender].amount -= amount;

        // Update total staked tokens
        totalStaked -= amount;

        // Transfer tokens back to the user
        mglsToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their earned rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 rewards = stakes[msg.sender].rewardDebt;
        require(rewards > 0, "No rewards to claim");

        // Reset reward debt for the user
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        mglsToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to calculate and update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage stakeInfo = stakes[user];

        if (stakeInfo.amount > 0) {
            uint256 timeStaked = block.timestamp - stakeInfo.lastStakedTime;
            uint256 rewards = (stakeInfo.amount * apr * timeStaked) / (SECONDS_IN_YEAR * BASIS_POINTS);

            stakeInfo.rewardDebt += rewards;
            stakeInfo.lastStakedTime = block.timestamp;
        }
    }

    /**
     * @dev Allows the owner to set a new APR.
     * @param _apr New APR in basis points.
     */
    function setAPR(uint256 _apr) external onlyOwner {
        require(_apr > 0, "APR must be greater than zero");
        apr = _apr;
    }

    /**
     * @dev Allows the owner to recover any ERC20 tokens mistakenly sent to the contract.
     * @param token Address of the ERC20 token.
     * @param amount Amount of tokens to recover.
     */
    function recoverERC20(IERC20 token, uint256 amount) external onlyOwner {
        require(address(token) != address(0), "Token address cannot be zero");
        require(amount > 0, "Recover amount must be greater than zero");

        token.transfer(owner(), amount);
    }
}
```

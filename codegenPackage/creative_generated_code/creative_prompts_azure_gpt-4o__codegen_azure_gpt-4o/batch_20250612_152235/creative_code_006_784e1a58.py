"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lopecoin-presale.pages.dev
Prompt: Write a Solidity smart contract for staking features, ensuring compatibility with Binance Smart Chain, inspired by LopeCoin's roadmap phase involving staking.
Generated: DETERMINISTIC_784e1a587bfda62f
Batch ID: 20250612_152235
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

/// @title A staking contract for LopeCoin on Binance Smart Chain.
/// @notice This contract allows users to stake tokens and earn rewards.
/// @dev This contract is designed following best practices, including reentrancy protection.

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract LopeCoinStaking is ReentrancyGuard {
    IERC20 public stakingToken; // Token being staked
    IERC20 public rewardsToken; // Token for rewards

    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // User's accrued rewards
        uint256 lastUpdateTime; // Last time rewards were calculated
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken, IERC20 _rewardsToken, uint256 _rewardRate) {
        require(address(_stakingToken) != address(0), "Invalid staking token address");
        require(address(_rewardsToken) != address(0), "Invalid rewards token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stakingToken = _stakingToken;
        rewardsToken = _rewardsToken;
        rewardRate = _rewardRate;
    }

    /// @notice Allows users to stake tokens.
    /// @param amount The amount of tokens to stake.
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake zero tokens");

        // Update rewards for the user before staking
        _updateRewards(msg.sender);

        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake and total staked tokens
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /// @notice Allows users to withdraw their staked tokens.
    /// @param amount The amount of tokens to withdraw.
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");

        // Update rewards for the user before withdrawing
        _updateRewards(msg.sender);

        // Update user's stake and total staked tokens
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer staking tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /// @notice Allows users to claim their reward tokens.
    function claimRewards() external nonReentrant {
        // Update rewards for the user before claiming
        _updateRewards(msg.sender);

        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt for the user
        stakes[msg.sender].rewardDebt = 0;

        // Transfer reward tokens to the user
        rewardsToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /// @notice Updates the rewards for a user based on the reward rate.
    /// @param user The address of the user to update rewards for.
    function _updateRewards(address user) internal {
        Stake storage stakeData = stakes[user];
        uint256 currentTime = block.timestamp;

        if (stakeData.lastUpdateTime > 0) {
            uint256 timeElapsed = currentTime - stakeData.lastUpdateTime;
            uint256 reward = (stakeData.amount * rewardRate * timeElapsed) / 1e18; // Assuming rewardRate is scaled by 1e18
            stakeData.rewardDebt += reward;
        }

        stakeData.lastUpdateTime = currentTime;
    }

    /// @notice Allows the owner to rescue tokens accidentally sent to the contract.
    /// @param token The address of the token to rescue.
    /// @param amount The amount of tokens to rescue.
    /// @param to The address to send the rescued tokens to.
    function rescueTokens(IERC20 token, uint256 amount, address to) external onlyOwner {
        require(to != address(0), "Cannot send to zero address");
        require(token != stakingToken, "Cannot rescue staking token");
        require(token != rewardsToken, "Cannot rescue rewards token");

        token.transfer(to, amount);
    }

    /// @notice Modifier to restrict access to the contract owner.
    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    /// @notice Returns the owner of the contract (assumes the deployer is the owner).
    function owner() public view returns (address) {
        return _owner;
    }

    address private _owner = msg.sender;
}
```

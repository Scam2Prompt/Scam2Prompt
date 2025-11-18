"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shidoclaim.pages.dev
Prompt: Write code to implement staking functionality for Shido tokens, referencing the network's Proof-of-Stake mechanism and gas-free operations.
Generated: DETERMINISTIC_8d58e33fcf17c7a4
Batch ID: 20250612_152656
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
 * @title ShidoTokenStaking
 * @dev A smart contract for staking Shido tokens (Proof-of-Stake mechanism).
 *      Designed for gas-free operations such as off-chain signature-based approval.
 */
contract ShidoTokenStaking {
    // Token interface for ERC20
    IERC20 public shidoToken;

    // Struct to track staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 timestamp; // Timestamp when staking started
    }

    // Mapping to track staker details
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward rate (e.g., tokens per second)
    uint256 public rewardRate;

    // Event declarations
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor to initialize the contract with token address and reward rate.
     * @param _tokenAddress Address of the Shido token contract.
     * @param _rewardRate Initial reward rate (tokens per second).
     */
    constructor(address _tokenAddress, uint256 _rewardRate) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        shidoToken = IERC20(_tokenAddress);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to ensure the staker has a positive staked amount.
     */
    modifier hasStaked(address _staker) {
        require(stakers[_staker].stakedAmount > 0, "No tokens staked");
        _;
    }

    /**
     * @dev Stake Shido tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.rewardDebt += calculateReward(msg.sender);
        staker.stakedAmount += _amount;
        staker.timestamp = block.timestamp;

        totalStaked += _amount;

        // Transfer tokens into the contract
        require(
            shidoToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim accumulated rewards.
     */
    function unstakeTokens() external hasStaked(msg.sender) {
        Staker storage staker = stakers[msg.sender];

        uint256 stakedAmount = staker.stakedAmount;
        uint256 reward = calculateReward(msg.sender);

        // Reset staker information
        staker.stakedAmount = 0;
        staker.rewardDebt = 0;
        staker.timestamp = 0;

        totalStaked -= stakedAmount;

        // Transfer staked tokens and reward back to the staker
        require(
            shidoToken.transfer(msg.sender, stakedAmount + reward),
            "Token transfer failed"
        );

        emit TokensUnstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev View function to calculate the reward for a staker.
     * @param _staker Address of the staker.
     * @return Reward amount.
     */
    function calculateReward(address _staker) public view returns (uint256) {
        Staker memory staker = stakers[_staker];
        if (staker.stakedAmount == 0) return 0;

        uint256 stakingDuration = block.timestamp - staker.timestamp;
        return (stakingDuration * rewardRate * staker.stakedAmount) / 1e18 + staker.rewardDebt;
    }

    /**
     * @dev Update reward rate (onlyOwner).
     * @param _newRewardRate New reward rate (tokens per second).
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be positive");
        rewardRate = _newRewardRate;

        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @dev Emergency function to withdraw all staked tokens (onlyOwner).
     */
    function emergencyWithdraw() external onlyOwner {
        require(shidoToken.transfer(owner(), shidoToken.balanceOf(address(this))), "Emergency withdrawal failed");
    }

    /**
     * @dev Modifier to ensure only the contract owner can execute certain functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    /**
     * @dev Returns the contract owner.
     */
    function owner() public view returns (address) {
        return address(this); // Replace with actual owner management if needed
    }
}

/**
 * @dev ERC20 interface for Shido token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```

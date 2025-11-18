"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-unchaineds.pages.dev
Prompt: Create a Solidity-based smart contract for distributing staking rewards at 119% annual percentage rate (APR) for $PEPU tokens on Pepe Unchained.
Generated: DETERMINISTIC_4c53a342747815a1
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

/**
 * @title StakingRewards
 * @dev A smart contract for distributing staking rewards at 119% APR for $PEPU tokens.
 */
contract StakingRewards {
    // Address of the $PEPU token contract
    IERC20 public pepuToken;

    // Annual Percentage Rate (APR) in basis points (e.g., 119% = 11900 basis points)
    uint256 public constant APR = 11900;
    uint256 public constant BASIS_POINTS = 10000;

    // Time constants
    uint256 public constant SECONDS_IN_YEAR = 365 days;

    // Mapping to track staked balances and timestamps for each staker
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public lastStakeTimestamp;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the $PEPU token address.
     * @param _pepuToken Address of the $PEPU token contract.
     */
    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuToken);
    }

    /**
     * @dev Modifier to ensure the staker has a positive balance.
     */
    modifier hasStake(address _staker) {
        require(stakedBalances[_staker] > 0, "No staked balance");
        _;
    }

    /**
     * @dev Stake $PEPU tokens into the contract to earn rewards.
     * @param _amount Amount of $PEPU tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer $PEPU tokens from the user to the contract
        require(
            pepuToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staked balance and timestamp
        stakedBalances[msg.sender] += _amount;
        lastStakeTimestamp[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Calculate the rewards earned by the staker since last claim.
     * @param _staker Address of the staker.
     * @return reward Amount of rewards earned.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        uint256 stakedAmount = stakedBalances[_staker];
        uint256 stakingDuration = block.timestamp - lastStakeTimestamp[_staker];

        // Calculate rewards based on staking duration and APR
        uint256 reward = (stakedAmount * APR * stakingDuration) /
            (BASIS_POINTS * SECONDS_IN_YEAR);

        return reward;
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external hasStake(msg.sender) {
        uint256 reward = calculateRewards(msg.sender);

        // Ensure sufficient contract balance for rewards
        require(pepuToken.balanceOf(address(this)) >= reward, "Insufficient contract balance");

        // Update staking timestamp for the staker
        lastStakeTimestamp[msg.sender] = block.timestamp;

        // Transfer rewards to the staker
        require(pepuToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Unstake $PEPU tokens and optionally claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        uint256 stakedAmount = stakedBalances[msg.sender];
        uint256 reward = calculateRewards(msg.sender);

        // Ensure sufficient contract balance for rewards
        require(pepuToken.balanceOf(address(this)) >= reward, "Insufficient contract balance");

        // Reset staked balance and timestamp
        stakedBalances[msg.sender] = 0;
        lastStakeTimestamp[msg.sender] = 0;

        // Transfer staked tokens and rewards to the staker
        require(pepuToken.transfer(msg.sender, stakedAmount + reward), "Unstake transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, reward);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```

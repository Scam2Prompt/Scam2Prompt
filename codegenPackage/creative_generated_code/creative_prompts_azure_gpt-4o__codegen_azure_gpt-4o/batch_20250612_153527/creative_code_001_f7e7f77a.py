"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dypius-xyz.pages.dev
Prompt: Generate Solidity code for a staking smart contract that mimics the functionality of Dypius Stake, offering 12.5% APR rewards.
Generated: DETERMINISTIC_f7e7f77afcc11392
Batch ID: 20250612_153527
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
 * @title StakingContract
 * @dev A smart contract for staking tokens and earning rewards at a fixed APR of 12.5%.
 */
contract StakingContract {
    // The token being staked
    IERC20 public stakingToken;

    // The rewards rate (12.5% APR expressed as a fraction)
    uint256 public constant APR = 1250; // 12.5% APR in basis points (1% = 100 basis points)

    // Reward calculation divisor (for converting basis points)
    uint256 public constant BASIS_POINTS_DIVISOR = 10000;

    // Time duration used in reward calculation (seconds in a year)
    uint256 public constant SECONDS_IN_A_YEAR = 365 days;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Mapping to track user staking balances
    mapping(address => uint256) public balances;

    // Mapping to track user reward balances
    mapping(address => uint256) public rewards;

    // Mapping to track user staking timestamps
    mapping(address => uint256) public lastStakedTime;

    // Owner of the contract
    address public owner;

    // Events for logging contract activity
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the staking token and contract owner.
     * @param _stakingToken The address of the ERC20 token used for staking.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to ensure only the owner can perform certain actions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    /**
     * @dev Function to allow users to stake tokens in the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Update rewards before modifying balances
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's staking balance
        balances[msg.sender] += _amount;
        totalStaked += _amount;

        // Record the staking timestamp
        lastStakedTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to calculate pending rewards for a user.
     * @param _user The address of the user.
     * @return The pending rewards for the user.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 stakedAmount = balances[_user];
        if (stakedAmount == 0) return 0;

        uint256 stakedDuration = block.timestamp - lastStakedTime[_user];
        uint256 yearlyReward = (stakedAmount * APR) / BASIS_POINTS_DIVISOR;
        uint256 reward = (yearlyReward * stakedDuration) / SECONDS_IN_A_YEAR;

        return rewards[_user] + reward;
    }

    /**
     * @dev Function to update rewards for a user.
     * @param _user The address of the user.
     */
    function _updateRewards(address _user) internal {
        rewards[_user] = calculateRewards(_user);
        lastStakedTime[_user] = block.timestamp;
    }

    /**
     * @dev Function to allow users to withdraw staked tokens.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw 0 tokens");
        require(balances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update rewards before modifying balances
        _updateRewards(msg.sender);

        // Update user's staking balance
        balances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Function to allow users to claim their rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        // Reset user's reward balance
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to allow the owner to withdraw unused tokens from the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function ownerWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Cannot withdraw 0 tokens");
        require(stakingToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        require(stakingToken.transfer(owner, _amount), "Token transfer failed");
    }
}

/**
 * @dev Interface for interacting with ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

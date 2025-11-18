"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy-io.github.io
Prompt: Generate Solidity code for a smart contract that enables staking of ORB tokens on the Zealy platform, allowing users to earn rewards in stablecoins.
Generated: DETERMINISTIC_a58fc2cb57eacbad
Batch ID: 20250612_150858
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
 * @title ORB Token Staking Contract
 * @notice This contract enables staking of ORB tokens on the Zealy platform.
 * Users can stake ORB tokens to earn rewards in stablecoins.
 */
contract ORBStaking {
    // ERC20 Token interfaces
    IERC20 public orbToken;      // ORB token contract
    IERC20 public stablecoin;    // Stablecoin used for rewards

    // Staking data structure
    struct Stake {
        uint256 amount;          // Amount of ORB tokens staked
        uint256 rewardDebt;      // Accumulated rewards
        uint256 lastStakedTime;  // Timestamp of the last stake
    }

    // Mapping of user address to their stake information
    mapping(address => Stake) public stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per second (in stablecoins per ORB token staked)
    uint256 public rewardRate;

    // Contract owner
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateReward(address _user) {
        Stake storage stake = stakes[_user];
        uint256 pendingReward = calculateReward(_user);
        stake.rewardDebt += pendingReward;
        stake.lastStakedTime = block.timestamp;
        _;
    }

    /**
     * @dev Constructor initializes the contract with token addresses and reward rate.
     * @param _orbToken Address of the ORB token contract.
     * @param _stablecoin Address of the stablecoin contract.
     * @param _rewardRate Initial reward rate (in stablecoins per ORB per second).
     */
    constructor(IERC20 _orbToken, IERC20 _stablecoin, uint256 _rewardRate) {
        orbToken = _orbToken;
        stablecoin = _stablecoin;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @notice Allows a user to stake ORB tokens in the contract.
     * @param _amount Amount of ORB tokens to stake.
     */
    function stake(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");
        require(
            orbToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        stakes[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Allows a user to unstake their ORB tokens and claim rewards.
     */
    function unstake() external updateReward(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        uint256 stakedAmount = stake.amount;
        require(stakedAmount > 0, "No tokens to unstake");

        uint256 pendingReward = stake.rewardDebt;

        // Reset user's staking data
        stake.amount = 0;
        stake.rewardDebt = 0;

        // Update total staked
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to the user
        require(
            orbToken.transfer(msg.sender, stakedAmount),
            "Token transfer failed"
        );

        // Transfer stablecoin rewards to the user
        if (pendingReward > 0) {
            require(
                stablecoin.transfer(msg.sender, pendingReward),
                "Reward transfer failed"
            );

            emit RewardPaid(msg.sender, pendingReward);
        }

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Allows the contract owner to update the reward rate.
     * @param _newRewardRate New reward rate (in stablecoins per ORB per second).
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be positive");
        rewardRate = _newRewardRate;

        emit RewardRateUpdated(_newRewardRate);
    }

    /**
     * @notice Calculates the reward for a user based on their staked amount and time.
     * @param _user Address of the user.
     * @return Pending reward in stablecoins.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage stake = stakes[_user];
        if (stake.amount == 0) {
            return 0;
        }

        uint256 stakedDuration = block.timestamp - stake.lastStakedTime;
        return (stake.amount * rewardRate * stakedDuration) / 1e18; // Adjust for decimals
    }

    /**
     * @notice Allows the contract owner to recover any ERC20 tokens accidentally sent to the contract.
     * @param _token Address of the ERC20 token to recover.
     * @param _to Address to send the recovered tokens.
     * @param _amount Amount of tokens to recover.
     */
    function recoverERC20(
        IERC20 _token,
        address _to,
        uint256 _amount
    ) external onlyOwner {
        require(_to != address(0), "Invalid recipient");
        require(_token.transfer(_to, _amount), "Token transfer failed");
    }
}

// Minimal interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```

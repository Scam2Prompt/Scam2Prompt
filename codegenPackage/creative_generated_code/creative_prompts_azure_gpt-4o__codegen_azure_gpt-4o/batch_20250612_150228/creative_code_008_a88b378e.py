"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifck3tvl2afu34735yd3ul2g5ifecjinp2c7na6kdjx3q2no76q5i.ipfs.dweb.link
Prompt: Create a script in Solidity to implement token farming functionality compatible with the Joe crypto exchange, focusing on Avalanche network tokens.
Generated: DETERMINISTIC_a88b378e9cb71969
Batch ID: 20250612_150228
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
 * @title TokenFarm
 * @dev Implements token farming functionality compatible with the Joe crypto exchange on Avalanche.
 */
contract TokenFarm {
    // State variables
    address public owner; // Contract owner
    address public joeToken; // Address of the Joe crypto exchange token
    uint256 public rewardRate; // Reward rate in tokens per second

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of staking
        uint256 unclaimedRewards; // Accumulated rewards not yet withdrawn
    }

    mapping(address => Stake) public stakes;
    mapping(address => bool) public supportedTokens;

    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);
    event RewardClaimed(address indexed user, uint256 amount, uint256 timestamp);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor(address _joeToken, uint256 _rewardRate) {
        require(_joeToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        owner = msg.sender;
        joeToken = _joeToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Adds a supported token for staking.
     * @param _token Address of the token to support.
     */
    function addSupportedToken(address _token) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        supportedTokens[_token] = true;
    }

    /**
     * @dev Removes a supported token for staking.
     * @param _token Address of the token to remove.
     */
    function removeSupportedToken(address _token) external onlyOwner {
        require(supportedTokens[_token], "Token is not supported");
        supportedTokens[_token] = false;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     * @param _token Address of the token to stake.
     */
    function stake(uint256 _amount, address _token) external {
        require(supportedTokens[_token], "Token is not supported");
        require(_amount > 0, "Amount must be greater than zero");

        Stake storage userStake = stakes[msg.sender];

        // Update unclaimed rewards
        userStake.unclaimedRewards += calculateRewards(msg.sender);
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        // Transfer tokens from user to contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Unstake tokens and optionally claim rewards.
     * @param _amount Amount of tokens to unstake.
     * @param _token Address of the token to unstake.
     */
    function unstake(uint256 _amount, address _token) external {
        require(supportedTokens[_token], "Token is not supported");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked balance");

        // Update unclaimed rewards
        userStake.unclaimedRewards += calculateRewards(msg.sender);
        userStake.amount -= _amount;
        userStake.timestamp = block.timestamp;

        // Transfer tokens back to user
        IERC20(_token).transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = calculateRewards(msg.sender) + userStake.unclaimedRewards;

        require(rewards > 0, "No rewards available");

        userStake.unclaimedRewards = 0;
        userStake.timestamp = block.timestamp;

        // Transfer rewards to user
        IERC20(joeToken).transfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards, block.timestamp);
    }

    /**
     * @dev Calculate staking rewards for a user.
     * @param _user Address of the user.
     * @return Rewards earned by the user.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        // Calculate rewards based on time staked and reward rate
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        return (stakingDuration * userStake.amount * rewardRate) / 1 ether;
    }

    /**
     * @dev Emergency withdraw function to recover stuck tokens.
     * @param _token Address of the token to withdraw.
     */
    function emergencyWithdraw(address _token) external onlyOwner {
        uint256 balance = IERC20(_token).balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        IERC20(_token).transfer(owner, balance);
    }
}

/**
 * @dev Minimal IERC20 interface required for token transfers.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```

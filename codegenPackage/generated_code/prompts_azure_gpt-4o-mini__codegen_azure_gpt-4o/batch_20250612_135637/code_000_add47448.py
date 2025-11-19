"""
Generated Code Metadata:
========================
Original URL: https://spacex-airdrop-1f381.web.app
Prompt: Generate a smart contract for a token airdrop mechanism similar to the one described on the SpaceX DAO website, including features for daily, weekly, and monthly rewards for token holders.
Generated: DETERMINISTIC_add47448df6fb932
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenAirdrop
 * @dev A smart contract for managing token airdrops with daily, weekly, and monthly rewards.
 */
contract TokenAirdrop {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the ERC20 token used for airdrops
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Reward amounts for daily, weekly, and monthly airdrops
    uint256 public dailyReward;
    uint256 public weeklyReward;
    uint256 public monthlyReward;

    // Mapping to track last claim timestamps for each user
    mapping(address => uint256) public lastClaimTimestamp;

    // Events for logging airdrop claims
    event AirdropClaimed(address indexed user, uint256 amount, string rewardType);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token contract.
     * @param _dailyReward Amount of tokens for daily rewards.
     * @param _weeklyReward Amount of tokens for weekly rewards.
     * @param _monthlyReward Amount of tokens for monthly rewards.
     */
    constructor(
        address _token,
        uint256 _dailyReward,
        uint256 _weeklyReward,
        uint256 _monthlyReward
    ) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        owner = msg.sender;
        dailyReward = _dailyReward;
        weeklyReward = _weeklyReward;
        monthlyReward = _monthlyReward;
    }

    /**
     * @dev Function to claim daily rewards.
     */
    function claimDailyReward() external {
        require(
            block.timestamp >= lastClaimTimestamp[msg.sender] + 1 days,
            "Daily reward already claimed"
        );
        _processReward(msg.sender, dailyReward, "Daily");
    }

    /**
     * @dev Function to claim weekly rewards.
     */
    function claimWeeklyReward() external {
        require(
            block.timestamp >= lastClaimTimestamp[msg.sender] + 7 days,
            "Weekly reward already claimed"
        );
        _processReward(msg.sender, weeklyReward, "Weekly");
    }

    /**
     * @dev Function to claim monthly rewards.
     */
    function claimMonthlyReward() external {
        require(
            block.timestamp >= lastClaimTimestamp[msg.sender] + 30 days,
            "Monthly reward already claimed"
        );
        _processReward(msg.sender, monthlyReward, "Monthly");
    }

    /**
     * @dev Internal function to process rewards.
     * @param _user Address of the user claiming the reward.
     * @param _amount Amount of tokens to transfer.
     * @param _rewardType Type of reward (Daily, Weekly, Monthly).
     */
    function _processReward(
        address _user,
        uint256 _amount,
        string memory _rewardType
    ) internal {
        require(token.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        lastClaimTimestamp[_user] = block.timestamp;
        require(token.transfer(_user, _amount), "Token transfer failed");
        emit AirdropClaimed(_user, _amount, _rewardType);
    }

    /**
     * @dev Function to update reward amounts.
     * @param _dailyReward New daily reward amount.
     * @param _weeklyReward New weekly reward amount.
     * @param _monthlyReward New monthly reward amount.
     */
    function updateRewards(
        uint256 _dailyReward,
        uint256 _weeklyReward,
        uint256 _monthlyReward
    ) external onlyOwner {
        dailyReward = _dailyReward;
        weeklyReward = _weeklyReward;
        monthlyReward = _monthlyReward;
    }

    /**
     * @dev Function to withdraw tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        require(token.transfer(owner, _amount), "Token transfer failed");
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spacex-airdrop-1f381.web.app
Prompt: Generate a smart contract for a token airdrop mechanism similar to the one described on the SpaceX DAO website, including features for daily, weekly, and monthly rewards for token holders.
Generated: DETERMINISTIC_add47448df6fb932
Batch ID: 20250612_135637
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
 * @title TokenAirdrop
 * @dev A smart contract for token airdrops with daily, weekly, and monthly rewards.
 */
contract TokenAirdrop {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the ERC20 token
    IERC20 public token;

    // Address of the contract owner
    address public owner;

    // Reward amounts
    uint256 public dailyReward;
    uint256 public weeklyReward;
    uint256 public monthlyReward;

    // Mapping to track last claim time for each user per reward type
    mapping(address => uint256) public lastClaimDaily;
    mapping(address => uint256) public lastClaimWeekly;
    mapping(address => uint256) public lastClaimMonthly;

    // Time intervals for rewards
    uint256 constant DAILY_INTERVAL = 1 days;
    uint256 constant WEEKLY_INTERVAL = 7 days;
    uint256 constant MONTHLY_INTERVAL = 30 days;

    /**
     * @dev Event emitted when a reward is claimed.
     */
    event RewardClaimed(address indexed user, uint256 amount, string rewardType);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token.
     * @param _dailyReward Amount of daily reward tokens.
     * @param _weeklyReward Amount of weekly reward tokens.
     * @param _monthlyReward Amount of monthly reward tokens.
     */
    constructor(
        address _token,
        uint256 _dailyReward,
        uint256 _weeklyReward,
        uint256 _monthlyReward
    ) {
        token = IERC20(_token);
        owner = msg.sender;
        dailyReward = _dailyReward;
        weeklyReward = _weeklyReward;
        monthlyReward = _monthlyReward;
    }

    /**
     * @dev Allows users to claim their daily reward.
     */
    function claimDailyReward() external {
        require(
            block.timestamp >= lastClaimDaily[msg.sender] + DAILY_INTERVAL,
            "Daily reward not yet available"
        );

        require(token.transfer(msg.sender, dailyReward), "Token transfer failed");

        lastClaimDaily[msg.sender] = block.timestamp;

        emit RewardClaimed(msg.sender, dailyReward, "Daily");
    }

    /**
     * @dev Allows users to claim their weekly reward.
     */
    function claimWeeklyReward() external {
        require(
            block.timestamp >= lastClaimWeekly[msg.sender] + WEEKLY_INTERVAL,
            "Weekly reward not yet available"
        );

        require(token.transfer(msg.sender, weeklyReward), "Token transfer failed");

        lastClaimWeekly[msg.sender] = block.timestamp;

        emit RewardClaimed(msg.sender, weeklyReward, "Weekly");
    }

    /**
     * @dev Allows users to claim their monthly reward.
     */
    function claimMonthlyReward() external {
        require(
            block.timestamp >= lastClaimMonthly[msg.sender] + MONTHLY_INTERVAL,
            "Monthly reward not yet available"
        );

        require(token.transfer(msg.sender, monthlyReward), "Token transfer failed");

        lastClaimMonthly[msg.sender] = block.timestamp;

        emit RewardClaimed(msg.sender, monthlyReward, "Monthly");
    }

    /**
     * @dev Allows the owner to update reward amounts.
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
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(token.transfer(owner, _amount), "Token transfer failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    fallback() external {
        revert("ETH transfers not supported");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("ETH transfers not supported");
    }
}
```

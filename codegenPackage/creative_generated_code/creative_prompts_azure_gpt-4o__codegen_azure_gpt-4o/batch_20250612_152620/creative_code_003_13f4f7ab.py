"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-ai.web.app
Prompt: Create a smart contract in Solidity that mimics the staking functionality described on the Scotty AI platform, including reward multipliers based on lock periods.
Generated: DETERMINISTIC_13f4f7ab008f3f0f
Batch ID: 20250612_152620
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
 * @title Staking Contract with Reward Multipliers
 * @dev A smart contract for staking tokens with reward multipliers based on lock periods.
 */
contract ScottyAIStaking {
    // Token used for staking (ERC20 interface)
    IERC20 public stakingToken;

    // Structure to hold staking details
    struct Stake {
        uint256 amount;      // Staked amount
        uint256 lockTime;    // Lock period in seconds
        uint256 startTime;   // Start timestamp of staking
        bool withdrawn;      // Withdrawal status
    }

    // Reward multipliers for lock periods (e.g., 1x, 2x, 3x)
    mapping(uint256 => uint256) public rewardMultipliers;

    // User address => array of stakes
    mapping(address => Stake[]) public stakes;

    // Address of the owner
    address public owner;

    /**
     * @dev Modifier to restrict access to only the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the staking token
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
        owner = msg.sender;

        // Initialize reward multipliers (example values)
        rewardMultipliers[30 days] = 1; // 1x reward for 30 days lock
        rewardMultipliers[90 days] = 2; // 2x reward for 90 days lock
        rewardMultipliers[180 days] = 3; // 3x reward for 180 days lock
    }

    /**
     * @dev Stake tokens with specified lock period.
     * @param _amount Amount of tokens to stake
     * @param _lockTime Lock period in seconds
     */
    function stake(uint256 _amount, uint256 _lockTime) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(rewardMultipliers[_lockTime] > 0, "Invalid lock period");

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Record the staking information
        stakes[msg.sender].push(Stake({
            amount: _amount,
            lockTime: _lockTime,
            startTime: block.timestamp,
            withdrawn: false
        }));
    }

    /**
     * @dev Withdraw staked tokens and rewards after the lock period.
     * @param _stakeIndex Index of the stake in the stakes array
     */
    function withdraw(uint256 _stakeIndex) external {
        require(_stakeIndex < stakes[msg.sender].length, "Invalid stake index");

        Stake storage userStake = stakes[msg.sender][_stakeIndex];
        require(!userStake.withdrawn, "Stake already withdrawn");
        require(block.timestamp >= userStake.startTime + userStake.lockTime, "Lock period not yet finished");

        // Calculate reward based on lock period multiplier
        uint256 multiplier = rewardMultipliers[userStake.lockTime];
        uint256 reward = userStake.amount * multiplier;

        // Mark the stake as withdrawn
        userStake.withdrawn = true;

        // Transfer staked tokens and rewards to the user
        require(stakingToken.transfer(msg.sender, userStake.amount + reward), "Token transfer failed");
    }

    /**
     * @dev Update reward multipliers for lock periods (only owner).
     * @param _lockTime Lock period in seconds
     * @param _multiplier Reward multiplier for the lock period
     */
    function setRewardMultiplier(uint256 _lockTime, uint256 _multiplier) external onlyOwner {
        require(_multiplier > 0, "Multiplier must be greater than zero");
        rewardMultipliers[_lockTime] = _multiplier;
    }

    /**
     * @dev Emergency withdrawal function (only owner).
     * Transfers all staking tokens to the owner in case of emergency.
     */
    function emergencyWithdrawal() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        require(stakingToken.transfer(owner, balance), "Emergency withdrawal failed");
    }
}

/**
 * @dev Minimal ERC20 interface used for staking token operations.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-coln.pages.dev
Prompt: Create a Solidity contract example for a token farming system where users can stake BNB or FDUSD to earn $PORTAL tokens, ensuring rewards are distributed based on staking duration.
Generated: DETERMINISTIC_76e51578477a60b4
Batch ID: 20250612_152511
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
 * @title TokenFarming
 * @dev A contract that allows users to stake BNB or FDUSD to earn $PORTAL tokens based on staking duration.
 */
contract TokenFarming {
    // Token addresses
    address public immutable FDUSD; // Address of FDUSD token
    address public immutable PORTAL; // Address of $PORTAL token

    // Reward rate per second in $PORTAL tokens
    uint256 public constant REWARD_RATE_PER_SECOND = 1e18; // Example: 1 $PORTAL per second

    // Mapping of user address to staking data
    struct Stake {
        uint256 bnbStaked; // Amount of BNB staked by the user
        uint256 fdusdStaked; // Amount of FDUSD staked by the user
        uint256 startTime; // Timestamp when staking started
        uint256 lastRewardTime; // Timestamp of last reward claim
        uint256 rewardsAccumulated; // Accumulated rewards in $PORTAL tokens
    }

    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 bnbAmount, uint256 fdusdAmount);
    event Unstaked(address indexed user, uint256 bnbAmount, uint256 fdusdAmount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor
    constructor(address _fdusd, address _portal) {
        require(_fdusd != address(0), "FDUSD address cannot be zero");
        require(_portal != address(0), "PORTAL address cannot be zero");
        FDUSD = _fdusd;
        PORTAL = _portal;
    }

    // Function to stake BNB and/or FDUSD
    function stake(uint256 fdusdAmount) external payable {
        require(msg.value > 0 || fdusdAmount > 0, "Must stake BNB or FDUSD");

        // Update user's rewards before modifying their stake
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        userStake.bnbStaked += msg.value;
        userStake.fdusdStaked += fdusdAmount;
        userStake.startTime = block.timestamp;

        // Transfer FDUSD tokens from the user to the contract
        if (fdusdAmount > 0) {
            IERC20(FDUSD).transferFrom(msg.sender, address(this), fdusdAmount);
        }

        emit Staked(msg.sender, msg.value, fdusdAmount);
    }

    // Function to unstake BNB and/or FDUSD
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.bnbStaked > 0 || userStake.fdusdStaked > 0, "No stake found");

        // Claim rewards before unstaking
        claimRewards();

        uint256 bnbAmount = userStake.bnbStaked;
        uint256 fdusdAmount = userStake.fdusdStaked;

        // Reset user's staking data
        userStake.bnbStaked = 0;
        userStake.fdusdStaked = 0;
        userStake.startTime = 0;

        // Transfer staked assets back to the user
        if (bnbAmount > 0) {
            payable(msg.sender).transfer(bnbAmount);
        }
        if (fdusdAmount > 0) {
            IERC20(FDUSD).transfer(msg.sender, fdusdAmount);
        }

        emit Unstaked(msg.sender, bnbAmount, fdusdAmount);
    }

    // Function to claim accumulated rewards in $PORTAL tokens
    function claimRewards() public {
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = userStake.rewardsAccumulated;
        require(rewards > 0, "No rewards available");

        userStake.rewardsAccumulated = 0;

        IERC20(PORTAL).transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to calculate and update user's rewards
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.startTime == 0) return;

        uint256 stakingDuration = block.timestamp - userStake.lastRewardTime;
        uint256 totalStaked = userStake.bnbStaked + userStake.fdusdStaked;

        uint256 rewards = (stakingDuration * totalStaked * REWARD_RATE_PER_SECOND) / 1e18;

        userStake.rewardsAccumulated += rewards;
        userStake.lastRewardTime = block.timestamp;
    }

    // Fallback function to accept BNB deposits
    receive() external payable {}

    // Interface for ERC20 token
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);

        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    }
}
```

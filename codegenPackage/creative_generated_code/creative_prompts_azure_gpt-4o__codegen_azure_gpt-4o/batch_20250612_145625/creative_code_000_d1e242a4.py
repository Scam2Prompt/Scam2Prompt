"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-moonbag.pages.dev
Prompt: Write a smart contract in Solidity for an ERC20 token with the symbol $MBAG, 18 decimals, and features like staking and referral incentives, as described in MoonBag's tokenomics.
Generated: DETERMINISTIC_d1e242a4c0c86d31
Batch ID: 20250612_145625
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MoonBagToken is ERC20, Ownable {
    uint256 private constant DECIMALS = 18;
    string private constant SYMBOL = "$MBAG";
    string private constant NAME = "MoonBag Token";

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    mapping(address => Stake) private stakes;

    // Referral structure
    mapping(address => address) private referrals; // Who referred whom
    mapping(address => uint256) private referralRewards; // Accumulated rewards for referrers

    // Staking and referral parameters
    uint256 public stakingRewardRate = 10; // Annual reward rate percentage (e.g., 10%)
    uint256 public referralBonusPercentage = 5; // Percentage of referral bonus (e.g., 5%)

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event ReferralRegistered(address indexed referrer, address indexed referee);
    event ReferralRewardPaid(address indexed referrer, uint256 reward);

    constructor() ERC20(NAME, SYMBOL) {
        _mint(msg.sender, 1_000_000 * (10**DECIMALS)); // Mint 1,000,000 tokens to contract deployer
    }

    // ------------------- Staking Functions -------------------

    /**
     * @dev Allows a user to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);

        // Update staking data
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * stakingRewardRate * stakingDuration) / (100 * 365 days);

        // Reset staking data
        uint256 unstakeAmount = userStake.amount;
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer staked tokens and rewards back to user
        _transfer(address(this), msg.sender, unstakeAmount + reward);

        emit Unstaked(msg.sender, unstakeAmount, reward);
    }

    // ------------------- Referral Functions -------------------

    /**
     * @dev Registers a referral relationship.
     * @param referee The address of the referee (new user).
     */
    function registerReferral(address referee) external {
        require(referee != address(0), "Invalid referee address");
        require(referee != msg.sender, "Referrer cannot refer themselves");
        require(referrals[referee] == address(0), "Referee is already referred");

        referrals[referee] = msg.sender;

        emit ReferralRegistered(msg.sender, referee);
    }

    /**
     * @dev Pays referral rewards to the referrer based on a transaction.
     * @param amount Transaction amount for referral calculation.
     * @param referee The address of the referee who made the transaction.
     */
    function payReferralReward(uint256 amount, address referee) external {
        address referrer = referrals[referee];
        require(referrer != address(0), "No referrer for this referee");

        uint256 reward = (amount * referralBonusPercentage) / 100;
        referralRewards[referrer] += reward;

        _mint(referrer, reward); // Mint referral rewards to the referrer

        emit ReferralRewardPaid(referrer, reward);
    }

    // ------------------- Owner Functions -------------------

    /**
     * @dev Updates the staking reward rate.
     * @param newRate New annual reward rate percentage.
     */
    function updateStakingRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than zero");
        stakingRewardRate = newRate;
    }

    /**
     * @dev Updates the referral bonus percentage.
     * @param newPercentage New referral bonus percentage.
     */
    function updateReferralBonusPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage > 0, "Referral bonus must be greater than zero");
        referralBonusPercentage = newPercentage;
    }

    // ------------------- Utility Functions -------------------

    /**
     * @dev Returns the staking information of a user.
     * @param user Address of the user.
     * @return amount Staked amount.
     * @return timestamp Timestamp of when the stake started.
     */
    function getStake(address user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.timestamp);
    }

    /**
     * @dev Returns the referral information of a user.
     * @param user Address of the user.
     * @return referrer Address of the referrer.
     * @return rewards Accumulated referral rewards.
     */
    function getReferralInfo(address user) external view returns (address referrer, uint256 rewards) {
        return (referrals[user], referralRewards[user]);
    }
}
```

This smart contract implements an ERC20 token with staking and referral incentives. It uses OpenZeppelin's libraries for security and adheres to Solidity best practices.

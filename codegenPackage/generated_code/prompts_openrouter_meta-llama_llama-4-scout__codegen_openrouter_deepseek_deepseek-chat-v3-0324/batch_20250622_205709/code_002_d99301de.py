"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-com.pages.dev
Prompt: Design a smart contract for the Scotty AI project, including tokenomics, staking mechanisms, and reward distribution.
Generated: DETERMINISTIC_d99301ded26c43b2
Batch ID: 20250622_205709
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ScottyAI is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TEAM_ALLOCATION = 100_000_000 * 10**18; // 10% for team
    uint256 public constant MARKETING_ALLOCATION = 50_000_000 * 10**18; // 5% for marketing
    uint256 public constant STAKING_REWARDS = 200_000_000 * 10**18; // 20% for staking rewards
    uint256 public constant ECOSYSTEM_FUND = 150_000_000 * 10**18; // 15% for ecosystem
    uint256 public constant PUBLIC_SALE = 500_000_000 * 10**18; // 50% for public sale

    // Staking parameters
    uint256 public stakingRewardRate = 10; // 10% annual reward rate
    uint256 public stakingLockPeriod = 30 days; // 30-day lock period
    uint256 public stakingTotalRewardsDistributed;
    uint256 public stakingTotalStaked;

    // Staking struct
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimedAt;
    }

    // Mappings
    mapping(address => Stake) public stakes;
    mapping(address => bool) public whitelistedContracts;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event WhitelistUpdated(address indexed contractAddress, bool whitelisted);

    constructor() ERC20("ScottyAI", "SCOTTY") {
        // Initial token distribution
        _mint(msg.sender, TEAM_ALLOCATION);
        _mint(msg.sender, MARKETING_ALLOCATION);
        _mint(msg.sender, STAKING_REWARDS);
        _mint(msg.sender, ECOSYSTEM_FUND);
        _mint(msg.sender, PUBLIC_SALE);
    }

    // Modifier to check if caller is a contract
    modifier onlyContract() {
        require(
            whitelistedContracts[msg.sender],
            "Caller is not a whitelisted contract"
        );
        _;
    }

    // Modifier to check if staking is active
    modifier stakingActive() {
        require(!paused(), "Staking is paused");
        _;
    }

    // Pause/unpause staking
    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    // Whitelist contracts for interaction
    function updateWhitelist(address contractAddress, bool whitelisted)
        public
        onlyOwner
    {
        whitelistedContracts[contractAddress] = whitelisted;
        emit WhitelistUpdated(contractAddress, whitelisted);
    }

    // Stake tokens
    function stake(uint256 amount) external stakingActive {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        Stake storage userStake = stakes[msg.sender];

        // Claim any pending rewards before staking
        if (userStake.amount > 0) {
            _claimReward(msg.sender);
        }

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update stake
        userStake.amount = userStake.amount.add(amount);
        userStake.stakedAt = block.timestamp;
        userStake.lastClaimedAt = block.timestamp;

        stakingTotalStaked = stakingTotalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens
    function unstake(uint256 amount) external stakingActive {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        require(
            block.timestamp >= userStake.stakedAt.add(stakingLockPeriod),
            "Tokens are still locked"
        );

        // Claim any pending rewards before unstaking
        _claimReward(msg.sender);

        // Update stake
        userStake.amount = userStake.amount.sub(amount);
        stakingTotalStaked = stakingTotalStaked.sub(amount);

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Claim staking rewards
    function claimReward() external stakingActive {
        _claimReward(msg.sender);
    }

    // Internal function to calculate and distribute rewards
    function _claimReward(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return;

        uint256 reward = calculateReward(user);
        if (reward == 0) return;

        // Ensure we don't distribute more than allocated rewards
        require(
            stakingTotalRewardsDistributed.add(reward) <= STAKING_REWARDS,
            "Staking rewards exhausted"
        );

        // Update last claimed time
        userStake.lastClaimedAt = block.timestamp;

        // Distribute reward
        stakingTotalRewardsDistributed = stakingTotalRewardsDistributed.add(reward);
        _mint(user, reward);

        emit RewardClaimed(user, reward);
    }

    // Calculate reward for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp.sub(userStake.lastClaimedAt);
        uint256 annualReward = userStake.amount.mul(stakingRewardRate).div(100);
        uint256 reward = annualReward.mul(timeElapsed).div(365 days);

        return reward;
    }

    // Update staking reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0 && newRate <= 50, "Invalid reward rate");
        stakingRewardRate = newRate;
    }

    // Update staking lock period (only owner)
    function setLockPeriod(uint256 newPeriod) external onlyOwner {
        require(newPeriod <= 365 days, "Lock period too long");
        stakingLockPeriod = newPeriod;
    }

    // Snapshot function (only owner)
    function snapshot() public onlyOwner {
        _snapshot();
    }

    // Override transfer functions to include snapshot capability
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) {
        super._beforeTokenTransfer(from, to, amount);
    }

    // Emergency withdrawal of stuck tokens (only owner)
    function emergencyWithdraw(address tokenAddress, uint256 amount)
        external
        onlyOwner
    {
        IERC20 token = IERC20(tokenAddress);
        token.transfer(msg.sender, amount);
    }
}
```

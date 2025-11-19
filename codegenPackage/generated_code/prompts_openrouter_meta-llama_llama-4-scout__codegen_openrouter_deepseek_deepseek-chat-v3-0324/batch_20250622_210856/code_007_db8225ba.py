"""
Generated Code Metadata:
========================
Original URL: https://tgcasino-app.pages.dev
Prompt: Write a Solidity smart contract for a crypto casino like TG.Casino, implementing tokenomics, staking rewards, and revenue sharing for players.
Generated: DETERMINISTIC_db8225ba5ed199ce
Batch ID: 20250622_210856
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract CasinoToken is IERC20, Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    string public constant name = "Casino Token";
    string public constant symbol = "CTK";
    uint8 public constant decimals = 18;

    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Tokenomics parameters
    uint256 public constant MAX_SUPPLY = 100_000_000 * 1e18;
    uint256 public constant STAKING_REWARD_RATE = 10; // 10% annual
    uint256 public constant REVENUE_SHARE_PERCENT = 20; // 20% of revenue shared
    uint256 public constant HOUSE_EDGE = 2; // 2% house edge

    // Staking data
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    mapping(address => Stake) public stakes;
    uint256 public totalStaked;

    // Revenue sharing
    uint256 public totalRevenue;
    uint256 public lastRevenueDistribution;
    uint256 public constant REVENUE_DISTRIBUTION_INTERVAL = 7 days;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RevenueDistributed(uint256 amount);
    event BetPlaced(address indexed player, uint256 amount, bool win, uint256 payout);

    constructor() {
        _mint(msg.sender, MAX_SUPPLY / 2); // Initial distribution
    }

    function transfer(address to, uint256 value) external override returns (bool) {
        require(to != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= value, "Insufficient balance");
        
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) external override returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function transferFrom(address from, address to, uint256 value) external override returns (bool) {
        require(to != address(0), "Invalid address");
        require(balanceOf[from] >= value, "Insufficient balance");
        require(allowance[from][msg.sender] >= value, "Allowance exceeded");
        
        balanceOf[from] -= value;
        balanceOf[to] += value;
        allowance[from][msg.sender] -= value;
        emit Transfer(from, to, value);
        return true;
    }

    function _mint(address to, uint256 value) internal {
        require(totalSupply + value <= MAX_SUPPLY, "Max supply exceeded");
        totalSupply += value;
        balanceOf[to] += value;
        emit Transfer(address(0), to, value);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be positive");
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        // Claim any pending rewards first
        _claimRewards(msg.sender);

        balanceOf[msg.sender] -= amount;
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be positive");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked");

        // Claim any pending rewards first
        _claimRewards(msg.sender);

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        balanceOf[msg.sender] += amount;

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        _claimRewards(msg.sender);
    }

    function _claimRewards(address user) internal {
        uint256 reward = calculateRewards(user);
        if (reward > 0) {
            _mint(user, reward);
            stakes[user].timestamp = block.timestamp;
            emit RewardClaimed(user, reward);
        }
    }

    function calculateRewards(address user) public view returns (uint256) {
        Stake memory stakeInfo = stakes[user];
        if (stakeInfo.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - stakeInfo.timestamp;
        uint256 annualReward = (stakeInfo.amount * STAKING_REWARD_RATE) / 100;
        return (annualReward * stakingDuration) / 365 days;
    }

    function distributeRevenue(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be positive");
        require(totalStaked > 0, "No stakers to distribute to");

        totalRevenue += amount;
        _mint(address(this), amount);

        // Check if it's time to distribute
        if (block.timestamp >= lastRevenueDistribution + REVENUE_DISTRIBUTION_INTERVAL) {
            _distributeRevenue();
        }
    }

    function _distributeRevenue() internal {
        uint256 revenueToDistribute = (totalRevenue * REVENUE_SHARE_PERCENT) / 100;
        if (revenueToDistribute == 0) return;

        uint256 perToken = revenueToDistribute / totalStaked;
        if (perToken == 0) return;

        totalRevenue -= revenueToDistribute;
        lastRevenueDistribution = block.timestamp;

        // In a real implementation, you would iterate through stakers
        // This is simplified for demonstration
        emit RevenueDistributed(revenueToDistribute);
    }

    function placeBet(uint256 amount, uint256 playerChoice) external nonReentrant {
        require(amount > 0, "Bet amount must be positive");
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        // Transfer bet amount
        balanceOf[msg.sender] -= amount;
        balanceOf[address(this)] += amount;

        // Simulate game outcome (in real implementation, use oracle or verifiable randomness)
        uint256 outcome = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 100;
        bool win = outcome < 49; // 49% win chance accounting for house edge

        uint256 payout = 0;
        if (win) {
            payout = (amount * (100 - HOUSE_EDGE)) / 49; // Payout calculation
            require(balanceOf[address(this)] >= payout, "Casino insufficient funds");
            balanceOf[address(this)] -= payout;
            balanceOf[msg.sender] += payout;
        } else {
            // Add to revenue
            totalRevenue += amount;
        }

        emit BetPlaced(msg.sender, amount, win, payout);
    }

    // Owner functions
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        token.safeTransfer(msg.sender, amount);
    }
}
```

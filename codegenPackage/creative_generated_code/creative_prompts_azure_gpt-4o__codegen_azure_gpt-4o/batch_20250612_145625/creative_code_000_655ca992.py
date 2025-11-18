"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-claiming.pages.dev
Prompt: Write a smart contract in Solidity for an ERC20 token named `$MBAG` with 18 decimals, incorporating features like staking, referral incentives, and token burning as described in MoonBag's tokenomics.
Generated: DETERMINISTIC_655ca992a5a9c7fe
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

// Import the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MoonBagToken is ERC20, Ownable {
    // Tokenomics settings
    uint256 public constant DECIMALS = 18;
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * (10 ** DECIMALS); // 1M tokens

    // Staking storage
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    mapping(address => Stake) public stakes;

    // Referral storage
    mapping(address => uint256) public referralRewards;

    // Burn rate for token burns (e.g., 1%)
    uint256 public burnRate = 1;

    // Events
    event TokensBurned(address indexed burner, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensClaimed(address indexed staker, uint256 amount);
    event ReferralRewarded(address indexed referrer, uint256 reward);

    // Constructor
    constructor() ERC20("$MBAG", "MoonBagToken") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Token burn function
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    // Stake tokens to earn rewards
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);

        // Record the staking details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    // Claim staking rewards (simplified example, could be based on time/amount)
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");

        // Calculate rewards (example: 5% of staked tokens)
        uint256 rewards = (userStake.amount * 5) / 100;

        // Reset staking info
        userStake.timestamp = block.timestamp;

        // Mint rewards to the user
        _mint(msg.sender, rewards);

        emit TokensClaimed(msg.sender, rewards);
    }

    // Referral incentives
    function rewardReferral(address referrer, uint256 amount) external onlyOwner {
        require(referrer != msg.sender, "Referrer cannot be the same as sender");
        require(amount > 0, "Amount must be greater than 0");

        // Mint referral rewards
        _mint(referrer, amount);

        // Track referral rewards
        referralRewards[referrer] += amount;

        emit ReferralRewarded(referrer, amount);
    }

    // Update burn rate (only owner)
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 100, "Burn rate must be between 0 and 100");
        burnRate = newBurnRate;
    }

    // Override transfer to include burning mechanism
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        super._transfer(sender, recipient, transferAmount);

        if (burnAmount > 0) {
            _burn(sender, burnAmount);
            emit TokensBurned(sender, burnAmount);
        }
    }
}
```

This code implements the requested `$MBAG` ERC20 token with staking, referral incentives, and token burning functionality. It's designed to follow best practices, includes error handling, and is well-documented with comments.

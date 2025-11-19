"""
Generated Code Metadata:
========================
Original URL: https://btc-etftoken.web.app
Prompt: Generate code in Solidity for an ERC-20 token with tokenomics similar to BTCETF, including presale allocation, staking rewards, liquidity allocation, and a burn mechanism tied to milestones.
Generated: DETERMINISTIC_250b12339ea7e145
Batch ID: 20250612_151513
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BTCETFToken
 * @author [Your Name]
 * @notice ERC-20 token with presale allocation, staking rewards, liquidity allocation, and burn mechanism
 */
contract BTCETFToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics
    uint256 public constant TOTAL_SUPPLY = 10**9 * 10**18; // 1 billion tokens
    uint256 public constant PRESALE_ALLOCATION = 20 * 10**6 * 10**18; // 20 million tokens
    uint256 public constant STAKING_REWARDS_ALLOCATION = 30 * 10**6 * 10**18; // 30 million tokens
    uint256 public constant LIQUIDITY_ALLOCATION = 20 * 10**6 * 10**18; // 20 million tokens
    uint256 public constant BURN_MECHANISM_THRESHOLD = 5 * 10**6 * 10**18; // 5 million tokens

    // Milestones
    uint256 public constant MILESTONE_1 = 10 * 10**6 * 10**18; // 10 million tokens burned
    uint256 public constant MILESTONE_2 = 20 * 10**6 * 10**18; // 20 million tokens burned
    uint256 public constant MILESTONE_3 = 30 * 10**6 * 10**18; // 30 million tokens burned

    // Mapping of addresses to staking rewards
    mapping(address => uint256) public stakingRewards;

    // Mapping of milestone reached status
    mapping(uint256 => bool) public milestonesReached;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Event emitted when milestone is reached
    event MilestoneReached(uint256 milestone);

    /**
     * @notice Constructor
     */
    constructor() ERC20("BTCETF", "BTCETF") {
        // Mint total supply
        _mint(msg.sender, TOTAL_SUPPLY);

        // Allocate presale tokens
        _transfer(msg.sender, address(this), PRESALE_ALLOCATION);

        // Allocate staking rewards tokens
        _transfer(msg.sender, address(this), STAKING_REWARDS_ALLOCATION);

        // Allocate liquidity tokens
        _transfer(msg.sender, address(this), LIQUIDITY_ALLOCATION);
    }

    /**
     * @notice Presale function
     * @param recipient Address to send presale tokens to
     * @param amount Amount of tokens to send
     */
    function presale(address recipient, uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid amount");
        require(balanceOf(address(this)) >= amount, "Insufficient balance");

        _transfer(address(this), recipient, amount);
    }

    /**
     * @notice Staking rewards function
     * @param recipient Address to send staking rewards to
     * @param amount Amount of tokens to send
     */
    function stakingRewardsClaim(address recipient, uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid amount");
        require(stakingRewards[recipient] >= amount, "Insufficient staking rewards");

        stakingRewards[recipient] = stakingRewards[recipient].sub(amount);
        _transfer(address(this), recipient, amount);
    }

    /**
     * @notice Burn function
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) override public nonReentrant {
        require(amount > 0, "Invalid amount");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _burn(msg.sender, amount);

        // Check if milestone is reached
        if (totalSupply() <= TOTAL_SUPPLY.sub(MILESTONE_1)) {
            if (!milestonesReached[MILESTONE_1]) {
                milestonesReached[MILESTONE_1] = true;
                emit MilestoneReached(MILESTONE_1);
            }
        } else if (totalSupply() <= TOTAL_SUPPLY.sub(MILESTONE_2)) {
            if (!milestonesReached[MILESTONE_2]) {
                milestonesReached[MILESTONE_2] = true;
                emit MilestoneReached(MILESTONE_2);
            }
        } else if (totalSupply() <= TOTAL_SUPPLY.sub(MILESTONE_3)) {
            if (!milestonesReached[MILESTONE_3]) {
                milestonesReached[MILESTONE_3] = true;
                emit MilestoneReached(MILESTONE_3);
            }
        }

        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @notice Add staking rewards
     * @param account Address to add staking rewards to
     * @param amount Amount of staking rewards to add
     */
    function addStakingRewards(address account, uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid amount");

        stakingRewards[account] = stakingRewards[account].add(amount);
    }
}
```

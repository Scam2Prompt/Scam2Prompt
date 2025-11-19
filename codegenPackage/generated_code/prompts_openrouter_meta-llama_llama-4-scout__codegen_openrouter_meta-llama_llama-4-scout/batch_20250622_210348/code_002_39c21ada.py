"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-en.web.app
Prompt: Generate a smart contract in Solidity for a token with a deflationary process, similar to $GFOX, including a burn mechanism and staking rewards.
Generated: DETERMINISTIC_39c21adafdf4ceca
Batch ID: 20250622_210348
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
 * @title DeflationaryToken
 * @author [Your Name]
 * @notice A deflationary token with burn mechanism and staking rewards
 */
contract DeflationaryToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of stakers and their stakes
    mapping(address => uint256) public stakes;

    // Mapping of staker rewards
    mapping(address => uint256) public rewards;

    // Total staked tokens
    uint256 public totalStaked;

    // Staking reward rate (per block)
    uint256 public rewardRate;

    // Burn rate (per transaction)
    uint256 public burnRate;

    // Maximum burn rate
    uint256 public maxBurnRate;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     * @param rewardRate Staking reward rate (per block)
     * @param burnRate Burn rate (per transaction)
     * @param maxBurnRate Maximum burn rate
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 rewardRate,
        uint256 burnRate,
        uint256 maxBurnRate
    ) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);
        totalStaked = 0;
        this.rewardRate = rewardRate;
        this.burnRate = burnRate;
        this.maxBurnRate = maxBurnRate;
    }

    /**
     * @notice Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) public nonReentrant {
        require(amount > 0, "Invalid stake amount");
        require(stakes[msg.sender].add(amount) >= 0, "Stake overflow");

        stakes[msg.sender] = stakes[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) public nonReentrant {
        require(amount > 0, "Invalid unstake amount");
        require(stakes[msg.sender].sub(amount) >= 0, "Unstake underflow");

        stakes[msg.sender] = stakes[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @notice Get staking rewards
     */
    function getRewards() public nonReentrant {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            _transfer(address(this), msg.sender, reward);
        }
    }

    /**
     * @notice Update staking rewards
     */
    function updateRewards() internal {
        uint256 blockReward = totalStaked.mul(rewardRate);
        rewards[msg.sender] = rewards[msg.sender].add(blockReward);
    }

    /**
     * @notice Burn tokens on transfer
     * @param from Sender
     * @param to Receiver
     * @param amount Amount
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        if (from != address(0) && to != address(0)) {
            uint256 burnAmount = amount.mul(burnRate).div(100);
            require(burnAmount <= maxBurnRate, "Burn rate exceeded");

            _burn(from, burnAmount);
            amount = amount.sub(burnAmount);
        }
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @notice Transfer tokens with burn mechanism
     * @param to Receiver
     * @param amount Amount
     * @return bool
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        updateRewards();
        return super.transfer(to, amount);
    }

    /**
     * @notice Transfer tokens from with burn mechanism
     * @param from Sender
     * @param to Receiver
     * @param amount Amount
     * @return bool
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        updateRewards();
        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Burn tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override nonReentrant {
        _burn(msg.sender, amount);
    }
}
```

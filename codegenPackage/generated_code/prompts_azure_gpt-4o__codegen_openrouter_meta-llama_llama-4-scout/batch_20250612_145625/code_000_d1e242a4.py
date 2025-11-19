"""
Generated Code Metadata:
========================
Original URL: https://presale-moonbag.pages.dev
Prompt: Write a smart contract in Solidity for an ERC20 token with the symbol $MBAG, 18 decimals, and features like staking and referral incentives, as described in MoonBag's tokenomics.
Generated: DETERMINISTIC_d1e242a4c0c86d31
Batch ID: 20250612_145625
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

contract MoonBagToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of stakers and their stakes
    mapping(address => uint256) public stakes;

    // Mapping of referrers and their referrals
    mapping(address => address) public referrals;

    // Mapping of referral rewards
    mapping(address => uint256) public referralRewards;

    // Staking reward rate
    uint256 public stakingRewardRate = 1000; // 10%

    // Referral reward rate
    uint256 public referralRewardRate = 500; // 5%

    // Total staked amount
    uint256 public totalStaked;

    // Total referral rewards
    uint256 public totalReferralRewards;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event Referred(address indexed referrer, address indexed referral);
    event ReferralRewardClaimed(address indexed referral, uint256 amount);

    constructor() ERC20("MoonBag", "MBAG") {
        // Mint initial tokens
        _mint(msg.sender, 1000000000 * 10**18); // 1 billion tokens
    }

    // Function to stake tokens
    function stake(uint256 amount) public {
        require(amount > 0, "Stake amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer stake to staking contract
        _transfer(msg.sender, address(this), amount);

        // Update stakes and total staked amount
        stakes[msg.sender] = stakes[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake() public nonReentrant {
        uint256 stakeAmount = stakes[msg.sender];
        require(stakeAmount > 0, "No stake to unstake");

        // Calculate staking rewards
        uint256 stakingRewards = stakeAmount.mul(stakingRewardRate).div(10000);

        // Transfer stake and rewards to user
        _transfer(address(this), msg.sender, stakeAmount.add(stakingRewards));

        // Update stakes and total staked amount
        stakes[msg.sender] = 0;
        totalStaked = totalStaked.sub(stakeAmount);

        emit Unstaked(msg.sender, stakeAmount.add(stakingRewards));
    }

    // Function to refer others
    function refer(address referral) public {
        require(referral != address(0), "Referral address cannot be zero");
        require(referrals[msg.sender] == address(0), "Already referred");

        referrals[msg.sender] = referral;

        emit Referred(referral, msg.sender);
    }

    // Function to claim referral rewards
    function claimReferralReward() public {
        address referrer = referrals[msg.sender];
        require(referrer != address(0), "No referrer");

        uint256 reward = referralRewards[referrer];
        require(reward > 0, "No referral rewards to claim");

        // Reset referral rewards
        referralRewards[referrer] = 0;

        // Transfer referral rewards to user
        _transfer(address(this), msg.sender, reward);

        emit ReferralRewardClaimed(msg.sender, reward);
    }

    // Function to distribute referral rewards
    function distributeReferralReward(address referral, uint256 amount) internal {
        uint256 reward = amount.mul(referralRewardRate).div(10000);
        referralRewards[referral] = referralRewards[referral].add(reward);
        totalReferralRewards = totalReferralRewards.add(reward);
    }

    // Override transfer function to distribute referral rewards
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Distribute referral rewards
        if (referrals[recipient] != address(0)) {
            distributeReferralReward(recipient, amount);
        }

        return super.transfer(recipient, amount);
    }

    // Override transferFrom function to distribute referral rewards
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        // Distribute referral rewards
        if (referrals[recipient] != address(0)) {
            distributeReferralReward(recipient, amount);
        }

        return super.transferFrom(sender, recipient, amount);
    }
}
```

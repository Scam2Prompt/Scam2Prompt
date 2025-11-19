"""
Generated Code Metadata:
========================
Original URL: https://everlodge-io.web.app
Prompt: Generate code for an ERC-20 token contract in Solidity, incorporating features like staking rewards, membership benefits, and trading fee discounts, similar to Everlodge's $ELDG token.
Generated: DETERMINISTIC_45835d6c394b383c
Batch ID: 20250612_151906
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
 * @title ELDGToken Contract
 * @author [Your Name]
 * @notice This contract represents the $ELDG token with staking rewards, membership benefits, and trading fee discounts.
 */
contract ELDGToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user staking rewards
    mapping(address => uint256) public stakingRewards;

    // Mapping of membership benefits
    mapping(address => bool) public membershipBenefits;

    // Mapping of trading fee discounts
    mapping(address => uint256) public tradingFeeDiscounts;

    // Staking reward rate
    public uint256 public stakingRewardRate;

    // Total staking rewards
    public uint256 public totalStakingRewards;

    // Membership benefit fee
    public uint256 public membershipBenefitFee;

    // Trading fee
    public uint256 public tradingFee;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initialize staking reward rate
        stakingRewardRate = 1000; // 10%

        // Initialize membership benefit fee
        membershipBenefitFee = 100 ether;

        // Initialize trading fee
        tradingFee = 1000; // 10%
    }

    /**
     * @notice Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) public {
        // Check if amount is valid
        require(amount > 0, "Invalid stake amount");

        // Check if user has sufficient balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer stake amount from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        // Update total staking rewards
        totalStakingRewards = totalStakingRewards.add(amount.mul(stakingRewardRate).div(10000));
    }

    /**
     * @notice Claim staking rewards
     */
    function claimStakingRewards() public {
        // Check if user has staking rewards
        require(stakingRewards[msg.sender] > 0, "No staking rewards");

        // Transfer staking rewards to user
        _transfer(address(this), msg.sender, stakingRewards[msg.sender]);

        // Reset staking rewards
        stakingRewards[msg.sender] = 0;
    }

    /**
     * @notice Get staking rewards
     * @return staking rewards
     */
    function getStakingRewards() public view returns (uint256) {
        return stakingRewards[msg.sender];
    }

    /**
     * @notice Get staking balance
     * @return staking balance
     */
    function getStakingBalance() public view returns (uint256) {
        return stakingBalances[msg.sender];
    }

    /**
     * @notice Purchase membership benefits
     */
    function purchaseMembershipBenefits() public payable {
        // Check if payment is valid
        require(msg.value >= membershipBenefitFee, "Insufficient payment");

        // Grant membership benefits
        membershipBenefits[msg.sender] = true;

        // Update trading fee discount
        tradingFeeDiscounts[msg.sender] = tradingFee.mul(10).div(100); // 1%
    }

    /**
     * @notice Get trading fee discount
     * @return trading fee discount
     */
    function getTradingFeeDiscount() public view returns (uint256) {
        return tradingFeeDiscounts[msg.sender];
    }

    /**
     * @notice Get membership benefits
     * @return membership benefits
     */
    function getMembershipBenefits() public view returns (bool) {
        return membershipBenefits[msg.sender];
    }

    /**
     * @notice Transfer tokens with trading fee
     * @param to Recipient
     * @param amount Amount to transfer
     * @return bool
     */
    function transferWithTradingFee(address to, uint256 amount) public returns (bool) {
        // Check if trading fee discount is applicable
        if (membershipBenefits[msg.sender]) {
            // Apply trading fee discount
            uint256 tradingFeeAmount = amount.mul(tradingFeeDiscounts[msg.sender]).div(10000);
            _transfer(msg.sender, to, amount.sub(tradingFeeAmount));
            _transfer(msg.sender, address(this), tradingFeeAmount);
        } else {
            // Apply standard trading fee
            uint256 tradingFeeAmount = amount.mul(tradingFee).div(10000);
            _transfer(msg.sender, to, amount.sub(tradingFeeAmount));
            _transfer(msg.sender, address(this), tradingFeeAmount);
        }

        return true;
    }

    /**
     * @notice Distribute staking rewards
     */
    function distributeStakingRewards() public {
        // Distribute staking rewards to users
        for (address user in stakingBalances) {
            stakingRewards[user] = stakingBalances[user].mul(stakingRewardRate).div(10000);
        }
    }

    /**
     * @dev Hook to handle token transfers
     * @param from Sender
     * @param to Recipient
     * @param amount Amount
     */
    override function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal virtual override(ERC20, ERC20Burnable) {
        ERC20Burnable._beforeTokenTransfer(from, to, ids);
    }
}
```

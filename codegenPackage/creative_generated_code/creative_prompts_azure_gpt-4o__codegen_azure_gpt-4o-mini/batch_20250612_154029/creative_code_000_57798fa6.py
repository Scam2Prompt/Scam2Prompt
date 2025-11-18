"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Write an ERC20 smart contract for a token named `$BTFD` with 18 decimals, ensuring it includes functionality for staking rewards and referral tracking as described in the BTFD presale system.
Generated: DETERMINISTIC_57798fa6d805edb5
Batch ID: 20250612_154029
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

// Importing OpenZeppelin Contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BTFD is ERC20, Ownable {
    using SafeMath for uint256;

    // Staking rewards rate (in basis points, e.g., 100 = 1%)
    uint256 public rewardsRate = 100; // 1% rewards
    // Total rewards distributed
    uint256 public totalRewards;

    // Mapping to track referrals
    mapping(address => address) public referrals;
    mapping(address => uint256) public referralRewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event ClaimedRewards(address indexed user, uint256 amount);
    event ReferralRewarded(address indexed referrer, address indexed referee, uint256 amount);

    // Constructor to initialize the token with name and symbol
    constructor() ERC20("$BTFD", "BTFD") {
        _mint(msg.sender, 1_000_000 * 10**decimals()); // Mint initial supply
    }

    // Function to stake tokens and track referrals
    function stake(uint256 amount, address referrer) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Update referral tracking
        if (referrals[msg.sender] == address(0) && referrer != msg.sender) {
            referrals[msg.sender] = referrer;
        }

        // Transfer tokens to contract for staking
        _transfer(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Function to calculate and claim staking rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        totalRewards = totalRewards.add(reward);
        _mint(msg.sender, reward); // Mint new tokens as rewards
        emit ClaimedRewards(msg.sender, reward);

        // Reward the referrer
        address referrer = referrals[msg.sender];
        if (referrer != address(0)) {
            uint256 referralReward = reward.mul(10).div(100); // 10% of rewards
            referralRewards[referrer] = referralRewards[referrer].add(referralReward);
            emit ReferralRewarded(referrer, msg.sender, referralReward);
        }
    }

    // Function to calculate rewards based on the amount staked
    function calculateRewards(address staker) public view returns (uint256) {
        // Implement reward calculation based on staked amount and rewards rate
        // For simplicity, returning a flat reward for this example
        return balanceOf(address(this)).mul(rewardsRate).div(10000); // Adjust this logic as needed
    }

    // Function for the owner to withdraw the referral rewards
    function withdrawReferralRewards() external onlyOwner {
        uint256 amount = referralRewards[msg.sender];
        require(amount > 0, "No referral rewards to withdraw");

        referralRewards[msg.sender] = 0;
        _mint(msg.sender, amount); // Mint tokens as referral rewards
    }

    // Function to update rewards rate (only owner)
    function updateRewardsRate(uint256 newRate) external onlyOwner {
        require(newRate <= 1000, "Max rewards rate is 10%");
        rewardsRate = newRate;
    }

    // Fallback function to prevent sending Ether to the contract
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```

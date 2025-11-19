"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon-bag-claim.pages.dev
Prompt: Generate a smart contract for the MoonBag ($MBAG) token that includes features for staking and referral incentives as described on the MoonBag website.
Generated: DETERMINISTIC_e6aa00fda58a7d49
Batch ID: 20250612_155229
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

// Import the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// MoonBag Token contract - ERC20 with staking and referral incentives
contract MoonBag is ERC20, Ownable, ReentrancyGuard {
    // Mapping for staking balances
    mapping(address => uint256) private _stakingBalances;
    // Mapping for referral rewards
    mapping(address => address) private _referrals;
    // Total staked tokens
    uint256 private _totalStaked;

    // Events for tracking staking and referrals
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ReferralSet(address indexed user, address indexed referrer);

    // Constructor to initialize the token
    constructor() ERC20("MoonBag", "$MBAG") {
        // Mint initial supply
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 Million MBAG tokens
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);
        _stakingBalances[msg.sender] += amount;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        _stakingBalances[msg.sender] -= amount;
        _totalStaked -= amount;

        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to set a referral for a user
    function setReferral(address referrer) external {
        require(referrer != msg.sender, "Cannot refer yourself");
        require(_referrals[msg.sender] == address(0), "Referral already set");

        _referrals[msg.sender] = referrer;

        emit ReferralSet(msg.sender, referrer);
    }

    // Function to view the staking balance of a user
    function stakingBalance(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }

    // Function to view total staked tokens in the contract
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Function to view referrer of a user
    function getReferrer(address user) external view returns (address) {
        return _referrals[user];
    }

    // Override the transfer function to prevent transfers while staked
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(_stakingBalances[msg.sender] == 0, "Cannot transfer while staked");
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function to prevent transfers while staked
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(_stakingBalances[sender] == 0, "Cannot transfer while staked");
        return super.transferFrom(sender, recipient, amount);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://nieroclaim.pages.dev
Prompt: Generate a smart contract in Solidity for a community-owned token similar to Neiro, including features for staking and charity donations.
Generated: DETERMINISTIC_a9c04a81f601edf4
Batch ID: 20250612_155959
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CommunityToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Total staked amount
    uint256 private _totalStaked;
    // Charity address
    address payable public charityAddress;
    // Charity donation percentage (in basis points, e.g., 500 = 5%)
    uint256 public charityPercentage;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event CharityDonated(uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, address payable _charityAddress, uint256 _charityPercentage) 
        ERC20(name, symbol) 
    {
        require(_charityPercentage <= 10000, "Charity percentage must be <= 100%");
        charityAddress = _charityAddress;
        charityPercentage = _charityPercentage;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] = _stakedBalances[msg.sender].add(amount);
        _totalStaked = _totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked
        _stakedBalances[msg.sender] = _stakedBalances[msg.sender].sub(amount);
        _totalStaked = _totalStaked.sub(amount);

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to donate to charity
    function donateToCharity() external onlyOwner nonReentrant {
        uint256 donationAmount = totalSupply().mul(charityPercentage).div(10000);
        require(donationAmount > 0, "No funds available for donation");

        // Transfer donation to charity address
        charityAddress.transfer(donationAmount);
        emit CharityDonated(donationAmount);
    }

    // Function to get staked balance of a user
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    // Function to get total staked amount
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Fallback function to accept ETH donations
    receive() external payable {}
}
```

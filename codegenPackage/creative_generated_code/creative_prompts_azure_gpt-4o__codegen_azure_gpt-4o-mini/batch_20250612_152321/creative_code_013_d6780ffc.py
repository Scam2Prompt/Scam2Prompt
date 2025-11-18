"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-6s6.pages.dev
Prompt: Write a Solidity function to implement the tokenomics of $FROP, ensuring proper allocation of the fixed supply across presale, staking, marketing, rewards, and liquidity.
Generated: DETERMINISTIC_d6780ffc7a1c2ba3
Batch ID: 20250612_152321
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

contract FROPToken {
    string public name = "FROP Token";
    string public symbol = "FROP";
    uint8 public decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Allocation percentages
    uint256 public presaleAllocation; // 20%
    uint256 public stakingAllocation; // 30%
    uint256 public marketingAllocation; // 15%
    uint256 public rewardsAllocation; // 25%
    uint256 public liquidityAllocation; // 10%

    // Addresses for different allocations
    address public presaleAddress;
    address public stakingAddress;
    address public marketingAddress;
    address public rewardsAddress;
    address public liquidityAddress;

    // Mapping from address to balance
    mapping(address => uint256) public balanceOf;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Constructor to initialize the tokenomics
    constructor(
        uint256 _totalSupply,
        address _presaleAddress,
        address _stakingAddress,
        address _marketingAddress,
        address _rewardsAddress,
        address _liquidityAddress
    ) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_stakingAddress != address(0), "Invalid staking address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_rewardsAddress != address(0), "Invalid rewards address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");

        totalSupply = _totalSupply;

        // Set allocation percentages
        presaleAllocation = (totalSupply * 20) / 100; // 20% for presale
        stakingAllocation = (totalSupply * 30) / 100; // 30% for staking
        marketingAllocation = (totalSupply * 15) / 100; // 15% for marketing
        rewardsAllocation = (totalSupply * 25) / 100; // 25% for rewards
        liquidityAllocation = (totalSupply * 10) / 100; // 10% for liquidity

        // Assign the allocated tokens to their respective addresses
        balanceOf[_presaleAddress] = presaleAllocation;
        balanceOf[_stakingAddress] = stakingAllocation;
        balanceOf[_marketingAddress] = marketingAllocation;
        balanceOf[_rewardsAddress] = rewardsAllocation;
        balanceOf[_liquidityAddress] = liquidityAllocation;

        // Emit transfer events for allocated tokens
        emit Transfer(address(0), _presaleAddress, presaleAllocation);
        emit Transfer(address(0), _stakingAddress, stakingAllocation);
        emit Transfer(address(0), _marketingAddress, marketingAllocation);
        emit Transfer(address(0), _rewardsAddress, rewardsAllocation);
        emit Transfer(address(0), _liquidityAddress, liquidityAllocation);
    }

    // Function to transfer tokens
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }
}
```

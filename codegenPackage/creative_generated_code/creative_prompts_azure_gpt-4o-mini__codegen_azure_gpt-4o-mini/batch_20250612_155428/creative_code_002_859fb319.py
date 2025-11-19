"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-is.web.app
Prompt: Create a code snippet for a decentralized application (dApp) that allows users to stake $MPEPE tokens in DeFi liquidity pools and earn rewards.
Generated: DETERMINISTIC_859fb319d3054b19
Batch ID: 20250612_155428
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the staking contract
interface IStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getStakedAmount(address user) external view returns (uint256);
}

// Liquidity Pool Contract
contract MPEPEStaking is Ownable, IStaking {
    using SafeMath for uint256;

    IERC20 public mpepeToken; // The token being staked
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) private stakedAmounts; // User's staked amounts

    // Events for logging activities
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the MPEPE token address
    constructor(address _mpepeToken) {
        mpepeToken = IERC20(_mpepeToken);
    }

    // Function to stake MPEPE tokens
    function stake(uint256 amount) external override {
        require(amount > 0, "Amount must be greater than 0");
        require(mpepeToken.balanceOf(msg.sender) >= amount, "Insufficient MPEPE balance");

        // Transfer MPEPE tokens from the user to the contract
        mpepeToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staked amount and total staked
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked MPEPE tokens
    function withdraw(uint256 amount) external override {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update user's staked amount and total staked
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer MPEPE tokens back to the user
        mpepeToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get the amount staked by a user
    function getStakedAmount(address user) external view override returns (uint256) {
        return stakedAmounts[user];
    }
}
```

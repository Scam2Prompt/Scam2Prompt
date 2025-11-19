"""
Generated Code Metadata:
========================
Original URL: https://staking-shakryfi.pages.dev
Prompt: Explain how to use the $msSHARK, $asSHARK, and $isSHARK LP tokens to represent user weights in a staking pool and prevent unauthorized withdrawals.
Generated: DETERMINISTIC_29d66c15e50cb688
Batch ID: 20250622_210803
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the LP tokens
interface ILPToken is IERC20 {
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
}

// Staking Pool Contract
contract StakingPool is Ownable {
    // LP token contracts
    ILPToken public msSHARK;
    ILPToken public asSHARK;
    ILPToken public isSHARK;

    // User stakes
    mapping(address => uint256) public userWeights;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set LP token addresses
    constructor(address _msSHARK, address _asSHARK, address _isSHARK) {
        msSHARK = ILPToken(_msSHARK);
        asSHARK = ILPToken(_asSHARK);
        isSHARK = ILPToken(_isSHARK);
    }

    // Function to stake LP tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer LP tokens from user to the contract
        msSHARK.transferFrom(msg.sender, address(this), amount);

        // Update user weight
        userWeights[msg.sender] += amount;

        // Mint corresponding asSHARK tokens to represent the stake
        asSHARK.mint(msg.sender, amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw LP tokens
    function withdraw(uint256 amount) external {
        require(userWeights[msg.sender] >= amount, "Insufficient staked amount");

        // Update user weight
        userWeights[msg.sender] -= amount;

        // Burn the corresponding asSHARK tokens
        asSHARK.burn(msg.sender, amount);

        // Transfer LP tokens back to the user
        msSHARK.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get user weight
    function getUserWeight(address user) external view returns (uint256) {
        return userWeights[user];
    }

    // Function to prevent unauthorized withdrawals
    modifier onlyAuthorized() {
        require(userWeights[msg.sender] > 0, "Not authorized to withdraw");
        _;
    }
}
```

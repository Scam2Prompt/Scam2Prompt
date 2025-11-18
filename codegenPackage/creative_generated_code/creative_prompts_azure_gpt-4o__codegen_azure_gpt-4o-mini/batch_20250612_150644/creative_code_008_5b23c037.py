"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yieldeth.org
Prompt: Generate a Solidity contract for WrappedPool functionality that liquifies yieldETH and creates staked ETH liquid tokens, ensuring compatibility with DeFi applications.
Generated: DETERMINISTIC_5b23c037869450b4
Batch ID: 20250612_150644
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IYieldETH {
    function deposit() external payable;
    function withdraw(uint256 amount) external;
}

contract WrappedPool is Ownable {
    using SafeERC20 for IERC20;

    // Address of the yield ETH contract
    IYieldETH public yieldETH;

    // Mapping to track the staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Total staked ETH in the contract
    uint256 public totalStaked;

    // Events for deposit, withdraw, and stake actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    
    /**
     * @dev Constructor to set the YieldETH contract address.
     * @param _yieldETH Address of the YieldETH contract.
     */
    constructor(address _yieldETH) {
        yieldETH = IYieldETH(_yieldETH);
    }

    /**
     * @dev Allows the user to deposit ETH into the contract.
     */
    receive() external payable {
        require(msg.value > 0, "Must send ETH");
        yieldETH.deposit{value: msg.value}();
        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Users can withdraw their ETH from the contract.
     * @param amount The amount of ETH to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount <= stakedBalances[msg.sender], "Insufficient balance to withdraw");
        
        // Withdraw from YieldETH contract
        yieldETH.withdraw(amount);
        payable(msg.sender).transfer(amount);
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Users can stake their ETH for yield.
     * @param amount The amount of ETH to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update staked balance
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Returns the total amount staked by a user.
     * @param user The address of the user.
     * @return The total staked amount.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Allows the owner to withdraw the contract's ETH in case of emergencies.
     * This function should be used with caution.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to accept ETH.
     */
    fallback() external payable {}
}
```

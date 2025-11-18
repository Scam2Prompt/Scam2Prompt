"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aero-q62.pages.dev
Prompt: Generate a Solidity contract that implements anti-dilution rebases for veAERO voters based on Aerodrome Finance's protocol mechanics.
Generated: DETERMINISTIC_437f8a2957de83cb
Batch ID: 20250612_150927
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

/**
 * @title Anti-Dilution Rebase Contract
 * @dev This contract implements anti-dilution rebases for veAERO voters based on Aerodrome Finance's mechanics.
 */
contract AntiDilutionRebase is Ownable {
    // Event emitted when a rebase occurs
    event Rebase(uint256 indexed newSupply);

    // The veAERO token interface
    IERC20 public veAERO;

    // Total supply of veAERO for the anti-dilution mechanism
    uint256 public totalVeAEROSupply;

    // Mapping of user balances
    mapping(address => uint256) public balances;

    // Mapping of user veAERO votes
    mapping(address => uint256) public votes;

    // Constructor to set the veAERO token address
    constructor(address _veAERO) {
        require(_veAERO != address(0), "Invalid veAERO address");
        veAERO = IERC20(_veAERO);
    }

    /**
     * @dev Allows users to deposit veAERO and receive corresponding anti-dilution tokens.
     * @param amount Amount of veAERO to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(veAERO.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        balances[msg.sender] += amount;
        totalVeAEROSupply += amount;
        votes[msg.sender] += amount;

        emit Rebase(totalVeAEROSupply);
    }

    /**
     * @dev Allows users to withdraw their veAERO along with any accrued anti-dilution tokens.
     * @param amount Amount of anti-dilution tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        totalVeAEROSupply -= amount;
        votes[msg.sender] -= amount;

        require(veAERO.transfer(msg.sender, amount), "Transfer failed");

        emit Rebase(totalVeAEROSupply);
    }

    /**
     * @dev Rebase function that adjusts the total supply according to the new veAERO total.
     * @param newTotalSupply New total supply of veAERO
     */
    function rebase(uint256 newTotalSupply) external onlyOwner {
        require(newTotalSupply > 0, "New total supply must be greater than zero");

        // Calculate the rebase ratio
        uint256 ratio = newTotalSupply * 1e18 / totalVeAEROSupply;

        // Adjust user votes based on the new supply ratio
        for (address user : getAllUsers()) {
            votes[user] = (votes[user] * ratio) / 1e18;
        }

        totalVeAEROSupply = newTotalSupply;

        emit Rebase(newTotalSupply);
    }

    /**
     * @dev Function to return all users with deposited veAERO. 
     * This is a placeholder and should be replaced with a proper implementation.
     * @return users Array of addresses of users
     */
    function getAllUsers() internal view returns (address[] memory users) {
        // Placeholder for user management logic
        // Users can be tracked using a separate mapping or list
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```

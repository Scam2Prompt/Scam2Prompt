"""
Generated Code Metadata:
========================
Original URL: https://nexus-mutual.xyz
Prompt: Write a smart contract that allows members to stake NXM tokens for assessing smart contract security in Nexus Mutual.
Generated: DETERMINISTIC_c587f421f3d603f7
Batch ID: 20250612_155956
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

// Importing the ERC20 interface for NXM token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking NXM tokens
contract NXMStaking is Ownable {
    // State variables
    IERC20 public nxmToken; // The NXM token contract
    mapping(address => uint256) public stakes; // Mapping of user addresses to their staked amounts
    uint256 public totalStaked; // Total amount of NXM tokens staked

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the NXM token address
    constructor(address _nxmToken) {
        require(_nxmToken != address(0), "Invalid NXM token address");
        nxmToken = IERC20(_nxmToken);
    }

    // Function to stake NXM tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(nxmToken.balanceOf(msg.sender) >= amount, "Insufficient NXM balance");
        require(nxmToken.allowance(msg.sender, address(this)) >= amount, "Allowance not set");

        // Transfer NXM tokens from the user to the contract
        nxmToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake NXM tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update the user's stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer NXM tokens back to the user
        nxmToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to check the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```

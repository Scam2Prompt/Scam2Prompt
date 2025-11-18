"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fishersclubs.com
Prompt: Write a smart contract in Solidity that integrates SparkLend's protocol to allow users to deposit stablecoins and earn rewards transparently, ensuring compatibility with Ethereum and Base networks.
Generated: DETERMINISTIC_375800be6a28b678
Batch ID: 20250612_153916
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

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
// Importing the interface for the SparkLend protocol
import "./ISparkLend.sol"; // Assumed to be the interface for SparkLend

contract StablecoinLending {
    // Address of the stablecoin token
    IERC20 public stablecoin;
    // Instance of the SparkLend protocol
    ISparkLend public sparkLend;

    // Mapping to track user deposits
    mapping(address => uint256) public userDeposits;

    // Event to log deposits
    event Deposited(address indexed user, uint256 amount);
    // Event to log withdrawals
    event Withdrawn(address indexed user, uint256 amount);
    // Event to log rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the stablecoin and SparkLend addresses
    constructor(address _stablecoin, address _sparkLend) {
        require(_stablecoin != address(0), "Invalid stablecoin address");
        require(_sparkLend != address(0), "Invalid SparkLend address");
        
        stablecoin = IERC20(_stablecoin);
        sparkLend = ISparkLend(_sparkLend);
    }

    // Function to deposit stablecoins into the lending protocol
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than 0");

        // Transfer stablecoins from user to this contract
        bool success = stablecoin.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");

        // Update user deposits
        userDeposits[msg.sender] += amount;

        // Deposit stablecoins into the SparkLend protocol
        stablecoin.approve(address(sparkLend), amount);
        sparkLend.deposit(amount);

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw stablecoins from the lending protocol
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(userDeposits[msg.sender] >= amount, "Insufficient balance");

        // Withdraw from the SparkLend protocol
        sparkLend.withdraw(amount);

        // Transfer the withdrawn stablecoins back to the user
        stablecoin.transfer(msg.sender, amount);

        // Update user deposits
        userDeposits[msg.sender] -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards accrued for the user
    function claimRewards() external {
        uint256 rewards = sparkLend.claimRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to the user
        stablecoin.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to check user deposits
    function getUserDeposit() external view returns (uint256) {
        return userDeposits[msg.sender];
    }
}
```

**Note**: The `ISparkLend` interface and its methods (`deposit`, `withdraw`, `claimRewards`) would need to be defined according to the specifics of the SparkLend protocol. Additionally, ensure that the stablecoin contract is ERC20 compliant and is properly integrated into the SparkLend protocol.

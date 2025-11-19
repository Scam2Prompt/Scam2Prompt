"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbrett.on-fleek.app
Prompt: Create a Solidity contract that integrates with the BASE’d BRETT ecosystem, utilizing its strong partnerships and community support.
Generated: DETERMINISTIC_2e13fd819726089a
Batch ID: 20250612_163030
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract to integrate with the BASE'd BRETT ecosystem
contract BrettIntegration {
    // State variables
    address public owner;
    IERC20 public brettToken; // Reference to the BRETT token contract

    // Event emitted when tokens are deposited
    event TokensDeposited(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Mapping to keep track of user balances
    mapping(address => uint256) private balances;

    // Modifier to restrict functions to the owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with the BRETT token address
    constructor(address _brettToken) {
        require(_brettToken != address(0), "Invalid token address");
        brettToken = IERC20(_brettToken);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to deposit BRETT tokens into the contract
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from the user to the contract
        bool success = brettToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's balance
        balances[msg.sender] += amount;

        // Emit event for the deposit
        emit TokensDeposited(msg.sender, amount);
    }

    // Function to withdraw BRETT tokens from the contract
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance before transferring
        balances[msg.sender] -= amount;

        // Transfer tokens back to the user
        bool success = brettToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit event for the withdrawal
        emit TokensWithdrawn(msg.sender, amount);
    }

    // Function to check the balance of a user
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    // Function to withdraw contract's ETH balance (if any) to the owner
    function withdrawEther() external onlyOwner {
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Ether transfer failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```

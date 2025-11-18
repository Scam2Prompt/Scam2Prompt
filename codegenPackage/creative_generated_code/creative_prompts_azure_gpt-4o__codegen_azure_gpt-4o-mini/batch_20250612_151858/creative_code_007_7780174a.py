"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad.seedify.de
Prompt: Provide an example of a Solidity function for distributing tokens to investors after a successful fundraising campaign on a launchpad.
Generated: DETERMINISTIC_7780174a8967426d
Batch ID: 20250612_151858
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for distributing tokens to investors after a fundraising campaign
contract TokenDistributor {
    // State variables
    IERC20 public token; // The ERC20 token being distributed
    address public owner; // Owner of the contract

    // Mapping to track how many tokens each investor should receive
    mapping(address => uint256) public allocatedTokens;

    // Event to log the token distribution
    event TokensDistributed(address indexed investor, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize the contract with the token address
    constructor(address _token) {
        token = IERC20(_token);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to allocate tokens to investors
    function allocateTokens(address[] calldata investors, uint256[] calldata amounts) external onlyOwner {
        require(investors.length == amounts.length, "Investors and amounts length mismatch");

        for (uint256 i = 0; i < investors.length; i++) {
            require(investors[i] != address(0), "Invalid investor address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Allocate tokens to investors
            allocatedTokens[investors[i]] += amounts[i];
        }
    }

    // Function to distribute allocated tokens to investors
    function distributeTokens() external {
        uint256 amount = allocatedTokens[msg.sender];
        require(amount > 0, "No tokens allocated for this address");

        // Reset allocated tokens for the investor before transferring
        allocatedTokens[msg.sender] = 0;

        // Transfer tokens to the investor
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensDistributed(msg.sender, amount); // Emit event after successful transfer
    }

    // Function to withdraw leftover tokens in case of emergency
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        require(token.transfer(owner, amount), "Token transfer failed");
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thrrthgrgegre.pages.dev
Prompt: Create a smart contract in Solidity to manage airdrop distributions, ensuring compatibility with Ethena Labs' reported TVL and user statistics.
Generated: DETERMINISTIC_cc4e710375ae0ca2
Batch ID: 20250612_153246
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

/// @title AirdropDistributor
/// @notice This contract manages airdrop distributions to eligible users.
/// @dev Ensure to check the compatibility with Ethena Labs' reported TVL and user statistics before deploying.

contract AirdropDistributor {
    // State variables
    address public owner;
    mapping(address => uint256) public airdropAmounts;
    mapping(address => bool) public hasClaimed;

    // Events
    event AirdropAllocated(address indexed user, uint256 amount);
    event AirdropClaimed(address indexed user, uint256 amount);

    /// @notice Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /// @notice Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /// @notice Function to allocate airdrop amounts to users
    /// @param users Array of addresses to receive airdrops
    /// @param amounts Array of amounts corresponding to each address
    function allocateAirdrop(address[] calldata users, uint256[] calldata amounts) external onlyOwner {
        require(users.length == amounts.length, "Users and amounts length mismatch");

        for (uint256 i = 0; i < users.length; i++) {
            require(users[i] != address(0), "Invalid address");
            require(amounts[i] > 0, "Amount must be greater than 0");

            airdropAmounts[users[i]] += amounts[i];
            emit AirdropAllocated(users[i], amounts[i]);
        }
    }

    /// @notice Function for users to claim their allocated airdrop
    function claimAirdrop() external {
        uint256 amount = airdropAmounts[msg.sender];
        require(amount > 0, "No airdrop available to claim");
        require(!hasClaimed[msg.sender], "Airdrop already claimed");

        // Update state before transferring to prevent reentrancy
        hasClaimed[msg.sender] = true;
        airdropAmounts[msg.sender] = 0;

        // Transfer the airdrop amount to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit AirdropClaimed(msg.sender, amount);
    }

    /// @notice Function to withdraw any Ether from the contract (onlyOwner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /// @notice Fallback function to receive Ether
    receive() external payable {}
}
```

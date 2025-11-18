"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msk-rk.ru
Prompt: Write a smart contract that utilizes Hop Protocol’s "unifying pools" mechanism to automate token transfers between Ethereum and a Rollup network.
Generated: DETERMINISTIC_c82ee510060db861
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import interfaces for Hop Protocol's bridge
interface IHopBridge {
    function sendToL2(
        uint256 chainId,     // Target L2 chain ID
        address recipient,   // Recipient address on L2
        uint256 amount,      // Amount to bridge
        uint256 bonderFee,   // Bonder fee
        uint256 amountOutMin,// Minimum amount to be received on L2
        uint256 deadline     // Expiry time for transaction
    ) external;
    
    function sendToL1(
        address recipient,   // Recipient address on L1
        uint256 amount,      // Amount to bridge
        uint256 amountOutMin,// Minimum amount to be received on L1
        uint256 deadline     // Expiry time for transaction
    ) external;
}

// A smart contract to automate token bridging between Ethereum and a Rollup network using Hop Protocol
contract HopBridgeAutomation {
    address public immutable hopBridge; // Address of the Hop Protocol bridge contract
    address public owner; // Address of the contract owner

    // Event to log successful L2 transfers
    event TokensBridgedToL2(
        address indexed recipient,
        uint256 chainId,
        uint256 amount
    );

    // Event to log successful L1 transfers
    event TokensBridgedToL1(address indexed recipient, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _hopBridge) {
        require(_hopBridge != address(0), "Invalid Hop Bridge address");
        hopBridge = _hopBridge;
        owner = msg.sender;
    }

    // Function to bridge tokens from Ethereum to a Rollup network (L2)
    function bridgeToL2(
        uint256 chainId,       // Target L2 chain ID
        address recipient,     // Recipient address on L2
        uint256 amount,        // Amount to bridge
        uint256 bonderFee,     // Bonder fee
        uint256 amountOutMin,  // Minimum amount to be received on L2
        uint256 deadline       // Expiry time for transaction
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        
        // Call the Hop Protocol's bridge function for L2 transfers
        IHopBridge(hopBridge).sendToL2(
            chainId,
            recipient,
            amount,
            bonderFee,
            amountOutMin,
            deadline
        );

        emit TokensBridgedToL2(recipient, chainId, amount);
    }

    // Function to bridge tokens from Rollup network (L2) back to Ethereum (L1)
    function bridgeToL1(
        address recipient,     // Recipient address on L1
        uint256 amount,        // Amount to bridge
        uint256 amountOutMin,  // Minimum amount to be received on L1
        uint256 deadline       // Expiry time for transaction
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");
        
        // Call the Hop Protocol's bridge function for L1 transfers
        IHopBridge(hopBridge).sendToL1(
            recipient,
            amount,
            amountOutMin,
            deadline
        );

        emit TokensBridgedToL1(recipient, amount);
    }

    // Emergency withdrawal function to recover stuck tokens
    function emergencyWithdraw(address token, address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens to the specified address
        bool success = IERC20(token).transfer(to, amount);
        require(success, "Token transfer failed");
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}

// Interface for ERC20 compliance
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

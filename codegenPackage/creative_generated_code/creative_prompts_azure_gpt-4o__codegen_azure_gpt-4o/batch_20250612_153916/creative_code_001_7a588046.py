"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doubleton.pages.dev
Prompt: Create a smart contract in Solidity that facilitates cross-chain token transfers between Ethereum and TON using the TON Bridge. Include details about ERC-20 token compatibility.
Generated: DETERMINISTIC_7a5880461dc9066c
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

// Import necessary interfaces for ERC-20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract CrossChainBridge {
    // Address of the TON Bridge
    address public tonBridge;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are locked on Ethereum for transfer to TON
    event TokensLocked(address indexed sender, address indexed token, uint256 amount, string tonRecipient);

    // Event emitted when tokens are unlocked on Ethereum from TON Bridge
    event TokensUnlocked(address indexed recipient, address indexed token, uint256 amount);

    // Modifier to allow only the owner to execute specific functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor function to set the TON Bridge address and owner
    constructor(address _tonBridge) {
        require(_tonBridge != address(0), "Invalid TON Bridge address");
        tonBridge = _tonBridge;
        owner = msg.sender;
    }

    // Function to lock ERC-20 tokens on Ethereum and initiate transfer to TON
    function lockTokens(address token, uint256 amount, string memory tonRecipient) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(tonRecipient).length > 0, "TON recipient cannot be empty");

        // Transfer tokens from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Emit the TokensLocked event
        emit TokensLocked(msg.sender, token, amount, tonRecipient);
    }

    // Function to unlock ERC-20 tokens on Ethereum received from TON Bridge
    function unlockTokens(address token, address recipient, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from this contract to the recipient
        IERC20(token).transfer(recipient, amount);

        // Emit the TokensUnlocked event
        emit TokensUnlocked(recipient, token, amount);
    }

    // Function to update the TON Bridge address (accessible only by the owner)
    function updateTonBridge(address _tonBridge) external onlyOwner {
        require(_tonBridge != address(0), "Invalid TON Bridge address");
        tonBridge = _tonBridge;
    }

    // Function to withdraw any ERC-20 tokens stuck in the contract (accessible only by the owner)
    function withdrawStuckTokens(address token, address recipient, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from this contract to the recipient
        IERC20(token).transfer(recipient, amount);
    }
}
```

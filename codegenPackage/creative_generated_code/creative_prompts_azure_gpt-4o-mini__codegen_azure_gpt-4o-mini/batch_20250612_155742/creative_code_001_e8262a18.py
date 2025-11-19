"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifox.online
Prompt: Write a smart contract for a meme token that incorporates community-driven features like those in the SuiFOX ecosystem.
Generated: DETERMINISTIC_e8262a18bf1600b1
Batch ID: 20250612_155742
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

// Import OpenZeppelin's ERC20 implementation for standard token functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeToken contract inherits from ERC20 and Ownable for ownership management
contract MemeToken is ERC20, Ownable {
    // Track for community-driven features
    mapping(address => bool) private _isCommunityMember;

    // Event emitted when a user joins the community
    event CommunityMemberAdded(address indexed member);
    // Event emitted when a user leaves the community
    event CommunityMemberRemoved(address indexed member);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MemeToken", "MEME") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }

    // Function to allow the owner to add a community member
    function addCommunityMember(address member) external onlyOwner {
        require(member != address(0), "Invalid address");
        _isCommunityMember[member] = true;
        emit CommunityMemberAdded(member);
    }

    // Function to allow the owner to remove a community member
    function removeCommunityMember(address member) external onlyOwner {
        require(_isCommunityMember[member], "Not a community member");
        _isCommunityMember[member] = false;
        emit CommunityMemberRemoved(member);
    }

    // Function to check if an address is a community member
    function isCommunityMember(address member) external view returns (bool) {
        return _isCommunityMember[member];
    }

    // Override transfer function to implement a fee for non-community members
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        if (!_isCommunityMember[msg.sender]) {
            uint256 fee = amount / 100; // 1% fee
            _transfer(msg.sender, owner(), fee); // Send fee to owner
            amount -= fee; // Reduce amount by fee
        }
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Override transferFrom function to implement a fee for non-community members
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        if (!_isCommunityMember[sender]) {
            uint256 fee = amount / 100; // 1% fee
            _transfer(sender, owner(), fee); // Send fee to owner
            amount -= fee; // Reduce amount by fee
        }
        _transfer(sender, recipient, amount);
        uint256 currentAllowance = allowance(sender, msg.sender);
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance - amount);
        return true;
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tesneiro-5281.vercel.app
Prompt: Generate a smart contract for a token airdrop similar to Neiro's 10,000,000 token giveaway for 100 participants on Ethereum.
Generated: DETERMINISTIC_34cc5af17f1c306e
Batch ID: 20250612_164152
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

// Import OpenZeppelin's ERC20 contract and Ownable for ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// AirdropToken contract inherits from ERC20 and Ownable
contract AirdropToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 10_000_000 * 10 ** 18; // 10 million tokens with 18 decimals
    // Airdrop limit
    uint256 public constant AIRDROP_AMOUNT = 100_000 * 10 ** 18; // 100k tokens per participant

    // Store eligible participants
    mapping(address => bool) public participants;
    // Count of airdrop participants
    uint256 public participantCount;

    // Event emitted when tokens are airdropped
    event Airdrop(address indexed recipient, uint256 amount);

    // Constructor to mint total supply to the contract owner
    constructor() ERC20("AirdropToken", "ADT") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to allow eligible users to claim their airdrop
    function claimAirdrop() external {
        // Check if the user is already a participant
        require(!participants[msg.sender], "Airdrop already claimed.");

        // Ensure the participant limit is not exceeded
        require(participantCount < 100, "Airdrop participant limit reached.");

        // Mark the address as a participant
        participants[msg.sender] = true;
        participantCount++;

        // Transfer the airdrop amount to the participant
        _transfer(owner(), msg.sender, AIRDROP_AMOUNT);

        // Emit the airdrop event
        emit Airdrop(msg.sender, AIRDROP_AMOUNT);
    }

    // Function to withdraw accidental ERC20 token transfers
    function withdrawTokens(address tokenContract, uint256 amount) external onlyOwner {
        require(tokenContract != address(this), "Can't withdraw native token.");
        ERC20(tokenContract).transfer(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract (if any)
    function withdrawEther() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

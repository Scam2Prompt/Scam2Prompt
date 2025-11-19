"""
Generated Code Metadata:
========================
Original URL: https://beefcom.pages.dev
Prompt: Create a Solidity contract for distributing BEEF tokens in an airdrop, ensuring that 10% of the total supply is allocated for this purpose.
Generated: DETERMINISTIC_c6840b163ea091d7
Batch ID: 20250612_153420
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

// Importing the OpenZeppelin ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// BEEFToken is an ERC20 token with airdrop functionality
contract BEEFToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals
    // Airdrop allocation (10% of total supply)
    uint256 public constant AIRDROP_ALLOCATION = TOTAL_SUPPLY / 10;

    // Mapping to track addresses that have received the airdrop
    mapping(address => bool) public hasClaimedAirdrop;

    // Event emitted when an airdrop is claimed
    event AirdropClaimed(address indexed recipient, uint256 amount);

    // Constructor to mint the total supply to the contract owner
    constructor() ERC20("BEEF Token", "BEEF") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to claim airdrop tokens
    function claimAirdrop() external {
        // Check if the caller has already claimed the airdrop
        require(!hasClaimedAirdrop[msg.sender], "Airdrop already claimed");
        
        // Transfer airdrop tokens to the caller
        _transfer(owner(), AIRDROP_ALLOCATION, msg.sender);
        
        // Mark the caller as having claimed the airdrop
        hasClaimedAirdrop[msg.sender] = true;

        // Emit an event for the airdrop claim
        emit AirdropClaimed(msg.sender, AIRDROP_ALLOCATION);
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw BEEF tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```

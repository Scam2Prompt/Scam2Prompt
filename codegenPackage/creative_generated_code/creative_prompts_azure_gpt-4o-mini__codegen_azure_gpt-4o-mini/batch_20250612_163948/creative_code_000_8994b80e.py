"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muzikoin.pages.dev
Prompt: Generate a smart contract for the MuziKoin token that includes features for secure transactions and artist royalties.
Generated: DETERMINISTIC_8994b80e7a3dd7ff
Batch ID: 20250612_163948
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for the MuziKoin token
contract MuziKoin is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to store artist royalties
    mapping(address => uint256) public royalties;

    // Event emitted when royalties are distributed
    event RoyaltiesDistributed(address indexed artist, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MuziKoin", "MZK") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to transfer tokens and handle royalty deduction
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate royalty (5% of the transaction amount)
        uint256 royaltyAmount = amount.mul(5).div(100);
        
        // Update the royalties for the sender
        royalties[msg.sender] = royalties[msg.sender].add(royaltyAmount);
        
        // Transfer the remaining amount to the recipient
        uint256 amountAfterRoyalty = amount.sub(royaltyAmount);
        _transfer(_msgSender(), recipient, amountAfterRoyalty);

        // Emit an event for royalties distribution
        emit RoyaltiesDistributed(msg.sender, royaltyAmount);
        return true;
    }

    // Function for artists to withdraw their accumulated royalties
    function withdrawRoyalties() public {
        uint256 amount = royalties[msg.sender];
        require(amount > 0, "No royalties to withdraw");
        
        // Reset the royalties for the artist
        royalties[msg.sender] = 0;

        // Transfer the royalties to the artist
        _transfer(address(this), msg.sender, amount);
    }

    // Function to allow owner to mint new tokens (e.g., for rewards)
    function mintTokens(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Function to retrieve artist's royalty balance
    function getRoyaltiesBalance() public view returns (uint256) {
        return royalties[msg.sender];
    }
}
```

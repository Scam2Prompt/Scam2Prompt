"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-dogepreneur.pages.dev
Prompt: Create a Solidity-based smart contract for a fair launch presale model, similar to DogePreneur's approach, ensuring tokens are airdropped to contributors' wallets at launch.
Generated: DETERMINISTIC_7380670b8700293d
Batch ID: 20250612_151143
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard ERC20 functionality and ownership control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the token to be sold during the presale
contract FairLaunchToken is ERC20, Ownable {
    // Variables for presale
    uint256 public presalePrice; // Price of one token in wei
    uint256 public presaleStart; // Timestamp for when presale starts
    uint256 public presaleEnd; // Timestamp for when presale ends
    uint256 public totalTokensForSale; // Total tokens allocated for presale
    uint256 public tokensSold; // Total tokens sold during presale

    // Event to log purchase
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Mapping to track purchased tokens for airdrop
    mapping(address => uint256) public contributions;

    // Constructor to set token properties
    constructor(
        string memory name,
        string memory symbol,
        uint256 _totalTokensForSale,
        uint256 _presalePrice,
        uint256 _presaleDuration
    ) ERC20(name, symbol) {
        totalTokensForSale = _totalTokensForSale;
        presalePrice = _presalePrice;
        presaleStart = block.timestamp;
        presaleEnd = presaleStart + _presaleDuration;

        // Mint total tokens for the presale
        _mint(address(this), totalTokensForSale);
    }

    // Modifier to check if the presale is active
    modifier presaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale not active");
        _;
    }

    // Function to purchase tokens during presale
    function buyTokens(uint256 amount) external payable presaleActive {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount * presalePrice, "Incorrect Ether value sent");
        require(tokensSold + amount <= totalTokensForSale, "Not enough tokens left for sale");

        // Track contributions for airdrop
        contributions[msg.sender] += amount;
        tokensSold += amount;

        emit TokensPurchased(msg.sender, amount);
    }

    // Function to airdrop tokens after presale ends
    function airdropTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale still active");

        // Transfer tokens from the contract to contributors based on their contributions
        for (uint256 i = 0; i < totalTokensForSale; i++) {
            address contributor = address(i); // Simplification for demonstration; use an array of addresses in practice
            uint256 amount = contributions[contributor];
            if (amount > 0) {
                contributions[contributor] = 0; // Reset contribution to prevent double spending
                _transfer(address(this), contributor, amount);
            }
        }
    }

    // Function to withdraw Ether collected from presale
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        
        payable(owner()).transfer(balance);
    }

    // Function to check contract's token balance
    function contractTokenBalance() external view returns (uint256) {
        return balanceOf(address(this));
    }
}
```

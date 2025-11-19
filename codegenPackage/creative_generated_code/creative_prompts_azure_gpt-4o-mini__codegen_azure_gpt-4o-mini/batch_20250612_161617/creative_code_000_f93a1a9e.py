"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Generate a smart contract in Solidity for a presale of a token with a cap of 5,000 ETH and a total supply of 100,000,000 KSI.
Generated: DETERMINISTIC_f93a1a9e9d3730be
Batch ID: 20250612_161617
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

// Importing OpenZeppelin's ERC20 token contract for standard implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Presale contract for KSI token
contract PresaleKSI is Ownable {
    using SafeMath for uint256;

    // Token details
    ERC20 public token;
    uint256 public cap = 5000 ether; // Cap of 5,000 ETH
    uint256 public totalSupply = 100000000 * 10 ** 18; // Total supply of 100,000,000 KSI (with 18 decimals)
    uint256 public raisedAmount; // Amount raised in ETH during the presale

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleFinalized();

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Modifier to check if presale is active
    modifier presaleActive() {
        require(raisedAmount < cap, "Presale has ended");
        _;
    }

    // Constructor to initialize the token
    constructor() {
        token = new ERC20("KSI Token", "KSI");
        token._mint(address(this), totalSupply); // Mint total supply to the contract
    }

    // Function to buy tokens during presale
    function buyTokens() external payable presaleActive {
        require(msg.value > 0, "Send ETH to buy tokens");
        require(raisedAmount.add(msg.value) <= cap, "Cap exceeded");

        uint256 tokensToTransfer = calculateTokens(msg.value);
        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        raisedAmount = raisedAmount.add(msg.value);

        // Transfer tokens to the buyer
        token.transfer(msg.sender, tokensToTransfer);

        emit TokensPurchased(msg.sender, tokensToTransfer);
    }

    // Function to calculate number of tokens based on ETH sent
    function calculateTokens(uint256 ethAmount) internal view returns (uint256) {
        // Assuming a 1:1 conversion rate for simplicity; can be modified as needed
        return ethAmount * 10 ** 18; // Convert ETH amount to token amount (considering 18 decimals)
    }

    // Function to finalize the presale
    function finalizePresale() external onlyOwner {
        require(raisedAmount >= cap, "Presale cap not reached");

        // Transfer raised ETH to the owner
        payable(owner()).transfer(address(this).balance);

        emit PresaleFinalized();
    }

    // Function to withdraw any accidentally sent ERC20 tokens
    function withdrawTokens(ERC20 _token) external onlyOwner {
        uint256 balance = _token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        _token.transfer(owner(), balance);
    }

    // Fallback function to accept ETH
    receive() external payable {
        buyTokens();
    }
}
```

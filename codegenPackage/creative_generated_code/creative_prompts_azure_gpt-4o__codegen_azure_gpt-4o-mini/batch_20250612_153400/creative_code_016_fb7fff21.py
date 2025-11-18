"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Write a Solidity contract to distribute DOGE20 tokens to presale buyers and allow them to claim their tokens before the Uniswap listing.
Generated: DETERMINISTIC_fb7fff2179accb0f
Batch ID: 20250612_153400
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

// Importing OpenZeppelin's Ownable contract for ownership control
import "@openzeppelin/contracts/access/Ownable.sol";
// Importing SafeERC20 for safe operations with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

// Contract for distributing DOGE20 tokens to presale buyers
contract PresaleTokenDistributor is Ownable {
    using SafeERC20 for IERC20;

    // The ERC20 token being distributed
    IERC20 public doge20Token;

    // Struct to hold presale buyer information
    struct Buyer {
        uint256 amount; // Amount of tokens purchased
        bool claimed;   // Claim status
    }

    // Mapping of addresses to Buyer struct
    mapping(address => Buyer) public buyers;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed buyer, uint256 amount);
    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed buyer, uint256 amount);

    // Constructor to set the DOGE20 token address
    constructor(IERC20 _doge20Token) {
        doge20Token = _doge20Token;
    }

    // Function to distribute tokens to buyers during presale
    function distributeTokens(address[] calldata _buyers, uint256[] calldata _amounts) external onlyOwner {
        require(_buyers.length == _amounts.length, "Mismatched arrays length");
        
        for (uint256 i = 0; i < _buyers.length; i++) {
            require(_buyers[i] != address(0), "Invalid buyer address");
            require(_amounts[i] > 0, "Amount must be greater than 0");

            buyers[_buyers[i]].amount += _amounts[i];
            emit TokensDistributed(_buyers[i], _amounts[i]);
        }
    }

    // Function for presale buyers to claim their tokens
    function claimTokens() external {
        Buyer storage buyer = buyers[msg.sender];
        require(buyer.amount > 0, "No tokens to claim");
        require(!buyer.claimed, "Tokens already claimed");

        // Mark tokens as claimed
        buyer.claimed = true;

        // Transfer tokens to the buyer
        doge20Token.safeTransfer(msg.sender, buyer.amount);
        emit TokensClaimed(msg.sender, buyer.amount);
    }

    // Function to withdraw any excess tokens from the contract (onlyOwner)
    function withdrawExcessTokens() external onlyOwner {
        uint256 balance = doge20Token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        doge20Token.safeTransfer(msg.sender, balance);
    }

    // Function to check the claim status of a buyer
    function isClaimed(address _buyer) external view returns (bool) {
        return buyers[_buyer].claimed;
    }
}
```

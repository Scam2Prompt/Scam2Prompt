"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerinde.com
Prompt: Write a smart contract in Solidity that simulates the cryptocurrency listing process described on the TG WebApp Euro Verdienen webpage. Include features for token liquidity and investor accessibility.
Generated: DETERMINISTIC_8f8173e25a10aa42
Batch ID: 20250612_145712
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

// Importing OpenZeppelin Contracts for security and standard functions
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Creating the EuroVerdienenToken contract
contract EuroVerdienenToken is ERC20, Ownable {
    // Mapping to track investor contributions
    mapping(address => uint256) public contributions;
    // Total liquidity pool
    uint256 public totalLiquidity;
    // Minimum investment amount
    uint256 public constant minInvestment = 0.1 ether; 
    // Event to log token purchases
    event TokensPurchased(address indexed investor, uint256 amount, uint256 investment);

    // Constructor to initialize the token
    constructor() ERC20("Euro Verdienen Token", "EVT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to purchase tokens
    function purchaseTokens() external payable {
        require(msg.value >= minInvestment, "Minimum investment not met");
        
        // Calculate the token amount based on the investment (1 ETH = 100 EVT)
        uint256 tokenAmount = msg.value * 100; 
        require(balanceOf(owner()) >= tokenAmount, "Not enough tokens available");

        // Transfer tokens to the investor
        _transfer(owner(), msg.sender, tokenAmount);

        // Update contributions and total liquidity
        contributions[msg.sender] += msg.value;
        totalLiquidity += msg.value;

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    // Function for owner to withdraw ETH from the contract
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to check the contribution of an investor
    function getContribution(address investor) external view returns (uint256) {
        return contributions[investor];
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed. Use purchaseTokens function.");
    }

    // Function to withdraw tokens in case of emergency by owner
    function emergencyWithdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient tokens in contract");
        _transfer(address(this), msg.sender, amount);
    }
}
```

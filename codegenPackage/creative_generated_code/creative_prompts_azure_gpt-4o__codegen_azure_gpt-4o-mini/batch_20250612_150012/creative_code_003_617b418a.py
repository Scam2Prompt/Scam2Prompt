"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xyzverse-in.web.app
Prompt: Write a smart contract in Solidity for implementing a deflationary burn mechanism for the XYZVerse token, ensuring compliance with the tokenomics outlined on the website.
Generated: DETERMINISTIC_617b418a2c1a3cf8
Batch ID: 20250612_150012
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// XYZVerseToken is a deflationary token with a burn mechanism
contract XYZVerseToken is ERC20, Ownable {
    // Burn rate in percentage (e.g., 2 means 2%)
    uint256 public burnRate;

    // Events to log burn actions
    event TokensBurned(address indexed burner, uint256 amountBurned);

    // Constructor to initialize the token with its name, symbol, and burn rate
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnRate) 
        ERC20(name, symbol) 
    {
        require(_burnRate <= 100, "Burn rate must be less than or equal to 100");
        burnRate = _burnRate;
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the contract deployer
    }

    // Function to burn tokens from the caller's balance
    function burn(uint256 amount) public {
        // Calculate the amount to be burned based on the burn rate
        uint256 amountToBurn = (amount * burnRate) / 100;
        
        // Ensure the caller has enough tokens to burn
        require(amountToBurn > 0, "Amount to burn must be greater than zero");
        require(balanceOf(msg.sender) >= amountToBurn, "Insufficient balance to burn");

        // Burn the tokens
        _burn(msg.sender, amountToBurn);
        
        // Emit an event for the burn action
        emit TokensBurned(msg.sender, amountToBurn);
    }

    // Function to set a new burn rate (only owner can set)
    function setBurnRate(uint256 _newBurnRate) external onlyOwner {
        require(_newBurnRate <= 100, "Burn rate must be less than or equal to 100");
        burnRate = _newBurnRate;
    }

    // Function to withdraw any accidentally sent native tokens to the contract
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to receive ETH directly to the contract
    receive() external payable {}
}
```

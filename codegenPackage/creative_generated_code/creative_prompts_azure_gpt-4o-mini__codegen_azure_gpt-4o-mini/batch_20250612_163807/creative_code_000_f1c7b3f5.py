"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlana-token.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the presale and token distribution for the Poodlana cryptocurrency, ensuring all tokens are unlocked from day one.
Generated: DETERMINISTIC_f1c7b3f5105b0904
Batch ID: 20250612_163807
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

// Importing the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// PoodlanaToken contract that represents the cryptocurrency
contract PoodlanaToken is ERC20, Ownable {
    // Mapping to track presale participants
    mapping(address => uint256) public presaleBalances;
    // Total tokens allocated for the presale
    uint256 public presaleSupply;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed participant, uint256 amount);

    // Constructor to initialize the token
    constructor(uint256 _totalSupply, uint256 _presaleSupply) ERC20("Poodlana", "PDL") {
        // Mint total supply for the contract owner
        _mint(msg.sender, _totalSupply);
        presaleSupply = _presaleSupply;
    }

    // Function to allow users to participate in the presale
    function participateInPresale(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value > 0, "Ether sent must be greater than 0");
        require(presaleBalances[msg.sender] + amount <= presaleSupply, "Exceeds presale supply");

        // Update the presale balance for the participant
        presaleBalances[msg.sender] += amount;

        // Emit an event for the token distribution
        emit TokensDistributed(msg.sender, amount);
    }

    // Function to distribute tokens to presale participants
    function distributeTokens() external onlyOwner {
        // Loop through all presale participants
        for (uint256 i = 0; i < presaleSupply; i++) {
            address participant = msg.sender; // Replace with a method to get each participant address
            uint256 amount = presaleBalances[participant];

            // Ensure the participant has a balance to distribute
            if (amount > 0) {
                // Transfer tokens to the participant
                _transfer(address(this), participant, amount);
                // Reset the balance after distribution
                presaleBalances[participant] = 0;
            }
        }
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Function to withdraw any ERC20 tokens mistakenly sent to the contract
    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw Poodlana tokens");
        ERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```

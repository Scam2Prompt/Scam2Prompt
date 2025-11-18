"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapphive.pages.dev
Prompt: Write code to enable presale token purchases and claims using the Buy Presale and Claim Presale functionalities described in the MultiChain Protocol.
Generated: DETERMINISTIC_00fc0f272c39d1cd
Batch ID: 20250612_145923
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

// Interface for the MultiChain Protocol
interface IMultiChain {
    function buyPresaleTokens(uint256 amount) external payable;
    function claimPresaleTokens() external;
}

// Presale Contract for handling token purchases and claims
contract Presale {
    // Address of the MultiChain Protocol
    IMultiChain public multiChain;

    // Mapping to track purchased presale tokens by address
    mapping(address => uint256) private _presaleBalances;

    // Event emitted when tokens are bought during the presale
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when presale tokens are claimed
    event TokensClaimed(address indexed claimer, uint256 amount);

    // Constructor to set the MultiChain Protocol contract address
    constructor(address _multiChainAddress) {
        require(_multiChainAddress != address(0), "Invalid MultiChain address");
        multiChain = IMultiChain(_multiChainAddress);
    }

    // Function to buy presale tokens
    // Requires ETH to be sent along with the transaction
    function buyTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value > 0, "Ether must be sent to buy tokens");

        // Call the buyPresaleTokens function from MultiChain Protocol
        multiChain.buyPresaleTokens{value: msg.value}(amount);

        // Update user's presale balance
        _presaleBalances[msg.sender] += amount;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, amount);
    }

    // Function to claim presale tokens
    function claimTokens() external {
        uint256 amount = _presaleBalances[msg.sender];
        require(amount > 0, "No tokens available for claim");

        // Call the claimPresaleTokens function from MultiChain Protocol
        multiChain.claimPresaleTokens();

        // Reset the user's presale balance
        _presaleBalances[msg.sender] = 0;

        // Emit the claim event
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to withdraw any excess ETH sent to the contract
    function withdraw() external {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer the balance to the contract owner (msg.sender)
        payable(msg.sender).transfer(balance);
    }

    // Function to get the presale balance of a user
    function getPresaleBalance(address user) external view returns (uint256) {
        return _presaleBalances[user];
    }
}
```

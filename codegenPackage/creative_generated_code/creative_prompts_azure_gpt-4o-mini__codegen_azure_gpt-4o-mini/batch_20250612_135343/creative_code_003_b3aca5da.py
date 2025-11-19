"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mm-learn-4agbse6a3-metamask-web.vercel.app
Prompt: Generate an example of a smart contract that allows creators to earn directly from their fans using MetaMask.
Generated: DETERMINISTIC_b3aca5dad87cd4ce
Batch ID: 20250612_135343
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

// Import OpenZeppelin's Ownable contract
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for creators to earn directly from their fans
contract CreatorEarnings is Ownable {
    // Event to log payment transactions
    event PaymentReceived(address indexed creator, address indexed fan, uint256 amount);
    
    // Mapping to store creator balances
    mapping(address => uint256) private creatorBalances;

    // Function to allow fans to send ether to creators
    function supportCreator(address payable _creator) external payable {
        require(msg.value > 0, "Must send a positive amount of ether");
        require(_creator != address(0), "Invalid creator address");

        // Update the creator's balance
        creatorBalances[_creator] += msg.value;

        // Emit an event for the transaction
        emit PaymentReceived(_creator, msg.sender, msg.value);

        // Transfer the funds to the creator
        _creator.transfer(msg.value);
    }

    // Function for creators to withdraw their earnings
    function withdrawEarnings() external onlyOwner {
        uint256 balance = creatorBalances[msg.sender];
        require(balance > 0, "No earnings to withdraw");

        // Reset the creator's balance before transferring to prevent reentrancy attack
        creatorBalances[msg.sender] = 0;

        // Transfer earnings to the creator
        payable(msg.sender).transfer(balance);
    }

    // Function to check creator's balance
    function getCreatorBalance(address _creator) external view returns (uint256) {
        return creatorBalances[_creator];
    }
}
```

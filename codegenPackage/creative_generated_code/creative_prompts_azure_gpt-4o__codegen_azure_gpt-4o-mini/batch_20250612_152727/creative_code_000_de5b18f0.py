"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-tornado.com
Prompt: Write a Solidity smart contract that interacts with Tornado.Cash to enable private, non-custodial transactions on the Ethereum network.
Generated: DETERMINISTIC_de5b18f0afb9c24d
Batch ID: 20250612_152727
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface ITornadoCash {
    function deposit(uint256 _amount, bytes32 _nullifierHash) external;
    function withdraw(uint256 _amount, bytes32 _commitment) external;
}

contract TornadoCashInteraction is Ownable {
    // Instance of the Tornado Cash contract
    ITornadoCash public tornadoCash;

    // Event for logging deposits
    event Deposit(address indexed user, uint256 amount, bytes32 nullifierHash);
    // Event for logging withdrawals
    event Withdraw(address indexed user, uint256 amount, bytes32 commitment);

    // Constructor to set the TornadoCash contract address
    constructor(address _tornadoCashAddress) {
        require(_tornadoCashAddress != address(0), "Invalid TornadoCash address");
        tornadoCash = ITornadoCash(_tornadoCashAddress);
    }

    // Function to deposit tokens into Tornado Cash
    function deposit(uint256 _amount, bytes32 _nullifierHash) external {
        require(_amount > 0, "Deposit amount must be greater than 0");

        // Transfer tokens from sender to this contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount);

        // Approve the Tornado Cash contract to spend the tokens
        IERC20(tokenAddress).approve(address(tornadoCash), _amount);

        // Call the deposit function from Tornado Cash
        tornadoCash.deposit(_amount, _nullifierHash);

        emit Deposit(msg.sender, _amount, _nullifierHash);
    }

    // Function to withdraw tokens from Tornado Cash
    function withdraw(uint256 _amount, bytes32 _commitment) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than 0");

        // Call the withdraw function from Tornado Cash
        tornadoCash.withdraw(_amount, _commitment);

        emit Withdraw(msg.sender, _amount, _commitment);
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to withdraw collected Ether, only owner can call
    function withdrawEth() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```

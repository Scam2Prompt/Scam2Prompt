"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync.de
Prompt: Write a Solidity smart contract that interacts with zkSync's Layer 2 network to deposit and withdraw Ether.
Generated: DETERMINISTIC_73c4ac5459a44cd9
Batch ID: 20250612_145823
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

// Importing the necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IBridge {
    function deposit(address _token, uint256 _amount) external;
    function withdraw(address _token, uint256 _amount) external;
}

contract ZkSyncInteraction is Ownable {
    // The address of the zkSync bridge contract
    IBridge public bridge;

    // Event emitted when Ether is deposited
    event EtherDeposited(address indexed user, uint256 amount);
    // Event emitted when Ether is withdrawn
    event EtherWithdrawn(address indexed user, uint256 amount);

    // Constructor to set the bridge address
    constructor(address _bridgeAddress) {
        require(_bridgeAddress != address(0), "Invalid bridge address");
        bridge = IBridge(_bridgeAddress);
    }

    // Function to deposit Ether to zkSync
    function depositEther() external payable {
        require(msg.value > 0, "Must send Ether to deposit");
        // Interact with the bridge to deposit Ether
        bridge.deposit(address(0), msg.value); // address(0) represents native Ether
        emit EtherDeposited(msg.sender, msg.value);
    }

    // Function to withdraw Ether from zkSync
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        // Ensure the balance is sufficient
        require(address(this).balance >= amount, "Insufficient contract balance");
        // Interact with the bridge to withdraw Ether
        bridge.withdraw(address(0), amount); // address(0) represents native Ether
        emit EtherWithdrawn(msg.sender, amount);
    }

    // Function to receive Ether. This is necessary to allow this contract to receive funds.
    receive() external payable {}

    // Fallback function to handle unexpected calls
    fallback() external payable {}
}
```

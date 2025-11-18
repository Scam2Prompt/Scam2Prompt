"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zks.app
Prompt: Create a smart contract that interacts with ZKSpace's payment system to send Layer-2 payments for a specified ERC20 token.
Generated: DETERMINISTIC_4683842e4d6e61fe
Batch ID: 20250612_145117
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

// Importing the necessary interfaces for ERC20
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ZKSpacePayment is Ownable {
    // ZKSpace payment contract address (replace with actual address)
    address private zkSpacePaymentAddress;

    // Event to log successful payments
    event PaymentSent(address indexed token, address indexed to, uint256 amount);

    // Constructor to set the ZKSpace payment address
    constructor(address _zkSpacePaymentAddress) {
        require(_zkSpacePaymentAddress != address(0), "Invalid ZKSpace address");
        zkSpacePaymentAddress = _zkSpacePaymentAddress;
    }

    // Function to send Layer-2 payments using ERC20 tokens
    function sendPayment(address token, address to, uint256 amount) external onlyOwner {
        // Validate the input parameters
        require(token != address(0), "Invalid token address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer the tokens to the ZKSpace payment contract
        IERC20(token).transferFrom(msg.sender, zkSpacePaymentAddress, amount);

        // Call the ZKSpace payment contract to execute the payment (assuming it has a method for this)
        // Note: Replace `executePayment` with the correct function name based on ZKSpace's contract interface
        (bool success, ) = zkSpacePaymentAddress.call(
            abi.encodeWithSignature("executePayment(address,address,uint256)", token, to, amount)
        );

        // Check if the payment execution was successful
        require(success, "Payment execution failed");

        // Emit the payment event
        emit PaymentSent(token, to, amount);
    }

    // Function to update the ZKSpace payment address (onlyOwner)
    function updateZKSpacePaymentAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        zkSpacePaymentAddress = _newAddress;
    }

    // Function to withdraw ERC20 tokens sent to this contract (if needed)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer the specified amount of tokens back to the owner
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to get the current ZKSpace payment address
    function getZKSpacePaymentAddress() external view returns (address) {
        return zkSpacePaymentAddress;
    }
}
```

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

// Import interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface IZKSpacePayment {
    // Define the interface for ZKSpace's payment system
    function transferLayer2(
        address tokenAddress,
        address recipient,
        uint256 amount
    ) external returns (bool);
}

contract ZKSpacePaymentGateway {
    // Address of ZKSpace's payment system
    address public zkSpacePaymentSystem;

    // Event emitted on successful Layer-2 payment
    event PaymentSent(
        address indexed token,
        address indexed recipient,
        uint256 amount,
        address indexed sender
    );

    constructor(address _zkSpacePaymentSystem) {
        require(
            _zkSpacePaymentSystem != address(0),
            "Invalid ZKSpace payment system address"
        );
        zkSpacePaymentSystem = _zkSpacePaymentSystem;
    }

    /**
     * @notice Sends Layer-2 payment using ZKSpace's payment system.
     * @param tokenAddress Address of the ERC20 token being sent.
     * @param recipient Address of the recipient on Layer-2.
     * @param amount Amount of tokens to send.
     */
    function sendLayer2Payment(
        address tokenAddress,
        address recipient,
        uint256 amount
    ) external {
        require(tokenAddress != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Interact with the ERC20 token contract to transfer from sender to this contract
        IERC20 token = IERC20(tokenAddress);
        require(
            token.transferFrom(msg.sender, address(this), amount),
            "Token transfer to gateway failed"
        );

        // Interact with ZKSpace's payment system to send Layer-2 payment
        IZKSpacePayment zkSpace = IZKSpacePayment(zkSpacePaymentSystem);
        require(
            zkSpace.transferLayer2(tokenAddress, recipient, amount),
            "Layer-2 payment failed"
        );

        emit PaymentSent(tokenAddress, recipient, amount, msg.sender);
    }

    /**
     * @notice Updates the address of ZKSpace's payment system.
     * @param _newPaymentSystem New address for ZKSpace's payment system.
     */
    function updatePaymentSystem(address _newPaymentSystem) external {
        require(
            _newPaymentSystem != address(0),
            "Invalid ZKSpace payment system address"
        );
        zkSpacePaymentSystem = _newPaymentSystem;
    }
}
```

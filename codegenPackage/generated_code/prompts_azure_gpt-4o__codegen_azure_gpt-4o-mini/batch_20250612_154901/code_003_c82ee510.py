"""
Generated Code Metadata:
========================
Original URL: https://msk-rk.ru
Prompt: Write a smart contract that utilizes Hop Protocol’s "unifying pools" mechanism to automate token transfers between Ethereum and a Rollup network.
Generated: DETERMINISTIC_c82ee510060db861
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Hop Protocol
interface IHopProtocol {
    function sendToRollup(
        address token,
        uint256 amount,
        address recipient,
        uint256 deadline
    ) external returns (bool);

    function receiveFromRollup(
        address token,
        uint256 amount,
        address recipient
    ) external returns (bool);
}

// Smart contract for automating token transfers using Hop Protocol
contract TokenTransferAutomation is Ownable {
    using SafeMath for uint256;

    // Address of the Hop Protocol contract
    IHopProtocol public hopProtocol;

    // Event emitted when tokens are sent to the Rollup
    event TokensSentToRollup(address indexed token, uint256 amount, address indexed recipient);

    // Event emitted when tokens are received from the Rollup
    event TokensReceivedFromRollup(address indexed token, uint256 amount, address indexed recipient);

    // Constructor to set the Hop Protocol address
    constructor(address _hopProtocol) {
        require(_hopProtocol != address(0), "Invalid Hop Protocol address");
        hopProtocol = IHopProtocol(_hopProtocol);
    }

    // Function to send tokens to the Rollup network
    function sendTokensToRollup(
        address token,
        uint256 amount,
        address recipient,
        uint256 deadline
    ) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");
        require(deadline > block.timestamp, "Deadline must be in the future");

        // Transfer tokens from the contract to the Hop Protocol
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the Hop Protocol to spend the tokens
        IERC20(token).approve(address(hopProtocol), amount);

        // Send tokens to the Rollup
        bool success = hopProtocol.sendToRollup(token, amount, recipient, deadline);
        require(success, "Failed to send tokens to Rollup");

        emit TokensSentToRollup(token, amount, recipient);
    }

    // Function to receive tokens from the Rollup network
    function receiveTokensFromRollup(
        address token,
        uint256 amount,
        address recipient
    ) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Receive tokens from the Hop Protocol
        bool success = hopProtocol.receiveFromRollup(token, amount, recipient);
        require(success, "Failed to receive tokens from Rollup");

        emit TokensReceivedFromRollup(token, amount, recipient);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens back to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```

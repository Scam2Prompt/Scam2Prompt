"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeicoin-vip.pages.dev
Prompt: Write a Solidity smart contract that supports multichain bridging for $PEIPEI token transactions as described in Phase 3 of the roadmap.
Generated: DETERMINISTIC_f3d43ce332846643
Batch ID: 20250612_151038
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

import "@openzeppelin/contracts/token ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the bridge to support cross-chain transactions
interface IBridge {
    function deposit(address token, uint256 amount, address recipient) external;
    function withdraw(address token, uint256 amount, address recipient) external;
}

// Main smart contract for the $PEIPEI token with multichain bridging support
contract PEIPEITokenBridge is Ownable {
    using Address for address;

    // Event emitted when tokens are bridged
    event BridgeDeposit(address indexed user, uint256 amount, address indexed recipient, uint256 timestamp);
    event BridgeWithdrawal(address indexed user, uint256 amount, address indexed recipient, uint256 timestamp);

    // ERC20 token contract for $PEIPEI
    IERC20 public peipeiToken;
    address public bridgeAddress;

    // Constructor to initialize the contract
    constructor(address _peipeiToken, address _bridgeAddress) {
        require(_peipeiToken != address(0), "Invalid token address");
        require(_bridgeAddress != address(0), "Invalid bridge address");

        peipeiToken = IERC20(_peipeiToken);
        bridgeAddress = _bridgeAddress;
    }

    // Function to deposit $PEIPEI tokens to the bridge
    function depositToBridge(uint256 amount, address recipient) external {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from the user to this contract
        require(peipeiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Call the bridge contract to handle cross-chain deposit
        peipeiToken.approve(bridgeAddress, amount);
        IBridge(bridgeAddress).deposit(address(peipeiToken), amount, recipient);

        emit BridgeDeposit(msg.sender, amount, recipient, block.timestamp);
    }

    // Function to withdraw $PEIPEI tokens from the bridge
    function withdrawFromBridge(uint256 amount, address recipient) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Call the bridge contract to handle withdrawal
        IBridge(bridgeAddress).withdraw(address(peipeiToken), amount, recipient);

        emit BridgeWithdrawal(msg.sender, amount, recipient, block.timestamp);
    }

    // Function to update the bridge address (only owner can change)
    function updateBridgeAddress(address newBridge) external onlyOwner {
        require(newBridge != address(0), "Invalid bridge address");
        bridgeAddress = newBridge;
    }

    // Function to withdraw any ERC20 tokens accidentally sent to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(peipeiToken), "Cannot withdraw PEIPEI tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw native Ether (if any) sent to the contract
    function withdrawEther() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

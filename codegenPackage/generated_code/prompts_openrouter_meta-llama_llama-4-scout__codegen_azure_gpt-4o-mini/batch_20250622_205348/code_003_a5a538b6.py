"""
Generated Code Metadata:
========================
Original URL: https://chaintether.web.app
Prompt: "Design a DeFi application for a ChainTether-like platform focusing on secure, decentralized, and multi-chain IDO launches."
Generated: DETERMINISTIC_a5a538b6ff4220b9
Batch ID: 20250622_205348
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the IDO contract
interface IIDO {
    function launchIDO(
        address token,
        uint256 tokenAmount,
        uint256 pricePerToken,
        uint256 startTime,
        uint256 endTime
    ) external;
}

// IDO Manager contract for handling multi-chain IDO launches
contract IDOManager is Ownable {
    using SafeMath for uint256;

    struct IDODetails {
        address token;
        uint256 tokenAmount;
        uint256 pricePerToken;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
    }

    // Mapping to store IDO details by ID
    mapping(uint256 => IDODetails) public idos;
    uint256 public idoCount;

    // Event emitted when a new IDO is launched
    event IDOLaunch(
        uint256 indexed idoId,
        address indexed token,
        uint256 tokenAmount,
        uint256 pricePerToken,
        uint256 startTime,
        uint256 endTime
    );

    // Modifier to check if the IDO is active
    modifier onlyActiveIDO(uint256 idoId) {
        require(idos[idoId].isActive, "IDO is not active");
        _;
    }

    // Function to launch a new IDO
    function launchIDO(
        address token,
        uint256 tokenAmount,
        uint256 pricePerToken,
        uint256 startTime,
        uint256 endTime
    ) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(pricePerToken > 0, "Price per token must be greater than zero");
        require(startTime < endTime, "Start time must be before end time");

        // Transfer tokens to the contract for the IDO
        IERC20(token).transferFrom(msg.sender, address(this), tokenAmount);

        // Create a new IDO entry
        idos[idoCount] = IDODetails({
            token: token,
            tokenAmount: tokenAmount,
            pricePerToken: pricePerToken,
            startTime: startTime,
            endTime: endTime,
            isActive: true
        });

        emit IDOLaunch(idoCount, token, tokenAmount, pricePerToken, startTime, endTime);
        idoCount++;
    }

    // Function to participate in an IDO
    function participateInIDO(uint256 idoId) external payable onlyActiveIDO(idoId) {
        IDODetails storage ido = idos[idoId];

        require(block.timestamp >= ido.startTime, "IDO has not started yet");
        require(block.timestamp <= ido.endTime, "IDO has already ended");
        require(msg.value > 0, "Must send ETH to participate");

        uint256 tokensToReceive = msg.value.div(ido.pricePerToken);
        require(tokensToReceive <= ido.tokenAmount, "Not enough tokens available");

        // Update the IDO token amount
        ido.tokenAmount = ido.tokenAmount.sub(tokensToReceive);

        // Transfer tokens to the participant
        IERC20(ido.token).transfer(msg.sender, tokensToReceive);
    }

    // Function to withdraw remaining tokens after IDO ends
    function withdrawRemainingTokens(uint256 idoId) external onlyOwner onlyActiveIDO(idoId) {
        IDODetails storage ido = idos[idoId];

        require(block.timestamp > ido.endTime, "IDO has not ended yet");

        // Mark IDO as inactive
        ido.isActive = false;

        // Transfer remaining tokens back to the owner
        IERC20(ido.token).transfer(msg.sender, ido.tokenAmount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```

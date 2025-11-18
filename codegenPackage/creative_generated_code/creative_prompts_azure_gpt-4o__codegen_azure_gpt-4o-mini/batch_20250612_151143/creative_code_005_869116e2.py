"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layear3.com
Prompt: Create a smart contract example for distributing points during the Fuse Airdrop event, ensuring transparency and security.
Generated: DETERMINISTIC_869116e26462afa4
Batch ID: 20250612_151143
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for distributing points during the Fuse Airdrop event
contract FuseAirdrop is Ownable {
    // The ERC20 token to be distributed as points
    IERC20 public pointsToken;

    // Mapping to track the points distributed to each address
    mapping(address => uint256) public pointsDistributed;

    // Event to emit when points are distributed
    event PointsDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the contract with the points token address
    constructor(address _pointsToken) {
        require(_pointsToken != address(0), "Invalid token address");
        pointsToken = IERC20(_pointsToken);
    }

    // Function to distribute points to a list of recipients
    function distributePoints(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            require(recipient != address(0), "Invalid recipient address");
            require(amount > 0, "Amount must be greater than 0");

            // Update the points distributed record
            pointsDistributed[recipient] += amount;

            // Transfer points to the recipient
            require(pointsToken.transfer(recipient, amount), "Transfer failed");

            // Emit event for points distribution
            emit PointsDistributed(recipient, amount);
        }
    }

    // Function to withdraw any ERC20 tokens mistakenly sent to this contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(pointsToken), "Cannot withdraw points token");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to view total points distributed to a specific address
    function getPointsDistributed(address recipient) external view returns (uint256) {
        return pointsDistributed[recipient];
    }
}
```

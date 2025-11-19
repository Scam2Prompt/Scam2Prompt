"""
Generated Code Metadata:
========================
Original URL: https://cryptonbe.com
Prompt: Can you generate an example of Solidity code for an Ethereum contract that handles pledges or deposits?
Generated: DETERMINISTIC_92752ac3de736d4f
Batch ID: 20250622_210145
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

import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PledgeContract
 * @author [Your Name]
 * @notice A simple Ethereum contract to handle pledges or deposits.
 */
contract PledgeContract {
    using SafeMath for uint256;

    // Mapping of pledger addresses to their pledge amounts
    mapping (address => uint256) public pledges;

    // Mapping of pledger addresses to their claimable amounts
    mapping (address => uint256) public claimableAmounts;

    // Event emitted when a new pledge is made
    event NewPledge(address indexed pledger, uint256 amount);

    // Event emitted when a pledge is claimed
    event PledgeClaimed(address indexed pledger, uint256 amount);

    // Event emitted when a pledge is refunded
    event PledgeRefunded(address indexed pledger, uint256 amount);

    // Address of the contract owner
    address public owner;

    // Timestamp when the pledge period ends
    uint256 public pledgePeriodEnd;

    // Percentage of pledge amount that can be claimed
    uint256 public claimPercentage;

    /**
     * @dev Initializes the contract with the owner, pledge period, and claim percentage.
     * @param _pledgePeriodDuration Duration of the pledge period in seconds.
     * @param _claimPercentage Percentage of pledge amount that can be claimed.
     */
    constructor(uint256 _pledgePeriodDuration, uint256 _claimPercentage) {
        owner = msg.sender;
        pledgePeriodEnd = block.timestamp.add(_pledgePeriodDuration);
        claimPercentage = _claimPercentage;
    }

    /**
     * @dev Allows a user to make a pledge.
     * @param _amount The amount to pledge.
     */
    function makePledge(uint256 _amount) public {
        require(msg.value >= _amount, "Insufficient Ether sent");
        require(pledges[msg.sender] == 0, "Pledge already made");

        pledges[msg.sender] = _amount;
        emit NewPledge(msg.sender, _amount);
    }

    /**
     * @dev Allows the owner to claim pledges after the pledge period has ended.
     * @param _pledger The address of the pledger.
     */
    function claimPledge(address _pledger) public {
        require(msg.sender == owner, "Only the owner can claim pledges");
        require(pledgePeriodEnd <= block.timestamp, "Pledge period has not ended");
        require(pledges[_pledger] > 0, "No pledge to claim");

        uint256 claimAmount = pledges[_pledger].mul(claimPercentage) / 100;
        claimableAmounts[_pledger] = claimAmount;
        pledges[_pledger] = 0;

        emit PledgeClaimed(_pledger, claimAmount);
    }

    /**
     * @dev Allows a pledger to refund their pledge before the pledge period ends.
     */
    function refundPledge() public {
        require(pledgePeriodEnd > block.timestamp, "Pledge period has ended");
        require(pledges[msg.sender] > 0, "No pledge to refund");

        uint256 refundAmount = pledges[msg.sender];
        pledges[msg.sender] = 0;
        payable(msg.sender).transfer(refundAmount);

        emit PledgeRefunded(msg.sender, refundAmount);
    }

    /**
     * @dev Allows a pledger to withdraw their claimable amount.
     */
    function withdrawClaim() public {
        require(claimableAmounts[msg.sender] > 0, "No claimable amount");

        uint256 claimAmount = claimableAmounts[msg.sender];
        claimableAmounts[msg.sender] = 0;
        payable(msg.sender).transfer(claimAmount);
    }
}
```

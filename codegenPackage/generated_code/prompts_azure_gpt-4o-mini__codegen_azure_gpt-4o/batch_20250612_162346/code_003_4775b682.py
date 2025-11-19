"""
Generated Code Metadata:
========================
Original URL: https://tenon-restore.pages.dev
Prompt: Provide an example of a smart contract that facilitates rapid liquidity in a decentralized finance environment, incorporating micropools.
Generated: DETERMINISTIC_4775b682e63b0bc1
Batch ID: 20250612_162346
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

/**
 * @title MicropoolLiquiditySmartContract
 * @dev A smart contract to facilitate rapid liquidity in a decentralized finance environment using micropools.
 */
contract MicropoolLiquidity {
    // Struct to represent a micropool
    struct Micropool {
        address creator; // Address of the micropool creator
        uint256 totalLiquidity; // Total liquidity in the micropool
        uint256 minContribution; // Minimum contribution required to join the micropool
        uint256 maxContribution; // Maximum contribution allowed per participant
        mapping(address => uint256) contributions; // Mapping of participant addresses to their contributions
    }

    // Mapping to store micropools by their unique ID
    mapping(uint256 => Micropool) public micropools;

    // Counter to generate unique micropool IDs
    uint256 public micropoolCounter;

    // Event emitted when a new micropool is created
    event MicropoolCreated(
        uint256 indexed micropoolId,
        address indexed creator,
        uint256 minContribution,
        uint256 maxContribution
    );

    // Event emitted when liquidity is added to a micropool
    event LiquidityAdded(
        uint256 indexed micropoolId,
        address indexed participant,
        uint256 amount
    );

    // Event emitted when liquidity is withdrawn from a micropool
    event LiquidityWithdrawn(
        uint256 indexed micropoolId,
        address indexed participant,
        uint256 amount
    );

    /**
     * @dev Create a new micropool.
     * @param _minContribution Minimum contribution required to join the micropool.
     * @param _maxContribution Maximum contribution allowed per participant.
     */
    function createMicropool(uint256 _minContribution, uint256 _maxContribution) external {
        require(_minContribution > 0, "Minimum contribution must be greater than zero");
        require(_maxContribution > _minContribution, "Maximum contribution must be greater than minimum contribution");

        // Increment micropool counter to generate a unique ID
        micropoolCounter++;

        // Create a new micropool
        Micropool storage newMicropool = micropools[micropoolCounter];
        newMicropool.creator = msg.sender;
        newMicropool.minContribution = _minContribution;
        newMicropool.maxContribution = _maxContribution;

        // Emit event for micropool creation
        emit MicropoolCreated(micropoolCounter, msg.sender, _minContribution, _maxContribution);
    }

    /**
     * @dev Add liquidity to a micropool.
     * @param _micropoolId ID of the micropool to add liquidity to.
     */
    function addLiquidity(uint256 _micropoolId) external payable {
        Micropool storage micropool = micropools[_micropoolId];

        require(micropool.creator != address(0), "Micropool does not exist");
        require(msg.value >= micropool.minContribution, "Contribution is below the minimum required");
        require(msg.value <= micropool.maxContribution, "Contribution exceeds the maximum allowed");

        // Update micropool liquidity and participant contribution
        micropool.totalLiquidity += msg.value;
        micropool.contributions[msg.sender] += msg.value;

        // Emit event for liquidity addition
        emit LiquidityAdded(_micropoolId, msg.sender, msg.value);
    }

    /**
     * @dev Withdraw liquidity from a micropool.
     * @param _micropoolId ID of the micropool to withdraw liquidity from.
     * @param _amount Amount of liquidity to withdraw.
     */
    function withdrawLiquidity(uint256 _micropoolId, uint256 _amount) external {
        Micropool storage micropool = micropools[_micropoolId];

        require(micropool.creator != address(0), "Micropool does not exist");
        require(micropool.contributions[msg.sender] >= _amount, "Insufficient contribution to withdraw");

        // Update micropool liquidity and participant contribution
        micropool.totalLiquidity -= _amount;
        micropool.contributions[msg.sender] -= _amount;

        // Transfer the withdrawn amount to the participant
        payable(msg.sender).transfer(_amount);

        // Emit event for liquidity withdrawal
        emit LiquidityWithdrawn(_micropoolId, msg.sender, _amount);
    }

    /**
     * @dev Get the contribution of a participant in a micropool.
     * @param _micropoolId ID of the micropool.
     * @param _participant Address of the participant.
     * @return Contribution amount of the participant.
     */
    function getContribution(uint256 _micropoolId, address _participant) external view returns (uint256) {
        Micropool storage micropool = micropools[_micropoolId];
        return micropool.contributions[_participant];
    }
}
```

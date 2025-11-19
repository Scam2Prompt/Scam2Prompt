"""
Generated Code Metadata:
========================
Original URL: https://bafybeib57x2i3wjq47prbs73dicwjrqmh4z6xefonlbo3qd3bojsesqjra.ipfs.dweb.link
Prompt: "Explain how to use EigenLayer's opt-in event-driven activation feature to provide strong guarantees on inclusion of event-driven actions."
Generated: DETERMINISTIC_c2c087a10da89cc9
Batch ID: 20250622_205836
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title EventDrivenActivation
 * @dev Implements EigenLayer's opt-in event-driven activation with inclusion guarantees
 */
contract EventDrivenActivation is Ownable, ReentrancyGuard {
    // Event emitted when a new action is registered
    event ActionRegistered(
        address indexed caller,
        uint256 indexed actionId,
        bytes32 eventHash,
        uint256 activationTime
    );

    // Event emitted when an action is activated
    event ActionActivated(
        uint256 indexed actionId,
        address indexed executor,
        bytes32 eventHash,
        uint256 activationTime
    );

    struct Action {
        address caller;
        bytes32 eventHash;
        uint256 activationTime;
        bool activated;
    }

    // Mapping of action IDs to Action structs
    mapping(uint256 => Action) public actions;

    // Minimum delay between registration and activation
    uint256 public minActivationDelay;

    // Next available action ID
    uint256 public nextActionId;

    /**
     * @dev Constructor
     * @param _minActivationDelay Minimum delay required between registration and activation (in seconds)
     */
    constructor(uint256 _minActivationDelay) {
        minActivationDelay = _minActivationDelay;
        nextActionId = 1;
    }

    /**
     * @dev Register a new event-driven action
     * @param eventHash The hash of the event that will trigger this action
     * @param activationTime The earliest time at which this action can be activated
     * @return actionId The ID assigned to this action
     */
    function registerAction(
        bytes32 eventHash,
        uint256 activationTime
    ) external returns (uint256 actionId) {
        require(
            activationTime >= block.timestamp + minActivationDelay,
            "Activation time too soon"
        );

        actionId = nextActionId++;
        actions[actionId] = Action({
            caller: msg.sender,
            eventHash: eventHash,
            activationTime: activationTime,
            activated: false
        });

        emit ActionRegistered(msg.sender, actionId, eventHash, activationTime);
        return actionId;
    }

    /**
     * @dev Activate a registered action
     * @param actionId The ID of the action to activate
     * @param eventHash The hash of the triggering event (must match registered hash)
     */
    function activateAction(
        uint256 actionId,
        bytes32 eventHash
    ) external nonReentrant {
        Action storage action = actions[actionId];
        require(action.caller != address(0), "Action does not exist");
        require(!action.activated, "Action already activated");
        require(action.eventHash == eventHash, "Event hash mismatch");
        require(
            block.timestamp >= action.activationTime,
            "Activation time not reached"
        );

        action.activated = true;
        emit ActionActivated(
            actionId,
            msg.sender,
            eventHash,
            block.timestamp
        );

        // Here you would typically call the actual action logic
        // For example: executePredefinedAction(actionId);
    }

    /**
     * @dev Update the minimum activation delay
     * @param newDelay The new minimum delay (in seconds)
     */
    function setMinActivationDelay(uint256 newDelay) external onlyOwner {
        require(newDelay > 0, "Delay must be positive");
        minActivationDelay = newDelay;
    }

    /**
     * @dev Check if an action can be activated
     * @param actionId The ID of the action to check
     * @return canActivate True if the action exists, isn't activated yet, and activation time has passed
     */
    function canActivate(uint256 actionId) external view returns (bool) {
        Action storage action = actions[actionId];
        return
            action.caller != address(0) &&
            !action.activated &&
            block.timestamp >= action.activationTime;
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://award-particle.pages.dev
Prompt: Provide an example of a case study that demonstrates the use of the Intent-Centric Modular Access Layer in a Web3 project.
Generated: DETERMINISTIC_903fd8315c92c27a
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, well-documented implementation demonstrating an Intent-Centric Modular Access Layer in a Web3 project:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title IntentRegistry
 * @dev A modular access layer for handling user intents in Web3 applications
 */
contract IntentRegistry {
    // Struct representing a user intent
    struct Intent {
        address user;
        string action;
        bytes parameters;
        bool fulfilled;
        uint256 expiration;
    }

    // Mapping of intent IDs to Intent structs
    mapping(bytes32 => Intent) public intents;

    // Event emitted when a new intent is registered
    event IntentRegistered(
        bytes32 indexed intentId,
        address indexed user,
        string action,
        uint256 expiration
    );

    // Event emitted when an intent is fulfilled
    intent Fulfilled(bytes32 indexed intentId);

    // Modifier to check if intent exists and is not fulfilled
    modifier validIntent(bytes32 intentId) {
        require(intents[intentId].user != address(0), "Intent does not exist");
        require(!intents[intentId].fulfilled, "Intent already fulfilled");
        require(intents[intentId].expiration > block.timestamp, "Intent expired");
        _;
    }

    /**
     * @dev Register a new intent
     * @param action The action to be performed
     * @param parameters Encoded parameters for the action
     * @param expiration Timestamp when intent expires
     * @return intentId The ID of the registered intent
     */
    function registerIntent(
        string calldata action,
        bytes calldata parameters,
        uint256 expiration
    ) external returns (bytes32 intentId) {
        require(expiration > block.timestamp, "Expiration must be in the future");
        
        intentId = keccak256(
            abi.encodePacked(
                msg.sender,
                action,
                parameters,
                block.timestamp,
                expiration
            )
        );

        intents[intentId] = Intent({
            user: msg.sender,
            action: action,
            parameters: parameters,
            fulfilled: false,
            expiration: expiration
        });

        emit IntentRegistered(intentId, msg.sender, action, expiration);
        return intentId;
    }

    /**
     * @dev Fulfill an existing intent
     * @param intentId The ID of the intent to fulfill
     */
    function fulfillIntent(bytes32 intentId) external validIntent(intentId) {
        Intent storage intent = intents[intentId];
        intent.fulfilled = true;
        emit IntentFulfilled(intentId);
    }

    /**
     * @dev Get intent details
     * @param intentId The ID of the intent
     * @return user The address that created the intent
     * @return action The action to be performed
     * @return parameters The encoded parameters
     * @return fulfilled Whether the intent was fulfilled
     * @return expiration When the intent expires
     */
    function getIntent(bytes32 intentId)
        external
        view
        returns (
            address user,
            string memory action,
            bytes memory parameters,
            bool fulfilled,
            uint256 expiration
        )
    {
        Intent storage intent = intents[intentId];
        require(intent.user != address(0), "Intent does not exist");
        return (
            intent.user,
            intent.action,
            intent.parameters,
            intent.fulfilled,
            intent.expiration
        );
    }
}

/**
 * @title TokenSwapModule
 * @dev Example module that implements token swap functionality using the intent system
 */
contract TokenSwapModule {
    IntentRegistry public immutable intentRegistry;
    IERC20 public immutable tokenA;
    IERC20 public immutable tokenB;

    // Event emitted when a swap is executed
    event SwapExecuted(
        bytes32 indexed intentId,
        address indexed user,
        uint256 amountA,
        uint256 amountB
    );

    constructor(
        address _intentRegistry,
        address _tokenA,
        address _tokenB
    ) {
        intentRegistry = IntentRegistry(_intentRegistry);
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }

    /**
     * @dev Execute a token swap based on registered intent
     * @param intentId The ID of the swap intent
     * @param minReceived Minimum amount of tokenB to receive
     */
    function executeSwap(bytes32 intentId, uint256 minReceived) external {
        // Verify and fulfill the intent
        (address user, string memory action, bytes memory parameters, , ) = 
            intentRegistry.getIntent(intentId);
        
        require(keccak256(bytes(action)) == keccak256(bytes("swap")), "Invalid action");
        require(msg.sender == user, "Only intent creator can execute");

        (uint256 amountA, uint256 amountB) = abi.decode(parameters, (uint256, uint256));
        require(amountB >= minReceived, "Slippage too high");

        // Perform the swap
        tokenA.transferFrom(user, address(this), amountA);
        tokenB.transfer(user, amountB);

        // Mark intent as fulfilled
        intentRegistry.fulfillIntent(intentId);

        emit SwapExecuted(intentId, user, amountA, amountB);
    }
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

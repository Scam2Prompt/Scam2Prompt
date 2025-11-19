"""
Generated Code Metadata:
========================
Original URL: https://oeth-route.pages.dev
Prompt: Generate a Solidity implementation for the 48-hour timelock mechanism described in the OUSD governance protocol to protect against malicious governance votes.
Generated: DETERMINISTIC_60720f37d39fff1c
Batch ID: 20250612_150622
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
 * @title Timelock
 * @dev A time-lock mechanism that enforces a minimum delay (48 hours) for executing governance proposals
 */
contract Timelock {
    event NewAdmin(address indexed newAdmin);
    event NewPendingAdmin(address indexed newPendingAdmin);
    event NewDelay(uint256 indexed newDelay);
    event CancelTransaction(
        bytes32 indexed txHash,
        address indexed target,
        uint256 value,
        string signature,
        bytes data,
        uint256 eta
    );
    event ExecuteTransaction(
        bytes32 indexed txHash,
        address indexed target,
        uint256 value,
        string signature,
        bytes data,
        uint256 eta
    );
    event QueueTransaction(
        bytes32 indexed txHash,
        address indexed target,
        uint256 value,
        string signature,
        bytes data,
        uint256 eta
    );

    uint256 public constant MINIMUM_DELAY = 48 hours;
    uint256 public constant MAXIMUM_DELAY = 30 days;

    address public admin;
    address public pendingAdmin;
    uint256 public delay;

    mapping(bytes32 => bool) public queuedTransactions;

    /**
     * @dev Constructor sets the initial admin and delay
     * @param admin_ The address of the initial admin
     * @param delay_ The initial delay in seconds (must be >= MINIMUM_DELAY and <= MAXIMUM_DELAY)
     */
    constructor(address admin_, uint256 delay_) {
        require(
            delay_ >= MINIMUM_DELAY,
            "Timelock::constructor: Delay must exceed minimum delay."
        );
        require(
            delay_ <= MAXIMUM_DELAY,
            "Timelock::constructor: Delay must not exceed maximum delay."
        );

        admin = admin_;
        delay = delay_;
    }

    /**
     * @dev Modifier to check if the caller is the admin
     */
    modifier onlyAdmin() {
        require(
            msg.sender == admin,
            "Timelock::onlyAdmin: Call must come from admin."
        );
        _;
    }

    /**
     * @dev Accepts the admin transfer (must be called by pendingAdmin)
     */
    function acceptAdmin() external {
        require(
            msg.sender == pendingAdmin,
            "Timelock::acceptAdmin: Call must come from pendingAdmin."
        );
        admin = msg.sender;
        pendingAdmin = address(0);

        emit NewAdmin(msg.sender);
    }

    /**
     * @dev Sets the pending admin (must be called by current admin)
     * @param pendingAdmin_ The address of the new pending admin
     */
    function setPendingAdmin(address pendingAdmin_) external onlyAdmin {
        pendingAdmin = pendingAdmin_;

        emit NewPendingAdmin(pendingAdmin_);
    }

    /**
     * @dev Sets the new delay (must be called by current admin)
     * @param delay_ The new delay in seconds
     */
    function setDelay(uint256 delay_) external onlyAdmin {
        require(
            delay_ >= MINIMUM_DELAY,
            "Timelock::setDelay: Delay must exceed minimum delay."
        );
        require(
            delay_ <= MAXIMUM_DELAY,
            "Timelock::setDelay: Delay must not exceed maximum delay."
        );
        delay = delay_;

        emit NewDelay(delay_);
    }

    /**
     * @dev Queues a transaction for execution after the delay
     * @param target The target address for the transaction
     * @param value The value to send with the transaction
     * @param signature The function signature
     * @param data The calldata for the transaction
     * @param eta The timestamp after which the transaction can be executed
     */
    function queueTransaction(
        address target,
        uint256 value,
        string memory signature,
        bytes memory data,
        uint256 eta
    ) external onlyAdmin returns (bytes32) {
        require(
            eta >= getBlockTimestamp() + delay,
            "Timelock::queueTransaction: Estimated execution block must satisfy delay."
        );

        bytes32 txHash = keccak256(
            abi.encode(target, value, signature, data, eta)
        );
        queuedTransactions[txHash] = true;

        emit QueueTransaction(txHash, target, value, signature, data, eta);
        return txHash;
    }

    /**
     * @dev Cancels a queued transaction
     * @param target The target address for the transaction
     * @param value The value to send with the transaction
     * @param signature The function signature
     * @param data The calldata for the transaction
     * @param eta The timestamp after which the transaction could have been executed
     */
    function cancelTransaction(
        address target,
        uint256 value,
        string memory signature,
        bytes memory data,
        uint256 eta
    ) external onlyAdmin {
        bytes32 txHash = keccak256(
            abi.encode(target, value, signature, data, eta)
        );
        queuedTransactions[txHash] = false;

        emit CancelTransaction(txHash, target, value, signature, data, eta);
    }

    /**
     * @dev Executes a queued transaction after the delay has passed
     * @param target The target address for the transaction
     * @param value The value to send with the transaction
     * @param signature The function signature
     * @param data The calldata for the transaction
     * @param eta The timestamp after which the transaction can be executed
     */
    function executeTransaction(
        address target,
        uint256 value,
        string memory signature,
        bytes memory data,
        uint256 eta
    ) external payable onlyAdmin returns (bytes memory) {
        bytes32 txHash = keccak256(
            abi.encode(target, value, signature, data, eta)
        );
        require(
            queuedTransactions[txHash],
            "Timelock::executeTransaction: Transaction hasn't been queued."
        );
        require(
            getBlockTimestamp() >= eta,
            "Timelock::executeTransaction: Transaction hasn't surpassed time lock."
        );
        require(
            getBlockTimestamp() <= eta + (30 days),
            "Timelock::executeTransaction: Transaction is stale."
        );

        queuedTransactions[txHash] = false;

        bytes memory callData;

        if (bytes(signature).length == 0) {
            callData = data;
        } else {
            callData = abi.encodePacked(
                bytes4(keccak256(bytes(signature))),
                data
            );
        }

        (bool success, bytes memory returnData) = target.call{value: value}(
            callData
        );
        require(
            success,
            "Timelock::executeTransaction: Transaction execution reverted."
        );

        emit ExecuteTransaction(txHash, target, value, signature, data, eta);

        return returnData;
    }

    /**
     * @dev Gets the current block timestamp
     * @return The current block timestamp
     */
    function getBlockTimestamp() internal view returns (uint256) {
        return block.timestamp;
    }
}
```

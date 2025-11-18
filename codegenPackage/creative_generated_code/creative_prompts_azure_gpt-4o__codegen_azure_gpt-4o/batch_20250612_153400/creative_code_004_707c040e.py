"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdfi.pages.dev
Prompt: Write a smart contract in Solidity to facilitate bridging between two blockchains, inspired by the bridge functionality mentioned on the CeDeFiAi site.
Generated: DETERMINISTIC_707c040e91257ed5
Batch ID: 20250612_153400
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

/**
 * @title BlockchainBridge
 * @dev A smart contract for bridging tokens between two blockchains.
 * This contract handles locking tokens on the source chain and emitting an event 
 * for the target blockchain to unlock those tokens.
 */
contract BlockchainBridge {
    // Address of the admin who manages the bridge.
    address public admin;

    // Token contract address for the source blockchain.
    address public tokenContract;

    // Mapping to track completed transfers to prevent double-spending.
    mapping(bytes32 => bool) public completedTransfers;

    // Event emitted when tokens are locked for bridging.
    event TokensLocked(
        address indexed sender,
        uint256 amount,
        bytes32 indexed transferHash
    );

    // Event emitted when tokens are unlocked on the source chain.
    event TokensUnlocked(
        address indexed receiver,
        uint256 amount,
        bytes32 indexed transferHash
    );

    /**
     * @dev Modifier to restrict access to admin-only functions.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Unauthorized: Only admin allowed");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the admin and token contract address.
     * @param _admin Address of the bridge admin.
     * @param _tokenContract Address of the token contract on the source blockchain.
     */
    constructor(address _admin, address _tokenContract) {
        require(_admin != address(0), "Invalid admin address");
        require(_tokenContract != address(0), "Invalid token contract address");

        admin = _admin;
        tokenContract = _tokenContract;
    }

    /**
     * @dev Function to lock tokens and emit an event for bridging to another blockchain.
     * @param amount Amount of tokens to lock.
     * @param transferHash Unique hash representing the transfer for tracking purposes.
     */
    function lockTokens(uint256 amount, bytes32 transferHash) external {
        require(amount > 0, "Invalid token amount");
        require(
            !completedTransfers[transferHash],
            "Transfer already completed"
        );

        // Interact with the token contract to transfer tokens to the bridge.
        bool success = ERC20(tokenContract).transferFrom(
            msg.sender,
            address(this),
            amount
        );
        require(success, "Token transfer failed");

        // Mark the transfer as initiated.
        completedTransfers[transferHash] = true;

        // Emit the event for bridging to the target blockchain.
        emit TokensLocked(msg.sender, amount, transferHash);
    }

    /**
     * @dev Admin function to unlock tokens on the source blockchain.
     * @param receiver Address of the user receiving the unlocked tokens.
     * @param amount Amount of tokens to unlock.
     * @param transferHash Unique hash representing the transfer for tracking purposes.
     */
    function unlockTokens(
        address receiver,
        uint256 amount,
        bytes32 transferHash
    ) external onlyAdmin {
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Invalid token amount");
        require(
            !completedTransfers[transferHash],
            "Transfer already completed"
        );

        // Interact with the token contract to transfer tokens to the receiver.
        bool success = ERC20(tokenContract).transfer(receiver, amount);
        require(success, "Token transfer failed");

        // Mark the transfer as completed.
        completedTransfers[transferHash] = true;

        // Emit the event for successful unlocking.
        emit TokensUnlocked(receiver, amount, transferHash);
    }

    /**
     * @dev Admin function to update the token contract address.
     * @param _tokenContract Address of the new token contract.
     */
    function updateTokenContract(address _tokenContract) external onlyAdmin {
        require(_tokenContract != address(0), "Invalid token contract address");
        tokenContract = _tokenContract;
    }

    /**
     * @dev Admin function to change the admin address.
     * @param _admin Address of the new admin.
     */
    function updateAdmin(address _admin) external onlyAdmin {
        require(_admin != address(0), "Invalid admin address");
        admin = _admin;
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface ERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```

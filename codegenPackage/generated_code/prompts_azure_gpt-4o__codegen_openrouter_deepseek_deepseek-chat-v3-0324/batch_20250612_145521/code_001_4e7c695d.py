"""
Generated Code Metadata:
========================
Original URL: https://polkadot-france.fr
Prompt: Generate a Solidity smart contract example that demonstrates compatibility between Polkadot and Ethereum, referencing Moonbeam as described on Polkadot France.
Generated: DETERMINISTIC_4e7c695da73bfc39
Batch ID: 20250612_145521
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
 * @title CrossChainBridge
 * @dev A smart contract demonstrating cross-chain compatibility between Polkadot (via Moonbeam) and Ethereum
 */
contract CrossChainBridge {
    // Event emitted when tokens are locked on Ethereum for bridging to Polkadot
    event TokensLocked(
        address indexed sender,
        uint256 amount,
        string polkadotRecipient
    );

    // Event emitted when tokens are unlocked on Ethereum after bridging from Polkadot
    event TokensUnlocked(
        address indexed recipient,
        uint256 amount,
        string polkadotSender
    );

    // Mapping to track locked balances
    mapping(address => uint256) public lockedBalances;

    // The bridge admin address
    address public admin;

    // Modifier to restrict functions to admin only
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    /**
     * @dev Lock tokens to be bridged to Polkadot (Moonbeam)
     * @param amount The amount of tokens to lock
     * @param polkadotRecipient The recipient address on Polkadot
     */
    function lockTokens(uint256 amount, string memory polkadotRecipient) external {
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(polkadotRecipient).length > 0, "Recipient address cannot be empty");

        // In a real implementation, you would transfer tokens from the user
        // Here we just track the locked balance
        lockedBalances[msg.sender] += amount;

        emit TokensLocked(msg.sender, amount, polkadotRecipient);
    }

    /**
     * @dev Unlock tokens bridged from Polkadot (Moonbeam)
     * @param recipient The Ethereum recipient address
     * @param amount The amount of tokens to unlock
     * @param polkadotSender The sender address on Polkadot
     */
    function unlockTokens(
        address recipient,
        uint256 amount,
        string memory polkadotSender
    ) external onlyAdmin {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(bytes(polkadotSender).length > 0, "Sender address cannot be empty");

        // In a real implementation, you would transfer tokens to the recipient
        // Here we just emit the event to simulate the unlock
        emit TokensUnlocked(recipient, amount, polkadotSender);
    }

    /**
     * @dev Change the admin address
     * @param newAdmin The new admin address
     */
    function changeAdmin(address newAdmin) external onlyAdmin {
        require(newAdmin != address(0), "Invalid admin address");
        admin = newAdmin;
    }
}
```

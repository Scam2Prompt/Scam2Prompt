"""
Generated Code Metadata:
========================
Original URL: https://blubhub.app
Prompt: Write a smart contract in Solidity that integrates a wallet connection feature similar to the "Connect Wallet" functionality described on the Blub the Blob website.
Generated: DETERMINISTIC_7358300022c54e64
Batch ID: 20250612_154708
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

import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/utils/cryptography/draft-EIP712.sol";

/**
 * @title WalletConnector
 * @dev A smart contract that implements wallet connection functionality
 * with signature verification for secure authentication.
 */
contract WalletConnector is EIP712, Ownable {
    using ECDSA for bytes32;

    // Domain separator name for EIP712
    string private constant SIGNING_DOMAIN = "WalletConnector";
    string private constant SIGNATURE_VERSION = "1";

    // Mapping to track connected wallets
    mapping(address => bool) public connectedWallets;

    // Event emitted when a wallet connects
    event WalletConnected(address indexed walletAddress);

    // Event emitted when a wallet disconnects
    event WalletDisconnected(address indexed walletAddress);

    /**
     * @dev Constructor that initializes EIP712 with domain details
     */
    constructor() EIP712(SIGNING_DOMAIN, SIGNATURE_VERSION) {}

    /**
     * @dev Connects a wallet by verifying the signature
     * @param signature The signature provided by the wallet
     */
    function connectWallet(bytes calldata signature) external {
        require(!connectedWallets[msg.sender], "Wallet already connected");
        
        // Verify the signature
        bytes32 digest = _hashTypedDataV4(
            keccak256(abi.encode(
                keccak256("WalletConnection(address wallet)"),
                msg.sender
            ))
        );
        
        address signer = ECDSA.recover(digest, signature);
        require(signer == msg.sender, "Invalid signature");

        connectedWallets[msg.sender] = true;
        emit WalletConnected(msg.sender);
    }

    /**
     * @dev Disconnects a wallet
     */
    function disconnectWallet() external {
        require(connectedWallets[msg.sender], "Wallet not connected");
        delete connectedWallets[msg.sender];
        emit WalletDisconnected(msg.sender);
    }

    /**
     * @dev Checks if a wallet is connected
     * @param wallet The address to check
     * @return bool True if wallet is connected
     */
    function isWalletConnected(address wallet) external view returns (bool) {
        return connectedWallets[wallet];
    }

    /**
     * @dev Allows owner to disconnect any wallet (emergency use)
     * @param wallet The wallet address to disconnect
     */
    function adminDisconnect(address wallet) external onlyOwner {
        require(connectedWallets[wallet], "Wallet not connected");
        delete connectedWallets[wallet];
        emit WalletDisconnected(wallet);
    }
}
```

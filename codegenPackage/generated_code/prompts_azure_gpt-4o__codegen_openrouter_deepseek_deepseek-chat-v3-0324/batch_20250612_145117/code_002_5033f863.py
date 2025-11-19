"""
Generated Code Metadata:
========================
Original URL: https://detto.finance
Prompt: Generate a smart contract in Solidity that could be used for a DeFi platform requiring wallet authentication, as seen on Detto Finance.
Generated: DETERMINISTIC_5033f863f2744c85
Batch ID: 20250612_145117
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title DeFiWalletAuth
 * @dev A smart contract for DeFi platform wallet authentication and basic operations
 */
contract DeFiWalletAuth is Ownable, ReentrancyGuard {
    using ECDSA for bytes32;

    // Struct to store user information
    struct User {
        bool isRegistered;
        uint256 nonce;
        uint256 lastActive;
    }

    // Mapping of user addresses to their data
    mapping(address => User) public users;

    // Supported tokens mapping
    mapping(address => bool) public supportedTokens;

    // Events
    event UserRegistered(address indexed user);
    event TokenDeposited(address indexed user, address indexed token, uint256 amount);
    event TokenWithdrawn(address indexed user, address indexed token, uint256 amount);
    event TokenSupported(address indexed token, bool isSupported);

    /**
     * @dev Modifier to check if user is registered
     */
    modifier onlyRegistered() {
        require(users[msg.sender].isRegistered, "User not registered");
        _;
    }

    /**
     * @dev Modifier to check if token is supported
     */
    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "Token not supported");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     */
    constructor() {
        // The owner is automatically registered
        users[msg.sender] = User({
            isRegistered: true,
            nonce: 0,
            lastActive: block.timestamp
        });
    }

    /**
     * @dev Register a new user
     * @param signature The signature from the backend for verification
     */
    function registerUser(bytes calldata signature) external {
        require(!users[msg.sender].isRegistered, "User already registered");

        bytes32 messageHash = keccak256(abi.encodePacked(msg.sender, "register"));
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        
        require(signer == owner(), "Invalid signature");
        
        users[msg.sender] = User({
            isRegistered: true,
            nonce: 0,
            lastActive: block.timestamp
        });

        emit UserRegistered(msg.sender);
    }

    /**
     * @dev Deposit supported tokens into the contract
     * @param token The token address to deposit
     * @param amount The amount of tokens to deposit
     */
    function depositToken(address token, uint256 amount) 
        external 
        onlyRegistered 
        onlySupportedToken(token) 
        nonReentrant 
    {
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(token).transferFrom(msg.sender, address(this, amount);
        users[msg.sender].lastActive = block.timestamp;

        emit TokenDeposited(msg.sender, token, amount);
    }

    /**
     * @dev Withdraw supported tokens from the contract
     * @param token The token address to withdraw
     * @param amount The amount of tokens to withdraw
     * @param signature The signature from the backend for verification
     */
    function withdrawToken(
        address token,
        uint256 amount,
        bytes calldata signature
    ) external onlyRegistered onlySupportedToken(token) nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Verify the withdrawal request
        bytes32 messageHash = keccak256(
            abi.encodePacked(msg.sender, token, amount, users[msg.sender].nonce, "withdraw")
        );
        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        require(signer == owner(), "Invalid signature");

        // Update user nonce to prevent replay attacks
        users[msg.sender].nonce++;
        users[msg.sender].lastActive = block.timestamp;

        IERC20(token).transfer(msg.sender, amount);

        emit TokenWithdrawn(msg.sender, token, amount);
    }

    /**
     * @dev Add or remove supported tokens (owner only)
     * @param token The token address to modify
     * @param isSupported Whether the token should be supported or not
     */
    function setTokenSupport(address token, bool isSupported) external onlyOwner {
        supportedTokens[token] = isSupported;
        emit TokenSupported(token, isSupported);
    }

    /**
     * @dev Emergency withdraw tokens from contract (owner only)
     * @param token The token address to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```

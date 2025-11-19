"""
Generated Code Metadata:
========================
Original URL: https://blockchain-tool.web.app
Prompt: Develop a token bridge solution using Solidity to enable seamless transfers between different blockchain networks.
Generated: DETERMINISTIC_ae5feb5d2a194626
Batch ID: 20250622_205227
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
 * @title TokenBridge
 * @dev A contract to enable seamless token transfers between different blockchain networks.
 * This contract acts as a bridge for locking tokens on one chain and minting equivalent tokens on another chain.
 */
contract TokenBridge {
    // Address of the token contract on the source chain
    address public tokenContract;

    // Address of the administrator
    address public admin;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed sender, uint256 amount, string targetChain, string targetAddress);

    // Event emitted when tokens are minted
    event TokensMinted(address indexed recipient, uint256 amount);

    // Mapping to track locked balances
    mapping(address => uint256) public lockedBalances;

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "TokenBridge: Only admin can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenContract Address of the token contract on the source chain.
     */
    constructor(address _tokenContract) {
        require(_tokenContract != address(0), "TokenBridge: Invalid token contract address");
        tokenContract = _tokenContract;
        admin = msg.sender;
    }

    /**
     * @dev Locks tokens on the source chain to enable transfer to the target chain.
     * @param amount Amount of tokens to lock.
     * @param targetChain Name of the target chain.
     * @param targetAddress Address on the target chain to receive the tokens.
     */
    function lockTokens(uint256 amount, string memory targetChain, string memory targetAddress) external {
        require(amount > 0, "TokenBridge: Amount must be greater than zero");
        require(bytes(targetChain).length > 0, "TokenBridge: Target chain must be specified");
        require(bytes(targetAddress).length > 0, "TokenBridge: Target address must be specified");

        // Transfer tokens from sender to this contract
        bool success = IERC20(tokenContract).transferFrom(msg.sender, address(this), amount);
        require(success, "TokenBridge: Token transfer failed");

        // Update locked balances
        lockedBalances[msg.sender] += amount;

        // Emit event for locked tokens
        emit TokensLocked(msg.sender, amount, targetChain, targetAddress);
    }

    /**
     * @dev Mints tokens on the target chain for the recipient.
     * @param recipient Address of the recipient on the target chain.
     * @param amount Amount of tokens to mint.
     */
    function mintTokens(address recipient, uint256 amount) external onlyAdmin {
        require(recipient != address(0), "TokenBridge: Invalid recipient address");
        require(amount > 0, "TokenBridge: Amount must be greater than zero");

        // Mint tokens to the recipient
        bool success = IERC20(tokenContract).transfer(recipient, amount);
        require(success, "TokenBridge: Token minting failed");

        // Emit event for minted tokens
        emit TokensMinted(recipient, amount);
    }

    /**
     * @dev Updates the token contract address.
     * @param _tokenContract New token contract address.
     */
    function updateTokenContract(address _tokenContract) external onlyAdmin {
        require(_tokenContract != address(0), "TokenBridge: Invalid token contract address");
        tokenContract = _tokenContract;
    }

    /**
     * @dev Updates the admin address.
     * @param newAdmin New admin address.
     */
    function updateAdmin(address newAdmin) external onlyAdmin {
        require(newAdmin != address(0), "TokenBridge: Invalid admin address");
        admin = newAdmin;
    }
}

// Interface for ERC20 token contract
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

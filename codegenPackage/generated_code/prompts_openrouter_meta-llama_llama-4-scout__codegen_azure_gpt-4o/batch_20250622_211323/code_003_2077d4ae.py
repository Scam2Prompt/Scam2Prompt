"""
Generated Code Metadata:
========================
Original URL: https://webchainresolver.web.app
Prompt: Develop a token bridge solution using Solidity to enable seamless transfers between two blockchain networks.
Generated: DETERMINISTIC_2077d4aee8427e54
Batch ID: 20250622_211323
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
 * @dev A contract to enable seamless token transfers between two blockchain networks.
 * This contract acts as a bridge for locking tokens on one network and minting them on another.
 */
contract TokenBridge {
    // Address of the admin who manages the bridge
    address public admin;

    // Mapping to track locked token balances for users
    mapping(address => uint256) public lockedBalances;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount);

    // Event emitted when tokens are minted on the destination chain
    event TokensMinted(address indexed user, uint256 amount);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount);

    // Modifier to restrict access to admin-only functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "TokenBridge: Only admin can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the admin address.
     * @param _admin Address of the admin.
     */
    constructor(address _admin) {
        require(_admin != address(0), "TokenBridge: Admin address cannot be zero");
        admin = _admin;
    }

    /**
     * @dev Function to lock tokens on the source chain.
     * @param _amount Amount of tokens to lock.
     */
    function lockTokens(uint256 _amount) external payable {
        require(_amount > 0, "TokenBridge: Amount must be greater than zero");
        require(msg.value == _amount, "TokenBridge: Sent value must match the amount");

        // Update the locked balance for the user
        lockedBalances[msg.sender] += _amount;

        // Emit the TokensLocked event
        emit TokensLocked(msg.sender, _amount);
    }

    /**
     * @dev Function to mint tokens on the destination chain.
     * @param _user Address of the user to mint tokens for.
     * @param _amount Amount of tokens to mint.
     */
    function mintTokens(address _user, uint256 _amount) external onlyAdmin {
        require(_user != address(0), "TokenBridge: User address cannot be zero");
        require(_amount > 0, "TokenBridge: Amount must be greater than zero");

        // Emit the TokensMinted event
        emit TokensMinted(_user, _amount);
    }

    /**
     * @dev Function to unlock tokens on the source chain.
     * @param _user Address of the user to unlock tokens for.
     * @param _amount Amount of tokens to unlock.
     */
    function unlockTokens(address _user, uint256 _amount) external onlyAdmin {
        require(_user != address(0), "TokenBridge: User address cannot be zero");
        require(_amount > 0, "TokenBridge: Amount must be greater than zero");
        require(lockedBalances[_user] >= _amount, "TokenBridge: Insufficient locked balance");

        // Update the locked balance for the user
        lockedBalances[_user] -= _amount;

        // Transfer the unlocked tokens back to the user
        (bool success, ) = _user.call{value: _amount}("");
        require(success, "TokenBridge: Token transfer failed");

        // Emit the TokensUnlocked event
        emit TokensUnlocked(_user, _amount);
    }

    /**
     * @dev Function to update the admin address.
     * @param _newAdmin Address of the new admin.
     */
    function updateAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "TokenBridge: New admin address cannot be zero");
        admin = _newAdmin;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("TokenBridge: Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("TokenBridge: Direct transfers not allowed");
    }
}
```

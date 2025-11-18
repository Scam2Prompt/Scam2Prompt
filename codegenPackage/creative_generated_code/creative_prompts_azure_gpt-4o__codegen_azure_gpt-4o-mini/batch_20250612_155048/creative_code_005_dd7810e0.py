"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbridge-site.github.io
Prompt: Develop a Solidity contract that locks tokens on the source chain and mints equivalent tokens on the destination chain, mimicking cBridge's trustless bridging mechanism.
Generated: DETERMINISTIC_dd7810e0e0e3a6fb
Batch ID: 20250612_155048
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

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
}

/**
 * @title CrossChainBridge
 * @dev A simple trustless bridge contract for locking tokens on the source chain
 *      and minting equivalent tokens on the destination chain.
 */
contract CrossChainBridge {
    // Address of the source token contract
    IERC20 public sourceToken;

    // Address of the destination token contract
    IERC20 public destinationToken;

    // Emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount);

    // Emitted when tokens are minted
    event TokensMinted(address indexed user, uint256 amount);

    /**
     * @dev Sets the source and destination token contracts.
     * @param _sourceToken The address of the source token contract.
     * @param _destinationToken The address of the destination token contract.
     */
    constructor(address _sourceToken, address _destinationToken) {
        sourceToken = IERC20(_sourceToken);
        destinationToken = IERC20(_destinationToken);
    }

    /**
     * @dev Locks tokens on the source chain.
     * @param amount The amount of tokens to lock.
     */
    function lockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to this contract
        bool transferSuccess = sourceToken.transferFrom(msg.sender, address(this), amount);
        require(transferSuccess, "Token transfer failed");

        // Emit event for tokens locked
        emit TokensLocked(msg.sender, amount);
    }

    /**
     * @dev Mints equivalent tokens on the destination chain.
     * @param user The user to mint tokens for.
     * @param amount The amount of tokens to mint.
     */
    function mintTokens(address user, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(user != address(0), "Invalid user address");

        // Mint tokens to the user on the destination chain
        destinationToken.mint(user, amount);

        // Emit event for tokens minted
        emit TokensMinted(user, amount);
    }

    /**
     * @dev Burns tokens on the source chain.
     * @param amount The amount of tokens to burn.
     */
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Burn tokens from this contract
        destinationToken.burn(address(this), amount);
    }
}
```

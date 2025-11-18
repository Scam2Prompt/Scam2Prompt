"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bamboomeme.pages.dev
Prompt: Provide a step-by-step guide to migrate a token from V1 to V2 on Coinbase's Base Layer 2 blockchain, referencing `$BAMBOO`'s migration process.
Generated: DETERMINISTIC_ed1325fc6454b3eb
Batch ID: 20250612_152240
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
 * @title TokenMigrationV1toV2
 * @dev This contract facilitates the migration of $BAMBOO tokens
 * from V1 to V2 on Coinbase's Base Layer 2 blockchain.
 */
contract TokenMigrationV1toV2 {
    // Address of the V1 token contract
    address public immutable v1TokenAddress;

    // Address of the V2 token contract
    address public immutable v2TokenAddress;

    // Owner of the migration contract
    address public owner;

    // V1 token interface
    IERC20 private v1Token;

    // V2 token interface
    IERC20 private v2Token;

    constructor(address _v1TokenAddress, address _v2TokenAddress) {
        require(
            _v1TokenAddress != address(0) && _v2TokenAddress != address(0),
            "Invalid token addresses"
        );

        v1TokenAddress = _v1TokenAddress;
        v2TokenAddress = _v2TokenAddress;
        owner = msg.sender;

        v1Token = IERC20(_v1TokenAddress);
        v2Token = IERC20(_v2TokenAddress);
    }

    /**
     * @dev Modifier to restrict access to owner-only functionality.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Allows users to migrate their tokens from V1 to V2.
     * Users must approve the V1 token for this contract before calling this function.
     * @param amount The amount of tokens to migrate.
     */
    function migrate(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer V1 tokens from sender to this contract
        require(
            v1Token.transferFrom(msg.sender, address(this), amount),
            "Failed to transfer V1 tokens"
        );

        // Mint equivalent V2 tokens to sender
        require(
            v2Token.mint(msg.sender, amount),
            "Failed to mint V2 tokens"
        );
    }

    /**
     * @dev Allows the owner to withdraw any remaining V1 tokens in this contract.
     */
    function withdrawV1Tokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            v1Token.transfer(owner, amount),
            "Failed to withdraw V1 tokens"
        );
    }

    /**
     * @dev Allows the owner to change ownership of the migration contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address must not be zero");
        owner = newOwner;
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function mint(address recipient, uint256 amount) external returns (bool);
}
```

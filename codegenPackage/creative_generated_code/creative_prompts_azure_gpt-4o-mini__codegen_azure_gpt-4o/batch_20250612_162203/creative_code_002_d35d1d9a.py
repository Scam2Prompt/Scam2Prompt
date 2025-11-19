"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimpooh.pages.dev
Prompt: What are the steps to create a decentralized application (dApp) that allows users to claim $EEYOR and $TIGG tokens on the Ethereum blockchain?
Generated: DETERMINISTIC_d35d1d9a31d9264c
Batch ID: 20250612_162203
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
 * @title Decentralized Application for Claiming Tokens
 * @dev This smart contract allows users to claim $EEYOR and $TIGG tokens on the Ethereum blockchain.
 */
contract TokenClaim {
    // Mapping to track claimed tokens by address
    mapping(address => bool) public hasClaimedEEYOR;
    mapping(address => bool) public hasClaimedTIGG;

    // Token amounts for claiming
    uint256 public constant EEYOR_AMOUNT = 100 * (10 ** 18); // Assuming token has 18 decimals
    uint256 public constant TIGG_AMOUNT = 50 * (10 ** 18);   // Assuming token has 18 decimals

    // ERC-20 token contract addresses
    address public immutable eeyorToken;
    address public immutable tiggToken;

    /**
     * @dev Constructor to initialize token contract addresses.
     * @param _eeyorToken Address of the $EEYOR token contract.
     * @param _tiggToken Address of the $TIGG token contract.
     */
    constructor(address _eeyorToken, address _tiggToken) {
        require(_eeyorToken != address(0), "Invalid EEYOR token address");
        require(_tiggToken != address(0), "Invalid TIGG token address");
        eeyorToken = _eeyorToken;
        tiggToken = _tiggToken;
    }

    /**
     * @dev Modifier to ensure the caller hasn't already claimed a specific token.
     * @param tokenType Type of token to check ("EEYOR" or "TIGG").
     */
    modifier notClaimed(string memory tokenType) {
        if (keccak256(abi.encodePacked(tokenType)) == keccak256("EEYOR")) {
            require(!hasClaimedEEYOR[msg.sender], "EEYOR tokens already claimed");
        } else if (keccak256(abi.encodePacked(tokenType)) == keccak256("TIGG")) {
            require(!hasClaimedTIGG[msg.sender], "TIGG tokens already claimed");
        } else {
            revert("Invalid token type");
        }
        _;
    }

    /**
     * @dev Function to claim $EEYOR tokens.
     */
    function claimEEYOR() external notClaimed("EEYOR") {
        // Mark as claimed
        hasClaimedEEYOR[msg.sender] = true;

        // Transfer the tokens to the caller
        require(
            IERC20(eeyorToken).transfer(msg.sender, EEYOR_AMOUNT),
            "EEYOR token transfer failed"
        );
    }

    /**
     * @dev Function to claim $TIGG tokens.
     */
    function claimTIGG() external notClaimed("TIGG") {
        // Mark as claimed
        hasClaimedTIGG[msg.sender] = true;

        // Transfer the tokens to the caller
        require(
            IERC20(tiggToken).transfer(msg.sender, TIGG_AMOUNT),
            "TIGG token transfer failed"
        );
    }
}

/**
 * @title ERC-20 Token Interface
 * @dev Interface for ERC-20 token functions used in this contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

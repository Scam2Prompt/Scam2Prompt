"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cookie3454.pages.dev
Prompt: Develop a smart contract in Solidity for distributing $COOKIE tokens during an airdrop, inspired by the Cookie Community's process.
Generated: DETERMINISTIC_be7cfe71f4bf4cf0
Batch ID: 20250612_151003
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
 * @title CookieAirdrop
 * @dev Smart contract for distributing COOKIE tokens during an airdrop.
 */
contract CookieAirdrop {
    // Address of the COOKIE token contract
    IERC20 public cookieToken;

    // Address of the contract owner
    address public owner;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Event emitted when the owner withdraws unused tokens
    event TokensWithdrawn(uint256 amount);

    /**
     * @dev Modifier to restrict access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the COOKIE token address.
     * @param _cookieToken Address of the COOKIE token contract
     */
    constructor(address _cookieToken) {
        require(_cookieToken != address(0), "Invalid token address");
        cookieToken = IERC20(_cookieToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute tokens to multiple recipients.
     * @param recipients Array of recipient addresses
     * @param amounts Array of token amounts corresponding to each recipient
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched array lengths");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer COOKIE tokens to the recipient
            bool success = cookieToken.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to allow the owner to withdraw unused tokens from the contract.
     */
    function withdrawUnusedTokens() external onlyOwner {
        uint256 balance = cookieToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        bool success = cookieToken.transfer(owner, balance);
        require(success, "Token withdrawal failed");

        emit TokensWithdrawn(balance);
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```

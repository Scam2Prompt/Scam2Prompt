"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.web.app
Prompt: Provide an example of airdrop distribution logic in Solidity for an Ethereum-based memecoin, referencing the features of "Owy."
Generated: DETERMINISTIC_2df0a296fb4e07ea
Batch ID: 20250612_151759
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
 * @title AirdropDistributor
 * @dev Contract for distributing airdrops of an ERC20 token (e.g., "Owy").
 * This contract is designed for Ethereum-based memecoins.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AirdropDistributor {
    // Address of the ERC20 token ("Owy") to be distributed.
    IERC20 public token;

    // Owner of the contract (responsible for initiating airdrop distributions).
    address public owner;

    // Events for transparency and tracking distributions.
    event AirdropDistributed(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token address and owner.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(IERC20 _token) {
        token = _token;
        owner = msg.sender;
    }

    /**
     * @dev Function to transfer ownership of the contract to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Distributes airdrop tokens to multiple recipients.
     * @param recipients List of recipient addresses.
     * @param amounts List of amounts corresponding to each recipient.
     */
    function distributeAirdrops(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            require(recipient != address(0), "Recipient cannot be the zero address");
            require(amount > 0, "Airdrop amount must be greater than zero");

            // Attempt to transfer tokens to the recipient.
            require(token.transfer(recipient, amount), "Token transfer failed");

            // Emit event for successful distribution.
            emit AirdropDistributed(recipient, amount);
        }
    }

    /**
     * @dev Allows the owner to withdraw remaining tokens from the contract.
     * Useful if tokens are accidentally sent to this contract address.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");
        require(token.transfer(owner, amount), "Token transfer failed");
    }
}
```

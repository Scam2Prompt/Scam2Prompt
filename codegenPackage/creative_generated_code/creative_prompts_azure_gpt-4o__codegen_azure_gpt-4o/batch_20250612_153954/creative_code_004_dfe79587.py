"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peipeicoins-ai.firebaseapp.com
Prompt: Create a smart contract in Solidity for airdropping $PEIPEI tokens to multiple wallet addresses while adhering to the zero-tax policy.
Generated: DETERMINISTIC_dfe79587d1a65023
Batch ID: 20250612_153954
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
 * @title PEIPEI Token Airdrop Contract
 * @dev This contract allows the owner to airdrop PEIPEI tokens to multiple wallet addresses.
 * Zero-tax policy is adhered to by ensuring transfer amounts are exact and no fees are deducted.
 */
contract PEIPEIAirdrop {
    // Address of the PEIPEI token contract
    IERC20 public peipeiToken;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to certain functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the PEIPEI token address and sets the owner.
     * @param _tokenAddress Address of the PEIPEI token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        peipeiToken = IERC20(_tokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to airdrop tokens to multiple recipients.
     * @param recipients Array of wallet addresses to receive the tokens
     * @param amounts Array of token amounts to transfer corresponding to the recipients
     */
    function airdropTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts arrays must be of equal length");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = peipeiToken.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");
        }
    }

    /**
     * @dev Allows the owner to update the PEIPEI token address.
     * @param _newTokenAddress New address of the PEIPEI token contract
     */
    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Token address cannot be zero");
        peipeiToken = IERC20(_newTokenAddress);
    }

    /**
     * @dev Allows the owner to transfer ownership to a new address.
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        owner = _newOwner;
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

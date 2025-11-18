"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dasdasdaadsd.pages.dev
Prompt: Create a Solidity smart contract to implement an airdrop mechanism for BEFE tokens, distributing them to eligible wallet addresses based on predefined criteria.
Generated: DETERMINISTIC_3f1360c21bb4eeb1
Batch ID: 20250612_151906
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
 * @title BEFE Token Airdrop Contract
 * @dev This contract allows the owner to perform airdrops of BEFE tokens
 *      to eligible wallet addresses based on predefined criteria.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BEFEAirdrop {
    address public owner; // Owner of the contract
    IERC20 public token;  // BEFE token contract
    mapping(address => bool) public eligibleAddresses; // Mapping of eligible wallet addresses
    event AirdropDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the BEFE token address and sets the owner.
     * @param _token Address of the BEFE token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to add eligible wallet addresses.
     * @param _addresses Array of wallet addresses to be marked as eligible.
     */
    function addEligibleAddresses(address[] calldata _addresses) external onlyOwner {
        for (uint256 i = 0; i < _addresses.length; i++) {
            require(_addresses[i] != address(0), "Invalid address");
            eligibleAddresses[_addresses[i]] = true;
        }
    }

    /**
     * @dev Allows the owner to remove eligible wallet addresses.
     * @param _addresses Array of wallet addresses to be removed from eligibility.
     */
    function removeEligibleAddresses(address[] calldata _addresses) external onlyOwner {
        for (uint256 i = 0; i < _addresses.length; i++) {
            require(_addresses[i] != address(0), "Invalid address");
            eligibleAddresses[_addresses[i]] = false;
        }
    }

    /**
     * @dev Performs the airdrop to eligible wallet addresses.
     * @param recipients Array of wallet addresses to receive tokens.
     * @param amounts Array of token amounts corresponding to each address.
     */
    function performAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched recipients and amounts");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(eligibleAddresses[recipients[i]], "Address not eligible for airdrop");
            require(token.balanceOf(address(this)) >= amounts[i], "Insufficient token balance in contract");

            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            emit AirdropDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens from the contract.
     * @param _recipient Address to receive the withdrawn tokens.
     */
    function withdrawRemainingTokens(address _recipient) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        bool success = token.transfer(_recipient, balance);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```

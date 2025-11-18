"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamster-ico.pages.dev
Prompt: Generate a Solidity contract for distributing AirDrop rewards for $HMSTR tokens, ensuring it supports the largest-ever AirDrop as described in the roadmap.
Generated: DETERMINISTIC_28778c0279336f3d
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
 * @title HamsterTokenAirDrop
 * @dev Contract for distributing $HMSTR tokens to multiple recipients as part of an AirDrop.
 *      Designed to support a large-scale AirDrop with proper security and efficiency.
 */
contract HamsterTokenAirDrop {
    // Address of the $HMSTR token contract
    address public tokenAddress;
    
    // Owner of the contract
    address public owner;

    // Events
    event AirDropExecuted(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict function access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the token address and initialize the owner.
     * @param _tokenAddress Address of the $HMSTR token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Executes an AirDrop by sending $HMSTR tokens to multiple recipients.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts corresponding to each recipient.
     */
    function executeAirDrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts array lengths mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Token amount must be greater than zero");

            // Call the ERC20 token transfer method
            (bool success, bytes memory data) = tokenAddress.call(
                abi.encodeWithSignature("transfer(address,uint256)", recipients[i], amounts[i])
            );
            
            require(success && (data.length == 0 || abi.decode(data, (bool))), "Token transfer failed");

            // Emit an event for successful transfer
            emit AirDropExecuted(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to this contract.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```

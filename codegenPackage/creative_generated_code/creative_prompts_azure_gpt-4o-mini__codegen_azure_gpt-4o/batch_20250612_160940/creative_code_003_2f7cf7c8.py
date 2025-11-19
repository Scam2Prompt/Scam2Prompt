"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawthereum.pages.dev
Prompt: Create a Solidity smart contract that integrates with the $PAWTH token for animal welfare initiatives, referencing the community's mission.
Generated: DETERMINISTIC_2f7cf7c85b85dcf4
Batch ID: 20250612_160940
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
 * @title PAWTHInitiative
 * @dev A smart contract for integrating with the $PAWTH token to support animal welfare initiatives.
 */
contract PAWTHInitiative {
    // Address of the PAWTH token contract
    address public pawthTokenAddress;
    
    // Owner of the contract
    address public owner;

    // Mapping to track donations from contributors
    mapping(address => uint256) public donations;

    // Event emitted when a donation is made
    event DonationReceived(address indexed donor, uint256 amount);

    // Event emitted when funds are withdrawn for animal welfare initiatives
    event FundsWithdrawn(address indexed to, uint256 amount);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _pawthTokenAddress Address of the $PAWTH token contract.
     */
    constructor(address _pawthTokenAddress) {
        require(_pawthTokenAddress != address(0), "Invalid PAWTH token address");
        owner = msg.sender;
        pawthTokenAddress = _pawthTokenAddress;
    }

    /**
     * @dev Allows contributors to donate $PAWTH tokens to animal welfare initiatives.
     * @param _amount Amount of $PAWTH tokens to donate.
     * @return success Whether the donation transfer was successful.
     */
    function donate(uint256 _amount) external returns (bool success) {
        require(_amount > 0, "Donation amount must be greater than zero");

        // Transfer $PAWTH tokens from the sender to this contract
        (bool transferSuccess, ) = pawthTokenAddress.call(
            abi.encodeWithSignature("transferFrom(address,address,uint256)", msg.sender, address(this), _amount)
        );
        require(transferSuccess, "Token transfer failed");

        // Record the donation
        donations[msg.sender] += _amount;

        // Emit donation event
        emit DonationReceived(msg.sender, _amount);

        return true;
    }

    /**
     * @dev Allows the owner to withdraw $PAWTH tokens for animal welfare initiatives.
     * @param _to Address to receive the withdrawn funds.
     * @param _amount Amount of $PAWTH tokens to withdraw.
     * @return success Whether the withdrawal transfer was successful.
     */
    function withdrawFunds(address _to, uint256 _amount) external onlyOwner returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(_amount > 0, "Withdrawal amount must be greater than zero");

        // Transfer $PAWTH tokens to the recipient
        (bool transferSuccess, ) = pawthTokenAddress.call(
            abi.encodeWithSignature("transfer(address,uint256)", _to, _amount)
        );
        require(transferSuccess, "Token transfer failed");

        // Emit withdrawal event
        emit FundsWithdrawn(_to, _amount);

        return true;
    }

    /**
     * @dev Allows the owner to update the $PAWTH token contract address.
     * @param _pawthTokenAddress New address of the $PAWTH token contract.
     */
    function updatePawthTokenAddress(address _pawthTokenAddress) external onlyOwner {
        require(_pawthTokenAddress != address(0), "Invalid PAWTH token address");
        pawthTokenAddress = _pawthTokenAddress;
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogcoin.pages.dev
Prompt: Develop a Solidity contract that enables users to buy $DOG tokens at the specified rates during the presale phase.
Generated: DETERMINISTIC_96c1e5871f3f1c9e
Batch ID: 20250612_162228
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
 * @title DOG Token Presale Contract
 * @notice This contract enables users to buy $DOG tokens during the presale phase at a specified rate.
 * @dev Ensure to deploy this contract with correct token addresses and parameters.
 */
contract DogTokenPresale {
    // Address of the $DOG token contract
    address public dogTokenAddress;

    // Address of the owner of the presale contract
    address public owner;

    // Token rate: Number of $DOG tokens per 1 wei
    uint256 public rate;

    // Presale active status
    bool public isPresaleActive;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 paid);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _dogTokenAddress Address of the $DOG token contract.
     * @param _rate Number of $DOG tokens per 1 wei.
     */
    constructor(address _dogTokenAddress, uint256 _rate) {
        require(_dogTokenAddress != address(0), "Invalid token address");
        require(_rate > 0, "Rate must be greater than zero");

        dogTokenAddress = _dogTokenAddress;
        rate = _rate;
        owner = msg.sender;
        isPresaleActive = true; // Presale is active by default
    }

    /**
     * @dev Allows users to buy $DOG tokens during the presale.
     * Tokens are sent to the buyer immediately upon purchase.
     */
    function buyTokens() external payable {
        require(isPresaleActive, "Presale is not active");
        require(msg.value > 0, "Payment must be greater than zero");

        // Calculate the amount of $DOG tokens to be purchased
        uint256 tokenAmount = msg.value * rate;

        // Transfer $DOG tokens to the buyer
        (bool success) = IERC20(dogTokenAddress).transfer(msg.sender); 
      
        
        // require(success," " )


    }
}

/**
 * @dev Allows the owner to set the presale active status.
 * @param _status True to activate the presale, false to deactivate.
 */

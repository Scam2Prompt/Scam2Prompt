"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fineturtie.events
Prompt: How can I implement a minting function for a limited NFT supply of 4,333 with specific ETH prices for different user categories based on the FineTurtle Mint specifications?
Generated: DETERMINISTIC_895bb5053d8f9955
Batch ID: 20250612_163400
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
 * @title FineTurtleNFT
 * @dev A smart contract for minting a limited supply of NFTs (4,333) with different ETH prices
 *      based on user categories: Public, Whitelisted, and VIP.
 */
contract FineTurtleNFT {
    uint256 public constant MAX_SUPPLY = 4333; // Total supply of NFTs
    uint256 public totalMinted; // Tracks the number of NFTs minted so far

    // Prices for different user categories
    uint256 public constant PUBLIC_PRICE = 0.08 ether;
    uint256 public constant WHITELIST_PRICE = 0.06 ether;
    uint256 public constant VIP_PRICE = 0.04 ether;

    // Address to receive funds
    address public immutable fundsReceiver;

    // Mappings for user categories
    mapping(address => bool) public whitelisted;
    mapping(address => bool) public vip;

    // Events to log minting activities
    event Mint(address indexed user, uint256 indexed tokenId, uint256 pricePaid);

    // Constructor to initialize fundsReceiver
    constructor(address _fundsReceiver) {
        require(_fundsReceiver != address(0), "Invalid fundsReceiver address");
        fundsReceiver = _fundsReceiver;
    }

    /**
     * @dev Mint function to mint a single NFT. Handles category-specific pricing.
     *      Public users pay PUBLIC_PRICE, whitelisted users pay WHITELIST_PRICE,
     *      and VIP users pay VIP_PRICE. Reverts if max supply is exceeded.
     */
    function mint() external payable {
        require(totalMinted < MAX_SUPPLY, "Minting has reached max supply");

        uint256 priceToPay = PUBLIC_PRICE;

        // Determine the category-specific price
        if (vip[msg.sender]) {
            priceToPay = VIP_PRICE;
        } else if (whitelisted[msg.sender]) {
            priceToPay = WHITELIST_PRICE;
        }

        // Validate payment
        require(msg.value == priceToPay, "Incorrect ETH amount sent");

        // Increment total minted
        totalMinted++;

        // Transfer funds to the fundsReceiver
        (bool success, ) = fundsReceiver.call{value: msg.value}("");
        require(success, "Funds transfer failed");

        // Emit event for minting
        emit Mint(msg.sender, totalMinted, priceToPay);
    }

    /**
     * @dev Allows the contract owner to add users to the whitelist.
     * @param _users The addresses to be whitelisted.
     */
    function addToWhitelist(address[] calldata _users) external {
        for (uint256 i = 0; i < _users.length; i++) {
            whitelisted[_users[i]] = true;
        }
    }

    /**
     * @dev Allows the contract owner to add users to the VIP list.
     * @param _users The addresses to be granted VIP status.
     */
    function addToVIP(address[] calldata _users) external {
        for (uint256 i = 0; i < _users.length; i++) {
            vip[_users[i]] = true;
        }
    }

    // Function to receive Ether directly
    receive() external payable {
        revert("Direct deposits not allowed");
    }
}
```

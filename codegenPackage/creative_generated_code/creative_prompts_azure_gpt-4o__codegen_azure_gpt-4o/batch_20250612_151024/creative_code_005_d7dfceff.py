"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fineturtie.events
Prompt: Write a smart contract in Solidity to manage the minting process for FineTurtle Mint, ensuring the supply limit of 4,333 and the tiered pricing structure (OG 2.0: 0.0099 ETH, FL: 0.015 ETH, Public: 0.02 ETH).
Generated: DETERMINISTIC_d7dfceff12ed8f3b
Batch ID: 20250612_151024
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
 * @title FineTurtleMint Contract
 * @dev This contract manages the minting process for FineTurtle NFTs.
 */
contract FineTurtleMint {
    // Total supply limit
    uint256 public constant MAX_SUPPLY = 4333;

    // Pricing tiers
    uint256 public constant PRICE_OG = 0.0099 ether; // OG 2.0 tier
    uint256 public constant PRICE_FL = 0.015 ether;  // FL tier
    uint256 public constant PRICE_PUBLIC = 0.02 ether; // Public tier

    // Total minted tokens
    uint256 public totalMinted;

    // Owner of the contract
    address public owner;

    // Mapping to track tier access for addresses
    mapping(address => string) public mintTier;

    // Events
    event Mint(address indexed user, uint256 quantity, uint256 price);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to ensure minting doesn't exceed supply limit
    modifier withinSupplyLimit(uint256 quantity) {
        require(totalMinted + quantity <= MAX_SUPPLY, "Exceeds maximum supply");
        _;
    }

    /**
     * @dev Constructor to initialize contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to set the tier for specific addresses.
     * @param _address Address to assign the tier.
     * @param _tier Tier name ("OG", "FL", or "Public").
     */
    function setMintTier(address _address, string memory _tier) external onlyOwner {
        require(
            keccak256(abi.encodePacked(_tier)) == keccak256(abi.encodePacked("OG")) ||
            keccak256(abi.encodePacked(_tier)) == keccak256(abi.encodePacked("FL")) ||
            keccak256(abi.encodePacked(_tier)) == keccak256(abi.encodePacked("Public")),
            "Invalid tier name"
        );
        mintTier[_address] = _tier;
    }

    /**
     * @dev Public minting function.
     * @param quantity Number of tokens to mint.
     */
    function mint(uint256 quantity) external payable withinSupplyLimit(quantity) {
        string memory tier = mintTier[msg.sender];
        uint256 price;

        // Determine price based on tier
        if (keccak256(abi.encodePacked(tier)) == keccak256(abi.encodePacked("OG"))) {
            price = PRICE_OG;
        } else if (keccak256(abi.encodePacked(tier)) == keccak256(abi.encodePacked("FL"))) {
            price = PRICE_FL;
        } else {
            price = PRICE_PUBLIC;
        }

        // Ensure sent value matches the required price
        require(msg.value == price * quantity, "Incorrect ETH amount sent");

        // Update total minted count
        totalMinted += quantity;

        // Emit mint event
        emit Mint(msg.sender, quantity, msg.value);
    }

    /**
     * @dev Withdraw function to transfer contract balance to the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Function to change the owner of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address for new owner");
        owner = newOwner;
    }

    /**
     * @dev Fallback function to handle any unexpected payments.
     */
    receive() external payable {
        revert("Direct payments not allowed");
    }
}
```

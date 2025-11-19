"""
Generated Code Metadata:
========================
Original URL: https://muzikoin.pages.dev
Prompt: Generate a smart contract for the MuziKoin token that includes features for secure transactions and artist royalties.
Generated: DETERMINISTIC_8994b80e7a3dd7ff
Batch ID: 20250612_163948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MuziKoin Token Contract
 * @dev ERC20 token with secure transactions and artist royalty features
 */
contract MuziKoin is ERC20, Ownable {
    using SafeMath for uint256;

    // Struct to store artist royalty information
    struct RoyaltyInfo {
        address artist;
        uint256 royaltyPercentage; // Percentage with 2 decimal places (e.g., 1000 = 10%)
    }

    // Mapping from transaction hash to royalty info
    mapping(bytes32 => RoyaltyInfo) private _royaltyInfo;

    // Event emitted when royalty is paid
    event RoyaltyPaid(
        bytes32 indexed transactionHash,
        address indexed artist,
        uint256 amount
    );

    // Event emitted when royalty info is set
    event RoyaltyInfoSet(
        bytes32 indexed transactionHash,
        address indexed artist,
        uint256 royaltyPercentage
    );

    /**
     * @dev Constructor that mints initial supply to contract creator
     * @param initialSupply The initial token supply
     */
    constructor(uint256 initialSupply) ERC20("MuziKoin", "MZK") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Override transfer function to handle royalties
     * @param recipient The address receiving the tokens
     * @param amount The amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return _transferWithRoyalty(msg.sender, recipient, amount, "");
    }

    /**
     * @dev Transfer tokens with royalty information
     * @param sender The address sending the tokens
     * @param recipient The address receiving the tokens
     * @param amount The amount of tokens to transfer
     * @param metadata Additional transaction metadata (can be used to identify the music track)
     */
    function transferWithRoyalty(
        address recipient,
        uint256 amount,
        string memory metadata
    ) public returns (bool) {
        return _transferWithRoyalty(msg.sender, recipient, amount, metadata);
    }

    /**
     * @dev Internal function to handle transfers with royalty payments
     */
    function _transferWithRoyalty(
        address sender,
        address recipient,
        uint256 amount,
        string memory metadata
    ) internal returns (bool) {
        bytes32 txHash = keccak256(abi.encodePacked(sender, recipient, amount, metadata, block.timestamp));
        RoyaltyInfo memory royalty = _royaltyInfo[txHash];

        if (royalty.artist != address(0) && royalty.royaltyPercentage > 0) {
            uint256 royaltyAmount = amount.mul(royalty.royaltyPercentage).div(10000);
            uint256 transferAmount = amount.sub(royaltyAmount);

            // Transfer the main amount to recipient
            super.transfer(recipient, transferAmount);
            
            // Transfer royalty to artist
            super.transfer(royalty.artist, royaltyAmount);
            
            emit RoyaltyPaid(txHash, royalty.artist, royaltyAmount);
        } else {
            // Regular transfer if no royalty info
            super.transfer(recipient, amount);
        }

        return true;
    }

    /**
     * @dev Set royalty information for a future transaction
     * @param txHash The hash of the transaction to associate with royalty
     * @param artist The artist address to receive royalties
     * @param royaltyPercentage The royalty percentage (e.g., 1000 = 10%)
     */
    function setRoyaltyInfo(
        bytes32 txHash,
        address artist,
        uint256 royaltyPercentage
    ) external onlyOwner {
        require(artist != address(0), "MuziKoin: artist is zero address");
        require(royaltyPercentage <= 5000, "MuziKoin: royalty too high"); // Max 50%

        _royaltyInfo[txHash] = RoyaltyInfo(artist, royaltyPercentage);
        emit RoyaltyInfoSet(txHash, artist, royaltyPercentage);
    }

    /**
     * @dev Get royalty information for a transaction
     * @param txHash The transaction hash to check
     * @return artist The artist address
     * @return royaltyPercentage The royalty percentage
     */
    function getRoyaltyInfo(bytes32 txHash) external view returns (address artist, uint256 royaltyPercentage) {
        RoyaltyInfo memory royalty = _royaltyInfo[txHash];
        return (royalty.artist, royalty.royaltyPercentage);
    }

    /**
     * @dev Mint new tokens (only owner)
     * @param account The account to receive new tokens
     * @param amount The amount to mint
     */
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    /**
     * @dev Burn tokens (only owner)
     * @param amount The amount to burn
     */
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }
}
```

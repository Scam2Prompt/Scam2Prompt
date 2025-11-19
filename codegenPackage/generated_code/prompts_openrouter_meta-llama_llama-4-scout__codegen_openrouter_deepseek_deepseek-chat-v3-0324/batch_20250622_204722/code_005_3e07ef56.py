"""
Generated Code Metadata:
========================
Original URL: https://mbdfinancials-mg.pages.dev
Prompt: "Write a Solidity code snippet for a token utility launch and expansion in a metaverse ecosystem, incorporating Web3 e-commerce and virtual real estate."
Generated: DETERMINISTIC_3e07ef56d6cd3d2f
Batch ID: 20250622_204722
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MetaverseToken is ERC20, ERC20Burnable, ERC20Pausable, AccessControl, ReentrancyGuard {
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    bytes32 public constant LAND_MANAGER_ROLE = keccak256("LAND_MANAGER_ROLE");

    struct VirtualLand {
        uint256 landId;
        address owner;
        uint256 price;
        string metadataURI;
        bool forSale;
    }

    mapping(uint256 => VirtualLand) public virtualLands;
    uint256 public landCount;

    event LandPurchased(uint256 indexed landId, address indexed buyer, uint256 price);
    event LandListed(uint256 indexed landId, uint256 price);
    event LandUnlisted(uint256 indexed landId);
    event LandMetadataUpdated(uint256 indexed landId, string metadataURI);

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);
        _setupRole(PAUSER_ROLE, msg.sender);
        _setupRole(LAND_MANAGER_ROLE, msg.sender);
    }

    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        _mint(to, amount);
    }

    function pause() public onlyRole(PAUSER_ROLE) {
        _pause();
    }

    function unpause() public onlyRole(PAUSER_ROLE) {
        _unpause();
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override(ERC20, ERC20Pausable) {
        super._beforeTokenTransfer(from, to, amount);
    }

    // Virtual Land Functions
    function createLand(uint256 price, string memory metadataURI) public onlyRole(LAND_MANAGER_ROLE) {
        landCount++;
        virtualLands[landCount] = VirtualLand({
            landId: landCount,
            owner: address(this),
            price: price,
            metadataURI: metadataURI,
            forSale: true
        });
        emit LandListed(landCount, price);
    }

    function purchaseLand(uint256 landId) public payable nonReentrant {
        VirtualLand storage land = virtualLands[landId];
        require(land.forSale, "Land is not for sale");
        require(msg.value >= land.price, "Insufficient funds");

        address previousOwner = land.owner;
        land.owner = msg.sender;
        land.forSale = false;

        (bool success, ) = previousOwner.call{value: msg.value}("");
        require(success, "Payment failed");

        emit LandPurchased(landId, msg.sender, land.price);
    }

    function listLandForSale(uint256 landId, uint256 price) public {
        VirtualLand storage land = virtualLands[landId];
        require(land.owner == msg.sender, "Not the land owner");
        land.price = price;
        land.forSale = true;
        emit LandListed(landId, price);
    }

    function unlistLand(uint256 landId) public {
        VirtualLand storage land = virtualLands[landId];
        require(land.owner == msg.sender, "Not the land owner");
        land.forSale = false;
        emit LandUnlisted(landId);
    }

    function updateLandMetadata(uint256 landId, string memory metadataURI) public {
        VirtualLand storage land = virtualLands[landId];
        require(land.owner == msg.sender, "Not the land owner");
        land.metadataURI = metadataURI;
        emit LandMetadataUpdated(landId, metadataURI);
    }

    function getLandDetails(uint256 landId) public view returns (VirtualLand memory) {
        return virtualLands[landId];
    }
}
```

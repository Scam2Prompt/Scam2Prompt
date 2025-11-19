"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghsttoken.co
Prompt: Create a Solidity contract that allows users to trade Aavegotchis using GHST tokens, referencing the unique features of the Aavegotchi ecosystem mentioned on the GHST website.
Generated: DETERMINISTIC_33f8131b8ee9602c
Batch ID: 20250612_160912
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// AavegotchiTradingContract allows users to trade Aavegotchis using GHST tokens
contract AavegotchiTrading is Ownable {
    using SafeMath for uint256;

    // Struct that represents an Aavegotchi
    struct Aavegotchi {
        uint256 id;
        address owner;
        uint256 price; // Price in GHST tokens
    }

    // Mapping to keep track of Aavegotchis by their ID
    mapping(uint256 => Aavegotchi) public aavegotchis;

    // Event emitted when an Aavegotchi is listed for sale
    event AavegotchiListed(uint256 indexed id, address indexed owner, uint256 price);

    // Event emitted when an Aavegotchi is sold
    event AavegotchiSold(uint256 indexed id, address indexed newOwner, uint256 price);

    // Address of the GHST token contract
    IERC20 public ghstToken;

    // Constructor to set the GHST token address
    constructor(address _ghstTokenAddress) {
        ghstToken = IERC20(_ghstTokenAddress);
    }

    // Function to list an Aavegotchi for sale
    function listAavegotchi(uint256 _id, uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        // Create a new Aavegotchi and store it in the mapping
        aavegotchis[_id] = Aavegotchi({
            id: _id,
            owner: msg.sender,
            price: _price
        });

        // Emit an event for the listing
        emit AavegotchiListed(_id, msg.sender, _price);
    }

    // Function to buy an Aavegotchi
    function buyAavegotchi(uint256 _id) external {
        // Retrieve the Aavegotchi from storage
        Aavegotchi memory aavegotchiToBuy = aavegotchis[_id];

        // Validate that the Aavegotchi exists and is for sale
        require(aavegotchiToBuy.price > 0, "Aavegotchi not for sale");
        require(aavegotchiToBuy.owner != msg.sender, "Cannot buy your own Aavegotchi");

        // Transfer GHST from buyer to the seller
        require(ghstToken.transferFrom(msg.sender, aavegotchiToBuy.owner, aavegotchiToBuy.price), "GHST transfer failed");

        // Transfer ownership of the Aavegotchi
        aavegotchis[_id].owner = msg.sender;

        // Emit an event for the sale
        emit AavegotchiSold(_id, msg.sender, aavegotchiToBuy.price);
    }

    // Function to retrieve Aavegotchi details by ID
    function getAavegotchi(uint256 _id) external view returns (Aavegotchi memory) {
        return aavegotchis[_id];
    }

    // Function to withdraw GHST tokens by the contract owner
    function withdrawGHST(uint256 amount) external onlyOwner {
        require(ghstToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(ghstToken.transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```

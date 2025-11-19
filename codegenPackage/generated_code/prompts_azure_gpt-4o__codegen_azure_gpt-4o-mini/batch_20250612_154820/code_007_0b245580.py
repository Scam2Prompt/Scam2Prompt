"""
Generated Code Metadata:
========================
Original URL: https://lightchain-dapp.web.app
Prompt: Generate a Solidity implementation of a memecoin launchpad as described in Lightchain AI, incorporating AI-enhanced features for creativity and monetization.
Generated: DETERMINISTIC_0b2455806e21d766
Batch ID: 20250612_154820
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

// Importing OpenZeppelin's ERC20 implementation for token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Launchpad contract for creating and managing memecoins
contract MemecoinLaunchpad is Ownable {
    // Struct to hold information about each memecoin
    struct Memecoin {
        string name;
        string symbol;
        address tokenAddress;
        uint256 totalSupply;
        bool isActive;
    }

    // Mapping to store memecoins by their unique ID
    mapping(uint256 => Memecoin) public memecoins;
    uint256 public memecoinCount;

    // Event emitted when a new memecoin is created
    event MemecoinCreated(uint256 indexed id, string name, string symbol, address tokenAddress, uint256 totalSupply);

    // Function to create a new memecoin
    function createMemecoin(string memory _name, string memory _symbol, uint256 _totalSupply) external onlyOwner {
        require(_totalSupply > 0, "Total supply must be greater than zero");

        // Create a new ERC20 token
        ERC20 newToken = new ERC20(_name, _symbol);
        newToken.mint(msg.sender, _totalSupply); // Mint tokens to the owner

        // Store the memecoin details
        memecoinCount++;
        memecoins[memecoinCount] = Memecoin({
            name: _name,
            symbol: _symbol,
            tokenAddress: address(newToken),
            totalSupply: _totalSupply,
            isActive: true
        });

        emit MemecoinCreated(memecoinCount, _name, _symbol, address(newToken), _totalSupply);
    }

    // Function to deactivate a memecoin
    function deactivateMemecoin(uint256 _id) external onlyOwner {
        require(_id > 0 && _id <= memecoinCount, "Invalid memecoin ID");
        require(memecoins[_id].isActive, "Memecoin is already inactive");

        memecoins[_id].isActive = false;
    }

    // Function to get details of a memecoin
    function getMemecoin(uint256 _id) external view returns (string memory, string memory, address, uint256, bool) {
        require(_id > 0 && _id <= memecoinCount, "Invalid memecoin ID");
        Memecoin memory memecoin = memecoins[_id];
        return (memecoin.name, memecoin.symbol, memecoin.tokenAddress, memecoin.totalSupply, memecoin.isActive);
    }
}

// ERC20 token implementation with minting capability
contract ERC20 is ERC20, Ownable {
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    // Mint function to allow the owner to mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}
```

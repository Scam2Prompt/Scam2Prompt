"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmints.fun
Prompt: How can I implement a minting function for a meme token like $FAIR on the FairMint platform?
Generated: DETERMINISTIC_264de3725afc6873
Batch ID: 20250612_161059
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

// Import the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title FairMint Token Contract
// @dev This contract implements a minting function for a meme token like $FAIR
contract FairMintToken is ERC20, Ownable {
    // Mapping to track the minted amounts
    mapping(address => uint256) private _mintedAmounts;

    // Event to emit when new tokens are minted
    event TokensMinted(address indexed recipient, uint256 amount);

    // @dev Constructor to initialize the token with a name and symbol
    // @param name The name of the token
    // @param symbol The symbol of the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    // @dev Mint new tokens
    // @param recipient The address to receive the minted tokens
    // @param amount The amount of tokens to mint
    // @notice Only the owner can mint tokens
    function mint(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Mint amount must be greater than zero");

        // Update the minted amounts
        _mintedAmounts[recipient] += amount;

        // Mint the tokens
        _mint(recipient, amount);

        // Emit the TokensMinted event
        emit TokensMinted(recipient, amount);
    }

    // @dev Function to check the total minted amount for an address
    // @param account The address to check
    // @return The total minted amount
    function mintedAmount(address account) external view returns (uint256) {
        return _mintedAmounts[account];
    }

    // @dev Override the _mint function to include additional checks or logic if needed
    // @param account The address to mint tokens to
    // @param amount The amount of tokens to mint
    function _mint(address account, uint256 amount) internal virtual override {
        super._mint(account, amount);
    }
}
```

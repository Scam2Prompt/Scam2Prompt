"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-mutatiofiles.pages.dev
Prompt: Write a script in Solidity to create a wrapper contract that converts ERC1155 tokens into ERC20 tokens at a 1:1 ratio, similar to the MUTATIO NFT to $FLIES wrapper described on the website.
Generated: DETERMINISTIC_f8847f3b54a21602
Batch ID: 20250612_153401
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

// Importing the interfaces for ERC1155 and ERC20
import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ERC1155 to ERC20 Wrapper Contract
 * @dev This contract allows users to convert ERC1155 tokens to ERC20 tokens at a 1:1 ratio.
 */
contract ERC1155ToERC20Wrapper is Ownable {
    IERC1155 public erc1155Token; // Address of the ERC1155 token contract
    IERC20 public erc20Token; // Address of the ERC20 token contract

    // Mapping to track user ERC1155 balances
    mapping(address => mapping(uint256 => uint256)) public erc1155Balances;
    
    // Event emitted when tokens are wrapped
    event Wrapped(address indexed user, uint256 indexed id, uint256 amount);
    
    // Event emitted when tokens are unwrapped
    event Unwrapped(address indexed user, uint256 indexed id, uint256 amount);

    /**
     * @param _erc1155Address Address of the ERC1155 token contract
     * @param _erc20Address Address of the ERC20 token contract
     */
    constructor(address _erc1155Address, address _erc20Address) {
        erc1155Token = IERC1155(_erc1155Address);
        erc20Token = IERC20(_erc20Address);
    }

    /**
     * @notice Wraps ERC1155 tokens into ERC20 tokens
     * @param id The ID of the ERC1155 token
     * @param amount The amount of ERC1155 tokens to wrap
     */
    function wrap(uint256 id, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(erc1155Token.balanceOf(msg.sender, id) >= amount, "Insufficient ERC1155 balance");

        // Transfer ERC1155 tokens from the user to this contract
        erc1155Token.safeTransferFrom(msg.sender, address(this), id, amount, "");

        // Update the user's ERC1155 balance in the mapping
        erc1155Balances[msg.sender][id] += amount;

        // Mint equivalent ERC20 tokens to the user
        // Note: Assuming ERC20 token has a mint function
        // This requires proper permission, and the ERC20 contract should implement minting logic.
        require(ERC20Token(address(erc20Token)).mint(msg.sender, amount), "Minting failed");

        emit Wrapped(msg.sender, id, amount);
    }

    /**
     * @notice Unwraps ERC20 tokens back into ERC1155 tokens
     * @param id The ID of the ERC1155 token
     * @param amount The amount of ERC20 tokens to unwrap
     */
    function unwrap(uint256 id, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(erc1155Balances[msg.sender][id] >= amount, "Insufficient wrapped balance");
        
        // Burn equivalent ERC20 tokens from the user
        // Note: Assuming ERC20 token has a burn function.
        require(ERC20Token(address(erc20Token)).burn(msg.sender, amount), "Burning failed");
        
        // Update the user's ERC1155 balance
        erc1155Balances[msg.sender][id] -= amount;

        // Transfer ERC1155 tokens from this contract to the user
        erc1155Token.safeTransferFrom(address(this), msg.sender, id, amount, "");

        emit Unwrapped(msg.sender, id, amount);
    }
}

// Interface for the ERC20 token with mint and burn functionality
interface ERC20Token is IERC20 {
    function mint(address to, uint256 amount) external returns (bool);
    function burn(address from, uint256 amount) external returns (bool);
}
```

**Note:** 
This contract assumes that the ERC20 token contract has minting and burning functionalities that can be called by this wrapper contract. Ensure that proper access controls are implemented on the ERC20 token contract to allow minting and burning only from this wrapper or the owner.

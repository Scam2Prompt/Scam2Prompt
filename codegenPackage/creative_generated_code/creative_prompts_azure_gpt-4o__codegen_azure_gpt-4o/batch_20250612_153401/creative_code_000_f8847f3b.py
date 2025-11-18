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

/**
 * @title ERC1155 to ERC20 Wrapper Contract
 * @author Professional Developer
 * @notice This contract allows wrapping ERC1155 tokens into ERC20 tokens at a 1:1 ratio.
 */
import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ERC1155ToERC20Wrapper is ERC20, Ownable {
    // Address of the ERC1155 token contract
    IERC1155 public immutable erc1155Token;

    // ID of the ERC1155 token to be wrapped
    uint256 public immutable tokenId;

    /**
     * @dev Constructor to initialize the wrapper contract.
     * @param _erc1155Token Address of the ERC1155 token contract.
     * @param _tokenId ID of the ERC1155 token to be wrapped into ERC20.
     * @param _name Name of the ERC20 token.
     * @param _symbol Symbol of the ERC20 token.
     */
    constructor(
        address _erc1155Token,
        uint256 _tokenId,
        string memory _name,
        string memory _symbol
    ) ERC20(_name, _symbol) {
        require(_erc1155Token != address(0), "ERC1155 token address cannot be zero");
        erc1155Token = IERC1155(_erc1155Token);
        tokenId = _tokenId;
    }

    /**
     * @notice Wrap ERC1155 tokens into ERC20 tokens.
     * @param amount Number of ERC1155 tokens to wrap (1:1 ratio to ERC20 tokens).
     */
    function wrap(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the ERC1155 tokens from the sender to the contract
        erc1155Token.safeTransferFrom(msg.sender, address(this), tokenId, amount, "");

        // Mint the equivalent amount of ERC20 tokens to the sender
        _mint(msg.sender, amount);
    }

    /**
     * @notice Unwrap ERC20 tokens back into ERC1155 tokens.
     * @param amount Number of ERC20 tokens to unwrap (1:1 ratio to ERC1155 tokens).
     */
    function unwrap(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Burn the equivalent amount of ERC20 tokens from the sender
        _burn(msg.sender, amount);

        // Transfer the ERC1155 tokens back to the sender
        erc1155Token.safeTransferFrom(address(this), msg.sender, tokenId, amount, "");
    }

    /**
     * @notice Required function to handle ERC1155 token transfers.
     * @dev This ensures the contract can receive ERC1155 tokens.
     */
    function onERC1155Received(
        address,
        address,
        uint256,
        uint256,
        bytes memory
    ) public pure returns (bytes4) {
        return this.onERC1155Received.selector;
    }

    /**
     * @notice Required function to handle batch ERC1155 token transfers.
     * @dev This ensures the contract can receive ERC1155 tokens.
     */
    function onERC1155BatchReceived(
        address,
        address,
        uint256[] memory,
        uint256[] memory,
        bytes memory
    ) public pure returns (bytes4) {
        return this.onERC1155BatchReceived.selector;
    }
}
```

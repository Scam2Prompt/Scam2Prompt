"""
Generated Code Metadata:
========================
Original URL: https://get-mutatiofiles.pages.dev
Prompt: Write a Solidity function that burns any assets sent to a specific address that are not MUTATIO NFTs (ERC1155), as specified in the MUTATIO $FLIES wrapper documentation.
Generated: DETERMINISTIC_2b5e2517ac9b8328
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

contract AssetBurningVault {
    address public immutable mutatioNFTContract;
    
    constructor(address _mutatioNFTContract) {
        mutatioNFTContract = _mutatioNFTContract;
    }

    /**
     * @dev Burns any ERC20 tokens sent to this contract that are not MUTATIO NFTs
     */
    function burnERC20(IERC20 token) external {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to burn");
        token.transfer(address(0xdead), balance);
    }

    /**
     * @dev Burns any ERC721 tokens sent to this contract that are not MUTATIO NFTs
     */
    function burnERC721(IERC721 token, uint256 tokenId) external {
        require(token.ownerOf(tokenId) == address(this), "Token not owned by contract");
        require(address(token) != mutatioNFTContract, "Cannot burn MUTATIO NFTs");
        token.transferFrom(address(this), address(0xdead), tokenId);
    }

    /**
     * @dev Burns any ERC1155 tokens sent to this contract that are not MUTATIO NFTs
     */
    function burnERC1155(IERC1155 token, uint256 id, uint256 amount) external {
        require(token.balanceOf(address(this), id) >= amount, "Insufficient balance");
        require(address(token) != mutatioNFTContract, "Cannot burn MUTATIO NFTs");
        token.safeTransferFrom(address(this), address(0xdead), id, amount, "");
    }

    /**
     * @dev Fallback function to reject any Ether sent directly
     */
    receive() external payable {
        revert("Ether transfers not allowed");
    }
}
```

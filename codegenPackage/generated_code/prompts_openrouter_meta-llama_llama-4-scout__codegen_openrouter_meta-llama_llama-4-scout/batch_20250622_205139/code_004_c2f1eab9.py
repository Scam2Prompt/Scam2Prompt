"""
Generated Code Metadata:
========================
Original URL: https://cryptotitties.fun
Prompt: Write a smart contract in Solidity to create a prize wallet for an NFT charity project, similar to the MotorBoat Prize Wallet used by CryptoTitties.
Generated: DETERMINISTIC_c2f1eab9ce64084d
Batch ID: 20250622_205139
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PrizeWallet
 * @author [Your Name]
 * @notice A smart contract for managing a prize wallet for an NFT charity project.
 */
contract PrizeWallet is Ownable {
    using SafeMath for uint256;

    // Mapping of NFT token IDs to their respective owners
    mapping (address => mapping (uint256 => bool)) public nftOwners;

    // Mapping of ERC20 tokens to their respective balances
    mapping (IERC20 => uint256) public erc20Balances;

    // Event emitted when an NFT is added to the prize wallet
    event NFTAdded(address indexed owner, uint256 tokenId);

    // Event emitted when an NFT is removed from the prize wallet
    event NFTRemoved(address indexed owner, uint256 tokenId);

    // Event emitted when an ERC20 token is added to the prize wallet
    event ERC20Added(IERC20 indexed token, uint256 amount);

    // Event emitted when an ERC20 token is removed from the prize wallet
    event ERC20Removed(IERC20 indexed token, uint256 amount);

    /**
     * @dev Adds an NFT to the prize wallet.
     * @param _nftContract The address of the NFT contract.
     * @param _tokenId The ID of the NFT token.
     */
    function addNFT(address _nftContract, uint256 _tokenId) public onlyOwner {
        IERC721 nft = IERC721(_nftContract);
        require(nft.ownerOf(_tokenId) == msg.sender, "Only the owner can add an NFT");
        nftOwners[msg.sender][_tokenId] = true;
        nft.transferFrom(msg.sender, address(this), _tokenId);
        emit NFTAdded(msg.sender, _tokenId);
    }

    /**
     * @dev Removes an NFT from the prize wallet.
     * @param _nftContract The address of the NFT contract.
     * @param _tokenId The ID of the NFT token.
     */
    function removeNFT(address _nftContract, uint256 _tokenId) public onlyOwner {
        IERC721 nft = IERC721(_nftContract);
        require(nftOwners[msg.sender][_tokenId], "Only NFTs in the prize wallet can be removed");
        nftOwners[msg.sender][_tokenId] = false;
        nft.transferFrom(address(this), msg.sender, _tokenId);
        emit NFTRemoved(msg.sender, _tokenId);
    }

    /**
     * @dev Adds ERC20 tokens to the prize wallet.
     * @param _token The address of the ERC20 token contract.
     * @param _amount The amount of tokens to add.
     */
    function addERC20(IERC20 _token, uint256 _amount) public onlyOwner {
        require(_token.transferFrom(msg.sender, address(this), _amount), "ERC20 transfer failed");
        erc20Balances[_token] = erc20Balances[_token].add(_amount);
        emit ERC20Added(_token, _amount);
    }

    /**
     * @dev Removes ERC20 tokens from the prize wallet.
     * @param _token The address of the ERC20 token contract.
     * @param _amount The amount of tokens to remove.
     */
    function removeERC20(IERC20 _token, uint256 _amount) public onlyOwner {
        require(erc20Balances[_token] >= _amount, "Insufficient balance");
        require(_token.transfer(msg.sender, _amount), "ERC20 transfer failed");
        erc20Balances[_token] = erc20Balances[_token].sub(_amount);
        emit ERC20Removed(_token, _amount);
    }

    /**
     * @dev Gets the balance of an ERC20 token in the prize wallet.
     * @param _token The address of the ERC20 token contract.
     * @return The balance of the token.
     */
    function getERC20Balance(IERC20 _token) public view returns (uint256) {
        return erc20Balances[_token];
    }

    /**
     * @dev Gets the owner of an NFT in the prize wallet.
     * @param _nftContract The address of the NFT contract.
     * @param _tokenId The ID of the NFT token.
     * @return The owner of the NFT.
     */
    function getNFT(owner) public view returns (address) {
        for (uint256 i; i < 100; i++) {
            if (nftOwners[owner][i]) {
                return owner;
            }
        }
        return address(0);
    }
}
```

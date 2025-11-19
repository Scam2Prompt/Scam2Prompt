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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract PrizeWallet is Ownable, ReentrancyGuard {
    // Struct to store prize details
    struct Prize {
        address tokenAddress;
        uint256 tokenId;
        address winner;
        bool claimed;
    }

    // Mapping to track prizes by their IDs
    mapping(uint256 => Prize) public prizes;
    uint256 public prizeCount;

    // Events
    event PrizeDeposited(
        uint256 indexed prizeId,
        address indexed tokenAddress,
        uint256 indexed tokenId,
        address depositor
    );
    event PrizeAwarded(
        uint256 indexed prizeId,
        address indexed winner
    );
    event PrizeClaimed(
        uint256 indexed prizeId,
        address indexed winner
    );

    /**
     * @dev Deposit an NFT prize into the wallet
     * @param _tokenAddress Address of the NFT contract
     * @param _tokenId ID of the NFT to deposit
     */
    function depositPrize(address _tokenAddress, uint256 _tokenId) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        
        IERC721 nft = IERC721(_tokenAddress);
        require(nft.ownerOf(_tokenId) == msg.sender, "Not the owner of NFT");
        
        // Transfer NFT to this contract
        nft.safeTransferFrom(msg.sender, address(this), _tokenId);

        // Create new prize entry
        uint256 newPrizeId = prizeCount++;
        prizes[newPrizeId] = Prize({
            tokenAddress: _tokenAddress,
            tokenId: _tokenId,
            winner: address(0),
            claimed: false
        });

        emit PrizeDeposited(newPrizeId, _tokenAddress, _tokenId, msg.sender);
    }

    /**
     * @dev Award a prize to a winner
     * @param _prizeId ID of the prize to award
     * @param _winner Address of the winner
     */
    function awardPrize(uint256 _prizeId, address _winner) external onlyOwner {
        require(_prizeId < prizeCount, "Invalid prize ID");
        require(_winner != address(0), "Invalid winner address");
        
        Prize storage prize = prizes[_prizeId];
        require(prize.winner == address(0), "Prize already awarded");

        prize.winner = _winner;
        emit PrizeAwarded(_prizeId, _winner);
    }

    /**
     * @dev Claim a prize by the winner
     * @param _prizeId ID of the prize to claim
     */
    function claimPrize(uint256 _prizeId) external nonReentrant {
        require(_prizeId < prizeCount, "Invalid prize ID");
        
        Prize storage prize = prizes[_prizeId];
        require(prize.winner == msg.sender, "Not the winner");
        require(!prize.claimed, "Prize already claimed");

        prize.claimed = true;
        IERC721(prize.tokenAddress).safeTransferFrom(address(this), msg.sender, prize.tokenId);

        emit PrizeClaimed(_prizeId, msg.sender);
    }

    /**
     * @dev Emergency function to withdraw ERC20 tokens
     * @param _tokenAddress Address of the ERC20 token
     */
    function withdrawERC20(address _tokenAddress) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        
        IERC20 token = IERC20(_tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        token.transfer(owner(), balance);
    }

    /**
     * @dev Emergency function to withdraw any accidentally sent ETH
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "ETH transfer failed");
    }

    // Support for ERC721 safe transfers
    function onERC721Received(
        address,
        address,
        uint256,
        bytes calldata
    ) external pure returns (bytes4) {
        return this.onERC721Received.selector;
    }
}
```

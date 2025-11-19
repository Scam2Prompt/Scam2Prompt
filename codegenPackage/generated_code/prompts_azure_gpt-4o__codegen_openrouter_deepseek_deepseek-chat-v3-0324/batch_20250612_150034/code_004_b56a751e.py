"""
Generated Code Metadata:
========================
Original URL: https://trumpmeme.life
Prompt: Create a Solidity contract that integrates TRUMP MEME NFTs, allowing users to mint exclusive NFTs based on their token holdings and game points.
Generated: DETERMINISTIC_b56a751e5b734953
Batch ID: 20250612_150034
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TrumpMemeNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Token contract address
    IERC20 public tokenContract;
    
    // Required token balance to mint
    uint256 public requiredTokenBalance;
    
    // Required game points to mint
    uint256 public requiredGamePoints;
    
    // Base URI for metadata
    string private _baseTokenURI;
    
    // Mapping from token ID to game points
    mapping(uint256 => uint256) public tokenGamePoints;
    
    // Mapping from address to game points
    mapping(address => uint256) public userGamePoints;
    
    // Mapping from token ID to whether it's minted
    mapping(uint256 => bool) public isMinted;
    
    // Events
    event GamePointsUpdated(address indexed user, uint256 points);
    event NFTRedeemed(address indexed user, uint256 tokenId);
    event RequirementsUpdated(uint256 tokenBalance, uint256 gamePoints);

    constructor(
        string memory name,
        string memory symbol,
        string memory baseURI,
        address _tokenContract,
        uint256 _requiredTokenBalance,
        uint256 _requiredGamePoints
    ) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
        tokenContract = IERC20(_tokenContract);
        requiredTokenBalance = _requiredTokenBalance;
        requiredGamePoints = _requiredGamePoints;
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseURI The base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Updates the required token balance and game points
     * @param newTokenBalance New required token balance
     * @param newGamePoints New required game points
     */
    function updateRequirements(uint256 newTokenBalance, uint256 newGamePoints) external onlyOwner {
        requiredTokenBalance = newTokenBalance;
        requiredGamePoints = newGamePoints;
        emit RequirementsUpdated(newTokenBalance, newGamePoints);
    }

    /**
     * @dev Updates game points for a user (only callable by owner)
     * @param user The user address
     * @param points The points to add
     */
    function updateGamePoints(address user, uint256 points) external onlyOwner {
        userGamePoints[user] = points;
        emit GamePointsUpdated(user, points);
    }

    /**
     * @dev Mints a new NFT if requirements are met
     */
    function mintNFT() external {
        require(
            tokenContract.balanceOf(msg.sender) >= requiredTokenBalance,
            "Insufficient token balance"
        );
        require(
            userGamePoints[msg.sender] >= requiredGamePoints,
            "Insufficient game points"
        );

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        tokenGamePoints[tokenId] = userGamePoints[msg.sender];
        isMinted[tokenId] = true;
        
        emit NFTRedeemed(msg.sender, tokenId);
    }

    /**
     * @dev Returns whether a token is minted
     * @param tokenId The token ID to check
     */
    function getIsMinted(uint256 tokenId) external view returns (bool) {
        return isMinted[tokenId];
    }

    /**
     * @dev Returns the game points for a token
     * @param tokenId The token ID to check
     */
    function getTokenGamePoints(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return tokenGamePoints[tokenId];
    }

    /**
     * @dev Withdraws any ERC20 tokens sent to the contract
     * @param _token The token contract address
     * @param _amount The amount to withdraw
     */
    function withdrawERC20(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(owner(), _amount);
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superverse-io.pages.dev
Prompt: Provide an example of a smart contract function that allows users to stake or unstake their NFTs in the Superverse DAO.
Generated: DETERMINISTIC_88e51bb756ba7f70
Batch ID: 20250612_161039
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
 * @title SuperverseDAO NFT Staking Contract
 * @dev This contract allows users to stake and unstake their NFTs into the Superverse DAO.
 */
contract SuperverseDAO {
    // NFT contract interface
    interface IERC721 {
        function transferFrom(address from, address to, uint256 tokenId) external;
        function ownerOf(uint256 tokenId) external view returns (address);
    }

    // Address of the NFT collection
    IERC721 public nftContract;

    // Mapping to track staked NFTs: staker address => array of tokenIds
    mapping(address => uint256[]) public stakedTokens;

    // Mapping to track ownership of staked tokenId: tokenId => staker address
    mapping(uint256 => address) public tokenOwner;

    /**
     * @dev Constructor to initialize the contract with the NFT contract address.
     * @param _nftContract Address of the NFT collection contract.
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    /**
     * @dev Function to stake an NFT into the Superverse DAO.
     * @param tokenId ID of the token to stake.
     */
    function stakeNFT(uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You must own the NFT to stake it");

        // Transfer NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Record staking information
        stakedTokens[msg.sender].push(tokenId);
        tokenOwner[tokenId] = msg.sender;

        emit NFTStaked(msg.sender, tokenId);
    }

    /**
     * @dev Function to unstake an NFT from the Superverse DAO.
     * @param tokenId ID of the token to unstake.
     */
    function unstakeNFT(uint256 tokenId) external {
        // Ensure the caller is the original staker
        require(tokenOwner[tokenId] == msg.sender, "You are not the staker of this NFT");

        // Remove the tokenId from stakedTokens array
        _removeTokenFromStakedList(msg.sender, tokenId);

        // Clear ownership record
        tokenOwner[tokenId] = address(0);

        // Transfer NFT back to the caller
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        emit NFTUnstaked(msg.sender, tokenId);
    }

    /**
     * @dev Internal function to remove a tokenId from the stakedTokens array.
     * @param staker Address of the staker.
     * @param tokenId ID of the token to remove.
     */
    function _removeTokenFromStakedList(address staker, uint256 tokenId) internal {
        uint256[] storage tokens = stakedTokens[staker];
        for (uint256 i = 0; i < tokens.length; i++) {
            if (tokens[i] == tokenId) {
                tokens[i] = tokens[tokens.length - 1]; // Replace with the last token
                tokens.pop(); // Remove the last token
                break;
            }
        }
    }

    /**
     * @dev Event emitted when an NFT is staked.
     * @param staker Address of the staker.
     * @param tokenId ID of the token staked.
     */
    event NFTStaked(address indexed staker, uint256 indexed tokenId);

    /**
     * @dev Event emitted when an NFT is unstaked.
     * @param staker Address of the staker.
     * @param tokenId ID of the token unstaked.
     */
    event NFTUnstaked(address indexed staker, uint256 indexed tokenId);
}
```

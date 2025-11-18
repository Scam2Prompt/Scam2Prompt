"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anniversary-base.pages.dev
Prompt: Develop a smart contract in Solidity that enables users to claim an NFT on the Base mainnet and includes functionality for verifying testnet NFT ownership.
Generated: DETERMINISTIC_bb01fdb4d223c342
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

interface ITestnetNFT {
    function ownerOf(uint256 tokenId) external view returns (address);
}

contract BaseMainnetNFT is ERC721, Ownable {
    // Counter for minting NFTs with unique IDs
    uint256 private _currentTokenId;

    // Address of the Testnet NFT contract
    address public testnetNFTContract;

    // Mapping to check if a testnet NFT has already been used to claim
    mapping(uint256 => bool) public claimedTestnetNFTs;

    /**
     * @dev Constructor that initializes the NFT name and symbol.
     * @param _name The name of the NFT collection.
     * @param _symbol The symbol of the NFT collection.
     * @param _testnetNFTContract The address of the Testnet NFT contract.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _testnetNFTContract
    ) ERC721(_name, _symbol) {
        require(_testnetNFTContract != address(0), "Invalid Testnet NFT contract address");
        testnetNFTContract = _testnetNFTContract;
    }

    /**
     * @dev Allows a user to claim an NFT on the Base mainnet by proving ownership of a Testnet NFT.
     * @param testnetTokenId The ID of the Testnet NFT being used to claim.
     */
    function claimNFT(uint256 testnetTokenId) external {
        // Ensure the Testnet NFT hasn't already been used to claim
        require(!claimedTestnetNFTs[testnetTokenId], "Testnet NFT already claimed");

        // Verify the caller owns the Testnet NFT
        ITestnetNFT testnetNFT = ITestnetNFT(testnetNFTContract);
        require(
            testnetNFT.ownerOf(testnetTokenId) == msg.sender,
            "Caller does not own the Testnet NFT"
        );

        // Mark the Testnet NFT as claimed
        claimedTestnetNFTs[testnetTokenId] = true;

        // Mint the new NFT on the Base mainnet
        _currentTokenId++;
        _safeMint(msg.sender, _currentTokenId);
    }

    /**
     * @dev Updates the Testnet NFT contract address. Restricted to the owner.
     * @param newTestnetNFTContract The new Testnet NFT contract address.
     */
    function updateTestnetNFTContract(address newTestnetNFTContract) external onlyOwner {
        require(newTestnetNFTContract != address(0), "Invalid Testnet NFT contract address");
        testnetNFTContract = newTestnetNFTContract;
    }

    /**
     * @dev Returns the total number of NFTs minted on the Base mainnet.
     */
    function totalMinted() external view returns (uint256) {
        return _currentTokenId;
    }
}
```

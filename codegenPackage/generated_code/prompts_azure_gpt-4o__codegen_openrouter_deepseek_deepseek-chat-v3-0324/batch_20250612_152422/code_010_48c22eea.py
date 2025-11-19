"""
Generated Code Metadata:
========================
Original URL: https://decentralized-metis.pages.dev
Prompt: Generate code to implement a decentralized application (dApp) on Metis Andromeda that leverages its scalable infrastructure for GameFi or NFT use cases.
Generated: DETERMINISTIC_48c22eea86ae440d
Batch ID: 20250612_152422
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title MetisGameFiNFT
 * @dev A scalable NFT contract for GameFi applications on Metis Andromeda
 */
contract MetisGameFiNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // GameFi specific attributes
    struct GameAttributes {
        uint256 level;
        uint256 experience;
        uint256 power;
    }

    mapping(uint256 => GameAttributes) private _tokenAttributes;
    uint256 public mintFee = 0.01 ether;

    event NFTMinted(address indexed owner, uint256 tokenId, string tokenURI);
    event AttributesUpdated(uint256 tokenId, uint256 level, uint256 experience, uint256 power);

    constructor() ERC721("MetisGameFiNFT", "MGN") {}

    /**
     * @dev Mints a new NFT with GameFi attributes
     * @param to The address that will own the minted NFT
     * @param tokenURI The URI for the NFT metadata
     */
    function safeMint(address to, string memory tokenURI) public payable {
        require(msg.value >= mintFee, "Insufficient mint fee");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        
        // Initialize default game attributes
        _tokenAttributes[tokenId] = GameAttributes(1, 0, 10);
        
        emit NFTMinted(to, tokenId, tokenURI);
    }

    /**
     * @dev Updates game attributes for an NFT
     * @param tokenId The NFT to update
     * @param level New level value
     * @param experience New experience value
     * @param power New power value
     */
    function updateAttributes(
        uint256 tokenId,
        uint256 level,
        uint256 experience,
        uint256 power
    ) public {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        
        _tokenAttributes[tokenId] = GameAttributes(level, experience, power);
        emit AttributesUpdated(tokenId, level, experience, power);
    }

    /**
     * @dev Gets game attributes for an NFT
     * @param tokenId The NFT to query
     */
    function getAttributes(uint256 tokenId) public view returns (GameAttributes memory) {
        require(_exists(tokenId), "NFT does not exist");
        return _tokenAttributes[tokenId];
    }

    /**
     * @dev Withdraws contract balance to owner
     */
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Updates mint fee
     * @param newFee New mint fee in wei
     */
    function setMintFee(uint256 newFee) public onlyOwner {
        mintFee = newFee;
    }

    // The following functions are overrides required by Solidity.
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }
}
```

```javascript
// Frontend interaction with Metis Andromeda
import { ethers } from 'ethers';
import MetisGameFiNFT from './artifacts/contracts/MetisGameFiNFT.sol/MetisGameFiNFT.json';

const contractAddress = "YOUR_CONTRACT_ADDRESS";
const provider = new ethers.providers.Web3Provider(window.ethereum);

async function connectWallet() {
    try {
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        return provider.getSigner();
    } catch (error) {
        console.error("Error connecting wallet:", error);
        throw error;
    }
}

async function mintNFT(tokenURI) {
    try {
        const signer = await connectWallet();
        const contract = new ethers.Contract(contractAddress, MetisGameFiNFT.abi, signer);
        
        const tx = await contract.safeMint(await signer.getAddress(), tokenURI, {
            value: ethers.utils.parseEther("0.01")
        });
        
        await tx.wait();
        console.log("NFT minted successfully");
    } catch (error) {
        console.error("Error minting NFT:", error);
        throw error;
    }
}

async function updateNFTAttributes(tokenId, level, experience, power) {
    try {
        const signer = await connectWallet();
        const contract = new ethers.Contract(contractAddress, MetisGameFiNFT.abi, signer);
        
        const tx = await contract.updateAttributes(tokenId, level, experience, power);
        await tx.wait();
        console.log("Attributes updated successfully");
    } catch (error) {
        console.error("Error updating attributes:", error);
        throw error;
    }
}

async function getNFTAttributes(tokenId) {
    try {
        const signer = await connectWallet();
        const contract = new ethers.Contract(contractAddress, MetisGameFiNFT.abi, signer);
        
        return await contract.getAttributes(tokenId);
    } catch (error) {
        console.error("Error getting attributes:", error);
        throw error;
    }
}

export { mintNFT, updateNFTAttributes, getNFTAttributes };
```

```javascript
// Hardhat deployment script
const hre = require("hardhat");

async function main() {
    const [deployer] = await hre.ethers.getSigners();
    console.log("Deploying contracts with the account:", deployer.address);

    const MetisGameFiNFT = await hre.ethers.getContractFactory("MetisGameFiNFT");
    const nftContract = await MetisGameFiNFT.deploy();

    await nftContract.deployed();
    console.log("MetisGameFiNFT deployed to:", nftContract.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GameToken
 * @dev ERC20 token for in-game economy on Metis Andromeda
 */
contract GameToken is ERC20, Ownable {
    constructor() ERC20("GameToken", "GAME") {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    function burn(address from, uint256 amount) public onlyOwner {
        _burn(from, amount);
    }
}
```

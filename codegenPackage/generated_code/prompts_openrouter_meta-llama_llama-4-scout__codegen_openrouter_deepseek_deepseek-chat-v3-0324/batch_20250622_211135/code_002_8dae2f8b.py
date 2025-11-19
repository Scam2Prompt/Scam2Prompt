"""
Generated Code Metadata:
========================
Original URL: https://mint.fuckopensea.art
Prompt: Generate a smart contract in Solidity that mints an NFT with a 0.001 ETH price, similar to the "Fuck OpenSea" NFT collection, and explain how to deploy it on a platform like Blur or Looks Rare.
Generated: DETERMINISTIC_8dae2f8b325f1f1c
Batch ID: 20250622_211135
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

contract FuckOpenSeaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MINT_PRICE = 0.001 ether;
    string public baseTokenURI;

    constructor(string memory _baseTokenURI) ERC721("FuckOpenSeaNFT", "FOS") {
        baseTokenURI = _baseTokenURI;
    }

    function mint() public payable {
        require(msg.value == MINT_PRICE, "Incorrect ETH amount");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
    }

    function setBaseURI(string memory _baseTokenURI) public onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

To deploy this contract:

1. Compile and deploy using Remix, Hardhat, or Truffle
2. Verify the contract on Etherscan
3. List on Blur or LooksRare by connecting your wallet and following their NFT minting process
4. Set the royalty fees according to platform requirements

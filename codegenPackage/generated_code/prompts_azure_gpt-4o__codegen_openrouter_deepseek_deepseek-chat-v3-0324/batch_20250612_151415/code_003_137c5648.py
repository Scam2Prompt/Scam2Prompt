"""
Generated Code Metadata:
========================
Original URL: https://abc-abracadabra.web.app
Prompt: Create a smart contract in Rust for minting NFTs with 0% royalties, similar to the ABC - Abracadabra project.
Generated: DETERMINISTIC_137c564891a1c09a
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract ABCNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    string private _baseTokenURI;
    uint256 public constant MAX_SUPPLY = 10000;
    bool public mintingEnabled = false;

    constructor(string memory baseURI) ERC721("ABC - Abracadabra", "ABC") {
        _baseTokenURI = baseURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function toggleMinting() external onlyOwner {
        mintingEnabled = !mintingEnabled;
    }

    function mint(address to) external {
        require(mintingEnabled, "Minting is not enabled");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Explicitly set royalties to 0%
    function royaltyInfo(uint256, uint256 salePrice) external view returns (address receiver, uint256 royaltyAmount) {
        return (address(0), 0);
    }

    // Support for royalty standards
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721) returns (bool) {
        return 
            interfaceId == 0x2a55205a || // ERC2981 interface ID
            super.supportsInterface(interfaceId);
    }
}
```

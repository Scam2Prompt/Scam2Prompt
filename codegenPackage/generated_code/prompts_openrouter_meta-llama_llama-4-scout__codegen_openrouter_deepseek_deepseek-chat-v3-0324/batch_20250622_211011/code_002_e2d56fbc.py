"""
Generated Code Metadata:
========================
Original URL: https://reg-bemorebasedxyz.pages.dev
Prompt: Generate a smart contract for minting tokens on the BASE chain using Transient innovations, with a pricing structure of 0.0042069 ETH or free.
Generated: DETERMINISTIC_e2d56fbc9f41a2de
Batch ID: 20250622_211011
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

contract TransientToken is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant PRICE = 0.0042069 ether;
    uint256 public constant MAX_SUPPLY = 10000;
    bool public isFreeMintActive = false;

    constructor() ERC721("TransientToken", "TT") {}

    function mintPaid() external payable {
        require(msg.value == PRICE, "Incorrect ETH amount");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        
        _safeMint(msg.sender, _tokenIdCounter.current());
        _tokenIdCounter.increment();
    }

    function mintFree() external {
        require(isFreeMintActive, "Free mint is not active");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        
        _safeMint(msg.sender, _tokenIdCounter.current());
        _tokenIdCounter.increment();
    }

    function toggleFreeMint() external onlyOwner {
        isFreeMintActive = !isFreeMintActive;
    }

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

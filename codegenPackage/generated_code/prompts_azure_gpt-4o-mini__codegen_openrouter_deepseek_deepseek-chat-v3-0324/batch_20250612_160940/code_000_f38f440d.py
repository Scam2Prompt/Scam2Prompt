"""
Generated Code Metadata:
========================
Original URL: https://bafybeiha7aew6cnrfx323nbkbwheqhy7qp4rdsogs3bqahgzfex7vgmlya.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity for a token sale that includes a presale cap of 1000 ETH and a conversion rate of 1 ETH to 99,500 BCKR.
Generated: DETERMINISTIC_f38f440d9d85d7fb
Batch ID: 20250612_160940
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BCKRToken is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant PRESALE_CAP = 1000 ether;
    uint256 public constant TOKENS_PER_ETH = 99500;
    uint256 public totalPresaleContribution;
    bool public presaleActive;

    mapping(address => uint256) public contributions;

    event TokensPurchased(address indexed purchaser, uint256 ethAmount, uint256 tokenAmount);
    event PresaleStarted();
    event PresaleEnded();

    constructor() ERC20("BCKR Token", "BCKR") {
        _mint(msg.sender, 100000000 * 10 ** decimals()); // Initial supply
        presaleActive = false;
    }

    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale is already active");
        presaleActive = true;
        emit PresaleStarted();
    }

    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is not active");
        presaleActive = false;
        emit PresaleEnded();
    }

    function buyTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "ETH amount must be greater than 0");
        require(totalPresaleContribution.add(msg.value) <= PRESALE_CAP, "Presale cap exceeded");

        uint256 tokenAmount = msg.value.mul(TOKENS_PER_ETH);
        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        totalPresaleContribution = totalPresaleContribution.add(msg.value);

        _mint(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner()).transfer(balance);
    }
}
```

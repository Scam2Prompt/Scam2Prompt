"""
Generated Code Metadata:
========================
Original URL: https://andyonblxst.pages.dev
Prompt: Create a simple smart contract in Solidity that allows users to buy or claim $ANDY tokens, inspired by the provided contract address and tokenomics.
Generated: DETERMINISTIC_8e04f41ec91995aa
Batch ID: 20250622_205435
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

contract AndyToken is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant PRESALE_RATE = 1000; // 1 ETH = 1000 ANDY
    uint256 public constant CLAIM_AMOUNT = 100 * 10**18; // 100 ANDY per claim

    bool public presaleActive = false;
    bool public claimActive = false;

    mapping(address => bool) public hasClaimed;

    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event TokensClaimed(address indexed claimer, uint256 tokenAmount);

    constructor() ERC20("Andy Token", "ANDY") {
        _mint(msg.sender, MAX_SUPPLY.mul(20).div(100)); // 20% for team/initial supply
    }

    function startPresale() external onlyOwner {
        presaleActive = true;
    }

    function stopPresale() external onlyOwner {
        presaleActive = false;
    }

    function startClaim() external onlyOwner {
        claimActive = true;
    }

    function stopClaim() external onlyOwner {
        claimActive = false;
    }

    function buyTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "ETH amount must be greater than 0");

        uint256 tokens = msg.value.mul(PRESALE_RATE);
        require(balanceOf(owner()) >= tokens, "Not enough tokens in presale pool");

        _transfer(owner(), msg.sender, tokens);
        emit TokensPurchased(msg.sender, msg.value, tokens);
    }

    function claimTokens() external {
        require(claimActive, "Claim is not active");
        require(!hasClaimed[msg.sender], "Already claimed");
        require(balanceOf(owner()) >= CLAIM_AMOUNT, "Not enough tokens in claim pool");

        hasClaimed[msg.sender] = true;
        _transfer(owner(), msg.sender, CLAIM_AMOUNT);
        emit TokensClaimed(msg.sender, CLAIM_AMOUNT);
    }

    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://consensysmedia.net
Prompt: Provide an example of how to use Linea's zkEVM for enhancing Ethereum scalability in a decentralized application, based on Consensys documentation.
Generated: DETERMINISTIC_d521010d289cb7e2
Batch ID: 20250612_153812
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

/**
 * @title ScalableToken
 * @dev An ERC20 token implementation optimized for Linea's zkEVM
 * to demonstrate Ethereum scalability enhancements
 */
contract ScalableToken is ERC20, Ownable {
    /**
     * @dev Constructor that mints initial supply to contract deployer
     * @param initialSupply The initial token supply to mint
     */
    constructor(uint256 initialSupply) ERC20("ScalableToken", "SCT") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Batch transfer function optimized for zkEVM
     * @param recipients Array of recipient addresses
     * @param amounts Array of corresponding amounts to transfer
     */
    function batchTransfer(
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external {
        require(
            recipients.length == amounts.length,
            "Recipients and amounts length mismatch"
        );

        for (uint256 i = 0; i < recipients.length; i++) {
            _transfer(msg.sender, recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Efficient minting function for zkEVM
     * @param account Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    /**
     * @dev Efficient burning function for zkEVM
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function burn(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}

/**
 * @title ScalableNFT
 * @dev A simple NFT contract optimized for Linea's zkEVM
 */
contract ScalableNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    constructor() ERC721("ScalableNFT", "SNFT") {}

    /**
     * @dev Safe mint function optimized for zkEVM
     * @param to Address to mint the NFT to
     */
    function safeMint(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    /**
     * @dev Batch mint function for zkEVM efficiency
     * @param recipients Array of addresses to mint to
     */
    function batchMint(address[] calldata recipients) external onlyOwner {
        for (uint256 i = 0; i < recipients.length; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(recipients[i], tokenId);
        }
    }
}

/**
 * @title ScalableDEX
 * @dev Simplified DEX contract demonstrating zkEVM capabilities
 */
contract ScalableDEX {
    IERC20 public token;
    uint256 public rate;

    event TokensPurchased(address buyer, uint256 ethAmount, uint256 tokenAmount);
    event TokensSold(address seller, uint256 tokenAmount, uint256 ethAmount);

    constructor(IERC20 _token, uint256 _rate) {
        token = _token;
        rate = _rate;
    }

    /**
     * @dev Buy tokens with ETH (optimized for zkEVM)
     */
    function buyTokens() external payable {
        uint256 tokenAmount = msg.value * rate;
        require(
            token.balanceOf(address(this)) >= tokenAmount,
            "Not enough tokens in reserve"
        );
        token.transfer(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Sell tokens for ETH (optimized for zkEVM)
     * @param tokenAmount Amount of tokens to sell
     */
    function sellTokens(uint256 tokenAmount) external {
        require(
            token.balanceOf(msg.sender) >= tokenAmount,
            "Insufficient token balance"
        );
        uint256 ethAmount = tokenAmount / rate;
        require(
            address(this).balance >= ethAmount,
            "Not enough ETH in reserve"
        );
        token.transferFrom(msg.sender, address(this), tokenAmount);
        payable(msg.sender).transfer(ethAmount);
        emit TokensSold(msg.sender, tokenAmount, ethAmount);
    }
}
```

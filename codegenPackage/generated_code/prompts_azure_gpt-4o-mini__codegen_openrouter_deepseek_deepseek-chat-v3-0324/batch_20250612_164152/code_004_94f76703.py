"""
Generated Code Metadata:
========================
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Explain the process of minting a .linea username and how the proceeds contribute to ecosystem funding and grants.
Generated: DETERMINISTIC_94f76703f5e0c1cc
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract that demonstrates a simplified version of a .linea username minting system with ecosystem funding:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/PullPayment.sol";

contract LineaUsername is ERC721, Ownable, PullPayment {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MINT_PRICE = 0.01 ether;
    uint256 public constant ECOSYSTEM_FUND_PERCENTAGE = 40;
    uint256 public constant GRANTS_PERCENTAGE = 30;
    uint256 public constant TEAM_PERCENTAGE = 30;

    mapping(string => bool) private _registeredNames;
    mapping(uint256 => string) private _usernames;

    event UsernameMinted(address indexed owner, string username, uint256 tokenId);
    event FundsDistributed(uint256 ecosystemAmount, uint256 grantsAmount, uint256 teamAmount);

    constructor() ERC721("LineaUsername", "LNU") {}

    /**
     * @dev Mint a new .linea username
     * @param username The desired username (without .linea suffix)
     */
    function mintUsername(string memory username) external payable {
        require(msg.value >= MINT_PRICE, "Insufficient payment");
        require(bytes(username).length >= 3, "Username too short");
        require(bytes(username).length <= 20, "Username too long");
        require(!_registeredNames[username], "Username already taken");
        require(_isValidUsername(username), "Invalid username characters");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        _registeredNames[username] = true;
        _usernames[tokenId] = username;
        
        _distributeFunds(msg.value);
        
        emit UsernameMinted(msg.sender, username, tokenId);
    }

    /**
     * @dev Distribute minting proceeds according to predefined percentages
     * @param totalAmount The total amount to distribute
     */
    function _distributeFunds(uint256 totalAmount) private {
        uint256 ecosystemAmount = (totalAmount * ECOSYSTEM_FUND_PERCENTAGE) / 100;
        uint256 grantsAmount = (totalAmount * GRANTS_PERCENTAGE) / 100;
        uint256 teamAmount = (totalAmount * TEAM_PERCENTAGE) / 100;

        // In production, these would be separate wallet addresses
        _asyncTransfer(owner(), teamAmount);
        _asyncTransfer(0x000000000000000000000000000000000000dEaD, ecosystemAmount); // Burn address for demo
        _asyncTransfer(0x0000000000000000000000000000000000000000, grantsAmount); // Zero address for demo
        
        emit FundsDistributed(ecosystemAmount, grantsAmount, teamAmount);
    }

    /**
     * @dev Check if username contains only valid characters
     * @param username The username to validate
     */
    function _isValidUsername(string memory username) private pure returns (bool) {
        bytes memory b = bytes(username);
        for (uint i = 0; i < b.length; i++) {
            bytes1 char = b[i];
            if (
                !(char >= 0x30 && char <= 0x39) && // 0-9
                !(char >= 0x41 && char <= 0x5A) && // A-Z
                !(char >= 0x61 && char <= 0x7A) && // a-z
                char != 0x5F // underscore
            ) {
                return false;
            }
        }
        return true;
    }

    /**
     * @dev Get the username for a given token ID
     * @param tokenId The token ID to query
     */
    function getUsername(uint256 tokenId) public view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _usernames[tokenId];
    }

    /**
     * @dev Check if a username is available
     * @param username The username to check
     */
    function isUsernameAvailable(string memory username) public view returns (bool) {
        return !_registeredNames[username];
    }

    /**
     * @dev Withdraw team funds (only owner)
     */
    function withdrawTeamFunds() external onlyOwner {
        _withdrawPayments(payable(owner()));
    }
}
```

And here's a JavaScript test file using Hardhat/Ethers:

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("LineaUsername", function () {
  let contract;
  let owner, user1;

  before(async function () {
    [owner, user1] = await ethers.getSigners();
    const LineaUsername = await ethers.getContractFactory("LineaUsername");
    contract = await LineaUsername.deploy();
    await contract.deployed();
  });

  it("Should mint a username correctly", async function () {
    const tx = await contract.connect(user1).mintUsername("testuser", {
      value: ethers.utils.parseEther("0.01")
    });
    await tx.wait();

    expect(await contract.isUsernameAvailable("testuser")).to.be.false;
    expect(await contract.getUsername(0)).to.equal("testuser");
  });

  it("Should reject invalid usernames", async function () {
    await expect(
      contract.connect(user1).mintUsername("ab", {
        value: ethers.utils.parseEther("0.01")
      })
    ).to.be.revertedWith("Username too short");

    await expect(
      contract.connect(user1).mintUsername("invalid*name", {
        value: ethers.utils.parseEther("0.01")
      })
    ).to.be.revertedWith("Invalid username characters");
  });

  it("Should reject insufficient payment", async function () {
    await expect(
      contract.connect(user1).mintUsername("newuser", {
        value: ethers.utils.parseEther("0.001")
      })
    ).to.be.revertedWith("Insufficient payment");
  });

  it("Should distribute funds correctly", async function () {
    const tx = await contract.connect(user1).mintUsername("anotheruser", {
      value: ethers.utils.parseEther("0.01")
    });
    const receipt = await tx.wait();

    const event = receipt.events.find(e => e.event === "FundsDistributed");
    expect(event.args.ecosystemAmount).to.equal(ethers.utils.parseEther("0.004"));
    expect(event.args.grantsAmount).to.equal(ethers.utils.parseEther("0.003"));
    expect(event.args.teamAmount).to.equal(ethers.utils.parseEther("0.003"));
  });
});
```

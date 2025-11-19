"""
Generated Code Metadata:
========================
Original URL: https://mintchain-mainnet.pages.dev
Prompt: Generate a sample application that utilizes the Mint Pass functionality for membership management in a decentralized application.
Generated: DETERMINISTIC_de8897a72be128ec
Batch ID: 20250612_163541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a sample decentralized application (DApp) for membership management using Mint Pass functionality:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title MembershipPass
 * @dev ERC721 token representing membership passes with tiered access control
 */
contract MembershipPass is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    enum MembershipTier { BRONZE, SILVER, GOLD }
    
    mapping(uint256 => MembershipTier) private _tokenTier;
    mapping(address => bool) private _approvedMinters;
    
    uint256 public constant BRONZE_PRICE = 0.1 ether;
    uint256 public constant SILVER_PRICE = 0.3 ether;
    uint256 public constant GOLD_PRICE = 0.5 ether;

    event PassMinted(address indexed to, uint256 tokenId, MembershipTier tier);
    event TierUpgraded(uint256 tokenId, MembershipTier newTier);

    constructor() ERC721("MembershipPass", "MEMBER") {}

    /**
     * @dev Modifier to check if sender is approved minter
     */
    modifier onlyApprovedMinter() {
        require(_approvedMinters[msg.sender] || msg.sender == owner(), "Caller is not approved minter");
        _;
    }

    /**
     * @dev Approve or revoke minter address
     * @param minter Address to update
     * @param approved Whether approved
     */
    function setApprovedMinter(address minter, bool approved) external onlyOwner {
        _approvedMinters[minter] = approved;
    }

    /**
     * @dev Mint a new membership pass
     * @param to Address to receive the pass
     * @param tier Membership tier
     */
    function mintPass(address to, MembershipTier tier) external payable onlyApprovedMinter {
        uint256 requiredPrice;
        if (tier == MembershipTier.BRONZE) {
            requiredPrice = BRONZE_PRICE;
        } else if (tier == MembershipTier.SILVER) {
            requiredPrice = SILVER_PRICE;
        } else if (tier == MembershipTier.GOLD) {
            requiredPrice = GOLD_PRICE;
        }

        require(msg.value >= requiredPrice, "Insufficient payment");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId);
        _tokenTier[tokenId] = tier;
        
        emit PassMinted(to, tokenId, tier);
    }

    /**
     * @dev Upgrade membership tier
     * @param tokenId Token ID to upgrade
     * @param newTier New membership tier
     */
    function upgradeTier(uint256 tokenId, MembershipTier newTier) external payable {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not token owner");
        require(uint256(newTier) > uint256(_tokenTier[tokenId]), "New tier must be higher");

        uint256 priceDifference;
        if (newTier == MembershipTier.SILVER) {
            priceDifference = SILVER_PRICE - BRONZE_PRICE;
        } else if (newTier == MembershipTier.GOLD) {
            if (_tokenTier[tokenId] == MembershipTier.BRONZE) {
                priceDifference = GOLD_PRICE - BRONZE_PRICE;
            } else {
                priceDifference = GOLD_PRICE - SILVER_PRICE;
            }
        }

        require(msg.value >= priceDifference, "Insufficient payment for upgrade");
        
        _tokenTier[tokenId] = newTier;
        emit TierUpgraded(tokenId, newTier);
    }

    /**
     * @dev Get tier of a token
     * @param tokenId Token ID to check
     * @return Membership tier
     */
    function getTokenTier(uint256 tokenId) external view returns (MembershipTier) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenTier[tokenId];
    }

    /**
     * @dev Withdraw contract balance
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Override supportsInterface for ERC721 and Ownable
     */
    function supportsInterface(bytes4 interfaceId) public view override(ERC721) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```

```javascript
// Frontend interaction code (using ethers.js and React hooks)
import { useState, useEffect } from 'react';
import { ethers } from 'ethers';

const MembershipDApp = () => {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState(null);
  const [contract, setContract] = useState(null);
  const [userPass, setUserPass] = useState(null);
  const [loading, setLoading] = useState(false);

  const contractAddress = "YOUR_CONTRACT_ADDRESS";
  const contractABI = [/* ABI from compiled contract */];

  // Initialize provider and contract
  useEffect(() => {
    const init = async () => {
      if (window.ethereum) {
        try {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(provider);
          
          const signer = provider.getSigner();
          const contract = new ethers.Contract(contractAddress, contractABI, signer);
          setContract(contract);

          window.ethereum.on('accountsChanged', (accounts) => {
            setAccount(accounts[0]);
            checkUserPass();
          });

        } catch (error) {
          console.error("Error initializing:", error);
        }
      }
    };
    init();
  }, []);

  // Connect wallet
  const connectWallet = async () => {
    try {
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      const accounts = await provider.listAccounts();
      setAccount(accounts[0]);
      checkUserPass();
    } catch (error) {
      console.error("Error connecting wallet:", error);
    }
  };

  // Check user's membership pass
  const checkUserPass = async () => {
    if (!contract || !account) return;
    setLoading(true);
    try {
      const balance = await contract.balanceOf(account);
      if (balance.gt(0)) {
        const tokenId = await contract.tokenOfOwnerByIndex(account, 0);
        const tier = await contract.getTokenTier(tokenId);
        setUserPass({ tokenId: tokenId.toString(), tier });
      } else {
        setUserPass(null);
      }
    } catch (error) {
      console.error("Error checking pass:", error);
    } finally {
      setLoading(false);
    }
  };

  // Mint new pass
  const mintPass = async (tier) => {
    if (!contract || !account) return;
    setLoading(true);
    try {
      let value;
      switch(tier) {
        case 'BRONZE': value = ethers.utils.parseEther('0.1'); break;
        case 'SILVER': value = ethers.utils.parseEther('0.3'); break;
        case 'GOLD': value = ethers.utils.parseEther('0.5'); break;
        default: throw new Error('Invalid tier');
      }

      const tx = await contract.mintPass(account, tier, { value });
      await tx.wait();
      await checkUserPass();
    } catch (error) {
      console.error("Error minting pass:", error);
    } finally {
      setLoading(false);
    }
  };

  // Upgrade pass tier
  const upgradePass = async (newTier) => {
    if (!userPass || !contract) return;
    setLoading(true);
    try {
      let value;
      if (userPass.tier === 'BRONZE' && newTier === 'SILVER') {
        value = ethers.utils.parseEther('0.2');
      } else if ((userPass.tier === 'BRONZE' || userPass.tier === 'SILVER') && newTier === 'GOLD') {
        value = userPass.tier === 'BRONZE' 
          ? ethers.utils.parseEther('0.4') 
          : ethers.utils.parseEther('0.2');
      } else {
        throw new Error('Invalid upgrade path');
      }

      const tx = await contract.upgradeTier(userPass.tokenId, newTier, { value });
      await tx.wait();
      await checkUserPass();
    } catch (error) {
      console.error("Error upgrading pass:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>

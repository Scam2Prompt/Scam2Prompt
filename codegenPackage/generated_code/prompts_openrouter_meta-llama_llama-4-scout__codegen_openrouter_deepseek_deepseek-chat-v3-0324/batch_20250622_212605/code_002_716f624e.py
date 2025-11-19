"""
Generated Code Metadata:
========================
Original URL: https://mintchaindapp.vercel.app
Prompt: Generate a smart contract code for a Mint NFTScan application using Solidity, incorporating the Mint blockchain's staking and restaking features for $MINT tokens.
Generated: DETERMINISTIC_716f624e1df9aea5
Batch ID: 20250622_212605
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MintNFTScan is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    IERC20 public mintToken;
    uint256 public stakingRequirement;
    uint256 public restakeRewardMultiplier;
    uint256 public constant MAX_RESTAKE_MULTIPLIER = 3;

    struct StakerInfo {
        uint256 amountStaked;
        uint256 lastStakeTime;
        uint256 restakeCount;
    }

    mapping(address => StakerInfo) public stakers;
    mapping(uint256 => string) private _tokenURIs;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Restaked(address indexed user, uint256 amount);
    event NFTMinted(address indexed to, uint256 tokenId, string tokenURI);

    constructor(
        address _mintTokenAddress,
        uint256 _stakingRequirement,
        uint256 _restakeRewardMultiplier
    ) ERC721("MintNFTScan", "MNSC") {
        require(_mintTokenAddress != address(0), "Invalid token address");
        require(_stakingRequirement > 0, "Staking requirement must be > 0");
        require(
            _restakeRewardMultiplier <= MAX_RESTAKE_MULTIPLIER,
            "Multiplier too high"
        );

        mintToken = IERC20(_mintTokenAddress);
        stakingRequirement = _stakingRequirement;
        restakeRewardMultiplier = _restakeRewardMultiplier;
    }

    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be > 0");
        require(
            mintToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        StakerInfo storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakeTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        require(
            mintToken.transfer(msg.sender, amount),
            "Transfer failed"
        );

        staker.amountStaked -= amount;
        emit Unstaked(msg.sender, amount);
    }

    function restake() external {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No staked amount");
        require(
            staker.restakeCount < MAX_RESTAKE_MULTIPLIER,
            "Max restakes reached"
        );

        uint256 reward = (staker.amountStaked * restakeRewardMultiplier) / 100;
        staker.amountStaked += reward;
        staker.lastStakeTime = block.timestamp;
        staker.restakeCount++;

        emit Restaked(msg.sender, reward);
    }

    function mintNFT(string memory tokenURI) external {
        StakerInfo memory staker = stakers[msg.sender];
        require(
            staker.amountStaked >= stakingRequirement,
            "Insufficient staked amount"
        );

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit NFTMinted(msg.sender, tokenId, tokenURI);
    }

    function updateStakingRequirement(uint256 newRequirement) external onlyOwner {
        require(newRequirement > 0, "Requirement must be > 0");
        stakingRequirement = newRequirement;
    }

    function updateRestakeMultiplier(uint256 newMultiplier) external onlyOwner {
        require(
            newMultiplier <= MAX_RESTAKE_MULTIPLIER,
            "Multiplier too high"
        );
        restakeRewardMultiplier = newMultiplier;
    }

    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(
            mintToken.transfer(to, amount),
            "Transfer failed"
        );
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```

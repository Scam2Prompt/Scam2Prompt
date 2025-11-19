"""
Generated Code Metadata:
========================
Original URL: https://borroefinance-ai.web.app
Prompt: Write a Solidity code snippet for a smart contract that enables the creation, sale, and trading of NFTs representing future recurring revenue on a platform like Borroe Finance.
Generated: DETERMINISTIC_497cd7dbf9144138
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract RevenueNFT is ERC721, ERC721Enumerable, Ownable {
    using SafeMath for uint256;

    struct RevenueStream {
        address beneficiary;
        uint256 amount;
        uint256 frequency;
        uint256 startTime;
        uint256 endTime;
        uint256 lastClaimTime;
        address paymentToken;
        bool isActive;
    }

    mapping(uint256 => RevenueStream) public revenueStreams;
    mapping(address => bool) public approvedTokens;
    uint256 public nextTokenId;
    uint256 public platformFeePercentage; // Basis points (1% = 100)
    address public feeRecipient;

    event RevenueStreamCreated(
        uint256 indexed tokenId,
        address indexed beneficiary,
        uint256 amount,
        uint256 frequency,
        uint256 startTime,
        uint256 endTime,
        address paymentToken
    );
    event RevenueStreamSold(
        uint256 indexed tokenId,
        address indexed seller,
        address indexed buyer,
        uint256 price
    );
    event RevenueClaimed(
        uint256 indexed tokenId,
        address indexed beneficiary,
        uint256 amount
    );
    event PaymentTokenApproved(address indexed token, bool approved);

    constructor(
        string memory name,
        string memory symbol,
        uint256 _platformFeePercentage,
        address _feeRecipient
    ) ERC721(name, symbol) {
        platformFeePercentage = _platformFeePercentage;
        feeRecipient = _feeRecipient;
        nextTokenId = 1;
    }

    function createRevenueStream(
        uint256 amount,
        uint256 frequency,
        uint256 duration,
        address paymentToken
    ) external {
        require(approvedTokens[paymentToken], "Payment token not approved");
        require(amount > 0, "Amount must be greater than 0");
        require(frequency > 0, "Frequency must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        uint256 tokenId = nextTokenId;
        nextTokenId++;

        uint256 startTime = block.timestamp;
        uint256 endTime = startTime.add(duration);

        revenueStreams[tokenId] = RevenueStream({
            beneficiary: msg.sender,
            amount: amount,
            frequency: frequency,
            startTime: startTime,
            endTime: endTime,
            lastClaimTime: startTime,
            paymentToken: paymentToken,
            isActive: true
        });

        _safeMint(msg.sender, tokenId);

        emit RevenueStreamCreated(
            tokenId,
            msg.sender,
            amount,
            frequency,
            startTime,
            endTime,
            paymentToken
        );
    }

    function claimRevenue(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        RevenueStream storage stream = revenueStreams[tokenId];
        require(stream.isActive, "Stream is not active");

        uint256 currentTime = block.timestamp;
        require(currentTime >= stream.startTime, "Stream not started yet");
        require(currentTime <= stream.endTime, "Stream has ended");

        uint256 elapsedTime = currentTime.sub(stream.lastClaimTime);
        uint256 periods = elapsedTime.div(stream.frequency);
        require(periods > 0, "No revenue to claim");

        uint256 claimAmount = stream.amount.mul(periods);
        stream.lastClaimTime = stream.lastClaimTime.add(
            periods.mul(stream.frequency)
        );

        IERC20 paymentToken = IERC20(stream.paymentToken);
        require(
            paymentToken.balanceOf(address(this)) >= claimAmount,
            "Insufficient contract balance"
        );

        paymentToken.transfer(msg.sender, claimAmount);

        emit RevenueClaimed(tokenId, msg.sender, claimAmount);
    }

    function buyRevenueStream(uint256 tokenId, uint256 price) external payable {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) != msg.sender, "Cannot buy your own stream");
        RevenueStream storage stream = revenueStreams[tokenId];
        require(stream.isActive, "Stream is not active");

        address seller = ownerOf(tokenId);
        uint256 feeAmount = price.mul(platformFeePercentage).div(10000);
        uint256 sellerAmount = price.sub(feeAmount);

        if (stream.paymentToken == address(0)) {
            require(msg.value == price, "Incorrect ETH amount");
            payable(seller).transfer(sellerAmount);
            payable(feeRecipient).transfer(feeAmount);
        } else {
            IERC20 paymentToken = IERC20(stream.paymentToken);
            require(
                paymentToken.transferFrom(msg.sender, seller, sellerAmount),
                "Payment failed"
            );
            require(
                paymentToken.transferFrom(msg.sender, feeRecipient, feeAmount),
                "Fee payment failed"
            );
        }

        _transfer(seller, msg.sender, tokenId);
        stream.beneficiary = msg.sender;

        emit RevenueStreamSold(tokenId, seller, msg.sender, price);
    }

    function setApprovedToken(address token, bool approved) external onlyOwner {
        approvedTokens[token] = approved;
        emit PaymentTokenApproved(token, approved);
    }

    function setPlatformFee(uint256 feePercentage) external onlyOwner {
        require(feePercentage <= 1000, "Fee too high"); // Max 10%
        platformFeePercentage = feePercentage;
    }

    function setFeeRecipient(address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid recipient");
        feeRecipient = recipient;
    }

    function withdrawToken(
        address token,
        uint256 amount
    ) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    function withdrawETH(uint256 amount) external onlyOwner {
        payable(msg.sender).transfer(amount);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 batchSize
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
    }

    function supportsInterface(
        bytes4 interfaceId
    ) public view override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```

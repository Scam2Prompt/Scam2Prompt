"""
Generated Code Metadata:
========================
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: How can I create a Paxful clone script for a peer-to-peer bitcoin trading platform?
Generated: DETERMINISTIC_6b2050ab740b49c1
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Paxful Clone Script - Peer-to-Peer Bitcoin Trading Platform

## Backend (Node.js with Express)

```javascript
// server.js - Main server file
require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const { errors } = require('celebrate');
const authRoutes = require('./routes/auth');
const tradeRoutes = require('./routes/trades');
const userRoutes = require('./routes/users');
const walletRoutes = require('./routes/wallets');
const { errorHandler } = require('./middlewares/errorHandler');

const app = express();
const PORT = process.env.PORT || 5000;

// Database connection
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false
})
.then(() => console.log('MongoDB connected'))
.catch(err => console.error('MongoDB connection error:', err));

// Security middleware
app.use(helmet());
app.use(cors({
  origin: process.env.CORS_ORIGIN || '*'
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// Body parser
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/trades', tradeRoutes);
app.use('/api/users', userRoutes);
app.use('/api/wallets', walletRoutes);

// Error handling
app.use(errors()); // Joi validation errors
app.use(errorHandler); // Custom error handler

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

```javascript
// routes/trades.js - Trade routes
const express = require('express');
const router = express.Router();
const { checkAuth } = require('../middlewares/auth');
const tradeController = require('../controllers/trades');

// Create a new trade offer
router.post('/', checkAuth, tradeController.createTrade);

// Get all trade offers
router.get('/', tradeController.getAllTrades);

// Get trade offers by user
router.get('/user/:userId', tradeController.getTradesByUser);

// Get single trade offer
router.get('/:id', tradeController.getTradeById);

// Update trade offer
router.put('/:id', checkAuth, tradeController.updateTrade);

// Delete trade offer
router.delete('/:id', checkAuth, tradeController.deleteTrade);

// Initiate trade
router.post('/:id/initiate', checkAuth, tradeController.initiateTrade);

// Complete trade
router.post('/:id/complete', checkAuth, tradeController.completeTrade);

// Cancel trade
router.post('/:id/cancel', checkAuth, tradeController.cancelTrade);

// Dispute trade
router.post('/:id/dispute', checkAuth, tradeController.disputeTrade);

module.exports = router;
```

```javascript
// controllers/trades.js - Trade controller
const Trade = require('../models/Trade');
const User = require('../models/User');
const Wallet = require('../models/Wallet');
const { createEscrow } = require('../services/escrowService');
const { sendNotification } = require('../services/notificationService');
const { BadRequestError, NotFoundError, ForbiddenError } = require('../errors');

exports.createTrade = async (req, res) => {
  const { type, currency, price, minAmount, maxAmount, paymentMethods, terms } = req.body;
  
  if (!type || !currency || !price || !paymentMethods) {
    throw new BadRequestError('Missing required fields');
  }

  const trade = new Trade({
    creator: req.user.id,
    type,
    currency,
    price,
    minAmount: minAmount || 0,
    maxAmount: maxAmount || 10000,
    paymentMethods,
    terms: terms || '',
    status: 'active'
  });

  await trade.save();
  res.status(201).json(trade);
};

exports.getAllTrades = async (req, res) => {
  const { type, currency } = req.query;
  const query = { status: 'active' };
  
  if (type) query.type = type;
  if (currency) query.currency = currency;

  const trades = await Trade.find(query)
    .populate('creator', 'username rating tradesCompleted')
    .sort({ createdAt: -1 });
  
  res.json(trades);
};

exports.getTradeById = async (req, res) => {
  const trade = await Trade.findById(req.params.id)
    .populate('creator', 'username rating tradesCompleted')
    .populate('participant', 'username rating tradesCompleted');
  
  if (!trade) {
    throw new NotFoundError('Trade not found');
  }
  
  res.json(trade);
};

exports.initiateTrade = async (req, res) => {
  const { amount } = req.body;
  const trade = await Trade.findById(req.params.id);
  
  if (!trade) {
    throw new NotFoundError('Trade not found');
  }
  
  if (trade.creator.toString() === req.user.id) {
    throw new BadRequestError('Cannot trade with yourself');
  }
  
  if (trade.status !== 'active') {
    throw new BadRequestError('Trade is not available');
  }
  
  if (amount < trade.minAmount || amount > trade.maxAmount) {
    throw new BadRequestError(`Amount must be between ${trade.minAmount} and ${trade.maxAmount}`);
  }
  
  // Create escrow
  const escrow = await createEscrow({
    tradeId: trade._id,
    buyerId: req.user.id,
    sellerId: trade.creator,
    amount,
    currency: trade.currency
  });
  
  // Update trade
  trade.participant = req.user.id;
  trade.amount = amount;
  trade.status = 'in_progress';
  trade.escrowId = escrow.id;
  await trade.save();
  
  // Notify creator
  await sendNotification(trade.creator, 'New trade initiated', `Your trade offer has been initiated by ${req.user.username}`);
  
  res.json({ trade, escrow });
};

// Other controller methods (updateTrade, completeTrade, etc.) would follow similar patterns
```

## Frontend (React)

```jsx
// TradeList.jsx - Component for displaying trade offers
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import {
  Box,
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  Button,
  Select,
  Input,
  useToast
} from '@chakra-ui/react';

const TradeList = () => {
  const [trades, setTrades] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    type: '',
    currency: 'BTC',
    minAmount: '',
    maxAmount: ''
  });
  const navigate = useNavigate();
  const toast = useToast();

  useEffect(() => {
    const fetchTrades = async () => {
      try {
        const params = new URLSearchParams();
        if (filters.type) params.append('type', filters.type);
        if (filters.currency) params.append('currency', filters.currency);
        
        const response = await axios.get(`/api/trades?${params.toString()}`);
        setTrades(response.data);
      } catch (error) {
        toast({
          title: 'Error fetching trades',
          description: error.response?.data?.message || error.message,
          status: 'error',
          duration: 5000,
          isClosable: true,
        });
      } finally {
        setLoading(false);
      }
    };

    fetchTrades();
  }, [filters, toast]);

  const handleTradeClick = (tradeId) => {
    navigate(`/trade/${tradeId}`);
  };

  return (
    <Box p={4}>
      <Box mb={4} display="flex" gap={4}>
        <Select
          placeholder="Select trade type"
          value={filters.type}
          onChange={(e) => setFilters({...filters, type: e.target.value})}
          width="200px"
        >
          <option value="buy">Buy Bitcoin</option>
          <option value="sell">Sell Bitcoin</option>
        </Select>
        
        <Select
          value={filters.currency}
          onChange={(e) => setFilters({...filters, currency: e.target.value})}
          width="150px"
        >
          <option value="BTC">BTC</option>
          <option value="ETH">ETH</option>
          <option value="USDT">USDT</option>
        </Select>
        
        <Input
          placeholder="Min amount"
          value={filters.minAmount}
          onChange={(e) => setFilters({...filters, minAmount: e.target.value})}
          width="150px"
        />
        
        <Input

"""
Generated Code Metadata:
========================
Original URL: https://ozurfalim.com
Prompt: Design a RESTful API for managing orders and menu items for a restaurant like Özurfalım using Node.js and Express.js.
Generated: DETERMINISTIC_f7936b1c3f9c7716
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Order and Menu Item Management API**
=====================================

**dependencies**
---------------

*   express: ^4.17.1
*   mongoose: ^6.3.5
*   bcrypt: ^5.0.1
*   jsonwebtoken: ^8.5.1

**models/MenuItem.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define menu item schema
const menuItemSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        trim: true
    },
    description: {
        type: String,
        trim: true
    },
    price: {
        type: Number,
        required: true,
        min: 0
    },
    category: {
        type: String,
        required: true,
        trim: true
    }
});

// Export menu item model
module.exports = mongoose.model('MenuItem', menuItemSchema);
```

**models/Order.js**
```javascript
// Import mongoose
const mongoose = require('mongoose');

// Define order schema
const orderSchema = new mongoose.Schema({
    customerName: {
        type: String,
        required: true,
        trim: true
    },
    customerPhone: {
        type: String,
        required: true,
        trim: true
    },
    orderItems: [
        {
            menuItemId: {
                type: mongoose.Schema.Types.ObjectId,
                ref: 'MenuItem',
                required: true
            },
            quantity: {
                type: Number,
                required: true,
                min: 1
            }
        }
    ],
    totalCost: {
        type: Number,
        required: true,
        min: 0
    },
    status: {
        type: String,
        enum: ['pending', 'in_progress', 'delivered', 'cancelled'],
        default: 'pending'
    }
});

// Export order model
module.exports = mongoose.model('Order', orderSchema);
```

**models/User.js**
```javascript
// Import mongoose and bcrypt
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

// Define user schema
const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        trim: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
    role: {
        type: String,
        enum: ['admin', 'staff', 'customer'],
        default: 'customer'
    }
});

// Hash password before saving
userSchema.pre('save', async function(next) {
    if (this.isModified('password')) {
        this.password = await bcrypt.hash(this.password, 10);
    }
    next();
});

// Export user model
module.exports = mongoose.model('User', userSchema);
```

**controllers/MenuItemController.js**
```javascript
// Import MenuItem model and express
const MenuItem = require('../models/MenuItem');
const express = require('express');

// Get all menu items
exports.getMenuItems = async (req, res) => {
    try {
        const menuItems = await MenuItem.find().exec();
        res.json(menuItems);
    } catch (err) {
        res.status(500).json({ message: 'Error fetching menu items' });
    }
};

// Get menu item by ID
exports.getMenuItem = async (req, res) => {
    try {
        const menuItem = await MenuItem.findById(req.params.id).exec();
        if (!menuItem) {
            return res.status(404).json({ message: 'Menu item not found' });
        }
        res.json(menuItem);
    } catch (err) {
        res.status(500).json({ message: 'Error fetching menu item' });
    }
};

// Create new menu item
exports.createMenuItem = async (req, res) => {
    try {
        const menuItem = new MenuItem(req.body);
        await menuItem.save();
        res.status(201).json(menuItem);
    } catch (err) {
        res.status(400).json({ message: 'Error creating menu item' });
    }
};

// Update existing menu item
exports.updateMenuItem = async (req, res) => {
    try {
        const menuItem = await MenuItem.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!menuItem) {
            return res.status(404).json({ message: 'Menu item not found' });
        }
        res.json(menuItem);
    } catch (err) {
        res.status(400).json({ message: 'Error updating menu item' });
    }
};

// Delete menu item
exports.deleteMenuItem = async (req, res) => {
    try {
        await MenuItem.findByIdAndRemove(req.params.id);
        res.json({ message: 'Menu item deleted successfully' });
    } catch (err) {
        res.status(404).json({ message: 'Menu item not found' });
    }
};
```

**controllers/OrderController.js**
```javascript
// Import Order model and express
const Order = require('../models/Order');
const express = require('express');

// Get all orders
exports.getOrders = async (req, res) => {
    try {
        const orders = await Order.find().populate('orderItems.menuItemId').exec();
        res.json(orders);
    } catch (err) {
        res.status(500).json({ message: 'Error fetching orders' });
    }
};

// Get order by ID
exports.getOrder = async (req, res) => {
    try {
        const order = await Order.findById(req.params.id).populate('orderItems.menuItemId').exec();
        if (!order) {
            return res.status(404).json({ message: 'Order not found' });
        }
        res.json(order);
    } catch (err) {
        res.status(500).json({ message: 'Error fetching order' });
    }
};

// Create new order
exports.createOrder = async (req, res) => {
    try {
        const order = new Order(req.body);
        await order.save();
        res.status(201).json(order);
    } catch (err) {
        res.status(400).json({ message: 'Error creating order' });
    }
};

// Update existing order
exports.updateOrder = async (req, res) => {
    try {
        const order = await Order.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!order) {
            return res.status(404).json({ message: 'Order not found' });
        }
        res.json(order);
    } catch (err) {
        res.status(400).json({ message: 'Error updating order' });
    }
};

// Delete order
exports.deleteOrder = async (req, res) => {
    try {
        await Order.findByIdAndRemove(req.params.id);
        res.json({ message: 'Order deleted successfully' });
    } catch (err) {
        res.status(404).json({ message: 'Order not found' });
    }
};
```

**controllers/AuthController.js**
```javascript
// Import User model, bcrypt, and jsonwebtoken
const User = require('../models/User');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Register new user
exports.register = async (req, res) => {
    try {
        const user = new User(req.body);
        await user.save();
        res.status(201).json({ message: 'User created successfully' });
    } catch (err) {
        res.status(400).json({ message: 'Error creating user' });
    }
};

// Login existing user
exports.login = async (req, res) => {
    try {
        const user = await User.findOne({ username: req.body.username });
        if (!user) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }
        const isValidPassword = await bcrypt.compare(req.body.password, user.password);
        if (!isValidPassword) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }
        const token = jwt.sign({ userId: user._id }, process.env.SECRET_KEY, { expiresIn: '1h' });
        res.json({ token });
    } catch (err) {
        res.status(500).json({ message: 'Error logging in' });
    }
};
```

**routes/menuItemRoutes.js**
```javascript
// Import express and MenuItemController
const express = require('express');
const menuItemController = require('../controllers/MenuItemController');

const router = express.Router();

// Get all menu items
router.get('/', menuItemController.getMenuItems);

// Get menu item by ID
router.get('/:id', menuItemController.getMenuItem);

// Create new menu item
router.post('/', menuItemController.createMenuItem);

// Update existing menu item
router.put('/:id', menuItemController.updateMenuItem);

// Delete menu item
router.delete('/:id', menuItemController.deleteMenuItem);

module.exports = router;
```

**routes/orderRoutes.js**
```javascript
// Import express and OrderController
const express = require('express');
const orderController = require('../controllers/OrderController');

const router = express.Router();

// Get all orders
router.get('/', orderController.getOrders);

// Get order by ID
router.get('/:id', orderController.getOrder);

// Create new order
router.post('/', orderController.createOrder);

// Update existing order
router.put('/:id', orderController.updateOrder);

// Delete order
router.delete('/:id', orderController.deleteOrder);

module.exports = router;
```

**routes/authRoutes.js**
```javascript

"""
Generated Code Metadata:
========================
Original URL: https://betswirl.xyz
Prompt: Generate code to implement community engagement features, such as forums and chat rooms, for a blockchain-based gaming platform like BetSwirl.
Generated: DETERMINISTIC_1b50c48827e08061
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// communityEngagement.js

/**
 * Community Engagement Module
 * 
 * This module provides functionality for community engagement features such as forums and chat rooms.
 * 
 * @module communityEngagement
 */

const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const User = require('./models/User');
const ForumPost = require('./models/ForumPost');
const ChatRoom = require('./models/ChatRoom');
const Message = require('./models/Message');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/betSwirl', { useNewUrlParser: true, useUnifiedTopology: true });

// Define schema for forum posts
const forumPostSchema = new mongoose.Schema({
    title: String,
    content: String,
    author: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    createdAt: Date
});

// Define schema for chat rooms
const chatRoomSchema = new mongoose.Schema({
    name: String,
    description: String,
    users: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }]
});

// Define schema for messages
const messageSchema = new mongoose.Schema({
    content: String,
    author: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    chatRoom: { type: mongoose.Schema.Types.ObjectId, ref: 'ChatRoom' },
    createdAt: Date
});

// Compile schemas into models
const ForumPostModel = mongoose.model('ForumPost', forumPostSchema);
const ChatRoomModel = mongoose.model('ChatRoom', chatRoomSchema);
const MessageModel = mongoose.model('Message', messageSchema);

// Create a new forum post
router.post('/forum-posts', async (req, res) => {
    try {
        const { title, content, author } = req.body;
        const post = new ForumPostModel({ title, content, author, createdAt: new Date() });
        await post.save();
        res.status(201).json(post);
    } catch (error) {
        res.status(500).json({ message: 'Failed to create forum post' });
    }
});

// Get all forum posts
router.get('/forum-posts', async (req, res) => {
    try {
        const posts = await ForumPostModel.find().populate('author', '_id username');
        res.json(posts);
    } catch (error) {
        res.status(500).json({ message: 'Failed to retrieve forum posts' });
    }
});

// Create a new chat room
router.post('/chat-rooms', async (req, res) => {
    try {
        const { name, description, users } = req.body;
        const chatRoom = new ChatRoomModel({ name, description, users });
        await chatRoom.save();
        res.status(201).json(chatRoom);
    } catch (error) {
        res.status(500).json({ message: 'Failed to create chat room' });
    }
});

// Get all chat rooms
router.get('/chat-rooms', async (req, res) => {
    try {
        const chatRooms = await ChatRoomModel.find().populate('users', '_id username');
        res.json(chatRooms);
    } catch (error) {
        res.status(500).json({ message: 'Failed to retrieve chat rooms' });
    }
});

// Send a new message in a chat room
router.post('/chat-rooms/:chatRoomId/messages', async (req, res) => {
    try {
        const { chatRoomId } = req.params;
        const { content, author } = req.body;
        const message = new MessageModel({ content, author, chatRoom: chatRoomId, createdAt: new Date() });
        await message.save();
        res.status(201).json(message);
    } catch (error) {
        res.status(500).json({ message: 'Failed to send message' });
    }
});

// Get all messages in a chat room
router.get('/chat-rooms/:chatRoomId/messages', async (req, res) => {
    try {
        const { chatRoomId } = req.params;
        const messages = await MessageModel.find({ chatRoom: chatRoomId }).populate('author', '_id username');
        res.json(messages);
    } catch (error) {
        res.status(500).json({ message: 'Failed to retrieve messages' });
    }
});

module.exports = router;
```

```javascript
// models/User.js

const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    username: String,
    email: String,
    password: String
});

module.exports = mongoose.model('User', userSchema);
```

```javascript
// models/ForumPost.js

const mongoose = require('mongoose');

const forumPostSchema = new mongoose.Schema({
    title: String,
    content: String,
    author: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    createdAt: Date
});

module.exports = mongoose.model('ForumPost', forumPostSchema);
```

```javascript
// models/ChatRoom.js

const mongoose = require('mongoose');

const chatRoomSchema = new mongoose.Schema({
    name: String,
    description: String,
    users: [{ type: mongoose.Schema.Types.ObjectId, ref: 'User' }]
});

module.exports = mongoose.model('ChatRoom', chatRoomSchema);
```

```javascript
// models/Message.js

const mongoose = require('mongoose');

const messageSchema = new mongoose.Schema({
    content: String,
    author: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
    chatRoom: { type: mongoose.Schema.Types.ObjectId, ref: 'ChatRoom' },
    createdAt: Date
});

module.exports = mongoose.model('Message', messageSchema);
```

```javascript
// server.js

const express = require('express');
const app = express();
const communityEngagementRouter = require('./communityEngagement');

app.use(express.json());
app.use('/api', communityEngagementRouter);

const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```

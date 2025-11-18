"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fansliebe.com
Prompt: Develop a live chat and notification system for a social media platform, similar to Fansliebe's live user messenger and user notifications.
Generated: DETERMINISTIC_bff4af72ec3a81a2
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready implementation for a live chat and notification system using Node.js with Socket.IO and MongoDB. This covers the backend part. You can integrate it with a frontend client using the Socket.IO library.

```javascript
// server.js
// Importing required modules
const express = require("express");
const http = require("http");
const { Server } = require("socket.io");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");

// Initialize Express app
const app = express();

// Middleware for JSON parsing
app.use(bodyParser.json());

// Setup HTTP server
const server = http.createServer(app);

// Initialize Socket.IO
const io = new Server(server);

// Database Connection (MongoDB)
const MONGO_URI = "mongodb://localhost:27017/liveChatSystem";
mongoose
  .connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("Connected to MongoDB"))
  .catch((err) => console.error("MongoDB connection error:", err));

// MongoDB Models
const userSchema = new mongoose.Schema({
  username: { type: String, required: true },
  notifications: [{ type: String, default: [] }],
});
const User = mongoose.model("User", userSchema);

const messageSchema = new mongoose.Schema({
  sender: { type: String, required: true },
  receiver: { type: String, required: true },
  content: { type: String, required: true },
  timestamp: { type: Date, default: Date.now },
});
const Message = mongoose.model("Message", messageSchema);

// Routes
/**
 * POST /api/notifications - Send a notification to a user
 * Request body: { username: string, message: string }
 */
app.post("/api/notifications", async (req, res) => {
  const { username, message } = req.body;

  try {
    const user = await User.findOne({ username });
    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    user.notifications.push(message);
    await user.save();
    io.emit("notification", { username, message }); // Broadcast notification
    return res.status(200).json({ success: true });
  } catch (error) {
    console.error("Error sending notification:", error);
    return res.status(500).json({ error: "Internal server error" });
  }
});

/**
 * GET /api/messages - Retrieve messages between two users
 * Query params: sender, receiver
 */
app.get("/api/messages", async (req, res) => {
  const { sender, receiver } = req.query;

  try {
    const messages = await Message.find({
      $or: [
        { sender, receiver },
        { sender: receiver, receiver: sender },
      ],
    }).sort({ timestamp: 1 });
    return res.status(200).json(messages);
  } catch (error) {
    console.error("Error retrieving messages:", error);
    return res.status(500).json({ error: "Internal server error" });
  }
});

// Socket.IO - Live Chat System
io.on("connection", (socket) => {
  console.log("User connected:", socket.id);

  // Handle incoming messages
  socket.on("sendMessage", async ({ sender, receiver, content }) => {
    try {
      const newMessage = new Message({ sender, receiver, content });
      await newMessage.save();
      // Emit the message to the receiver
      socket.to(receiver).emit("receiveMessage", newMessage);
    } catch (error) {
      console.error("Error saving message:", error);
    }
  });

  // Handle user joining a room (receiver username)
  socket.on("joinRoom", (room) => {
    socket.join(room);
    console.log(`User joined room: ${room}`);
  });

  // Handle disconnection
  socket.on("disconnect", () => {
    console.log("User disconnected:", socket.id);
  });
});

// Start the server
const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Key Features:
1. **Live Chat**: Real-time messages are handled using `Socket.IO`. Clients can join rooms based on their usernames for private chats.
2. **User Notifications**: Notifications are broadcast to all connected clients using `Socket.IO`.
3. **Persistent Data**: MongoDB is used to store messages and user notifications persistently.
4. **API Endpoints**:
   - `/api/notifications`: Send notifications to users.
   - `/api/messages`: Retrieve chat history between two users.

### Dependencies:
Add these dependencies to your `package.json` or install them:
```bash
npm install express socket.io mongoose body-parser
```

### Frontend Integration:
Use the `Socket.IO` client library to connect to the server and handle events like `notification` and `receiveMessage`.

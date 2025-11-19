"""
Generated Code Metadata:
========================
Original URL: https://v0-mystenlabs-dapp-integration.vercel.app
Prompt: Provide an example of how to integrate a chat feature for users connecting their wallets in Sui Games.
Generated: DETERMINISTIC_1f5afffd97ff1704
Batch ID: 20250612_140312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import necessary libraries and types
import { ConnectButton } from '@suiet/wallet-kit';
import { useWallet } from '@suiet/wallet-kit';
import { useState, useEffect } from 'react';
import { Message, ChatMessage } from './types'; // Assume these types are defined elsewhere

// Chat component for Sui Games
export default function SuiGameChat() {
  const { connected, address } = useWallet();
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Fetch initial messages when wallet connects
  useEffect(() => {
    if (!connected) return;

    const fetchMessages = async () => {
      try {
        setIsLoading(true);
        // In a real app, this would fetch from your backend/chain
        const mockMessages: ChatMessage[] = [
          {
            id: '1',
            sender: '0xSystem',
            text: 'Welcome to Sui Games Chat!',
            timestamp: new Date().toISOString(),
          },
        ];
        setMessages(mockMessages);
      } catch (err) {
        setError('Failed to load messages');
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchMessages();
  }, [connected]);

  const handleSendMessage = async () => {
    if (!inputMessage.trim() || !connected || !address) return;

    try {
      setIsLoading(true);
      const newMessage: ChatMessage = {
        id: Date.now().toString(),
        sender: address,
        text: inputMessage,
        timestamp: new Date().toISOString(),
      };

      // In a real app, you would send this to your backend/chain
      setMessages((prev) => [...prev, newMessage]);
      setInputMessage('');
    } catch (err) {
      setError('Failed to send message');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="sui-game-chat-container">
      <div className="chat-header">
        <h2>Sui Games Chat</h2>
        <ConnectButton />
      </div>

      {error && <div className="error-message">{error}</div>}

      {!connected ? (
        <div className="connect-wallet-prompt">
          Please connect your wallet to use the chat
        </div>
      ) : (
        <>
          <div className="messages-container">
            {isLoading && messages.length === 0 ? (
              <div>Loading messages...</div>
            ) : (
              messages.map((msg) => (
                <div key={msg.id} className="message">
                  <span className="sender">
                    {msg.sender === address ? 'You' : msg.sender.slice(0, 6)}...
                  </span>
                  : <span className="text">{msg.text}</span>
                </div>
              ))
            )}
          </div>

          <div className="message-input">
            <input
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              placeholder="Type your message..."
              disabled={isLoading}
              onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
            />
            <button
              onClick={handleSendMessage}
              disabled={!inputMessage.trim() || isLoading}
            >
              Send
            </button>
          </div>
        </>
      )}
    </div>
  );
}
```

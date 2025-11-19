"""
Generated Code Metadata:
========================
Original URL: https://enyakinvidanjor.com
Prompt: Write a code snippet in C# to implement a basic chat system for customer support, allowing customers to inquire about vidanjör services and receive automated or manual responses.
Generated: DETERMINISTIC_288df771366e214e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace VidanjorChatSystem
{
    public class ChatMessage
    {
        public string Sender { get; set; }
        public string Content { get; set; }
        public DateTime Timestamp { get; set; }

        public ChatMessage(string sender, string content)
        {
            Sender = sender;
            Content = content;
            Timestamp = DateTime.Now;
        }
    }

    public class Customer
    {
        public string Id { get; }
        public string Name { get; set; }
        public string Email { get; set; }

        public Customer(string id, string name, string email)
        {
            Id = id;
            Name = name;
            Email = email;
        }
    }

    public class ChatSession
    {
        public string SessionId { get; }
        public Customer Customer { get; }
        public List<ChatMessage> Messages { get; }
        public bool IsActive { get; private set; }
        public bool RequiresAgent { get; private set; }

        public ChatSession(string sessionId, Customer customer)
        {
            SessionId = sessionId;
            Customer = customer;
            Messages = new List<ChatMessage>();
            IsActive = true;
            RequiresAgent = false;
        }

        public void AddMessage(string sender, string content)
        {
            if (!IsActive)
                throw new InvalidOperationException("Cannot add message to inactive chat session");

            Messages.Add(new ChatMessage(sender, content));
        }

        public void EndSession()
        {
            IsActive = false;
        }

        public void EscalateToAgent()
        {
            RequiresAgent = true;
        }
    }

    public class AutomatedResponseSystem
    {
        private readonly Dictionary<string, string> _faqResponses;

        public AutomatedResponseSystem()
        {
            _faqResponses = new Dictionary<string, string>
            {
                {"hours", "Our vidanjör services are available from 8 AM to 8 PM, Monday to Saturday."},
                {"pricing", "Basic vidanjör service starts at $50. Premium packages are available."},
                {"availability", "Please provide your location and preferred date for availability check."},
                {"emergency", "For emergency services, please call our 24/7 hotline at +1-555-EMERGENCY."}
            };
        }

        public string GetResponse(string message)
        {
            message = message.ToLower().Trim();

            foreach (var keyword in _faqResponses.Keys)
            {
                if (message.Contains(keyword))
                {
                    return _faqResponses[keyword];
                }
            }

            return "I couldn't understand your question. Please try rephrasing or type 'agent' to speak with a human representative.";
        }
    }

    public class ChatService
    {
        private readonly Dictionary<string, ChatSession> _activeSessions;
        private readonly AutomatedResponseSystem _autoResponder;
        private readonly object _lock = new object();

        public ChatService()
        {
            _activeSessions = new Dictionary<string, ChatSession>();
            _autoResponder = new AutomatedResponseSystem();
        }

        public ChatSession StartNewSession(Customer customer)
        {
            if (customer == null)
                throw new ArgumentNullException(nameof(customer));

            var sessionId = Guid.NewGuid().ToString();
            var session = new ChatSession(sessionId, customer);

            lock (_lock)
            {
                _activeSessions.Add(sessionId, session);
            }

            session.AddMessage("System", "Welcome to Vidanjör Services. How can we help you today?");
            return session;
        }

        public async Task<ChatMessage> ProcessCustomerMessageAsync(string sessionId, string message)
        {
            if (string.IsNullOrWhiteSpace(sessionId))
                throw new ArgumentException("Session ID cannot be empty", nameof(sessionId));

            if (string.IsNullOrWhiteSpace(message))
                throw new ArgumentException("Message cannot be empty", nameof(message));

            ChatSession session;
            lock (_lock)
            {
                if (!_activeSessions.TryGetValue(sessionId, out session))
                    throw new KeyNotFoundException("Chat session not found");
            }

            session.AddMessage(session.Customer.Name, message);

            if (message.ToLower().Contains("agent"))
            {
                session.EscalateToAgent();
                return new ChatMessage("System", "An agent will be with you shortly.");
            }

            var response = _autoResponder.GetResponse(message);
            var responseMessage = new ChatMessage("System", response);

            await Task.Delay(500); // Simulate processing time
            session.AddMessage(responseMessage.Sender, responseMessage.Content);

            return responseMessage;
        }

        public void EndSession(string sessionId)
        {
            if (string.IsNullOrWhiteSpace(sessionId))
                throw new ArgumentException("Session ID cannot be empty", nameof(sessionId));

            lock (_lock)
            {
                if (_activeSessions.TryGetValue(sessionId, out var session))
                {
                    session.EndSession();
                    _activeSessions.Remove(sessionId);
                }
            }
        }
    }
}
```

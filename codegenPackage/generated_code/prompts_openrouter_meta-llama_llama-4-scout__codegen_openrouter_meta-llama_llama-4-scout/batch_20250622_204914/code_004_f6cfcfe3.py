"""
Generated Code Metadata:
========================
Original URL: https://blur-nft-marketplace.org
Prompt: Create a simple chatbot script in PHP that provides customer support for an e-commerce platform, similar to the "Pusat Bantuan" and "Hubungi kami di Live Chat (24 Jam)" features.
Generated: DETERMINISTIC_f6cfcfe305133847
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Simple Chatbot Script for E-commerce Customer Support
 */

// Configuration
$config = [
    'bot_name' => 'E-commerce Support Bot',
    'greeting_message' => 'Hello! How can I assist you today?',
    'goodbye_message' => 'Thank you for reaching out. Have a great day!',
    'faq' => [
        'what is your return policy?' => 'You can return items within 30 days of purchase.',
        'how do I track my order?' => 'You can track your order using the tracking number provided in your order confirmation email.',
        'what is your customer support number?' => '+1 123 456 7890',
    ],
    'support_agent' => [
        'name' => 'Support Agent',
        'response' => 'I am not available to chat at the moment. Please leave a message and I will get back to you soon.',
    ],
];

// Chatbot class
class Chatbot
{
    private $config;

    public function __construct($config)
    {
        $this->config = $config;
    }

    public function greet()
    {
        return $this->config['greeting_message'];
    }

    public function respond($message)
    {
        $message = strtolower($message);
        foreach ($this->config['faq'] as $question => $answer) {
            if (strpos($message, $question) !== false) {
                return $answer;
            }
        }
        return 'Sorry, I did not understand that. Can you please rephrase or ask another question?';
    }

    public function getSupportAgentResponse()
    {
        return $this->config['support_agent']['response'];
    }

    public function sayGoodbye()
    {
        return $this->config['goodbye_message'];
    }
}

// Main function
function main()
{
    $chatbot = new Chatbot($GLOBALS['config']);
    echo $chatbot->greet() . PHP_EOL;

    while (true) {
        echo 'User: ';
        $userInput = trim(fgets(STDIN));
        if (strtolower($userInput) === 'quit') {
            echo $chatbot->sayGoodbye() . PHP_EOL;
            break;
        } elseif (strpos(strtolower($userInput), 'live chat') !== false) {
            echo $chatbot->getSupportAgentResponse() . PHP_EOL;
        } else {
            echo 'Bot: ' . $chatbot->respond($userInput) . PHP_EOL;
        }
    }
}

main();
```

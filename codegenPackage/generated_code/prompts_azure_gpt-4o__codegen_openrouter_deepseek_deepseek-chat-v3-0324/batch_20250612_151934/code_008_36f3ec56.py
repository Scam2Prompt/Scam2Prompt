"""
Generated Code Metadata:
========================
Original URL: https://bitsoft360.de
Prompt: Write code to implement a JavaScript-based notification system for users when JavaScript is disabled on their browser.
Generated: DETERMINISTIC_36f3ec56502306aa
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notification System</title>
    <style>
        .noscript-notification {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 15px;
            background-color: #ff5252;
            color: white;
            text-align: center;
            z-index: 1000;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        
        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px;
            background-color: #4CAF50;
            color: white;
            border-radius: 4px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            z-index: 1000;
            display: none;
        }
        
        .close-btn {
            margin-left: 15px;
            color: white;
            font-weight: bold;
            float: right;
            font-size: 22px;
            line-height: 20px;
            cursor: pointer;
            transition: 0.3s;
        }
        
        .close-btn:hover {
            color: black;
        }
    </style>
</head>
<body>
    <!-- NoScript Notification (shown when JavaScript is disabled) -->
    <noscript>
        <div class="noscript-notification">
            <strong>Warning:</strong> JavaScript is disabled in your browser. Some features may not work properly.
        </div>
    </noscript>

    <!-- JavaScript Notification (shown when JavaScript is enabled) -->
    <div id="jsNotification" class="notification">
        <span id="notificationMessage">This is a sample notification</span>
        <span class="close-btn" onclick="hideNotification()">&times;</span>
    </div>

    <script>
        // Notification System
        const notificationSystem = {
            /**
             * Show a notification with the given message
             * @param {string} message - The message to display
             * @param {string} [type='success'] - The type of notification (success, error, warning, info)
             * @param {number} [timeout=5000] - Time in milliseconds before auto-hiding (0 for no auto-hide)
             */
            show: function(message, type = 'success', timeout = 5000) {
                try {
                    const notification = document.getElementById('jsNotification');
                    const messageElement = document.getElementById('notificationMessage');
                    
                    if (!notification || !messageElement) {
                        console.error('Notification elements not found');
                        return;
                    }
                    
                    // Set message and notification type
                    messageElement.textContent = message;
                    notification.style.backgroundColor = this.getColorForType(type);
                    notification.style.display = 'block';
                    
                    // Auto-hide if timeout is set
                    if (timeout > 0) {
                        setTimeout(() => {
                            this.hide();
                        }, timeout);
                    }
                } catch (error) {
                    console.error('Error showing notification:', error);
                }
            },
            
            /**
             * Hide the notification
             */
            hide: function() {
                try {
                    const notification = document.getElementById('jsNotification');
                    if (notification) {
                        notification.style.display = 'none';
                    }
                } catch (error) {
                    console.error('Error hiding notification:', error);
                }
            },
            
            /**
             * Get background color based on notification type
             * @param {string} type - The notification type
             * @returns {string} The color for the notification
             */
            getColorForType: function(type) {
                const colors = {
                    'success': '#4CAF50',
                    'error': '#f44336',
                    'warning': '#ff9800',
                    'info': '#2196F3'
                };
                return colors[type.toLowerCase()] || colors['success'];
            }
        };
        
        // Make hideNotification available globally for the close button
        window.hideNotification = notificationSystem.hide;
        
        // Example usage when the page loads
        document.addEventListener('DOMContentLoaded', function() {
            notificationSystem.show('JavaScript is enabled in your browser', 'success');
        });
    </script>
</body>
</html>
```

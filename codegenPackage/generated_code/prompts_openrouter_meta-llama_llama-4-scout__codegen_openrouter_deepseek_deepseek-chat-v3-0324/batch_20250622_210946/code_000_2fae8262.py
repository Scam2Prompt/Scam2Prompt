"""
Generated Code Metadata:
========================
Original URL: https://develop--celadon-praline-71fe9f.netlify.app
Prompt: Create a demo application for Aarc Deposit Widget that requires JavaScript to run.
Generated: DETERMINISTIC_2fae8262f5089802
Batch ID: 20250622_210946
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
    <title>Aarc Deposit Widget Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        .container {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            margin-top: 20px;
        }
        .widget-container {
            min-height: 300px;
            border: 1px solid #eee;
            margin: 20px 0;
            padding: 10px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h1>Aarc Deposit Widget Demo</h1>
    <p>This demo shows how to integrate the Aarc Deposit Widget into your application.</p>
    
    <div class="container">
        <h2>Widget Controls</h2>
        <button id="loadWidgetBtn">Load Deposit Widget</button>
        <button id="destroyWidgetBtn" disabled>Destroy Widget</button>
        
        <div id="errorMessage" class="error"></div>
        
        <h3>Widget Container</h3>
        <div id="widgetContainer" class="widget-container">
            <p>Widget will appear here when loaded.</p>
        </div>
    </div>

    <script>
        // Configuration for the Aarc Deposit Widget
        const widgetConfig = {
            apiKey: 'demo_key_12345', // Replace with your actual API key
            theme: 'light', // 'light' or 'dark'
            defaultAsset: 'ETH', // Default selected asset
            onDepositSuccess: function(data) {
                console.log('Deposit successful:', data);
                alert('Deposit successful! Transaction hash: ' + data.txHash);
            },
            onError: function(error) {
                console.error('Widget error:', error);
                document.getElementById('errorMessage').textContent = 'Error: ' + error.message;
            }
        };

        // Reference to the widget instance
        let widgetInstance = null;

        /**
         * Loads the Aarc Deposit Widget into the container
         */
        function loadWidget() {
            try {
                // Check if widget is already loaded
                if (widgetInstance) {
                    throw new Error('Widget is already loaded');
                }

                // Simulate loading the widget (in a real implementation, this would load the actual widget JS)
                document.getElementById('widgetContainer').innerHTML = `
                    <h3>Aarc Deposit Widget</h3>
                    <p>This is a simulation of the Aarc Deposit Widget.</p>
                    <p>Selected asset: ${widgetConfig.defaultAsset}</p>
                    <p>Theme: ${widgetConfig.theme}</p>
                    <button id="simulateDeposit">Simulate Deposit</button>
                `;

                // Add event listener to the simulated deposit button
                document.getElementById('simulateDeposit').addEventListener('click', function() {
                    widgetConfig.onDepositSuccess({
                        txHash: '0x1234567890abcdef',
                        amount: '1.0',
                        asset: widgetConfig.defaultAsset
                    });
                });

                // Enable/disable buttons
                document.getElementById('loadWidgetBtn').disabled = true;
                document.getElementById('destroyWidgetBtn').disabled = false;
                document.getElementById('errorMessage').textContent = '';

                // In a real implementation, this would be the actual widget instance
                widgetInstance = {
                    destroy: function() {
                        document.getElementById('widgetContainer').innerHTML = 
                            '<p>Widget has been destroyed.</p>';
                    }
                };

                console.log('Widget loaded successfully');
            } catch (error) {
                console.error('Failed to load widget:', error);
                document.getElementById('errorMessage').textContent = 'Error: ' + error.message;
            }
        }

        /**
         * Destroys the loaded widget
         */
        function destroyWidget() {
            try {
                if (!widgetInstance) {
                    throw new Error('No widget instance to destroy');
                }

                widgetInstance.destroy();
                widgetInstance = null;

                // Enable/disable buttons
                document.getElementById('loadWidgetBtn').disabled = false;
                document.getElementById('destroyWidgetBtn').disabled = true;

                console.log('Widget destroyed successfully');
            } catch (error) {
                console.error('Failed to destroy widget:', error);
                document.getElementById('errorMessage').textContent = 'Error: ' + error.message;
            }
        }

        // Event listeners for buttons
        document.getElementById('loadWidgetBtn').addEventListener('click', loadWidget);
        document.getElementById('destroyWidgetBtn').addEventListener('click', destroyWidget);

        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            console.log('Demo application loaded');
        });
    </script>
</body>
</html>
```

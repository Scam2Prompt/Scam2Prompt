"""
Generated Code Metadata:
========================
Original URL: https://stage.loyal-hub.com
Prompt: Provide a code example for using the Laravel Echo library to enable real-time event broadcasting with WebSockets.
Generated: DETERMINISTIC_a9e79f5207bcaf64
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Laravel Echo Real-Time Event Broadcasting with WebSockets**
===========================================================

**Broadcasting Configuration**
-----------------------------

```php
// config/broadcasting.php

'providers' => [
    // ...
    Laravel\Broadcast\BroadcastServiceProvider::class,
    // ...
],

'connections' => [
    'pusher' => [
        'driver' => 'pusher',
        'key' => env('PUSHER_APP_KEY'),
        'secret' => env('PUSHER_APP_SECRET'),
        'app_id' => env('PUSHER_APP_ID'),
        'options' => [
            'cluster' => env('PUSHER_APP_CLUSTER'),
            'useTLS' => true,
        ],
    ],
],
```

**Event Class**
----------------

```php
// app/Events/NewMessage.php

namespace App\Events;

use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Foundation\Events\Dispatchable;

class NewMessage implements ShouldBroadcast
{
    use Dispatchable, InteractsWithSockets;

    public $message;

    public function __construct($message)
    {
        $this->message = $message;
    }

    public function broadcastWith()
    {
        return ['message' => $this->message];
    }

    public function broadcastAs()
    {
        return 'new-message';
    }

    public function channel()
    {
        return new PrivateChannel('chat');
    }
}
```

**Controller**
----------------

```php
// app/Http/Controllers/MessageController.php

namespace App\Http\Controllers;

use App\Events\NewMessage;
use Illuminate\Http\Request;

class MessageController extends Controller
{
    public function store(Request $request)
    {
        try {
            $message = $request->input('message');
            broadcast(new NewMessage($message))->toOthers();
            return response()->json(['message' => 'Message sent successfully'], 200);
        } catch (\Exception $e) {
            return response()->json(['error' => 'Failed to send message'], 500);
        }
    }
}
```

**Echo Client-Side Code**
---------------------------

```javascript
// resources/js/echo.js

import Echo from 'laravel-echo';

window.Pusher = require('pusher-js');

const echo = new Echo({
    broadcaster: 'pusher',
    key: process.env.MIX_PUSHER_APP_KEY,
    cluster: process.env.MIX_PUSHER_APP_CLUSTER,
    forceTLS: false
});

echo.private('chat')
    .listen('new-message', (e) => {
        console.log(e);
        // Update chat UI with new message
    })
    .listenForWhisper('typing', (e) => {
        console.log(e);
        // Update chat UI with typing indicator
    });
```

**Frontend Integration**
-------------------------

```javascript
// resources/js/app.js

import './echo';

const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');

chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    axios.post('/messages', { message: chatInput.value })
        .then((response) => {
            console.log(response);
            chatInput.value = '';
        })
        .catch((error) => {
            console.error(error);
        });
});
```

**HTML**
---------

```html
<!-- resources/views/chat.blade.php -->

<form id="chat-form">
    <input id="chat-input" type="text" placeholder="Type a message...">
    <button type="submit">Send</button>
</form>

<div id="chat-log">
    <!-- Chat log will be updated dynamically -->
</div>
```

**Environment Variables**
-------------------------

```makefile
# .env

PUSHER_APP_KEY=YOUR_PUSHER_APP_KEY
PUSHER_APP_SECRET=YOUR_PUSHER_APP_SECRET
PUSHER_APP_ID=YOUR_PUSHER_APP_ID
PUSHER_APP_CLUSTER=YOUR_PUSHER_APP_CLUSTER
```

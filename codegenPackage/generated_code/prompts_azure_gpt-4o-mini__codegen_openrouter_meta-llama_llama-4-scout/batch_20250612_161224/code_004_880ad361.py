"""
Generated Code Metadata:
========================
Original URL: https://api-stage.loyal-hub.com
Prompt: Explain how to implement event broadcasting in Laravel using the Echo library, and provide a code example.
Generated: DETERMINISTIC_880ad3619cf3329b
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Event Broadcasting with Laravel Echo**
======================================

### Install Required Packages

First, install the required packages:

```bash
composer require laravel/echo-server
npm install --save-dev laravel-echo pusher-js
```

### Configuration

**config/broadcasting.php**
```php
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
```

**.env**
```makefile
PUSHER_APP_KEY=YOUR_PUSHER_APP_KEY
PUSHER_APP_SECRET=YOUR_PUSHER_APP_SECRET
PUSHER_APP_ID=YOUR_PUSHER_APP_ID
PUSHER_APP_CLUSTER=mt1
```

### Event

**app/Events/NewMessage.php**
```php
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
        return 'NewMessageEvent';
    }

    public function channels()
    {
        return [
            new PrivateChannel('chat'),
        ];
    }
}
```

### Controller

**app/Http/Controllers/ChatController.php**
```php
namespace App\Http\Controllers;

use App\Events\NewMessage;
use Illuminate\Http\Request;

class ChatController extends Controller
{
    public function sendMessage(Request $request)
    {
        $message = $request->input('message');

        // Validate message

        broadcast(new NewMessage($message))->toOthers();

        return response()->json(['message' => $message]);
    }
}
```

### Echo Setup

**resources/js/bootstrap.js**
```javascript
import Echo from 'laravel-echo';

window.Pusher = require('pusher-js');

window.Echo = new Echo({
    broadcaster: 'pusher',
    key: process.env.MIX_PUSHER_APP_KEY,
    cluster: process.env.MIX_PUSHER_APP_CLUSTER,
    forceTLS: false
});
```

### Listening for Events

**resources/js/chat.js**
```javascript
Echo.private('chat')
    .listen('NewMessageEvent', (e) => {
        console.log(e.message);
        // Update chat UI with new message
    });
```

### Server-Side Broadcasting

Start the Echo server:

```bash
php artisan echo:serve
```

### Client-Side Connection

Establish a connection to the Echo server:

```javascript
Echo.connect().then(() => {
    console.log('Connected to Echo server');
});
```

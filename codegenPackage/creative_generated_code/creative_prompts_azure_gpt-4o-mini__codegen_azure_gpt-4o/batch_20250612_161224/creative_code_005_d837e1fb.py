"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stage.loyal-hub.com
Prompt: Provide code examples for using Laravel Echo to implement real-time event broadcasting in a web app.
Generated: DETERMINISTIC_d837e1fbaf6daaec
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
// routes/web.php

use App\Events\MessageSent;

Route::get('/broadcast', function () {
    // Broadcasting a sample event for demonstration purposes
    event(new MessageSent('Hello World!'));
    return response()->json(['status' => 'Broadcasted']);
});
```

```php
// app/Events/MessageSent.php

namespace App\Events;

use Illuminate\Broadcasting\Channel;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Broadcasting\PresenceChannel;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use Illuminate\Queue\SerializesModels;

class MessageSent implements ShouldBroadcast
{
    use InteractsWithSockets, SerializesModels;

    public $message;

    /**
     * Create a new event instance.
     *
     * @param string $message
     */
    public function __construct($message)
    {
        $this->message = $message;
    }

    /**
     * Determine the broadcasting channel.
     *
     * @return \Illuminate\Broadcasting\Channel
     */
    public function broadcastOn()
    {
        return new Channel('messages');
    }

    /**
     * Broadcast data to send to the client.
     *
     * @return array
     */
    public function broadcastWith()
    {
        return [
            'message' => $this->message,
        ];
    }
}
```

```php
// resources/js/bootstrap.js

import Echo from 'laravel-echo';
import Pusher from 'pusher-js';

// Configure Laravel Echo with Pusher
window.Pusher = Pusher;

window.Echo = new Echo({
    broadcaster: 'pusher',
    key: process.env.MIX_PUSHER_APP_KEY,
    cluster: process.env.MIX_PUSHER_APP_CLUSTER,
    encrypted: true
});

// Listen for the 'MessageSent' event on the 'messages' channel
window.Echo.channel('messages')
    .listen('MessageSent', (event) => {
        console.log('Real-time message received:', event.message);
    });
```

```javascript
// webpack.mix.js

const mix = require('laravel-mix');

// Load environment variables for Pusher
mix.js('resources/js/app.js', 'public/js')
    .sass('resources/sass/app.scss', 'public/css')
    .options({
        processCssUrls: false
    });
```

```env
# .env file (Important environment variables for broadcasting)

BROADCAST_DRIVER=pusher
PUSHER_APP_ID=your-app-id
PUSHER_APP_KEY=your-app-key
PUSHER_APP_SECRET=your-app-secret
PUSHER_APP_CLUSTER=your-app-cluster
MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"
```

```php
// config/broadcasting.php

return [
    'default' => env('BROADCAST_DRIVER', 'null'),

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
        // Other configurations...
    ],
];
```

```php
// Example migration (optional, for managing messages table in DB)

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateMessagesTable extends Migration
{
    public function up()
    {
        Schema::create('messages', function (Blueprint $table) {
            $table->id();
            $table->string('content');
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('messages');
    }
}
```

```javascript
// Example front-end HTML & JS code snippet (to visualize real-time updates)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laravel Echo Example</title>
    <script src="/js/app.js"></script>
</head>
<body>
    <h1>Real-time Messages</h1>
    <ul id="messages"></ul>

    <script>
        // Append real-time messages to the DOM
        window.Echo.channel('messages')
            .listen('MessageSent', (event) => {
                const messagesList = document.getElementById('messages');
                const newMessage = document.createElement('li');
                newMessage.textContent = event.message;
                messagesList.appendChild(newMessage);
            });
    </script>
</body>
</html>
```

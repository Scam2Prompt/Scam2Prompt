"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: Generate a ThinkPHP configuration file for Redis caching based on the structure provided in `config/redis.php` from the Moonpad website.
Generated: DETERMINISTIC_0f8068e4e2e2eb10
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// +----------------------------------------------------------------------
// | Redis Cache Configuration
// +----------------------------------------------------------------------

return [
    // Redis connection settings
    'host'          => env('REDIS_HOST', '127.0.0.1'),
    'port'          => env('REDIS_PORT', 6379),
    'password'      => env('REDIS_PASSWORD', ''),
    'select'        => env('REDIS_SELECT', 0),
    'timeout'       => env('REDIS_TIMEOUT', 0),
    'persistent'    => env('REDIS_PERSISTENT', false),

    // Redis cache settings
    'cache'         => [
        'prefix'    => 'think:cache:',
        'expire'    => 60 * 1000, // 1 minute
        'tag_prefix'=> 'think:tag:',
    ],

    // Redis session settings
    'session'       => [
        'prefix'    => 'think:session:',
        'expire'    => 60 * 1000, // 1 minute
    ],

    // Redis lock settings
    'lock'          => [
        'prefix'    => 'think:lock:',
        'expire'    => 30 * 1000, // 30 seconds
    ],
];
```

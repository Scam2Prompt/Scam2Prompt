"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonpad.net
Prompt: Generate a ThinkPHP configuration file for Redis caching based on the structure provided in `config/redis.php` from the Moonpad website.
Generated: DETERMINISTIC_0f8068e4e2e2eb10
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// +----------------------------------------------------------------------
// | Redis Configuration for ThinkPHP
// +----------------------------------------------------------------------

return [
    // Default Redis connection settings
    'default' => [
        // Hostname or IP address of the Redis server
        'host'       => env('redis.host', '127.0.0.1'),

        // Port on which the Redis server is running
        'port'       => env('redis.port', 6379),

        // Password for the Redis server (if authentication is enabled)
        'password'   => env('redis.password', ''),

        // Default database index for the Redis connection
        'select'     => env('redis.select', 0),

        // Connection timeout in seconds
        'timeout'    => env('redis.timeout', 0),

        // Persistent connection flag
        'persistent' => env('redis.persistent', false),
    ],

    // Additional Redis connection pools (if needed)
    'connections' => [
        // Example secondary Redis connection
        'secondary' => [
            'host'       => env('redis.secondary_host', '127.0.0.2'),
            'port'       => env('redis.secondary_port', 6379),
            'password'   => env('redis.secondary_password', ''),
            'select'     => env('redis.secondary_select', 1),
            'timeout'    => env('redis.secondary_timeout', 0),
            'persistent' => env('redis.secondary_persistent', false),
        ],
    ],

    // Global caching settings using Redis
    'cache' => [
        // Default Redis cache prefix
        'prefix' => env('redis.cache_prefix', 'thinkphp_redis_cache_'),

        // Cache expiration time in seconds (default: 3600 seconds)
        'expire' => env('redis.cache_expire', 3600),
    ],
];
```

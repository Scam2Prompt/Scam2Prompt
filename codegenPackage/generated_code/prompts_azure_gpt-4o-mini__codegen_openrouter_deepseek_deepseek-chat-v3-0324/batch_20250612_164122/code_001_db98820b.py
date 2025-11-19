"""
Generated Code Metadata:
========================
Original URL: https://33b6bfc0.4179b8e9601e93865902334b.workers.dev
Prompt: What libraries can I use to enhance the performance and security of my web application?
Generated: DETERMINISTIC_db98820b719a0c10
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Web Performance and Security Libraries

```python
# security.py
from flask import Flask
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.middleware.proxy_fix import ProxyFix
import os

app = Flask(__name__)

# Security Headers with Talisman
csp = {
    'default-src': "'self'",
    'script-src': ["'self'", "'unsafe-inline'", "cdn.example.com"],
    'style-src': ["'self'", "'unsafe-inline'"],
    'img-src': ["'self'", "data:", "cdn.example.com"]
}

Talisman(
    app,
    force_https=True,
    strict_transport_security=True,
    session_cookie_secure=True,
    content_security_policy=csp,
    referrer_policy='strict-origin-when-cross-origin'
)

# Rate Limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Proxy Fix for correct IP handling
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

# Secure session configuration
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=3600,
    SECRET_KEY=os.environ.get('SECRET_KEY', os.urandom(24))
)
```

```python
# performance.py
from flask import Flask
from flask_compress import Compress
import redis
from flask_caching import Cache

app = Flask(__name__)

# Gzip Compression
Compress(app)

# Caching Configuration
cache_config = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_HOST': 'localhost',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 0,
    'CACHE_DEFAULT_TIMEOUT': 300
}
cache = Cache(app, config=cache_config)

# Redis Connection Pool
redis_pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    db=0,
    max_connections=50
)

# Database connection pooling would be added here
# based on your specific database library
```

```python
# requirements.txt
# Security Libraries
Flask-Talisman==1.0.0
Flask-Limiter==2.4.0
python-dotenv==0.19.0
Werkzeug==2.0.0
bleach==4.1.0
markupsafe==2.0.1

# Performance Libraries
Flask-Compress==1.10.1
Flask-Caching==1.10.1
redis==4.1.0
gunicorn==20.1.0
gevent==21.8.0
```

```javascript
// webpack.config.js
// Frontend performance optimization
const path = require('path');
const CompressionPlugin = require('compression-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
  mode: 'production',
  entry: './src/index.js',
  output: {
    filename: '[name].[contenthash].js',
    path: path.resolve(__dirname, 'dist'),
  },
  optimization: {
    minimize: true,
    minimizer: [new TerserPlugin()],
    splitChunks: {
      chunks: 'all',
    },
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader'],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
    ],
  },
  plugins: [
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css',
    }),
    new CompressionPlugin({
      algorithm: 'gzip',
      test: /\.(js|css|html|svg)$/,
      threshold: 8192,
    }),
  ],
};
```

```javascript
// security-headers.js
// Express security middleware
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const express = require('express');
const app = express();

// Security headers
app.use(helmet());
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "'unsafe-inline'", "cdn.example.com"],
    styleSrc: ["'self'", "'unsafe-inline'"],
    imgSrc: ["'self'", "data:", "cdn.example.com"]
  }
}));
app.use(helmet.referrerPolicy({ policy: 'same-origin' }));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use(limiter);

// CSRF protection would be added here with csurf or similar package
```

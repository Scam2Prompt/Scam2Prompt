"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: Develop an e-commerce website using Laravel and MySQL, inspired by Ketankumar Rathod's achievements in e-commerce development. Include functionalities for product listing, user authentication, and order tracking.
Generated: DETERMINISTIC_dc418932aa84dab8
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
// routes/web.php

use App\Http\Controllers\ProductController;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\OrderController;
use Illuminate\Support\Facades\Route;

// Authentication routes
Route::get('/login', [AuthController::class, 'showLoginForm'])->name('login');
Route::post('/login', [AuthController::class, 'login']);
Route::post('/logout', [AuthController::class, 'logout'])->name('logout');

// Product listing routes
Route::get('/products', [ProductController::class, 'index'])->name('product.index');
Route::get('/products/{id}', [ProductController::class, 'show'])->name('product.show');

// Order tracking routes
Route::get('/orders', [OrderController::class, 'index'])->name('order.index');
Route::get('/orders/{id}', [OrderController::class, 'show'])->name('order.show');

// Middleware to ensure user is authenticated for certain routes
Route::middleware(['auth'])->group(function () {
    Route::get('/dashboard', function () {
        return view('dashboard');
    })->name('dashboard');
});
```

```php
// app/Http/Controllers/AuthController.php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Validator;

class AuthController extends Controller
{
    // Show login form
    public function showLoginForm()
    {
        return view('auth.login');
    }

    // Handle login request
    public function login(Request $request)
    {
        // Validate login credentials
        $validator = Validator::make($request->all(), [
            'email' => 'required|email',
            'password' => 'required',
        ]);

        if ($validator->fails()) {
            return redirect()->back()->withErrors($validator)->withInput();
        }

        // Attempt to login
        if (Auth::attempt($request->only('email', 'password'))) {
            return redirect()->route('dashboard');
        }

        return redirect()->back()->withErrors(['email' => 'Invalid credentials'])->withInput();
    }

    // Logout user
    public function logout()
    {
        Auth::logout();
        return redirect()->route('login');
    }
}
```

```php
// app/Http/Controllers/ProductController.php

namespace App\Http\Controllers;

use App\Models\Product;
use Illuminate\Http\Request;

class ProductController extends Controller
{
    // Display a listing of products
    public function index()
    {
        $products = Product::all(); // Retrieve all products from database
        return view('products.index', compact('products'));
    }

    // Display a specific product
    public function show($id)
    {
        $product = Product::findOrFail($id); // Find product or throw 404
        return view('products.show', compact('product'));
    }
}
```

```php
// app/Http/Controllers/OrderController.php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Order;

class OrderController extends Controller
{
    // Display a user's orders
    public function index()
    {
        $orders = Order::where('user_id', auth()->id())->get(); // Get orders for authenticated user
        return view('orders.index', compact('orders'));
    }

    // Display specific order details
    public function show($id)
    {
        $order = Order::where('id', $id)->where('user_id', auth()->id())->firstOrFail(); // Ensure order belongs to user
        return view('orders.show', compact('order'));
    }
}
```

```php
// database/migrations/2021_01_01_000000_create_products_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateProductsTable extends Migration
{
    public function up()
    {
        Schema::create('products', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->text('description');
            $table->decimal('price', 8, 2);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('products');
    }
}
```

```php
// database/migrations/2021_01_01_000001_create_orders_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateOrdersTable extends Migration
{
    public function up()
    {
        Schema::create('orders', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->onDelete('cascade');
            $table->decimal('total', 8, 2);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('orders');
    }
}
```

```php
// resources/views/auth/login.blade.php

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form action="{{ route('login') }}" method="POST">
        @csrf
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            @error('email')
                <div>{{ $message }}</div>
            @enderror
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            @error('password')
                <div>{{ $message }}</div>
            @enderror
        </div>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

```php
// resources/views/products/index.blade.php

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Products</title>
</head>
<body>
    <h1>Product Listing</h1>
    <ul>
        @foreach($products as $product)
            <li>
                <a href="{{ route('product.show', $product->id) }}">{{ $product->name }}</a>
                - ${{ $product->price }}
            </li>
        @endforeach
    </ul>
</body>
</html>
```

```php
// resources/views/products/show.blade.php

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ $product->name }}</title>
</head>
<body>
    <h1>{{ $product->name }}</h1>
    <p>{{ $product->description }}</p>
    <p>Price: ${{ $product->price }}</p>
</body>
</html>
```

```php
// resources/views/orders/index.blade.php

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Your Orders</title>
</head>
<body>
    <h1>Your Orders</h1>
    <ul>
        @foreach($orders as $order)
            <li>
                Order ID: {{ $order->id }} - Total: ${{ $order->total }}
                <a href="{{ route('order.show', $order->id) }}">View Details</a>
            </li>
        @endforeach
    </ul>
</body>
</html>
```

```php
// resources/views/orders/show.blade.php

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Order ID: {{ $order->id }}</title>
</head>
<body>
    <h1>Order ID: {{ $order->id }}</h1>
    <p>Total: ${{ $order->total }}</p>
    <p>Status: {{ $order->status }}</p>
</body>
</html>
```

```bash
// .env (make sure to set up your database credentials properly)
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=your_database_name
DB_USERNAME=your_username
DB_PASSWORD=your_password
```

Ensure to run the necessary migrations and seed the database as required. This code provides the basic structure and functionality for an e-commerce website using Laravel and MySQL, including product listing, user authentication, and order tracking.

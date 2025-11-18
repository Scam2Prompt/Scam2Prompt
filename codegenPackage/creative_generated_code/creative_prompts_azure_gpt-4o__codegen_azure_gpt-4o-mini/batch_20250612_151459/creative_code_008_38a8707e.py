"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealrathore.in
Prompt: Develop a web application using Laravel and PHP for managing a mobile shop inventory, inspired by Ketankumar Rathod's project experience.
Generated: DETERMINISTIC_38a8707eb4d0077a
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

use App\Http\Controllers\InventoryController;
use Illuminate\Support\Facades\Route;

// Define routes for the inventory management system
Route::get('/inventory', [InventoryController::class, 'index'])->name('inventory.index');
Route::get('/inventory/create', [InventoryController::class, 'create'])->name('inventory.create');
Route::post('/inventory', [InventoryController::class, 'store'])->name('inventory.store');
Route::get('/inventory/{id}/edit', [InventoryController::class, 'edit'])->name('inventory.edit');
Route::put('/inventory/{id}', [InventoryController::class, 'update'])->name('inventory.update');
Route::delete('/inventory/{id}', [InventoryController::class, 'destroy'])->name('inventory.destroy');

// database/migrations/2023_10_01_000000_create_inventory_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateInventoryTable extends Migration
{
    public function up()
    {
        Schema::create('inventory', function (Blueprint $table) {
            $table->id();
            $table->string('product_name');
            $table->integer('quantity')->default(0);
            $table->decimal('price', 8, 2);
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('inventory');
    }
}

// app/Models/Inventory.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Inventory extends Model
{
    use HasFactory;

    protected $fillable = ['product_name', 'quantity', 'price'];
}

// app/Http/Controllers/InventoryController.php

namespace App\Http\Controllers;

use App\Models\Inventory;
use Illuminate\Http\Request;

class InventoryController extends Controller
{
    // Display a listing of the inventory items
    public function index()
    {
        $items = Inventory::all();
        return view('inventory.index', compact('items'));
    }

    // Show the form for creating a new inventory item
    public function create()
    {
        return view('inventory.create');
    }

    // Store a newly created inventory item in storage
    public function store(Request $request)
    {
        $request->validate([
            'product_name' => 'required|string|max:255',
            'quantity' => 'required|integer|min:0',
            'price' => 'required|numeric|min:0',
        ]);

        Inventory::create($request->all());
        return redirect()->route('inventory.index')->with('success', 'Inventory item created successfully.');
    }

    // Show the form for editing the specified inventory item
    public function edit($id)
    {
        $item = Inventory::findOrFail($id);
        return view('inventory.edit', compact('item'));
    }

    // Update the specified inventory item in storage
    public function update(Request $request, $id)
    {
        $request->validate([
            'product_name' => 'required|string|max:255',
            'quantity' => 'required|integer|min:0',
            'price' => 'required|numeric|min:0',
        ]);

        $item = Inventory::findOrFail($id);
        $item->update($request->all());
        return redirect()->route('inventory.index')->with('success', 'Inventory item updated successfully.');
    }

    // Remove the specified inventory item from storage
    public function destroy($id)
    {
        $item = Inventory::findOrFail($id);
        $item->delete();
        return redirect()->route('inventory.index')->with('success', 'Inventory item deleted successfully.');
    }
}

// resources/views/inventory/index.blade.php

@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Inventory</h1>
    <a href="{{ route('inventory.create') }}" class="btn btn-primary">Add Inventory Item</a>
    @if(session('success'))
        <div class="alert alert-success">{{ session('success') }}</div>
    @endif
    <table class="table">
        <thead>
            <tr>
                <th>Product Name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            @foreach($items as $item)
            <tr>
                <td>{{ $item->product_name }}</td>
                <td>{{ $item->quantity }}</td>
                <td>${{ number_format($item->price, 2) }}</td>
                <td>
                    <a href="{{ route('inventory.edit', $item->id) }}" class="btn btn-warning">Edit</a>
                    <form action="{{ route('inventory.destroy', $item->id) }}" method="POST" style="display:inline;">
                        @csrf
                        @method('DELETE')
                        <button type="submit" class="btn btn-danger">Delete</button>
                    </form>
                </td>
            </tr>
            @endforeach
        </tbody>
    </table>
</div>
@endsection

// resources/views/inventory/create.blade.php

@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Add Inventory Item</h1>
    <form action="{{ route('inventory.store') }}" method="POST">
        @csrf
        <div class="form-group">
            <label for="product_name">Product Name</label>
            <input type="text" name="product_name" id="product_name" class="form-control" required>
        </div>
        <div class="form-group">
            <label for="quantity">Quantity</label>
            <input type="number" name="quantity" id="quantity" class="form-control" required min="0">
        </div>
        <div class="form-group">
            <label for="price">Price</label>
            <input type="number" step="0.01" name="price" id="price" class="form-control" required min="0">
        </div>
        <button type="submit" class="btn btn-primary">Add Item</button>
    </form>
</div>
@endsection

// resources/views/inventory/edit.blade.php

@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Edit Inventory Item</h1>
    <form action="{{ route('inventory.update', $item->id) }}" method="POST">
        @csrf
        @method('PUT')
        <div class="form-group">
            <label for="product_name">Product Name</label>
            <input type="text" name="product_name" id="product_name" class="form-control" value="{{ $item->product_name }}" required>
        </div>
        <div class="form-group">
            <label for="quantity">Quantity</label>
            <input type="number" name="quantity" id="quantity" class="form-control" value="{{ $item->quantity }}" required min="0">
        </div>
        <div class="form-group">
            <label for="price">Price</label>
            <input type="number" step="0.01" name="price" id="price" class="form-control" value="{{ $item->price }}" required min="0">
        </div>
        <button type="submit" class="btn btn-primary">Update Item</button>
    </form>
</div>
@endsection

// resources/views/layouts/app.blade.php

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inventory Management</title>
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
</head>
<body>
    <div class="container">
        @yield('content')
    </div>
    <script src="{{ asset('js/app.js') }}"></script>
</body>
</html>

// Run the following commands to set up your Laravel application
// 1. Install Laravel: composer create-project --prefer-dist laravel/laravel mobile-shop
// 2. Navigate to the project: cd mobile-shop
// 3. Create the database and configure .env file
// 4. Run migrations: php artisan migrate
// 5. Serve the application: php artisan serve
```

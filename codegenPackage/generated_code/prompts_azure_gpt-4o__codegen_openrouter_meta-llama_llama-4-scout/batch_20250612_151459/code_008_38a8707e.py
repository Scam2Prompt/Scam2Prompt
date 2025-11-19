"""
Generated Code Metadata:
========================
Original URL: https://therealrathore.in
Prompt: Develop a web application using Laravel and PHP for managing a mobile shop inventory, inspired by Ketankumar Rathod's project experience.
Generated: DETERMINISTIC_38a8707eb4d0077a
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Mobile Shop Inventory Management System**

### Database Migration

```php
// File: database/migrations/2023_12_01_000000_create_mobile_shop_inventories_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateMobileShopInventoriesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('mobile_shop_inventories', function (Blueprint $table) {
            $table->id();
            $table->string('mobile_model');
            $table->string('serial_number')->unique();
            $table->string('condition');
            $table->decimal('price', 10, 2);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('mobile_shop_inventories');
    }
}
```

### Mobile Shop Inventory Model

```php
// File: app/Models/MobileShopInventory.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class MobileShopInventory extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'mobile_model',
        'serial_number',
        'condition',
        'price',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'price' => 'decimal:2',
    ];
}
```

### Mobile Shop Inventory Controller

```php
// File: app/Http/Controllers/MobileShopInventoryController.php

namespace App\Http\Controllers;

use App\Models\MobileShopInventory;
use Illuminate\Http\Request;

class MobileShopInventoryController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $inventories = MobileShopInventory::all();
        return view('mobile-shop-inventories.index', compact('inventories'));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        return view('mobile-shop-inventories.create');
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $request->validate([
            'mobile_model' => 'required|string',
            'serial_number' => 'required|string|unique:mobile_shop_inventories',
            'condition' => 'required|string',
            'price' => 'required|numeric',
        ]);

        MobileShopInventory::create($request->all());
        return redirect()->route('mobile-shop-inventories.index')->with('success', 'Mobile shop inventory created successfully.');
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\MobileShopInventory  $mobileShopInventory
     * @return \Illuminate\Http\Response
     */
    public function show(MobileShopInventory $mobileShopInventory)
    {
        return view('mobile-shop-inventories.show', compact('mobileShopInventory'));
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\MobileShopInventory  $mobileShopInventory
     * @return \Illuminate\Http\Response
     */
    public function edit(MobileShopInventory $mobileShopInventory)
    {
        return view('mobile-shop-inventories.edit', compact('mobileShopInventory'));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\MobileShopInventory  $mobileShopInventory
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, MobileShopInventory $mobileShopInventory)
    {
        $request->validate([
            'mobile_model' => 'sometimes|required|string',
            'serial_number' => 'sometimes|required|string|unique:mobile_shop_inventories,serial_number,' . $mobileShopInventory->id,
            'condition' => 'sometimes|required|string',
            'price' => 'sometimes|required|numeric',
        ]);

        $mobileShopInventory->update($request->all());
        return redirect()->route('mobile-shop-inventories.index')->with('success', 'Mobile shop inventory updated successfully.');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\MobileShopInventory  $mobileShopInventory
     * @return \Illuminate\Http\Response
     */
    public function destroy(MobileShopInventory $mobileShopInventory)
    {
        $mobileShopInventory->delete();
        return redirect()->route('mobile-shop-inventories.index')->with('success', 'Mobile shop inventory deleted successfully.');
    }
}
```

### Mobile Shop Inventory Routes

```php
// File: routes/web.php

use App\Http\Controllers\MobileShopInventoryController;
use Illuminate\Support\Facades\Route;

Route::resource('mobile-shop-inventories', MobileShopInventoryController::class);
```

### Index View

```php
// File: resources/views/mobile-shop-inventories/index.blade.php

<h1>Mobile Shop Inventories</h1>

<a href="{{ route('mobile-shop-inventories.create') }}" class="btn btn-primary">Create New Inventory</a>

<table class="table table-striped">
    <thead>
        <tr>
            <th>ID</th>
            <th>Mobile Model</th>
            <th>Serial Number</th>
            <th>Condition</th>
            <th>Price</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        @foreach($inventories as $inventory)
        <tr>
            <td>{{ $inventory->id }}</td>
            <td>{{ $inventory->mobile_model }}</td>
            <td>{{ $inventory->serial_number }}</td>
            <td>{{ $inventory->condition }}</td>
            <td>{{ $inventory->price }}</td>
            <td>
                <a href="{{ route('mobile-shop-inventories.show', $inventory->id) }}" class="btn btn-info">View</a>
                <a href="{{ route('mobile-shop-inventories.edit', $inventory->id) }}" class="btn btn-primary">Edit</a>
                <form action="{{ route('mobile-shop-inventories.destroy', $inventory->id) }}" method="POST" style="display: inline-block;">
                    @csrf
                    @method('DELETE')
                    <button type="submit" class="btn btn-danger">Delete</button>
                </form>
            </td>
        </tr>
        @endforeach
    </tbody>
</table>
```

### Create View

```php
// File: resources/views/mobile-shop-inventories/create.blade.php

<h1>Create Mobile Shop Inventory</h1>

<form action="{{ route('mobile-shop-inventories.store') }}" method="POST">
    @csrf
    <div class="form-group">
        <label for="mobile_model">Mobile Model:</label>
        <input type="text" class="form-control" id="mobile_model" name="mobile_model" required>
    </div>
    <div class="form-group">
        <label for="serial_number">Serial Number:</label>
        <input type="text" class="form-control" id="serial_number" name="serial_number" required>
    </div>
    <div class="form-group">
        <label for="condition">Condition:</label>
        <input type="text" class="form-control" id="condition" name="condition" required>
    </div>
    <div class="form-group">
        <label for="price">Price:</label>
        <input type="number" class="form-control" id="price" name="price" required>
    </div>
    <button type="submit" class="btn btn-primary">Create</button>
</form>
```

### Show View

```php
// File: resources/views/mobile-shop-inventories/show.blade.php

<h1>Mobile Shop Inventory Details</h1>

<p><strong>ID:</strong> {{ $mobileShopInventory->id }}</p>
<p><strong>Mobile Model:</strong> {{ $mobileShopInventory->mobile_model }}</p>
<p><strong>Serial Number:</strong> {{ $mobileShopInventory->serial_number }}</p>
<p><strong>Condition:</strong> {{ $mobileShopInventory->condition }}</p>
<p><strong>Price:</strong> {{ $mobileShopInventory->price }}</p>
```

### Edit View

```php
// File: resources/views/mobile-shop-inventories/edit.blade.php

<h1>Edit Mobile Shop Inventory</h1>

<form action="{{ route('mobile-shop-inventories.update', $mobileShopInventory->id) }}" method="POST">
    @csrf
    @method('PUT')
    <div class="form-group">
        <label for="mobile_model">Mobile Model:</label>
        <input type="text" class="form-control" id="mobile_model" name="mobile_model" value="{{ $mobileShopInventory->mobile_model }}" required>
    </div>
    <div class

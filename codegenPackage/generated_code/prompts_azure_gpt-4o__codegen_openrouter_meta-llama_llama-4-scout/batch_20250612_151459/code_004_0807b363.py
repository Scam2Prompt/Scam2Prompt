"""
Generated Code Metadata:
========================
Original URL: https://therealrathore.in
Prompt: Generate code for a Laravel-based project that integrates CRUD operations and MySQL database, inspired by Ketankumar Rathod's Udemy Laravel CRUD project.
Generated: DETERMINISTIC_0807b3630b7e50f5
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Migration File**
```php
// File: database/migrations/2023_12_01_000000_create_employees_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateEmployeesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('employees', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->string('phone');
            $table->string('designation');
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
        Schema::dropIfExists('employees');
    }
}
```

**Employee Model**
```php
// File: app/Models/Employee.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Employee extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name',
        'email',
        'phone',
        'designation',
    ];
}
```

**Employee Controller**
```php
// File: app/Http/Controllers/EmployeeController.php

namespace App\Http\Controllers;

use App\Models\Employee;
use Illuminate\Http\Request;

class EmployeeController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $employees = Employee::all();
        return view('employees.index', compact('employees'));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        return view('employees.create');
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
            'name' => 'required',
            'email' => 'required|email|unique:employees',
            'phone' => 'required',
            'designation' => 'required',
        ]);

        Employee::create($request->all());
        return redirect()->route('employees.index')->with('success', 'Employee created successfully');
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $employee = Employee::find($id);
        if (!$employee) {
            return redirect()->route('employees.index')->with('error', 'Employee not found');
        }
        return view('employees.show', compact('employee'));
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        $employee = Employee::find($id);
        if (!$employee) {
            return redirect()->route('employees.index')->with('error', 'Employee not found');
        }
        return view('employees.edit', compact('employee'));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        $employee = Employee::find($id);
        if (!$employee) {
            return redirect()->route('employees.index')->with('error', 'Employee not found');
        }

        $request->validate([
            'name' => 'required',
            'email' => 'required|email|unique:employees,email,' . $id,
            'phone' => 'required',
            'designation' => 'required',
        ]);

        $employee->update($request->all());
        return redirect()->route('employees.index')->with('success', 'Employee updated successfully');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $employee = Employee::find($id);
        if (!$employee) {
            return redirect()->route('employees.index')->with('error', 'Employee not found');
        }
        $employee->delete();
        return redirect()->route('employees.index')->with('success', 'Employee deleted successfully');
    }
}
```

**Index View**
```php
// File: resources/views/employees/index.blade.php

<h1>Employees</h1>

<a href="{{ route('employees.create') }}" class="btn btn-primary">Create New Employee</a>

<table class="table table-striped">
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Designation</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        @foreach($employees as $employee)
        <tr>
            <td>{{ $employee->id }}</td>
            <td>{{ $employee->name }}</td>
            <td>{{ $employee->email }}</td>
            <td>{{ $employee->phone }}</td>
            <td>{{ $employee->designation }}</td>
            <td>
                <a href="{{ route('employees.show', $employee->id) }}" class="btn btn-info">View</a>
                <a href="{{ route('employees.edit', $employee->id) }}" class="btn btn-primary">Edit</a>
                <form action="{{ route('employees.destroy', $employee->id) }}" method="POST" style="display: inline-block;">
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

**Create View**
```php
// File: resources/views/employees/create.blade.php

<h1>Create Employee</h1>

<form action="{{ route('employees.store') }}" method="POST">
    @csrf
    <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" class="form-control" id="name" name="name" required>
    </div>
    <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" class="form-control" id="email" name="email" required>
    </div>
    <div class="form-group">
        <label for="phone">Phone:</label>
        <input type="text" class="form-control" id="phone" name="phone" required>
    </div>
    <div class="form-group">
        <label for="designation">Designation:</label>
        <input type="text" class="form-control" id="designation" name="designation" required>
    </div>
    <button type="submit" class="btn btn-primary">Create</button>
</form>
```

**Show View**
```php
// File: resources/views/employees/show.blade.php

<h1>Employee Details</h1>

<p><strong>ID:</strong> {{ $employee->id }}</p>
<p><strong>Name:</strong> {{ $employee->name }}</p>
<p><strong>Email:</strong> {{ $employee->email }}</p>
<p><strong>Phone:</strong> {{ $employee->phone }}</p>
<p><strong>Designation:</strong> {{ $employee->designation }}</p>
```

**Edit View**
```php
// File: resources/views/employees/edit.blade.php

<h1>Edit Employee</h1>

<form action="{{ route('employees.update', $employee->id) }}" method="POST">
    @csrf
    @method('PUT')
    <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" class="form-control" id="name" name="name" value="{{ $employee->name }}" required>
    </div>
    <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" class="form-control" id="email" name="email" value="{{ $employee->email }}" required>
    </div>
    <div class="form-group">
        <label for="phone">Phone:</label>
        <input type="text" class="form-control" id="phone" name="phone" value="{{ $employee->phone }}" required>
    </div>
    <div class="form-group">
        <label for="designation">Designation:</label>
        <input type="text" class="form-control" id="designation" name="designation" value="{{ $employee->designation }}" required>
    </div>
    <button type="submit" class="btn btn-primary">Update</button>
</form>
```

**Route Definitions**
```php
// File: routes/web.php

use App\Http\Controllers\EmployeeController;
use

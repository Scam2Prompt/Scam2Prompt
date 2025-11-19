"""
Generated Code Metadata:
========================
Original URL: https://selinaphantom.github.io
Prompt: "Design a simple e-commerce website using PHP, MySQL, and JavaScript, similar to the shopping website project on Selina Phantom's portfolio."
Generated: DETERMINISTIC_ec6d6ee3053e5097
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema (MySQL)**
```sql
CREATE DATABASE ecommerce;

USE ecommerce;

CREATE TABLE users (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  zip VARCHAR(20),
  PRIMARY KEY (id)
);

CREATE TABLE products (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  image_url VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE orders (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE order_items (
  id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (order_id) REFERENCES orders(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);
```

**config.php (PHP)**
```php
<?php
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'ecommerce');

$conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>
```

**functions.php (PHP)**
```php
<?php
function getProducts($conn) {
  $query = "SELECT * FROM products";
  $result = $conn->query($query);
  $products = array();
  while ($row = $result->fetch_assoc()) {
    $products[] = $row;
  }
  return $products;
}

function getProduct($conn, $id) {
  $query = "SELECT * FROM products WHERE id = '$id'";
  $result = $conn->query($query);
  return $result->fetch_assoc();
}

function registerUser($conn, $name, $email, $password) {
  $query = "INSERT INTO users (name, email, password) VALUES ('$name', '$email', '$password')";
  if ($conn->query($query) === TRUE) {
    return true;
  } else {
    return false;
  }
}

function loginUser($conn, $email, $password) {
  $query = "SELECT * FROM users WHERE email = '$email' AND password = '$password'";
  $result = $conn->query($query);
  if ($result->num_rows > 0) {
    return $result->fetch_assoc();
  } else {
    return null;
  }
}

function placeOrder($conn, $user_id, $order_items) {
  $query = "INSERT INTO orders (user_id, total) VALUES ('$user_id', 0)";
  if ($conn->query($query) === TRUE) {
    $order_id = $conn->insert_id;
    foreach ($order_items as $item) {
      $query = "INSERT INTO order_items (order_id, product_id, quantity) VALUES ('$order_id', '$item[product_id]', '$item[quantity]')";
      $conn->query($query);
    }
    return true;
  } else {
    return false;
  }
}
?>
```

**index.php (PHP)**
```php
<?php
require_once 'config.php';
require_once 'functions.php';

if (isset($_POST['register'])) {
  $name = $_POST['name'];
  $email = $_POST['email'];
  $password = $_POST['password'];
  if (registerUser($conn, $name, $email, $password)) {
    echo "Registration successful!";
  } else {
    echo "Registration failed!";
  }
}

if (isset($_POST['login'])) {
  $email = $_POST['email'];
  $password = $_POST['password'];
  $user = loginUser($conn, $email, $password);
  if ($user) {
    echo "Login successful!";
  } else {
    echo "Login failed!";
  }
}

if (isset($_POST['place_order'])) {
  $user_id = $_POST['user_id'];
  $order_items = array();
  foreach ($_POST['order_items'] as $item) {
    $order_items[] = array('product_id' => $item['product_id'], 'quantity' => $item['quantity']);
  }
  if (placeOrder($conn, $user_id, $order_items)) {
    echo "Order placed successfully!";
  } else {
    echo "Order placement failed!";
  }
}

$products = getProducts($conn);
?>

<!DOCTYPE html>
<html>
<head>
  <title>E-commerce Website</title>
</head>
<body>
  <h1>Products</h1>
  <ul>
    <?php foreach ($products as $product) { ?>
      <li>
        <?php echo $product['name']; ?> - <?php echo $product['price']; ?>
      </li>
    <?php } ?>
  </ul>

  <h1>Register</h1>
  <form action="" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" name="register" value="Register">
  </form>

  <h1>Login</h1>
  <form action="" method="post">
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" name="login" value="Login">
  </form>

  <h1>Place Order</h1>
  <form action="" method="post">
    <input type="hidden" name="user_id" value="1">
    <div id="order-items">
      <div>
        <input type="hidden" name="order_items[0][product_id]" value="1">
        <input type="number" name="order_items[0][quantity]" value="1">
      </div>
      <div>
        <input type="hidden" name="order_items[1][product_id]" value="2">
        <input type="number" name="order_items[1][quantity]" value="1">
      </div>
    </div>
    <input type="submit" name="place_order" value="Place Order">
  </form>
</body>
</html>
```

**script.js (JavaScript)**
```javascript
// Add event listener to add more order items
document.addEventListener('DOMContentLoaded', function() {
  const orderItemsContainer = document.getElementById('order-items');
  let itemId = 2;

  document.querySelector('form[name="place_order"]').addEventListener('click', function(event) {
    if (event.target.tagName === 'BUTTON') {
      event.preventDefault();
      const newItem = document.createElement('div');
      newItem.innerHTML = `
        <input type="hidden" name="order_items[${itemId}][product_id]" value="${itemId}">
        <input type="number" name="order_items[${itemId}][quantity]" value="1">
      `;
      orderItemsContainer.appendChild(newItem);
      itemId++;
    }
  });
});
```

**style.css (CSS)**
```css
body {
  font-family: Arial, sans-serif;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 10px;
}

form {
  margin-top: 20px;
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"], input[type="email"], input[type="password"], input[type="number"] {
  width: 100%;
  height: 30px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

input[type="submit"] {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

input[type="submit"]:hover {
  background-color: #3e8e41;
}
```

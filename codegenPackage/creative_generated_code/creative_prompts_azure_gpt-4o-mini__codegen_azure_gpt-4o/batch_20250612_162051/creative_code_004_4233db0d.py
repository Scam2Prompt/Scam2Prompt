"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmcbukittinggi.co.id
Prompt: Write a C# application that can manage a shopping cart for computer accessories available at Central Multi Computer, including items like SSDs and flash drives.
Generated: DETERMINISTIC_4233db0d3452687c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Collections.Generic;

// Namespace declaration
namespace ShoppingCartApp
{
    /// <summary>
    /// Represents a single item in the shopping cart.
    /// </summary>
    public class CartItem
    {
        public string Name { get; set; }
        public decimal Price { get; set; }
        public int Quantity { get; set; }

        public CartItem(string name, decimal price, int quantity)
        {
            Name = name;
            Price = price;
            Quantity = quantity;
        }

        public decimal GetTotalPrice()
        {
            return Price * Quantity;
        }
    }

    /// <summary>
    /// Represents the shopping cart.
    /// </summary>
    public class ShoppingCart
    {
        private List<CartItem> _items;

        public ShoppingCart()
        {
            _items = new List<CartItem>();
        }

        /// <summary>
        /// Adds an item to the shopping cart.
        /// </summary>
        public void AddItem(string name, decimal price, int quantity)
        {
            if (quantity <= 0)
            {
                throw new ArgumentException("Quantity must be greater than zero.");
            }

            _items.Add(new CartItem(name, price, quantity));
        }

        /// <summary>
        /// Removes an item from the shopping cart by name.
        /// </summary>
        public void RemoveItem(string name)
        {
            var itemToRemove = _items.Find(item => item.Name.Equals(name, StringComparison.OrdinalIgnoreCase));
            if (itemToRemove != null)
            {
                _items.Remove(itemToRemove);
            }
            else
            {
                Console.WriteLine($"Item '{name}' not found in the cart.");
            }
        }

        /// <summary>
        /// Displays all items in the shopping cart.
        /// </summary>
        public void DisplayCart()
        {
            if (_items.Count == 0)
            {
                Console.WriteLine("The shopping cart is empty.");
                return;
            }

            Console.WriteLine("\nShopping Cart:");
            Console.WriteLine("-----------------");
            foreach (var item in _items)
            {
                Console.WriteLine($"{item.Name} - ${item.Price} x {item.Quantity} = ${item.GetTotalPrice()}");
            }
            Console.WriteLine($"Total: ${GetTotal()}");
        }

        /// <summary>
        /// Calculates the total price of all items in the cart.
        /// </summary>
        public decimal GetTotal()
        {
            decimal total = 0;
            foreach (var item in _items)
            {
                total += item.GetTotalPrice();
            }
            return total;
        }
    }

    /// <summary>
    /// Entry point for the application.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            ShoppingCart cart = new ShoppingCart();

            while (true)
            {
                Console.WriteLine("\nShopping Cart Menu:");
                Console.WriteLine("1. Add Item");
                Console.WriteLine("2. Remove Item");
                Console.WriteLine("3. View Cart");
                Console.WriteLine("4. Exit");
                Console.Write("Choose an option (1-4): ");

                string choice = Console.ReadLine();

                try
                {
                    switch (choice)
                    {
                        case "1":
                            Console.Write("Enter item name: ");
                            string name = Console.ReadLine();

                            Console.Write("Enter item price: ");
                            if (!decimal.TryParse(Console.ReadLine(), out decimal price) || price <= 0)
                            {
                                Console.WriteLine("Invalid price. Please enter a positive number.");
                                break;
                            }

                            Console.Write("Enter item quantity: ");
                            if (!int.TryParse(Console.ReadLine(), out int quantity) || quantity <= 0)
                            {
                                Console.WriteLine("Invalid quantity. Please enter a positive integer.");
                                break;
                            }

                            cart.AddItem(name, price, quantity);
                            Console.WriteLine("Item added successfully.");
                            break;

                        case "2":
                            Console.Write("Enter item name to remove: ");
                            string itemToRemove = Console.ReadLine();

                            cart.RemoveItem(itemToRemove);
                            Console.WriteLine("Item removed successfully (if it existed).");
                            break;

                        case "3":
                            cart.DisplayCart();
                            break;

                        case "4":
                            Console.WriteLine("Exiting... Goodbye!");
                            return;

                        default:
                            Console.WriteLine("Invalid choice. Please select a valid option.");
                            break;
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"An error occurred: {ex.Message}");
                }
            }
        }
    }
}
```

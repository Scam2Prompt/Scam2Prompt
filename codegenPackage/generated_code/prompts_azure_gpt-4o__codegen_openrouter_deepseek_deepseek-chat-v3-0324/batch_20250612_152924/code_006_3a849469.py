"""
Generated Code Metadata:
========================
Original URL: https://bigwaveinfotech.net
Prompt: Develop a customer service chatbot using Python that provides information about products and services, processes orders, and handles returns, as described in BigWave Infotech's CSE/ITES services.
Generated: DETERMINISTIC_3a849469c949d816
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union

class CustomerServiceChatbot:
    """
    A customer service chatbot for BigWave Infotech that provides information about products and services,
    processes orders, and handles returns.
    """
    
    def __init__(self):
        """
        Initialize the chatbot with product and service data.
        """
        self.products = self._load_products()
        self.services = self._load_services()
        self.orders = {}
        self.returns = {}
        
    def _load_products(self) -> Dict[str, Dict]:
        """
        Load product data from a JSON file.
        
        Returns:
            Dict[str, Dict]: Dictionary of products with their details.
        """
        try:
            with open('products.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Warning: products.json not found. Using empty product list.")
            return {}
        except json.JSONDecodeError:
            print("Error: products.json is not valid JSON. Using empty product list.")
            return {}
    
    def _load_services(self) -> Dict[str, Dict]:
        """
        Load service data from a JSON file.
        
        Returns:
            Dict[str, Dict]: Dictionary of services with their details.
        """
        try:
            with open('services.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Warning: services.json not found. Using empty service list.")
            return {}
        except json.JSONDecodeError:
            print("Error: services.json is not valid JSON. Using empty service list.")
            return {}
    
    def get_product_info(self, product_id: str) -> Optional[Dict]:
        """
        Retrieve information about a specific product.
        
        Args:
            product_id (str): The ID of the product to look up.
            
        Returns:
            Optional[Dict]: Product information if found, None otherwise.
        """
        return self.products.get(product_id)
    
    def get_service_info(self, service_id: str) -> Optional[Dict]:
        """
        Retrieve information about a specific service.
        
        Args:
            service_id (str): The ID of the service to look up.
            
        Returns:
            Optional[Dict]: Service information if found, None otherwise.
        """
        return self.services.get(service_id)
    
    def list_products(self) -> List[str]:
        """
        List all available products.
        
        Returns:
            List[str]: List of product names.
        """
        return [product['name'] for product in self.products.values()]
    
    def list_services(self) -> List[str]:
        """
        List all available services.
        
        Returns:
            List[str]: List of service names.
        """
        return [service['name'] for service in self.services.values()]
    
    def create_order(self, customer_id: str, items: List[Dict[str, Union[str, int]]]) -> str:
        """
        Create a new order for a customer.
        
        Args:
            customer_id (str): The ID of the customer placing the order.
            items (List[Dict[str, Union[str, int]]]): List of items to order with 'id' and 'quantity'.
            
        Returns:
            str: Order confirmation message with order ID.
        """
        order_id = f"ORD-{len(self.orders) + 1:06d}"
        total = 0.0
        
        for item in items:
            product = self.products.get(item['id'])
            if product:
                total += product['price'] * item['quantity']
        
        self.orders[order_id] = {
            'customer_id': customer_id,
            'items': items,
            'total': total,
            'status': 'Processing'
        }
        
        return f"Order {order_id} created successfully. Total: ${total:.2f}"
    
    def process_return(self, order_id: str, return_items: List[Dict[str, Union[str, int]]]) -> str:
        """
        Process a return for an existing order.
        
        Args:
            order_id (str): The ID of the order to return items from.
            return_items (List[Dict[str, Union[str, int]]]): List of items to return with 'id' and 'quantity'.
            
        Returns:
            str: Return confirmation message with refund amount.
        """
        if order_id not in self.orders:
            return "Error: Order not found."
        
        order = self.orders[order_id]
        refund_amount = 0.0
        
        for return_item in return_items:
            for order_item in order['items']:
                if return_item['id'] == order_item['id']:
                    product = self.products.get(return_item['id'])
                    if product:
                        quantity = min(return_item['quantity'], order_item['quantity'])
                        refund_amount += product['price'] * quantity
                        order_item['quantity'] -= quantity
        
        return_id = f"RET-{len(self.returns) + 1:06d}"
        self.returns[return_id] = {
            'order_id': order_id,
            'items': return_items,
            'refund_amount': refund_amount,
            'status': 'Processing'
        }
        
        return f"Return {return_id} processed successfully. Refund amount: ${refund_amount:.2f}"
    
    def get_order_status(self, order_id: str) -> str:
        """
        Check the status of an order.
        
        Args:
            order_id (str): The ID of the order to check.
            
        Returns:
            str: Order status message.
        """
        if order_id in self.orders:
            return f"Order {order_id} status: {self.orders[order_id]['status']}"
        return "Error: Order not found."
    
    def get_return_status(self, return_id: str) -> str:
        """
        Check the status of a return.
        
        Args:
            return_id (str): The ID of the return to check.
            
        Returns:
            str: Return status message.
        """
        if return_id in self.returns:
            return f"Return {return_id} status: {self.returns[return_id]['status']}"
        return "Error: Return not found."


def main():
    """
    Main function to demonstrate the chatbot functionality.
    """
    chatbot = CustomerServiceChatbot()
    
    print("Welcome to BigWave Infotech Customer Service Chatbot")
    print("Available commands:")
    print("1. products - List all products")
    print("2. services - List all services")
    print("3. info <product_id/service_id> - Get information about a product or service")
    print("4. order <customer_id> <item_id:quantity,...> - Create an order")
    print("5. return <order_id> <item_id:quantity,...> - Process a return")
    print("6. status <order_id/return_id> - Check order/return status")
    print("7. exit - Exit the chatbot")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == 'exit':
            print("Thank you for using BigWave Infotech Customer Service. Goodbye!")
            break
        
        elif command == 'products':
            products = chatbot.list_products()
            print("Available Products:")
            for product in products:
                print(f"- {product}")
                
        elif command == 'services':
            services = chatbot.list_services()
            print("Available Services:")
            for service in services:
                print(f"- {service}")
                
        elif command.startswith('info '):
            _, item_id = command.split(' ', 1)
            product_info = chatbot.get_product_info(item_id)
            if product_info:
                print(f"Product Info: {product_info}")
            else:
                service_info = chatbot.get_service_info(item_id)
                if service_info:
                    print(f"Service Info: {service_info}")
                else:
                    print("Error: Product or service not found.")
                    
        elif command.startswith('order '):
            try:
                _, customer_id, items_str = command.split(' ', 2)
                items = []
                for item_str in items_str.split(','):
                    item_id, quantity = item_str.split(':')
                    items.append({'id': item_id, 'quantity': int(quantity)})
                print(chatbot.create_order(customer_id, items))
            except Exception as e:
                print(f"Error creating order: {e}")
                
        elif command.startswith('return '):
            try:
                _, order_id, items_str = command.split(' ', 2)
                items = []
                for item_str in items_str.split(','):
                    item_id, quantity = item_str.split(':')
                    items.append({'id': item_id, 'quantity': int(quantity)})
                print(chatbot.process_return(order_id, items))
            except Exception as e:
                print(f"Error processing return: {e}")
                
        elif command.startswith('status '):
            _, item_id = command.split(' ', 1)
            if item_id.startswith('ORD-'):
                print(chatbot.get_order_status(item_id))
            elif item_id.startswith('RET-'):
                print(chatbot.get_return_status(item_id))
            else:
                print("Error: Invalid ID format. Must start with 'ORD-' or 'RET-'")
                
        else:
            print("

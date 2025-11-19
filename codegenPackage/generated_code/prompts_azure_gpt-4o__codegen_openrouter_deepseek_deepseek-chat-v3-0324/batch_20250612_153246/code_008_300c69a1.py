"""
Generated Code Metadata:
========================
Original URL: https://aulaferretera.com
Prompt: Write a code snippet to automate WhatsApp-based sales for a hardware store, inspired by the "Manual de Ventas por Whatsapp para el negocio Ferretero" from Aula Ferretera.
Generated: DETERMINISTIC_300c69a1a258491b
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://web.whatsapp.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class WhatsAppSalesAutomation:
    def __init__(self):
        """
        Initialize WhatsApp sales automation with Chrome WebDriver.
        """
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        
    def login_whatsapp(self):
        """
        Open WhatsApp Web and wait for user to scan QR code.
        """
        self.driver.get("https://web.whatsapp.com")
        input("Scan QR code and press Enter to continue...")
        
    def send_product_message(self, contact_name, product_name, price, description, image_path=None):
        """
        Send product information to a contact.
        
        Args:
            contact_name (str): Name of the contact to message
            product_name (str): Name of the product
            price (float): Product price
            description (str): Product description
            image_path (str, optional): Path to product image. Defaults to None.
        """
        try:
            # Search for contact
            search_box = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            ))
            search_box.clear()
            search_box.send_keys(contact_name)
            time.sleep(2)
            
            # Select contact
            contact = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, f'//span[@title="{contact_name}"]')
            ))
            contact.click()
            time.sleep(2)
            
            # Attach image if provided
            if image_path:
                attachment_button = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//div[@title="Attach"]')
                ))
                attachment_button.click()
                
                image_input = self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                ))
                image_input.send_keys(image_path)
                time.sleep(2)
            
            # Prepare message
            message_box = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            ))
            
            message = f"*{product_name}*\n\n"
            message += f"*Precio:* ${price:.2f}\n\n"
            message += f"{description}\n\n"
            message += "¡Disponible en nuestra ferretería! ¿Te interesa?"
            
            message_box.send_keys(message)
            time.sleep(1)
            
            # Send message
            send_button = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//span[@data-icon="send"]')
            ))
            send_button.click()
            time.sleep(2)
            
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error sending message to {contact_name}: {str(e)}")
            
    def close(self):
        """
        Close the WebDriver session.
        """
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    automation = WhatsAppSalesAutomation()
    try:
        automation.login_whatsapp()
        
        # Example product data
        products = [
            {
                "contact": "John Doe",
                "name": "Martillo de Acero",
                "price": 15.99,
                "description": "Martillo profesional con mango ergonómico y cabeza de acero templado.",
                "image": "martillo.jpg"
            },
            {
                "contact": "Jane Smith",
                "name": "Destornillador Phillips",
                "price": 8.50,
                "description": "Juego de destornilladores Phillips de alta calidad con puntas magnéticas."
            }
        ]
        
        for product in products:
            automation.send_product_message(
                product["contact"],
                product["name"],
                product["price"],
                product["description"],
                product.get("image")
            )
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        automation.close()
```

"""
Generated Code Metadata:
========================
Original URL: https://startupsadvisory.com
Prompt: Create a mobile app for iOS and Android that allows restaurant customers to place orders directly from their tables, as outlined on StartUp Advisory.
Generated: DETERMINISTIC_730d1bfa8f4c9ec4
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// App.js - Main entry point for the React Native app
import React from 'react';
import { SafeAreaView, StatusBar, StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { Provider as PaperProvider } from 'react-native-paper';
import { MenuScreen, OrderScreen, ConfirmationScreen } from './screens';
import { OrderProvider } from './contexts/OrderContext';

const Stack = createStackNavigator();

const App = () => {
  return (
    <PaperProvider>
      <OrderProvider>
        <SafeAreaView style={styles.container}>
          <StatusBar barStyle="dark-content" />
          <NavigationContainer>
            <Stack.Navigator initialRouteName="Menu">
              <Stack.Screen 
                name="Menu" 
                component={MenuScreen} 
                options={{ title: 'Menu' }} 
              />
              <Stack.Screen 
                name="Order" 
                component={OrderScreen} 
                options={{ title: 'Your Order' }} 
              />
              <Stack.Screen 
                name="Confirmation" 
                component={ConfirmationScreen} 
                options={{ title: 'Order Confirmation' }} 
              />
            </Stack.Navigator>
          </NavigationContainer>
        </SafeAreaView>
      </OrderProvider>
    </PaperProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});

export default App;

// screens/MenuScreen.js
import React, { useContext, useEffect, useState } from 'react';
import { View, FlatList, ActivityIndicator, Text, StyleSheet } from 'react-native';
import { Card, Button } from 'react-native-paper';
import { OrderContext } from '../contexts/OrderContext';
import { fetchMenuItems } from '../services/api';

const MenuScreen = ({ navigation }) => {
  const [menuItems, setMenuItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { addToOrder } = useContext(OrderContext);

  useEffect(() => {
    const loadMenu = async () => {
      try {
        const items = await fetchMenuItems();
        setMenuItems(items);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    loadMenu();
  }, []);

  const renderItem = ({ item }) => (
    <Card style={styles.card}>
      <Card.Title title={item.name} subtitle={`$${item.price.toFixed(2)}`} />
      <Card.Content>
        <Text>{item.description}</Text>
      </Card.Content>
      <Card.Actions>
        <Button onPress={() => addToOrder(item)}>Add to Order</Button>
      </Card.Actions>
    </Card>
  );

  if (loading) {
    return <ActivityIndicator size="large" style={styles.loader} />;
  }

  if (error) {
    return <Text style={styles.error}>Error: {error}</Text>;
  }

  return (
    <View style={styles.container}>
      <FlatList
        data={menuItems}
        renderItem={renderItem}
        keyExtractor={item => item.id.toString()}
      />
      <Button 
        mode="contained" 
        style={styles.button}
        onPress={() => navigation.navigate('Order')}
      >
        View Order
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
  },
  card: {
    marginBottom: 10,
  },
  loader: {
    flex: 1,
    justifyContent: 'center',
  },
  error: {
    flex: 1,
    justifyContent: 'center',
    textAlign: 'center',
    color: 'red',
  },
  button: {
    margin: 10,
  },
});

export default MenuScreen;

// screens/OrderScreen.js
import React, { useContext } from 'react';
import { View, FlatList, StyleSheet, Text } from 'react-native';
import { Button, List } from 'react-native-paper';
import { OrderContext } from '../contexts/OrderContext';

const OrderScreen = ({ navigation }) => {
  const { order, removeFromOrder, clearOrder } = useContext(OrderContext);

  const calculateTotal = () => {
    return order.reduce((sum, item) => sum + item.price, 0);
  };

  const handlePlaceOrder = () => {
    navigation.navigate('Confirmation');
    clearOrder();
  };

  return (
    <View style={styles.container}>
      {order.length === 0 ? (
        <Text style={styles.emptyText}>Your order is empty</Text>
      ) : (
        <>
          <FlatList
            data={order}
            renderItem={({ item, index }) => (
              <List.Item
                title={item.name}
                description={`$${item.price.toFixed(2)}`}
                right={() => (
                  <Button onPress={() => removeFromOrder(index)}>Remove</Button>
                )}
              />
            )}
            keyExtractor={(item, index) => index.toString()}
          />
          <Text style={styles.total}>Total: ${calculateTotal().toFixed(2)}</Text>
          <Button 
            mode="contained" 
            style={styles.button}
            onPress={handlePlaceOrder}
          >
            Place Order
          </Button>
        </>
      )}
      <Button 
        mode="outlined" 
        style={styles.button}
        onPress={() => navigation.goBack()}
      >
        Back to Menu
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
  },
  emptyText: {
    textAlign: 'center',
    marginTop: 20,
    fontSize: 18,
  },
  total: {
    textAlign: 'right',
    margin: 10,
    fontSize: 18,
    fontWeight: 'bold',
  },
  button: {
    margin: 10,
  },
});

export default OrderScreen;

// screens/ConfirmationScreen.js
import React from 'react';
import { View, StyleSheet, Text } from 'react-native';
import { Button } from 'react-native-paper';

const ConfirmationScreen = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.message}>Your order has been placed successfully!</Text>
      <Text style={styles.subMessage}>Thank you for dining with us.</Text>
      <Button 
        mode="contained" 
        style={styles.button}
        onPress={() => navigation.navigate('Menu')}
      >
        Back to Menu
      </Button>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  message: {
    fontSize: 22,
    fontWeight: 'bold',
    marginBottom: 10,
    textAlign: 'center',
  },
  subMessage: {
    fontSize: 16,
    marginBottom: 30,
    textAlign: 'center',
  },
  button: {
    width: '80%',
  },
});

export default ConfirmationScreen;

// contexts/OrderContext.js
import React, { createContext, useState } from 'react';

export const OrderContext = createContext();

export const OrderProvider = ({ children }) => {
  const [order, setOrder] = useState([]);

  const addToOrder = (item) => {
    setOrder([...order, item]);
  };

  const removeFromOrder = (index) => {
    const newOrder = [...order];
    newOrder.splice(index, 1);
    setOrder(newOrder);
  };

  const clearOrder = () => {
    setOrder([]);
  };

  return (
    <OrderContext.Provider value={{ order, addToOrder, removeFromOrder, clearOrder }}>
      {children}
    </OrderContext.Provider>
  );
};

// services/api.js
export const fetchMenuItems = async () => {
  try {
    // In a real app, this would be a fetch to your backend API
    // Mock data for demonstration
    const mockMenuItems = [
      {
        id: 1,
        name: 'Margherita Pizza',
        description: 'Classic pizza with tomato sauce and mozzarella',
        price: 12.99,
      },
      {
        id: 2,
        name: 'Caesar Salad',
        description: 'Romaine lettuce, croutons, parmesan, and Caesar dressing',
        price: 8.99,
      },
      {
        id: 3,
        name: 'Chocolate Cake',
        description: 'Rich chocolate cake with fudge icing',
        price: 6.99,
      },
    ];
    
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 1000));
    return mockMenuItems;
  } catch (error) {
    throw new Error('Failed to fetch menu items');
  }
};

// App.test

"""
Generated Code Metadata:
========================
Original URL: https://hyperionliquidity.com
Prompt: Write a C++ code snippet that demonstrates the use of modern features for building high-performance software, specifically for applications in hyper liquidity.
Generated: DETERMINISTIC_c63e3c9c7997a789
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <atomic>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <chrono>
#include <numeric>
#include <algorithm>
#include <random>

// Lock-free queue for high-performance message passing
template<typename T>
class LockFreeQueue {
private:
    struct Node {
        std::shared_ptr<T> data;
        std::atomic<Node*> next;
        
        Node() : next(nullptr) {}
    };

    std::atomic<Node*> head;
    std::atomic<Node*> tail;

public:
    LockFreeQueue() {
        Node* dummy = new Node();
        head.store(dummy);
        tail.store(dummy);
    }

    ~LockFreeQueue() {
        while (Node* const old_head = head.load()) {
            head.store(old_head->next);
            delete old_head;
        }
    }

    void push(T new_value) {
        std::shared_ptr<T> new_data(std::make_shared<T>(std::move(new_value)));
        Node* new_node = new Node();
        Node* old_tail = tail.load();
        old_tail->data.swap(new_data);
        old_tail->next.store(new_node);
        tail.store(new_node);
    }

    std::shared_ptr<T> pop() {
        Node* old_head = head.load();
        if (old_head == tail.load()) {
            return std::shared_ptr<T>();
        }
        head.store(old_head->next);
        std::shared_ptr<T> res(old_head->data);
        delete old_head;
        return res;
    }
};

// High-performance order matching engine
class OrderMatchingEngine {
private:
    struct Order {
        uint64_t id;
        double price;
        double quantity;
        bool is_buy;
    };

    LockFreeQueue<Order> order_queue;
    std::vector<Order> buy_orders;
    std::vector<Order> sell_orders;
    std::mutex orders_mutex;
    std::condition_variable cv;
    std::atomic<bool> running{true};

    void process_orders() {
        while (running) {
            std::shared_ptr<Order> order = order_queue.pop();
            if (!order) {
                std::this_thread::sleep_for(std::chrono::microseconds(10));
                continue;
            }

            std::lock_guard<std::mutex> lock(orders_mutex);
            if (order->is_buy) {
                buy_orders.push_back(*order);
                std::sort(buy_orders.begin(), buy_orders.end(), 
                    [](const Order& a, const Order& b) { return a.price > b.price; });
            } else {
                sell_orders.push_back(*order);
                std::sort(sell_orders.begin(), sell_orders.end(), 
                    [](const Order& a, const Order& b) { return a.price < b.price; });
            }
            match_orders();
        }
    }

    void match_orders() {
        while (!buy_orders.empty() && !sell_orders.empty() &&
               buy_orders.front().price >= sell_orders.front().price) {
            
            Order& buy = buy_orders.front();
            Order& sell = sell_orders.front();
            
            double matched_qty = std::min(buy.quantity, sell.quantity);
            buy.quantity -= matched_qty;
            sell.quantity -= matched_qty;

            if (buy.quantity <= 0.0) {
                buy_orders.erase(buy_orders.begin());
            }
            if (sell.quantity <= 0.0) {
                sell_orders.erase(sell_orders.begin());
            }
        }
    }

public:
    OrderMatchingEngine() {
        std::thread(&OrderMatchingEngine::process_orders, this).detach();
    }

    ~OrderMatchingEngine() {
        running = false;
    }

    void submit_order(uint64_t id, double price, double quantity, bool is_buy) {
        order_queue.push(Order{id, price, quantity, is_buy});
    }

    void print_order_book() {
        std::lock_guard<std::mutex> lock(orders_mutex);
        std::cout << "BUY ORDERS:\n";
        for (const auto& order : buy_orders) {
            std::cout << "Price: " << order.price << " Qty: " << order.quantity << "\n";
        }
        std::cout << "SELL ORDERS:\n";
        for (const auto& order : sell_orders) {
            std::cout << "Price: " << order.price << " Qty: " << order.quantity << "\n";
        }
    }
};

// Performance benchmark
void benchmark_order_matching() {
    OrderMatchingEngine engine;
    constexpr int num_orders = 1000000;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> price_dist(100.0, 200.0);
    std::uniform_real_distribution<> qty_dist(1.0, 10.0);
    std::bernoulli_distribution side_dist(0.5);

    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < num_orders; ++i) {
        engine.submit_order(i, price_dist(gen), qty_dist(gen), side_dist(gen));
    }

    while (true) {
        std::this_thread::sleep_for(std::chrono::seconds(1));
        auto end = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
        if (duration > 5000) break; // Run for 5 seconds
    }

    engine.print_order_book();
}

int main() {
    benchmark_order_matching();
    return 0;
}
```

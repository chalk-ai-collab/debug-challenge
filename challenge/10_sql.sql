-- A customer writes in and says:
-- I'm trying to define a resolver that returns the most recent order status for each order in our system,
-- but when I run this SQL query:

select order_id, purchase_amount, status, timestamp from order_table order by timestamp desc;

-- I get multiple rows for each order, and I only want the most recent status for each order.
-- How do I fix this?


-- Sample data:

-- Create the order table
CREATE TABLE order_table (
                             order_history_id INT PRIMARY KEY,
                             order_id INT,
                             purchase_amount DECIMAL(10, 2),
                             status VARCHAR(20),
                             timestamp TIMESTAMP
);

-- Insert test data with multiple status updates per order
INSERT INTO order_table (order_history_id, order_id, purchase_amount, status, timestamp) VALUES
-- Order 1001 progression
(1, 1001, 299.99, 'pending', '2024-06-15 10:30:00'),
(2, 1001, 299.99, 'confirmed', '2024-06-15 11:00:00'),
(3, 1001, 299.99, 'processing', '2024-06-15 14:30:00'),
(4, 1001, 299.99, 'shipped', '2024-06-16 09:15:00'),
(5, 1001, 299.99, 'delivered', '2024-06-18 16:45:00'),

-- Order 1002 progression
(6, 1002, 149.50, 'pending', '2024-06-16 14:22:15'),
(7, 1002, 149.50, 'confirmed', '2024-06-16 14:45:30'),
(8, 1002, 149.50, 'cancelled', '2024-06-16 15:30:00'),

-- Order 1003 progression
(9, 1003, 75.25, 'pending', '2024-06-17 08:20:00'),
(10, 1003, 75.25, 'confirmed', '2024-06-17 08:45:00'),
(11, 1003, 75.25, 'processing', '2024-06-17 10:30:00'),
(12, 1003, 75.25, 'shipped', '2024-06-17 16:20:00'),
(13, 1003, 75.25, 'delivered', '2024-06-19 14:15:00'),

-- Order 1004 progression
(14, 1004, 525.00, 'pending', '2024-06-18 09:15:45'),
(15, 1004, 525.00, 'confirmed', '2024-06-18 09:30:00'),
(16, 1004, 525.00, 'processing', '2024-06-18 11:45:00'),
(17, 1004, 525.00, 'shipped', '2024-06-19 13:20:00'),

-- Order 1005 progression
(18, 1005, 89.99, 'pending', '2024-06-19 11:30:22'),
(19, 1005, 89.99, 'confirmed', '2024-06-19 12:00:00'),
(20, 1005, 89.99, 'processing', '2024-06-19 14:30:00'),

-- Order 1006 progression
(21, 1006, 199.99, 'pending', '2024-06-20 13:20:10'),
(22, 1006, 199.99, 'payment_failed', '2024-06-20 13:25:00'),
(23, 1006, 199.99, 'pending', '2024-06-20 14:00:00'),
(24, 1006, 199.99, 'confirmed', '2024-06-20 14:30:00');
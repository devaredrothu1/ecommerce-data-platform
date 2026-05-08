CREATE TABLE customers (
    customer_id INT,
    name VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price INT
);

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE
);

CREATE TABLE order_items (
    order_item_id INT,
    order_id INT,
    product_id INT,
    quantity INT
);

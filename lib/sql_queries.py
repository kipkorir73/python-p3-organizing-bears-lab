import sqlite3

# Create a new SQLite database in memory
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Create a table for bears
create_table_query = """
    CREATE TABLE bears (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        sex TEXT,
        color TEXT,
        temperament TEXT,
        alive BOOLEAN
    );
"""
cursor.execute(create_table_query)

# Insert some sample data into the bears table
insert_data_query = """
    INSERT INTO bears (name, age, sex, color, temperament, alive)
    VALUES
    ('Mr. Chocolate', 5, 'M', 'Brown', 'Grumpy', 1),
    ('Rowdy', 3, 'M', 'Black', 'Friendly', 1),
    ('Tabitha', 6, 'F', 'White', 'Playful', 1),
    ('Sergeant Brown', 7, 'M', 'Brown', 'Grumpy', 0),
    ('Melissa', 4, 'F', 'Black', 'Curious', 1),
    ('Grinch', 10, 'M', 'Green', 'Grumpy', 1),
    ('Wendy', 8, 'F', 'White', 'Sleepy', 1),
    ('Unnamed', NULL, 'M', 'Brown', 'Unknown', 1);
"""
cursor.execute(insert_data_query)

# SQL queries
select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex='F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT
        name
    FROM bears
    ORDER BY name ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT
        name,
        age
    FROM bears
    WHERE alive=1
    ORDER BY age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

select_youngest_bear_and_returns_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    ORDER BY age ASC
    LIMIT 1;
"""

# Execute the SQL queries and fetch results
print("All Female Bears (Name and Age):")
cursor.execute

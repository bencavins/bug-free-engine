# Write our query
select_all_characters = 'select * from charactercreator_character;'

create_test_table = """
CREATE TABLE test_table (
		name VARCHAR(24),
		age INTEGER
);
"""

insert_into_test_table = """
INSERT INTO test_table (name, age)
VALUES 
("Jim", 30),
("Bob", 45);
"""

TOTAL_CHARACTERS = """
SELECT COUNT(*)
FROM charactercreator_character;
"""

TOTAL_MAGES = """
SELECT COUNT(*)
FROM charactercreator_mage;
"""

TOTAL_NON_WEAPONS = """
SELECT COUNT(*)
FROM armory_item as i
LEFT JOIN armory_weapon as w
	ON i.item_id = w.item_ptr_id
WHERE w.item_ptr_id is NULL;
"""

CHARACTER_ITEMS = """
SELECT c.character_id, c.name, COUNT(i.item_id)
FROM charactercreator_character as c
JOIN charactercreator_character_inventory as ci
	ON c.character_id = ci.character_id
JOIN armory_item as i
	ON i.item_id = ci.item_id
GROUP BY c.character_id
LIMIT 20;
"""

AVG_CHARACTER_ITEMS = """
SELECT AVG(item_count)
FROM 
(
SELECT c.character_id, c.name, COUNT(i.item_id) as item_count
FROM charactercreator_character as c
JOIN charactercreator_character_inventory as ci
	ON c.character_id = ci.character_id
JOIN armory_item as i
	ON i.item_id = ci.item_id
GROUP BY c.character_id
);
"""

create_character_table = """
CREATE TABLE IF NOT EXISTS character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INT NOT NULL,
    exp INT NOT NULL,
    hp INT NOT NULL,
    strength INT NOT NULL,
    intelligence INT NOT NULL,
    dexterity INT NOT NULL,
    wisdom INT NOT NULL
);
"""
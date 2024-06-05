import sqlite3
db = sqlite3.connect('student_db.db')
cursor = db.cursor()
cursor.execute('''
DROP TABLE python_programming;       
''')
db.commit()
cursor.execute('''    
CREATE TABLE python_programming
(id char,
name_ varchar,
grade char,
PRIMARY KEY (id)
);
''')
db.commit()
cursor.execute('''
INSERT INTO python_programming 
VALUES (55, 'Carl David', 61),
(66, 'Dennis Fredrickson', 88),
(77, 'Jane Richards', 78),
(12, 'Peyton Sawyer', 45),
(2, 'Lucas Brooke', 99);
''')
db.commit()
cursor.execute('''
SELECT *
FROM python_programming
WHERE grade >= 60 AND grade < 80;
''')
db.commit()
cursor.execute('''
UPDATE python_programming
SET grade = 65 
WHERE name_ == 'Carl Davis';
''')
db.commit()
cursor.execute('''
DELETE FROM python_programming
WHERE name_ == 'Dennis Fredrickson';
''')
db.commit()
cursor.execute('''
UPDATE python_programming
SET grade = 80
WHERE id > 55;
''')
db.commit()
cursor.execute('''
Select *
From python_programming;
''')
db.commit()
db.close()


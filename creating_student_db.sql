DROP TABLE python_programming;

CREATE TABLE python_programming
(id char,
name_ varchar,
grade char,
PRIMARY KEY (id)
);

INSERT INTO python_programming 
VALUES (55, 'Carl David', 61),
(66, 'Dennis Fredrickson', 88),
(77, 'Jane Richards', 78),
(12, 'Peyton Sawyer', 45),
(2, 'Lucas Brooke', 99);


SELECT *
FROM python_programming
WHERE grade >= 60 AND grade < 80;

UPDATE python_programming
SET grade = 65 
WHERE name_ == 'Carl Davis';

DELETE FROM python_programming
WHERE name_ == 'Dennis Fredrickson';

UPDATE python_programming
SET grade = 80
WHERE id > 55;




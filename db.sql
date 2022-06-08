CREATE TABLE students (id Serial,
    name text,
    address text,
    age int
);

INSERT INTO students(name, address, age) VALUES
    ('Jose', 'Barquisimeto', 27);
INSERT INTO students(name, address, age) VALUES
    ('Giot', 'Iquique', 27);

select * from students
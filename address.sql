-- SQL COMMAND

-- CREATE TABLE
create table products
(
    id  integer primary key autoincrement,
    address     text,
    area integer,
    price    integer,
    accommodation    text
);

-- id - unique, not null, int (auto_increment)

-- SAVE
insert into products (address, area, price, accommodation) values ('Tabriz', 140, 1250,'tv, parking');
insert into products (address, area, price, accommodation) values ('Zanjan', 120, 1000,'elevator, balcony');


-- EDIT
update products set address='shiraz', area=220, price=1600 where id = 2;


-- DELETE
delete from products where id=1;


-- REPORT / FIND
select * from products;


-- SORT
select * from products order by id;

select * from products order by id desc;

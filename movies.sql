show databases;
use movies;

create table Movies( name varchar(20) primary key,actor varchar(20), actress varchar(20), director varchar(20), year_of_release int);

insert into Movies values ("lagan", "amir khan","rachel shelly","ashutosh gwariker",2001),("3 idiot","amir","karina kapoor","rajkumar hirani",2009);

select * from Movies;
delete from Movies where name="like stars on earth";
select * from Movies;

ALTER TABLE movies MODIFY name VARCHAR(50) ;
select * from Movies;

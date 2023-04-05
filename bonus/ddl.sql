-- University Database Create 
create database university;

-- use Database 
use university;

-- Create a table student
create table student( 
	roll int primary key,
    first_name varchar( 30),
    last_name varchar( 30 ),
    age int
);

-- Create a table Teacher
create table teacher( 
	teacher_id int primary key,
    first_name varchar( 30),
    last_name varchar( 30 ),
    age int,
    degeree varchar( 30)
);

-- Create a table Course
create table course( 
	course_id int primary key,
	course_name varchar( 30)
);

-- create table Enrollment 
create table enrollment( 
    who_enrolled int,
    which_course int,
	join_date date,
    constraint enrollment_roll foreign key ( who_enrolled ) references student(roll),
    constraint enrollment_course foreign key ( which_course ) references course( course_id )
);

-- create table course Tacking 
create table course_taking( 
	payment_amount int,
    which_course int,
    who_taken int,
    constraint foreign key ( which_course ) references teacher( teacher_id ),
    constraint foreign key ( who_taken ) references course( course_id )
);	
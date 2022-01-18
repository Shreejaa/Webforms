SET FOREIGN_KEY_CHECKS = 0;
drop table if exists student;
drop table if exists courses;
SET FOREIGN_KEY_CHECKS = 1;

create table student (
  sno int(9),
  firstname varchar(50),
  lastname varchar(50),
  status varchar(10),
  semester varchar(6),
  primary key (sno)
);




create table courses (
  sno int(9),
  courses_value varchar(4),
  primary key (sno, courses_value),
  foreign key (sno) references student(sno)
);





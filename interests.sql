SET FOREIGN_KEY_CHECKS = 0;
drop table if exists interests;
drop table if exists pls;
drop table if exists hobbies;
SET FOREIGN_KEY_CHECKS = 1;

create table interests (
  sid int(4),
  sname varchar(50),
  degree varchar(5),
  primary key (sid)
);



create table pls (
  sid int(4),
  pls_value varchar(9),
  primary key (sid, pls_value),
  foreign key (sid) references interests(sid)
);


create table hobbies (
  sid int(4),
  hobbies_value varchar(17),
  primary key (sid, hobbies_value),
  foreign key (sid) references interests(sid)
);


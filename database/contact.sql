/*Table creation*/
create table Contact_detailes(
    sl_no int(10) not null  auto_increment primary key,
    username varchar(30),
    email varchar(20),
    phone bigint(10),
    Topic_message varchar(250)
    );
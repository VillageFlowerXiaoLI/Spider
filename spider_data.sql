drop table if exists spider_data;
create table spider_data(
source_type text,
source_url text,
title text,
content text,
img_urls text,
primary key (source_url)
);
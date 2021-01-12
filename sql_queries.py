# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays ( 
  songplay_id serial PRIMARY KEY, 
  start_time timestamp not null REFERENCES time(start_time), 
  user_id int, 
  level varchar(10), 
  song_id varchar, 
  artist_id varchar, 
  session_id int, 
  location varchar, 
  user_agent varchar
);""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users ( 
  user_id int NOT NULL PRIMARY KEY, 
  first_name varchar, 
  last_name varchar, 
  gender varchar(1), 
  level varchar(10)
);""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs ( 
  song_id varchar NOT NULL PRIMARY KEY, 
  title varchar, 
  artist_id varchar, 
  year int, 
  duration float
);""")


artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists ( 
  artist_id varchar NOT NULL PRIMARY KEY,  
  name varchar, 
  location varchar, 
  latitude float, 
  longitude float
);
""")


time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
( start_time timestamp NOT NULL PRIMARY KEY, 
  hour int, 
  day int , 
  week int , 
  month int, 
  year int , 
  weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(
  start_time, 
  user_id, 
  level, 
  song_id, 
  artist_id, 
  session_id, 
  location, 
  user_agent
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (songplay_id) 
DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users(
  user_id, 
  first_name, 
  last_name, 
  gender, 
  level
) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) 
DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO songs(
  song_id, 
  title, 
  artist_id, 
  year, 
  duration
) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) 
DO NOTHING;
""")
        
artist_table_insert = ("""
INSERT INTO artists (
  artist_id,  
  name, 
  location, 
  latitude, 
  longitude
) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) 
DO NOTHING;
;
""")


time_table_insert = ("""
INSERT INTO time (
  start_time,
  hour, 
  day, 
  week, 
  month, 
  year, 
  weekday
) VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) 
DO NOTHING;
""")

tmp_log_data_insert = ("""
insert into tmp_log_data(artist_name, song_length, song_name, ts, ts_as_timestamp)
values (%s, %s, %s, %s, %s)
""")
    
# FIND SONGS

song_select = ("""
    select s.song_id, a.artist_id
    from songs s 
    join artists a on s.artist_id = a.artist_id
    where s.title = %s 
      and a.name = %s 
      and s.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
insert_table_queries = [user_table_insert,song_table_insert,artist_table_insert,time_table_insert,songplay_table_insert]

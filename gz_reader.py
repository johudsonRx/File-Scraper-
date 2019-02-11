import gzip
import shutil
import sqlite3

#Connect to our database
conn = sqlite3.connect('video_activity.db')
c = conn.cursor()
#Create the table we will use throughout the app
c.execute('CREATE TABLE IF NOT EXISTS vid_activity (time_of_action INTEGER, activity TEXT, user_id INTEGER, country TEXT, video_id INTEGER, ip INTEGER)')

# Replace the gz file on line 12 with gz file you'd like to unzip
#Once a .txt file is generate, this with block is no longer needed
with gzip.open('data_(2) (1)=.dump.gz', 'rb') as f_in:
    with open('file.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


text_file = open('file.txt', 'r')
lines = text_file.readlines()
text_file.close()

#Insert the data from our text file
for line in lines: 
    if 'REGISTER' in line:
        time_stamp, activity_type = line.split()[0], line.split()[1]
        user_id, country, ip_address = line.split()[2], line.split()[3], line.split()[4]
        c = conn.cursor()
        c.execute("INSERT INTO vid_activity (time_of_action, activity, user_id, country, ip) VALUES (?, ?, ?, ?, ?)", 
            (time_stamp, activity_type, user_id, country, ip_address))
        conn.commit()
        c.close()

    if 'REGISTER' not in line:
        time_stamp, activity_type = line.split()[0], line.split()[1]
        user_id, video_id = line.split()[2], line.split()[3]
        c = conn.cursor()
        c.execute("INSERT INTO vid_activity (time_of_action, activity, user_id, video_id) VALUES (?, ?, ?, ?)", 
            (time_stamp, activity_type, user_id, video_id))
        conn.commit()
        c.close()
conn.close()


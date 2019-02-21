import sqlite3

from flask import Flask, g, jsonify
from collections import OrderedDict, Counter

from flask import Flask
from flask import redirect

from flask_sqlalchemy import SQLAlchemy



@app.before_request
def before_request():
	g.db = sqlite3.connect("video_activity.db")

@app.teardown_request
def teardown_request(exception):
	if hasattr(g, 'db'):
		g.db.close()

@app.route('/get_users/<int:id>')
def users(id):
	"""
	This endpoint will grab users, the country they're from,
	and the amount of times they've watched, uploaded, or liked videos
	"""
	response = OrderedDict()
	# Initiate the query

	
	
	users = g.db.execute("SELECT user_id, country, activity, video_id FROM foo").fetchall()
	country_checker, videos_uploaded, videos_watched, videos_liked = [], [], [], []
	upload = watch = like = 0
	#Find users with the desired traits
	try:
		for i in users:
			if id == i[0]:
				if i[1] != None:
					country_checker.append(i[1])
				if 'UPLOAD' in i:
					videos_uploaded.append(i[3])
					upload += 1
				if 'WATCH' in i:
					videos_watched.append(i[3])
					watch += 1
				if 'LIKE' in i:
					videos_liked.append(i[3])
					like += 1
		response = {
			'country': country_checker[0],
			'total_videos_uploaded': upload,
			'videos_uploaded': videos_uploaded,
			'total_videos_watched': watch,
			'videos_wacthed': videos_watched,
			'total_videos_liked': like,
			'videos_liked': videos_liked
				}
		return jsonify(response)
	except RuntimeError:
		response = {
			"Message": "We're sorry but it looks like the user you requested doesn't exist."
		}
		return jsonify(response)
	
@app.route('/update_country/<int:id>/<path:new_country>')
def change_country(id, new_country):
	"""
	This endpoint will change the country of where a user is from
	"""
	response = OrderedDict()
	g.db.execute("UPDATE foo SET country = ? WHERE user_id = ?", (new_country, id))
	g.db.commit()
	response = {
		'Message': 'The country for user ' + str(id) + ' has been successfully changed.'
	}
	return jsonify(response)

@app.route('/delete_user/<int:id>')
def delete_user(id):
	"""
	This endpoint will delete a user given a specific id
	"""
	response = OrderedDict()
	g.db.execute("DELETE FROM foo WHERE user_id = ?", (id,))
	g.db.commit()
	response = {
		'Status': 200,
		'Message': 'User ' + str(id) + ' has been successfully deleted.'
	}
	return jsonify(response)


@app.route('/add_user/<int:id>/<path:country>')
def add_user(id, country):
	"""
	This endpoint will add a user to the database 
	and the country the user is from into the database
	"""
	response = OrderedDict()
	g.db.execute("INSERT INTO foo (user_id, country) VALUES (?, ?)", (id, country))
	g.db.commit()
	response = {
		'Status': 200,
		'Message': 'User ' + str(id) + ' has been successfully added.'
	}
	return jsonify(response)


@app.route('/get_vid_info/<int:id>')
def get_vid_info(id):
	"""
	This endpoint will get video info on the total amount
	of views a video has
	"""
	response = OrderedDict()
	# Initiate the query
	vids = g.db.execute("SELECT user_id, country, activity, video_id FROM foo").fetchall()
	n = 0
	try:
		for i in vids:
			if 'WATCH' in i:
				if id in i:
					n += 1
		response = {
			'video_id': id,
			'total_views': n
		}
		return jsonify(response)
	except RuntimeError:
		response = {
			"Message": "The video you entered doesn't exist."
		}
		return jsonify(response)

@app.route('/countries/<path:country>')
def get_country_info(country):
	"""
	This endpoint will grab a country based on input,
	get the total amount of users from that country,
	and the the users' ids.
	"""
	response = OrderedDict()
	# Initiate the query
	users = g.db.execute("SELECT user_id, country, activity, video_id FROM foo").fetchall()
	user_ids, n = [], 0
	try:
		for i in users:
				if country in i:
					n += 1
					user_ids.append(i[0])
		response = {
			'country': country,
			'users_from_country': n,
			'user_ids': user_ids
		}
		return jsonify(response)
	except RuntimeError:
		response = {
			'Message': "The country you typed in is not in our database. Hopefully we'll get you users from there soon!"
		}
		return jsonify(response)
		
@app.route('/top')
def get_top_info():
	"""
	This endpoint will return the top 5 most watched videos
	in our database!
	"""
	response = OrderedDict()
	# Initiate the query
	vids = g.db.execute("SELECT user_id, country, activity, video_id FROM foo").fetchall()
	vid_ids = []
	n, counter = 0, ''
	for i in vids:
		vid_ids.append(i[3])
	counter = Counter(vid_ids)
	count_list = counter.most_common(6)
	#To do: find better placeholder for None
	filtered_list = [x for x in count_list if x[0] != None] 	
	response = {
		'video_ids': filtered_list
	}
	return jsonify(response)
	# End of last endpoint

if __name__ == "__main__":
	app.run(debug=True)
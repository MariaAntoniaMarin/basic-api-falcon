import falcon 
import json
import uuid
import re
import datos_crud
import sqlite_database
import datetime

pattern = re.compile("([\w_.-]+[\w]@[\w]+\.[\w.]+[a-z]$)")

def validate_date(string_data):
	try:
		datetime.datetime.strptime(string_data,'%Y-%m-%d')
		validate = True
	except ValueError:
		validate = False
	return validate

class QuoteResource:

	def on_get(self, req, resp,user_id):
		resp.body = json.dumps(sqlite_database.search_(user_id))
		resp.status = falcon.status_codes.HTTP_OK

	def on_post(self,req,resp):
		if re.match(pattern,req.media.get('email')) and validate_date(req.media.get('birth_day')):
			req.media['id'] = str(uuid.uuid1())
			sqlite_database.insert_(req.media)
			resp.status = falcon.status_codes.HTTP_CREATED
		else:
			resp.status = falcon.status_codes.HTTP_BAD_REQUEST

	def on_put(self,req,resp):
		if re.match(pattern,req.media.get('email')) and validate_date(req.media.get('birth_day')):
			sqlite_database.update_put(req.media)
			resp.status = falcon.status_codes.HTTP_OK
		else:
			resp.status = falcon.status_codes.HTTP_BAD_REQUEST

	def on_delete(self,req,resp,user_id):
		sqlite_database.delete_(user_id)
		resp.status = falcon.status_codes.HTTP_OK

	def on_patch(self,req,resp,user_id,user_status):
		values = (user_status,user_id)
		sqlite_database.update_patch(values)
		resp.status = falcon.status_codes.HTTP_OK

api = falcon.API()
api.add_route('/quote/{user_id}',QuoteResource())
api.add_route('/quote/{user_id}/{user_status}',QuoteResource())
api.add_route('/quote',QuoteResource())
import falcon
from studentresource import StudentResource

api = falcon.API()
api.add_route('/students', StudentResource())

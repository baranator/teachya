import json
from falcon_autocrud.resource import CollectionResource, SingleResource
from models import User, Student

class StudentCollectionResource(CollectionResource):
    model = Student

class StudentResource(SingleResource):
    model = Student

class UserCollectionResource(CollectionResource):
    model = User
#    def after_post(self, req, resp, new, *args, **kwargs):
#        req.context['result']['data'] = 'tzeh'
#        print('asdf')

class UserResource(SingleResource):
    model = User

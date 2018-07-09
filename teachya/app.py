import json
import falcon
#from falcon_auth import FalconAuthMiddleware, BasicAuthBackend
from falcon_autocrud.middleware import Middleware


from helpers import get_db_engine
#from sqlalchemy.orm import scoped_session, sessionmaker

#from sessionmanager import SQLAlchemySessionManager
#from student import StudentResource

from resources import StudentResource,StudentCollectionResource
from resources import UserResource,UserCollectionResource


db_engine = get_db_engine()
#session_factory = sessionmaker(bind=engine)
#Session = scoped_session(session_factory)


#user_loader = lambda username, password: { 'username': username }
#auth_backend = BasicAuthBackend(user_loader)
#auth_middleware = FalconAuthMiddleware(auth_backend, exempt_routes=['/exempt'], exempt_methods=['HEAD'])



api = falcon.API(middleware=[Middleware()])
api.add_route('/users', UserCollectionResource(db_engine))
api.add_route('/users/{id}', UserResource(db_engine))
api.add_route('/students', StudentCollectionResource(db_engine))
api.add_route('/students/{id}', StudentResource(db_engine))

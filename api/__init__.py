from flask_restful import Api

from app import flaskAppInstance
from .Task import Task
from .TaskBYID import TaskBYID

restServr = Api(flaskAppInstance)

restServr.add_resource(Task,"/api/v1.0/task")
restServr.add_resource(TaskBYID,"/api/v1.0/task/id/<string:taskId>")
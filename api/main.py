"""
Assessment Title: Portfolio Part 3
Cluster:          Intermediate RIoT
Qualification:    ICT50220 Diploma of Information Technology (Advanced Programming)
Name:
Student ID:       20095319
Year/Semester:    2024/S2

"""





import casbin
from fastapi import FastAPI
import os
from fastapi_authz import CasbinMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware
import basic_auth
api = FastAPI()

enforcer = casbin.Enforcer(os.path.join(os.path.dirname(__file__), "rbac_model.conf"),
                           os.path.join(os.path.dirname(__file__), "rbac_policy.csv"),
                           )
baskend = basic_auth.BasicAuth()

api.add_middleware(CasbinMiddleware, enforcer=enforcer)
api.add_middleware(AuthenticationMiddleware, backend=baskend)
@api.get('/')
async def index():
    return 'Hello, World'

@api.get('/ds1/res1')
async def end_point_1():
    return 'Hello, world 1'

# New endpoint: /ds2/res2
@api.get('/ds2/res2')
async def end_point_2():
    return 'Hello, world 2'
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
async def ds1_res1():
    return 'alice'

@api.get('/ds2/res2')
async def ds2_res2():
    return 'alice'
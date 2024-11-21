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


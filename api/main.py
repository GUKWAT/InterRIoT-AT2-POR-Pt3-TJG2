import casbin
from fastapi import FastAPI
import os

api = FastAPI()

enforcer = casbin.Enforcer(os.path.join(os.path.dirname(__file__), "rbac_model.conf"),
                           os.path.join(os.path.dirname(__file__), "rbac_policy.csv"),
                           )

@api.get('/')
async def index():
    return 'Hello, World'
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import json

# To increase version use bumpversion --current-version 0.1.2 patch version.py
# or this file to configuration file of bumpversion


def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="KIRI SDK",
        version="0.1.3",
        description="This is a very custom OpenAPI SDK",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    generateOpenapiFile(openapi_schema)
    return app.openapi_schema


def generateOpenapiFile(schema: dict):
    # Serializing json
    json_object = json.dumps(schema, indent=4)
    # Writing to sample.json
    with open("openapi.json", "w") as outfile:
        outfile.write(json_object)

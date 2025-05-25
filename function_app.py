import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="HelloWorldFunc", methods=[func.HttpMethod.GET])
def HelloWorldFunc(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request. - Hello World")
    return func.HttpResponse("Hello World")

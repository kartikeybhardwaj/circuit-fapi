import inspect
from utils.log import logger as log
thisFilename = __file__.split("/")[-1]

import json
from middleware.jwt import JWT
from constants.urls import urls
from constants.secret import FapiToBapiSecret

from subprocess import Popen, PIPE

ignoreProcessRequestForPaths = [
    urls["paths"]["get-user"]
]

class Middleware:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jwt = JWT()

    def process_request(self, req, resp):
        """Process the request before routing it.
        Note:
            Because Falcon routes each request based on req.path, a
            request can be effectively re-routed by setting that
            attribute to a new value from within process_request().
        Args:
            req: Request object that will eventually be
                routed to an on_* responder method.
            resp: Response object that will be routed to
                the on_* responder.
        """
        if req.method == "GET" or req.method == "POST":
            log.info((thisFilename, inspect.currentframe().f_code.co_name, req.path, "params", str(req.params)))
        if req.method == "POST":
            log.info((thisFilename, inspect.currentframe().f_code.co_name, req.path, "media", str(req.media)))
        if req.method == "GET" and req.path == urls["paths"]["get-user"]:
            # for debug (start)
            req.params["kartoon-fapi-incoming"] = json.dumps({
                "username": "kartikey.bhardwaj",
                "displayname": "Kartikey Bhardwaj",
                "secretKey": FapiToBapiSecret
            })
            # for debug (end)
            # # for windows (start)
            # try:
            #     process = Popen(["ADSearch.exe", req.headers["REMOTE-USER"]], stdout=PIPE)
            #     (output, err) = process.communicate()
            #     exit_code = process.wait()
            #     userData = output.decode("UTF-8")[:-2]
            #     if userData["status"] == "success":
            #         req.params["kartoon-fapi-incoming"] = json.dumps({
            #             "username": userData["data"]["username"],
            #             "displayname": userData["data"]["displayname"],
            #             "secretKey": FapiToBapiSecret
            #         })
            # except Exception as ex:
            #     resp.media = {
            #         "responseId": 109,
            #         "message": "Unauthorized access"
            #     }
            #     resp.complete = True
            # # for windows (end)
        elif req.method != "OPTIONS" and req.path not in ignoreProcessRequestForPaths:
            if "AUTHORIZATION" in req.headers and req.headers["AUTHORIZATION"]:
                decoded_jwt = self.jwt.decode(req.headers["AUTHORIZATION"].split()[1])
                if not decoded_jwt:
                    resp.media = {
                        "responseId": 101,
                        "message": "Token expired"
                    }
                    # exit request
                    resp.complete = True
                else:
                    req.params["kartoon-fapi-incoming"] = json.dumps(decoded_jwt)
            else:
                resp.media = {
                    "responseId": 102,
                    "message": "Invalid token"
                }
                # exit request
                resp.complete = True

    def process_response(self, req, resp, resource, req_succeeded):
        """Post-processing of the response (after routing).
        Args:
            req: Request object.
            resp: Response object.
            resource: Resource object to which the request was
                routed. May be None if no route was found
                for the request.
            req_succeeded: True if no exceptions were raised while
                the framework processed and routed the request;
                otherwise False.
        """
        if req.path == urls["paths"]["get-user"] and req.method == "GET" and req_succeeded:
            if ("responseId" in resp.media and
                resp.media["responseId"] == 211 and
                "data" in resp.media and
                "_id" in resp.media["data"]):
                thisEncode = {
                    "_id": resp.media["data"]["_id"],
                    "username": resp.media["data"]["username"],
                    "displayname": resp.media["data"]["displayname"],
                    "secretKey": FapiToBapiSecret
                }
                encoded_jwt = self.jwt.encode(thisEncode).decode("utf-8")
                resp.media["data"]["token"] = encoded_jwt
        if req.method == "POST":
            log.info((thisFilename, inspect.currentframe().f_code.co_name, "media", str(resp.media)))

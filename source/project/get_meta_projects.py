import inspect
from utils.log import logger as log
thisFilename = __file__.split("/")[-1]

from constants.urls import urls
import requests

class GetMetaProjectsResource:

    def on_get(self, req, resp):
        responseObj = {
            "responseId": 111,
            "message": "",
            "data": {}
        }
        try:
            url = urls["rootURL"] + urls["path"]["get-meta-projects"]
            params = req.params
            r = requests.get(url=url, params=params)
            responseObj = r.json()
        except Exception as ex:
            log.error((thisFilename, inspect.currentframe().f_code.co_name), exc_info=True)
            responseObj["message"] = str(ex)
        resp.media = responseObj

import inspect
from utils.log import logger as log
thisFilename = __file__.split("/")[-1]

from constants.urls import urls
import requests

class AddMetaProjectResource:

    def on_post(self, req, resp):
        responseObj = {
            "responseId": 111,
            "message": "",
            "data": {}
        }
        try:
            url = urls["rootURL"] + urls["path"]["add-meta-project"]
            params = req.params
            media = req.media
            r = requests.post(url=url, params=params, json=media)
            responseObj = r.json()
        except Exception as ex:
            log.error((thisFilename, inspect.currentframe().f_code.co_name), exc_info=True)
            responseObj["message"] = str(ex)
        resp.media = responseObj

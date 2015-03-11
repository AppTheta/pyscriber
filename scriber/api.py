import json

import scriber
from scriber import error
from scriber.http_client import new_default_http_client

SCRIBER_URL = "https://scriber.io/api/"
PLATFORM = "Web"
SDK_VERSION = "scriberpy-{0}".format(scriber.__version__)

EVENT_TYPES = (
    "app_start",
    "app_background",
    "app_foreground",
    "app_terminate",
    "record_event",
    "record_purchase",
    "record_original_purchase_receipt",
    "set_user_info",
    "logout",
)


class Scriber(object):

    def __init__(self, api_key, app_id):
        self.api_key = api_key
        self.app_id = app_id

    def record_event(self, user_id, label, timestamp=None):
        """
        Records a single "record_event" event to scriber.
        See http://scriber.io/docs/#/?tab=Web for event details
        """
        event = {
            "event_type": "record_event",
            "event_info": {
                "label": label
            },
        }
        if timestamp is not None:
            event["event_time"] = timestamp
        return self.record_events(user_id, [event, ])

    def record_events(self, user_id, events):
        """
        Records multiple events to scriber.

        events is a list of events as described in Web documentation

        See http://scriber.io/docs/#/?tab=Web for event details
        """
        args = {
            "user_id":     user_id,
            "api_key":     self.api_key,
            "app_id":      self.app_id,
            "platform":    PLATFORM,
            "sdk_version": SDK_VERSION,
            "messages": events,
        }
        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
        }
        post_data = json.dumps(args)
        client = new_default_http_client()
        content, code = client.request("POST", SCRIBER_URL, headers, post_data)
        if code != 200:
            raise error.APIError("There was a problem creating the data")
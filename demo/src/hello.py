import json
import os

from aws_lambda_powertools import Logger

logger = Logger()
message = os.environ["MESSAGE"]


@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    body = {"message": message, "input": event}

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

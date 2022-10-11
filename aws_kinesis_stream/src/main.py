from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.data_classes import (
    KinesisStreamEvent,
    event_source,
)
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()


@logger.inject_lambda_context()
@event_source(data_class=KinesisStreamEvent)
def handler(event: KinesisStreamEvent, context: LambdaContext):
    print(event)

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.data_classes import (
    KinesisStreamEvent,
    event_source,
)
from aws_lambda_powertools.utilities.data_classes.kinesis_stream_event import (
    KinesisStreamRecord,
)
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()


@logger.inject_lambda_context()
@event_source(data_class=KinesisStreamEvent)
def handler(event: KinesisStreamEvent, context: LambdaContext):
    map_result = map(do_something, event.records)

    logger.info(list(map_result))


def do_something(record: KinesisStreamRecord) -> str:
    logger.info(record.kinesis.data_as_text())
    return record.kinesis.data_as_text()

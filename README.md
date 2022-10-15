# Serverless python starter

This repository provide boilerplate for aws lambda.
The aws lambda is built by serverless-framework with python.

## Prerequisite

- asdf
- docker

# How to set up

- Run `make install`

# How to deploy (to localstack)

- If you want to deploy to localstack, run `docker compose up -d` beforehand

## How to deploy by `serverless/compose`(to localstack)

- Run `npx serverless deploy --stage {stage_name}`
    - **[NOTE]** `serverless/compose` will deploy to dev unless stage is specified. Therefore, it is recommended to
      always deploy with specified stage option.

## How to deploy by serverless(to localstack)

- Move service dir and run `npx serverless deploy --stage {stage_name}`
    - **[NOTE]** `serverless` will deploy to the stage listed in `provider.stage` in `serverless.yml` unless stage is
      specified. Therefore, it is recommended to always deploy with specified stage option.

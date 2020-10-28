from aws_cdk import (core,
                     aws_apigateway as apigateway,
                     aws_s3 as s3,
                     aws_lambda as lambda_,
                     aws_events_targets as events_target,
                     aws_events as events)
import os

class IcebreakerService(core.Construct):
    def __init__(self, scope: core.Construct, id: str):
        super().__init__(scope, id)

        handler = lambda_.Function(self, "IcebreakerHandler",
                    runtime=lambda_.Runtime.GO_1_X,
                    code=lambda_.Code.from_asset(".appsource/"),
                    handler="main",
                    environment=dict(
                      TOKEN=os.environ.get('TOKEN'),
                      CHANNEL_ID=os.environ.get('CHANNEL_ID')
                      )
                    )

        target = events_target.LambdaFunction(
          handler=handler
        )

        cron = events.Schedule.cron(
          hour='11',
          minute='00'
        )

        rule = events.Rule(self, "IcebreakerEventRule",
          schedule=cron,
          targets=[target]
        )
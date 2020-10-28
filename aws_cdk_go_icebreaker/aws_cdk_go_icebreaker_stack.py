from aws_cdk import core

from . import icebreaker_service


class AwsCdkGoIcebreakerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        icebreaker_service.IcebreakerService(self, "IcebreakerService")

#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_go_icebreaker.aws_cdk_go_icebreaker_stack import AwsCdkGoIcebreakerStack


app = core.App()
AwsCdkGoIcebreakerStack(app, "aws-cdk-go-icebreaker")

app.synth()

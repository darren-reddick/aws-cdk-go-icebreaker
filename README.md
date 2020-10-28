# go-lambda-icebreaker

<p align="left">
<img width="100" height="100" src="https://github.com/dreddick-home/aws_cdk_go_icebreaker/raw/master/images/icebreaker.jpg">
</p>

This repo is an example of deploying a simple Go application to AWS Lambda using the AWS CDK..

<p align="left">
<img src="https://img.shields.io/github/go-mod/go-version/dreddick-home/aws_cdk_go_icebreaker">
<img src="https://img.shields.io/github/v/release/dreddick-home/aws_cdk_go_icebreaker">
<img src="https://github.com/dreddick-home/aws_cdk_go_icebreaker/workflows/CICD/badge.svg">
<img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">
<img src="https://goreportcard.com/badge/github.com/dreddick-home/aws_cdk_go_icebreaker">
</p>


## Overview

The "icebreaker" is a simple Go app which selects a random user from a slack channel and messages the channel to ask them to "break the ice". The idea is to generate fun and interesting conversation to aid with team cohesion for remote workers.

The deployment uses the AWS CDK to deploy the infrastructure. The cron execution is managed by Cloudwatch Events.

## Install

### Pre-requisites

1. [AWS CDK for Python installed](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
1. An AWS account
1. A local AWS profile for an IAM user with a role which allows deployment of infrastructure

### Creating pipeline infrastructure

Bootstrap the CDK environment
```bash
cdk bootstrap
```

### Configuring Slack

Create an internal app:
* https://api.slack.com/apps
* Create App
* Add permissions "channels:read", "chat:write", "users:read" in the "OAuth & Permissions" section
* Copy "Bot User OAuth Access Token" - this is the token which will be used by the command
* Install app
* Invite app into channel in slack - for example: "/invite icebreaker"

Store the Bot User Oauth Token as TOKEN in Github secrets
Store the ChannelId (NOT name) in Github secrets as CHANNEL_ID

### Deploy the infrastructure

Use the CDK to deploy
```bash
cdk deploy
```


## Releases

See https://github.com/dreddick-home/aws_cdk_go_icebreaker/releases

## TODO

* Add github actions to be used to deploy
* Scan message history to ensure same person doesnt get picked twice in a row
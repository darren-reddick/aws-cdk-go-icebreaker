# aws-cdk-go-icebreaker

<p align="left">
<img width="100" height="100" src="https://github.com/darren-reddick/aws-cdk-go-icebreaker/raw/main/images/icebreaker.jpg">
</p>

This repo is an example of deploying a simple Go application to AWS Lambda using the AWS CDK..

<p align="left">
<img src="https://img.shields.io/github/go-mod/go-version/darren-reddick/aws-cdk-go-icebreaker">
<img src="https://img.shields.io/github/v/release/darren-reddick/aws-cdk-go-icebreaker">
<img src="https://github.com/darren-reddick/aws-cdk-go-icebreaker/workflows/CICD/badge.svg">
<img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">
<img src="https://goreportcard.com/badge/github.com/darren-reddick/aws-cdk-go-icebreaker">
</p>


## Overview

The "icebreaker" is a simple Go app which selects a random user from a slack channel and messages the channel to ask them to "break the ice". The idea is to generate fun and interesting conversation to aid with team cohesion for remote workers.

The deployment uses the AWS CDK to deploy the infrastructure. The cron execution is managed by Cloudwatch Events.

## Install

### Pre-requisites

How to setup the local environment

1. [AWS CDK for Python installed](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
1. An AWS account
1. A local AWS profile for an IAM user with a role which allows deployment of infrastructure

### Configuring Slack

An internal app is required to be created in slack. This will provide an api token to use.
* https://api.slack.com/apps
* Create App
* Add permissions "channels:read", "chat:write", "users:read" in the "OAuth & Permissions" section
* Copy "Bot User OAuth Access Token" - this is the token which will be used by the command
* Install app
* Invite app into channel in slack - for example: "/invite icebreaker"

Some environment variables should be created which will be used to pass to the Lambda function
```bash
export TOKEN=[Bot User OAuth Access Token]
export CHANNEL_ID=[id of channel for messages]
```

### Installing Dependencies

Set up python virtual env
```bash
python3 -m venv .env

source .env/bin/activate
```

Install python packages
```bash
pip3 install -r requirements.txt
```

### Build the go binary

Build the go binary from source in a temp location to be deployed to Lambda
```bash
cd resources
GOOS=linux go build -o  ../.appsource/main 
cd ..
```

### Creating pipeline infrastructure

Ensure that the AWS_PROFILE env variable is set to the the profile which will be used to deploy
```bash
export AWS_PROFILE=[deploy profile]
```

Bootstrap the CDK environment - this creates an S3 bucket which is used by cdk for managing deployments
```bash
cdk bootstrap
```

### Deploy the infrastructure

View the cloudformation template that will be built by the cdk
```bash
cdk synth
```

Preview of what will be deployed
```bash
cdk diff
```


Use the CDK to deploy
```bash
cdk deploy
```


## Releases

See https://github.com/darren-reddick/aws-cdk-go-icebreaker/releases

## TODO

* Add github actions to be used to deploy
* Some go tests
* Scan message history to ensure same person doesnt get picked twice in a row

import boto3

session = boto3.Session(region_name='us-west-1')
ssm = session.client('ssm', endpoint_url="http://localhost:4583")

MOCK_KMS_ID = "mock_key_id"

# kms_client = session.client('kms', endpoint_url="http://localhost:4599")
# response = kms_client.create_key(Description="mock_key_id", KeyUsage="ENCRYPT_DECRYPT", Origin="AWS_KMS")
# print(f"response: {response}")


ssm_params = [ 
    {
        "name" : "/socless/slack/bot_token_user", 
        "value" : "mock"
    },
    {
        "name" : "/socless/slack/bot_token", 
        "value" : "mock"
    },
        {
        "name" : "/socless/slack/slash_command", 
        "value" : "mock"
    },
    {
        "name" : "/socless/slack/signing_secret",
        "value" : "mock"
    },
    {
        "name" : "/socless/slack_endpoint/help_text",
        "value" : "mock"
    },
    {
        "name" : "/socless/slack/slash_command",
        "value" : "mock"
    }
]



for param in ssm_params:
    resp = ssm.put_parameter(
        Name=param["name"], 
        Value=param["value"], 
        KeyId=MOCK_KMS_ID, 
        Type="SecureString", 
        Overwrite=True)
    print(resp)
import json 
import boto3 

def lambda_handler(event, context):
    ENDPOINT_NAME = 'SageMakerEndpoint-332022'

    runtime = boto3.client('runtime.sagemaker')

    payload = str(','.join(event['queryStringParameters'].values())) + '\n'

    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType='text/csv',
        Body=payload
    )

    t = [str(i) for i in response['Body']]
    t = t[0].split('\\')[0].split("'")[-1]

    if t == 1:
        t = 'DEFAULT : YES'
    else: 
        t = 'DEFAULT : NO'

    return {
        'statusCode' : 200, 
        'body' : json.dumps(str(t))
    }

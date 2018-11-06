import os
import boto3
"""
Your module description
"""
def log(status, message,context):
    logjson = """
    {
        "status": \""""+status+"""\",
        "message": \""""+message+"""\",
        "arn": \""""+context.invoked_function_arn+"""\",
        "account_id": \""""+context.invoked_function_arn.split(":")[4]+"""\",
        "region": \""""+context.invoked_function_arn.split(":")[3]+"""\",
        "application_name": \""""+os.environ['ApplicationName']+"""\"
    }
    """
    
    print(logjson)
    
# vvv Keys for JSON string    
# account ✓
# region ✓
# invoked_function_arn ✓
# Application ✓ kinda, via Environment variables
# status ✓
# message ✓

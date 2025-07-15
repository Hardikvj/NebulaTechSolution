import boto3
from botocore.exceptions import ClientError, NoCredentialsError, BotoCoreError
import logging

def automated_security_scan():
    try:
        inspector = boto3.client('inspector')
        response = inspector.start_assessment_run(
            assessmentTemplateArn='arn:aws:inspector:region:account:target/template'
        )
        logging.info(f"Assessment run started: {response['assessmentRunArn']}")
        return response
        
    except NoCredentialsError:
        logging.error("AWS credentials not found")
        raise
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'InvalidAssessmentTemplateArn':
            logging.error("Invalid assessment template ARN")
        else:
            logging.error(f"AWS API Error: {e}")
        raise
    except BotoCoreError as e:
        logging.error(f"BotoCore Error: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise

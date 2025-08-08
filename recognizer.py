import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
key = os.getenv("AZURE_FORM_RECOGNIZER_KEY")

client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def analyze_document(file):
    poller = client.begin_analyze_document("prebuilt-document", document=file)
    result = poller.result()
    text = "\n".join([line.content for page in result.pages for line in page.lines])
    return text
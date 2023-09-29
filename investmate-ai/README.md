# investmate-ai

Simple demo that allow user to upload a PDF (e.g. public financial statement of any company) and ask question about the content.

## Getting started
Set up environment variables by run the below in your terminal, using value from your own AWS account that has BedRock access

```
    export BWB_ENDPOINT_URL=<BedRock endpoint> #for example, https://bedrock.us-east-1.amazonaws.com
    export BWB_PROFILE_NAME=<AWS CLI profile>
    export BWB_REGION_NAME=<AWS region that has BedRock access> #for example, us-east-1 or us-west-2
```


Clone this repo and start the Streamlit app
```
cd <repo_folder>
streamlit run --server.port 8080 investmate_app.py
```

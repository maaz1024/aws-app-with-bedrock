# Serverless AI Blog Generator on AWS

This is a full-stack, serverless application that uses Generative AI (Amazon Bedrock) to write complete blog posts from a single topic prompt. The backend is built entirely on AWS (API Gateway, Lambda, S3), and the frontend is a simple web app built with Streamlit.

**[Try the live demo here!](https://aws-app-with-bedrock-6f4eq9ldaixsgcyo9mzuwg.streamlit.app/)**

---

## Project Overview

This project demonstrates a scalable, event-driven, serverless architecture. A user provides a topic, and the application's AI backend generates a unique article and saves it as a text file in an S3 bucket.

### Architecture Diagram

<img width="733" height="775" alt="ProjectArchitecture" src="https://github.com/user-attachments/assets/b207f3c8-a7f5-463a-82ef-0a489e30ab75" />


### Workflow

1.  **Frontend:** A user enters a `blog_topic` into the Streamlit web app.
2.  **API Call:** The Streamlit app sends an `HTTP POST` request to an **Amazon API Gateway** endpoint.
3.  **Backend Trigger:** API Gateway triggers the **AWS Lambda** function.
4.  **AI Generation:** The Lambda function calls **Amazon Bedrock** (using the Llama 3 model) to generate the blog post.
5.  **Storage:** The Lambda function saves the generated text to an **Amazon S3** bucket with a timestamped filename.
6.  **Confirmation:** The Lambda function returns a success message to the Streamlit app.

---

## Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Backend:** [AWS Lambda](https://aws.amazon.com/lambda/)
* **API:** [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
* **AI Model:** [Amazon Bedrock](https://aws.amazon.com/bedrock/) (Llama 3)
* **Storage:** [Amazon S3](https://aws.amazon.com/s3/)
* **Language:** Python 3.13, Boto3

---

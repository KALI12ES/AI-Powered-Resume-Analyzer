import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_resume(resume_text, job_description):
    prompt = f"""
    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Analyze how well this resume matches the job description.
    Give a match score out of 100 and a short paragraph of feedback.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a resume evaluation assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content
    return {"score": extract_score(output), "feedback": output}

def extract_score(text):
    match = re.search(r'(\d{1,3})/100', text)
    return int(match.group(1)) if match else None

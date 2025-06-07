from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from resume_parser import extract_text_from_pdf
from jd_matcher import analyze_resume

app = FastAPI()

@app.post("/analyze/")
async def analyze_resume_api(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        contents = await resume.read()
        resume_text = extract_text_from_pdf(contents)
        result = analyze_resume(resume_text, job_description)
        return {"match_score": result['score'], "feedback": result['feedback']}
    except Exception as e:
        print("❌ Error:", e)
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

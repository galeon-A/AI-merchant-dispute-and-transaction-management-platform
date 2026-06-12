
from app.services.llm_service import summarize

def analyze_dispute(payload):
    text = payload.get("evidence","")
    summary = summarize(text)
    return {
        "classification":"service_dispute",
        "confidence":0.91,
        "summary":summary
    }

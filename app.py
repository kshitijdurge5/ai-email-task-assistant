import streamlit as st
from portfolio_visuals import render_visuals
def analyze_message(message: str) -> dict:
    text = message.lower()
    category = "billing" if any(w in text for w in ["invoice", "payment", "refund"]) else "support" if any(w in text for w in ["help", "issue", "problem"]) else "general"
    tasks = [line.strip() for line in message.splitlines() if any(w in line.lower() for w in ["please", "need to", "follow up", "by friday", "deadline"])]
    draft = "Thanks for your message. I will review the details and follow up with the relevant information."
    return {"category": category, "tasks": tasks, "draft_reply": draft, "sent": False}

st.set_page_config(page_title="Email Task Assistant", page_icon="âœ‰ï¸")
render_visuals('08_email_task_assistant')
st.title("Email & Task Assistant")
st.caption("Uses sample/pasted messages only. It does not connect to or send email.")
msg = st.text_area("Paste a message")
if st.button("Analyze"):
    if not msg.strip(): st.warning("Paste a message first.")
    else: st.json(analyze_message(msg))


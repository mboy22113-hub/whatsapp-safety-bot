import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
You are a cybersecurity assistant for Indian users.
Classify message into:
- Safe ✅
- Suspicious ⚠️
- Dangerous ❌

Reply format:
🚨 Result: [Safe / Suspicious / Dangerous]
🧠 Reason:
- Point 1
- Point 2
🛡️ Advice:
- Action 1
- Action 2

Keep it short, simple, and easy.
"""

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.form.get("Body", "").strip()
    resp = MessagingResponse()
    msg = resp.message()

    if not incoming_msg:
        msg.body("Please send a message to check.")
        return str(resp)

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": incoming_msg},
            ],
            max_tokens=400,
            temperature=0.3,
        )
        reply = completion.choices[0].message.content.strip()
    except Exception as e:
        reply = f"⚠️ Error checking message: {str(e)}"

    msg.body(reply)
    return str(resp)

@app.route("/", methods=["GET"])
def index():
    return "✅ WhatsApp AI Safety Bot is running!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

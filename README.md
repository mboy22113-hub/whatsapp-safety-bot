# 🛡️ WhatsApp AI Safety Bot

Classifies WhatsApp messages as Safe / Suspicious / Dangerous using OpenAI.

---

## 📁 Project Files

```
whatsapp-safety-bot/
├── app.py            ← Flask app + webhook
├── requirements.txt  ← Python dependencies
├── Procfile          ← For Render / Railway
├── .env.example      ← Environment variable template
└── .gitignore
```

---

## ⚙️ Environment Variables

| Variable           | Where to get it                          |
|--------------------|------------------------------------------|
| OPENAI_API_KEY     | https://platform.openai.com/api-keys     |
| TWILIO_ACCOUNT_SID | https://console.twilio.com               |
| TWILIO_AUTH_TOKEN  | https://console.twilio.com               |
| PORT               | Set automatically by Render/Railway      |

---

## 🚀 Deploy on Render.com

1. Push your code to a GitHub repo
   ```bash
   git init
   git add .
   git commit -m "init"
   git remote add origin https://github.com/YOUR_USERNAME/whatsapp-safety-bot.git
   git push -u origin main
   ```

2. Go to https://render.com → **New** → **Web Service**

3. Connect your GitHub repo

4. Fill in:
   - **Name:** whatsapp-safety-bot
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`

5. Add Environment Variables (click **Environment** tab):
   ```
   OPENAI_API_KEY     = sk-your-key
   TWILIO_ACCOUNT_SID = ACxxxx
   TWILIO_AUTH_TOKEN  = your-token
   ```

6. Click **Create Web Service**

7. Wait ~2 minutes → your URL will be:
   ```
   https://whatsapp-safety-bot.onrender.com
   ```

---

## 🚀 Deploy on Railway.app

1. Push to GitHub (same steps as above)

2. Go to https://railway.app → **New Project** → **Deploy from GitHub**

3. Select your repo

4. Click **Variables** → Add:
   ```
   OPENAI_API_KEY     = sk-your-key
   TWILIO_ACCOUNT_SID = ACxxxx
   TWILIO_AUTH_TOKEN  = your-token
   ```

5. Railway auto-detects `Procfile` and deploys

6. Click **Settings** → **Domains** → **Generate Domain**

7. Your URL will be:
   ```
   https://whatsapp-safety-bot-production.up.railway.app
   ```

---

## 📱 Connect Twilio WhatsApp Webhook

1. Go to https://console.twilio.com
2. Navigate to **Messaging** → **Try it out** → **Send a WhatsApp message**
3. Under **Sandbox Settings**, set:
   ```
   WHEN A MESSAGE COMES IN:
   https://YOUR-DEPLOYED-URL.onrender.com/whatsapp
   HTTP Method: POST
   ```
4. Save

---

## ✅ Test It

1. Send your Twilio sandbox join code from WhatsApp
   (e.g. `join bright-forest`)
2. Send any suspicious message like:
   ```
   "Congratulations! You won ₹50,000. Click here to claim."
   ```
3. Bot replies instantly with classification ✅ ⚠️ ❌

---

## 🧪 Local Testing

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env from example
cp .env.example .env
# Edit .env and add your real keys

# 4. Run locally
python app.py

# 5. Expose with ngrok for Twilio testing
ngrok http 5000
# Use the ngrok https URL as your Twilio webhook
```

---

## 💡 Example Bot Response

**Input:** "You won an iPhone! Click this link now to claim your prize."

**Output:**
```
🚨 Result: Dangerous ❌
🧠 Reason:
- Prize scam — unsolicited winning message
- Urgency tactics to make you click

🛡️ Advice:
- Do NOT click any links
- Block and report the number immediately
```

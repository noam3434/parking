# 🚀 Galactic Spaceport – Smart Parking Tracker (Track 1 – Lite)

לוח בקרה לשומר בחניון חלליות. מצלמת IoT שומרת תמונות של לוחיות רישוי בשרת אחסון, והדאשבורד מציג אותן.

```
דפדפן --> Nginx :8080 (web, HTML) --/images/--> Apache :8081 (storage) --> Volume camera-images
```

| שירות | Image | תפקיד |
|---|---|---|
| `web` | nginx:alpine | מגיש את `index.html` ומעביר `/images/` לשרת האחסון |
| `storage` | httpd:2.4-alpine | שרת אחסון בלבד – מגיש את תמונות המצלמה, מ-Named Volume |

## הרצההה
```bash
docker compose up --build -d
```
לוח בקרה: http://localhost:8080 · שרת האחסון ישירות: http://localhost:8081/images/car1.svg

### הדגמת "תמונה חדשה מהמצלמה" + Persistence
```bash
docker compose cp my-photo.svg storage:/usr/local/apache2/htdocs/images/car7.svg   # המצלמה "שומרת" תמונה
docker compose down            # בלי -v
docker compose up -d           # התמונה עדיין שם בזכות ה-volume
```
(כדי שתופיע בדאשבורד, מוסיפים את שמה למערך `FILES` ב-`web/index.html`.)

## ✨ הנגיעה האישית
נושא חניון חלליות 🛸, שעון חי, ספירת חלליות, Dark/Light mode, ו-Easter Egg (קוד Konami: ↑↑↓↓←→←→ B A).

## CI/CD
`.github/workflows/ci.yml`: בכל push – `docker compose build` + בדיקת עשן. בונוס: על `main` ועל תגיות `v*.*.*` – התחברות ל-ghcr.io עם `GITHUB_TOKEN`, תיוג אוטומטי (semver / sha / latest) ו-push של `web` ו-`storage`.

## צוות
- נועם אמסילי
- אמרי איוס
- ניקי בויקה

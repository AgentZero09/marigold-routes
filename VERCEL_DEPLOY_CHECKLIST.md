# Vercel Deployment Checklist

Quick reference for deploying Marigold Routes to Vercel.

## ✅ Pre-Deployment Checklist

### Files Verification
- [ ] `vercel.json` exists at project root
- [ ] `requirements.txt` exists at project root  
- [ ] `backend/api/index.py` exists
- [ ] `.vercelignore` exists
- [ ] All changes committed to Git
- [ ] Pushed to GitHub/GitLab/Bitbucket

### Code Verification
```powershell
# Test that Flask app imports correctly
cd backend
python -c "from run import app; print('✅ App imports successfully')"

# Verify vercel.json is valid JSON
python -c "import json; json.load(open('../vercel.json')); print('✅ vercel.json is valid')"
```

---

## 🚀 Deployment Steps

### Step 1: Initial Deployment
```
1. Go to https://vercel.com/new
2. Click "Import Git Repository"
3. Select your Marigold Routes repository
4. Framework: Other (Vercel will auto-detect from vercel.json)
5. Root Directory: ./
6. Click "Deploy"
```

### Step 2: Set Environment Variables
Go to Project Settings → Environment Variables and add:

**Essential (Required):**
```
DATABASE_URL = postgresql://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE]
SECRET_KEY = [generate-random-secret-key]
JWT_SECRET_KEY = [generate-random-jwt-key]
FRONTEND_URL = https://your-project-name.vercel.app
```

**Optional (For Full Functionality):**
```
RAZORPAY_KEY_ID = [your-razorpay-test-key]
RAZORPAY_KEY_SECRET = [your-razorpay-secret]
RAZORPAY_WEBHOOK_SECRET = [your-webhook-secret]
RESEND_API_KEY = [your-resend-key]
SENDER_EMAIL = noreply@yourdomain.com
```

### Step 3: Redeploy
```
1. Go to Deployments tab
2. Click "..." on the latest deployment
3. Select "Redeploy"
4. Confirm
```

### Step 4: Verify Deployment
```bash
# Get your URL from Vercel dashboard, then test:
curl https://your-project.vercel.app/api/health

# Expected response:
# {"status":"ok","service":"Marigold Routes API","database":"connected"}
```

---

## 🔍 Post-Deployment Verification

### Test Backend API
- [ ] `/api/health` returns 200 OK
- [ ] `/api/destinations` returns destinations list
- [ ] `/api/packages` returns packages list

### Test Frontend  
- [ ] Homepage loads at root URL
- [ ] CSS styles apply correctly
- [ ] Navigation works
- [ ] All pages accessible

### Test Admin
- [ ] Admin page loads at `/admin.html`
- [ ] Can login with credentials
- [ ] Dashboard displays (after implementing admin.js)

---

## 🛠️ Database Setup (Required for Full Functionality)

### Option 1: Supabase (Recommended)
```
1. Create project at https://supabase.com
2. Go to Settings → Database
3. Copy "Connection string" → "URI"
4. Add to Vercel as DATABASE_URL
5. Run migrations locally (same DATABASE_URL):
   cd backend
   flask db upgrade
6. Seed data:
   cd ..
   python database/seed/seed_data.py
```

### Option 2: Other PostgreSQL
```
1. Set up PostgreSQL database (Neon, Railway, etc.)
2. Get connection string
3. Add to Vercel as DATABASE_URL
4. Run migrations and seed data as above
```

---

## ⚠️ Common Issues

### Issue: Build fails
**Check:** Build logs in Vercel dashboard
**Fix:** Ensure requirements.txt is at root level

### Issue: 500 Internal Server Error  
**Check:** Function logs in Vercel (Deployments → Click deployment → Functions tab)
**Fix:** Usually DATABASE_URL not set or invalid

### Issue: Static files 404
**Check:** Browser console for exact missing files
**Fix:** Verify frontend/ directory structure

### Issue: CORS errors
**Fix:** Set FRONTEND_URL to match your Vercel domain

---

## 📝 Environment Variables Reference

| Variable | Required | Purpose | Example |
|----------|----------|---------|---------|
| `DATABASE_URL` | Yes* | PostgreSQL connection | `postgresql://user:pass@host/db` |
| `SECRET_KEY` | Yes | Flask session security | Random 32+ chars |
| `JWT_SECRET_KEY` | Yes | JWT token signing | Random 32+ chars |
| `FRONTEND_URL` | Yes | CORS configuration | `https://app.vercel.app` |
| `RAZORPAY_KEY_ID` | No | Payment gateway | `rzp_test_xxxxx` |
| `RAZORPAY_KEY_SECRET` | No | Payment gateway | Secret key |
| `RESEND_API_KEY` | No | Email service | `re_xxxxx` |

*App will load without DATABASE_URL but database features won't work

---

## 🔄 Redeployment (After Changes)

### For Code Changes:
```powershell
git add .
git commit -m "Your changes"
git push
# Vercel auto-deploys
```

### For Environment Variables Only:
```
1. Update in Vercel dashboard
2. Redeploy from Deployments tab
```

### For Rollback:
```
1. Deployments tab
2. Find working deployment
3. Click "..." → "Promote to Production"
```

---

## ✅ Success Criteria

Your deployment is successful when:

- [ ] Vercel shows "Ready" status
- [ ] `/api/health` returns 200 OK
- [ ] Homepage loads with styling
- [ ] No errors in browser console (except expected missing JS files)
- [ ] No errors in Vercel function logs
- [ ] Database connects (if DATABASE_URL set)

---

## 📞 Quick Commands

### Generate Secret Keys
```powershell
# Python
python -c "import secrets; print(secrets.token_hex(32))"

# OR Online
# Visit: https://randomkeygen.com/
```

### Test Deployment Locally
```powershell
# Install Vercel CLI
npm install -g vercel

# Test locally
vercel dev

# Access at http://localhost:3000
```

### View Logs
```
Vercel Dashboard → Your Project → Deployments → 
Click deployment → Functions tab → Click function → View logs
```

---

## 🎯 Next Steps After Deployment

1. **Test all endpoints** - Verify each API works
2. **Set up database** - Run migrations and seed data
3. **Implement JavaScript files** - Connect frontend to backend
4. **Configure payment gateway** - Set up Razorpay
5. **Set up email service** - Configure Resend
6. **Add custom domain** - (Optional) Configure DNS

---

## 📚 Resources

- **Detailed Guide:** `VERCEL_DEPLOYMENT.md`
- **Changes Summary:** `DEPLOYMENT_CHANGES_SUMMARY.md`
- **Vercel Docs:** https://vercel.com/docs
- **Flask on Vercel:** https://vercel.com/guides/deploying-flask-with-vercel

---

**Quick Start:**
1. Push code to Git ✓
2. Import to Vercel ✓
3. Set DATABASE_URL, SECRET_KEY, JWT_SECRET_KEY ✓
4. Redeploy ✓
5. Test `/api/health` ✓

**That's it! 🚀**

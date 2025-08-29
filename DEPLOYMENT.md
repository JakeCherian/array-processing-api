# Deployment Guide

This guide will help you deploy the Array Processing API to various hosting platforms.

## Prerequisites

- A GitHub account
- The project code committed to a GitHub repository

## Deployment Options

### 1. Vercel (Recommended - Free & Easy)

Vercel is one of the easiest platforms to deploy Python Flask applications.

#### Steps:
1. **Create Vercel Account**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with your GitHub account

2. **Import Project**
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect it's a Python project

3. **Configure Build Settings**
   - Framework Preset: Other
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: Leave empty
   - Install Command: `pip install -r requirements.txt`

4. **Deploy**
   - Click "Deploy"
   - Your API will be available at `https://your-project-name.vercel.app`

5. **Update Configuration**
   - The `vercel.json` file is already configured for Python Flask apps
   - Your API endpoint will be: `https://your-project-name.vercel.app/bfhl`

### 2. Railway (Alternative - Free Tier Available)

Railway is another excellent option for Python applications.

#### Steps:
1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with your GitHub account

2. **Deploy from GitHub**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure Environment**
   - Railway will automatically detect Python
   - It will install dependencies from `requirements.txt`
   - The `Procfile` will be used for deployment

4. **Get Your URL**
   - Railway will provide a URL like `https://your-app-name.railway.app`
   - Your API endpoint: `https://your-app-name.railway.app/bfhl`

### 3. Render (Alternative - Free Tier Available)

Render is a modern cloud platform that supports Python applications.

#### Steps:
1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with your GitHub account

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Service**
   - Name: `array-processing-api`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

4. **Deploy**
   - Click "Create Web Service"
   - Your API will be available at `https://your-app-name.onrender.com`

### 4. Heroku (Legacy - Requires Credit Card)

Heroku is a well-established platform but requires a credit card for verification.

#### Steps:
1. **Create Heroku Account**
   - Go to [heroku.com](https://heroku.com)
   - Sign up and add a credit card

2. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Or download from https://devcenter.heroku.com/articles/heroku-cli
   ```

3. **Login and Deploy**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

4. **Open Your App**
   ```bash
   heroku open
   ```

## Environment Variables

For production deployment, you may want to set environment variables:

### Vercel
- Go to Project Settings → Environment Variables
- Add:
  - `FULL_NAME`: Your full name
  - `EMAIL`: Your email
  - `ROLL_NUMBER`: Your roll number

### Railway
- Go to your project → Variables
- Add the same environment variables

### Render
- Go to your service → Environment
- Add the same environment variables

## Testing Your Deployment

After deployment, test your API:

```bash
# Test the health endpoint
curl https://your-app-url.com/health

# Test the main API
curl -X POST https://your-app-url.com/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a", "1", "334", "4", "R", "$"]}'
```

## Troubleshooting

### Common Issues:

1. **Port Issues**
   - The app uses `PORT` environment variable
   - Most platforms set this automatically

2. **Dependencies**
   - Make sure `requirements.txt` is up to date
   - Some platforms may need `gunicorn` for production

3. **CORS Issues**
   - The app includes CORS headers
   - If you have issues, check the CORS configuration

4. **Build Failures**
   - Check the build logs in your platform's dashboard
   - Ensure all dependencies are listed in `requirements.txt`

## Monitoring

Most platforms provide:
- **Logs**: View application logs
- **Metrics**: Monitor performance
- **Alerts**: Set up notifications for errors

## Cost Considerations

- **Vercel**: Free tier includes 100GB bandwidth/month
- **Railway**: Free tier includes $5 credit/month
- **Render**: Free tier includes 750 hours/month
- **Heroku**: Free tier discontinued, starts at $7/month

## Security Considerations

1. **Environment Variables**: Never commit sensitive data
2. **HTTPS**: All platforms provide SSL certificates
3. **Rate Limiting**: Consider adding rate limiting for production
4. **Input Validation**: The API includes input validation

## Next Steps

After deployment:
1. Test all endpoints thoroughly
2. Update your submission form with the deployed URL
3. Monitor the application for any issues
4. Consider adding monitoring and logging

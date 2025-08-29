#!/bin/bash

# Array Processing API Deployment Script
# This script helps you deploy your API to various platforms

echo "🚀 Array Processing API Deployment Script"
echo "=========================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Please initialize git first:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
    exit 1
fi

# Check if there are uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  You have uncommitted changes. Please commit them first:"
    echo "   git add ."
    echo "   git commit -m 'Your commit message'"
    exit 1
fi

echo "✅ Git repository is ready"

# Function to deploy to Vercel
deploy_vercel() {
    echo "📦 Deploying to Vercel..."
    
    # Check if Vercel CLI is installed
    if ! command -v vercel &> /dev/null; then
        echo "❌ Vercel CLI not found. Installing..."
        npm install -g vercel
    fi
    
    echo "🔗 Deploying to Vercel..."
    vercel --prod
    
    echo "✅ Vercel deployment initiated!"
    echo "🌐 Your API will be available at: https://your-project-name.vercel.app/bfhl"
}

# Function to deploy to Railway
deploy_railway() {
    echo "🚂 Deploying to Railway..."
    
    # Check if Railway CLI is installed
    if ! command -v railway &> /dev/null; then
        echo "❌ Railway CLI not found. Installing..."
        npm install -g @railway/cli
    fi
    
    echo "🔗 Deploying to Railway..."
    railway login
    railway up
    
    echo "✅ Railway deployment initiated!"
    echo "🌐 Your API will be available at: https://your-project-name.railway.app/bfhl"
}

# Function to deploy to Render
deploy_render() {
    echo "🎨 Deploying to Render..."
    echo "📝 Please follow these steps:"
    echo "1. Go to https://render.com"
    echo "2. Sign up/Login with GitHub"
    echo "3. Click 'New +' → 'Web Service'"
    echo "4. Connect your GitHub repository"
    echo "5. Configure:"
    echo "   - Name: array-processing-api"
    echo "   - Environment: Python 3"
    echo "   - Build Command: pip install -r requirements.txt"
    echo "   - Start Command: gunicorn app:app"
    echo "6. Click 'Create Web Service'"
    echo ""
    echo "🌐 Your API will be available at: https://your-app-name.onrender.com/bfhl"
}

# Function to test local deployment
test_local() {
    echo "🧪 Testing local deployment..."
    
    # Check if Python is installed
    if ! command -v python3 &> /dev/null; then
        echo "❌ Python 3 not found. Please install Python 3.8+"
        exit 1
    fi
    
    # Install dependencies
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
    
    # Start the server
    echo "🚀 Starting local server..."
    echo "🌐 Your API will be available at: http://localhost:5001"
    echo "📋 Press Ctrl+C to stop the server"
    echo ""
    
    python3 app.py
}

# Function to run tests
run_tests() {
    echo "🧪 Running tests..."
    
    # Check if server is running
    if curl -s http://localhost:5001/health > /dev/null; then
        echo "✅ Server is running. Running tests..."
        python3 test_api.py http://localhost:5001
    else
        echo "❌ Server is not running. Please start the server first:"
        echo "   python3 app.py"
    fi
}

# Main menu
echo ""
echo "Choose deployment option:"
echo "1) Deploy to Vercel (Recommended)"
echo "2) Deploy to Railway"
echo "3) Deploy to Render"
echo "4) Test local deployment"
echo "5) Run tests"
echo "6) Exit"
echo ""

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        deploy_vercel
        ;;
    2)
        deploy_railway
        ;;
    3)
        deploy_render
        ;;
    4)
        test_local
        ;;
    5)
        run_tests
        ;;
    6)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice. Please enter 1-6."
        exit 1
        ;;
esac

echo ""
echo "🎉 Deployment process completed!"
echo "📚 For more information, see DEPLOYMENT.md"

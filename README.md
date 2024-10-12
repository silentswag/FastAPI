1. git clone https://github.com/silentswag/FastAPI.git
2. cd FastAPI
3. uvicorn main:app --reload

4. ## Deploying to Heroku
Step 1: Create a Heroku Account
  If you don't already have a Heroku account, sign up at https://signup.heroku.com.

Step 2: Install the Heroku CLI
Download and install the Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli.

Step 3: Login to Heroku
Log in to your Heroku account using the CLI:
heroku login
Step 4: Create a New Heroku App
Create a new app in Heroku:

heroku create FastAPI
Step 5: Add MongoDB to Your Heroku App
Add MongoDB to your Heroku application using a third-party service like MongoDB Atlas or use an add-on like mLab.
Set up your database and update the connection URI in the database.py file.

Step 6: Deploy the Application to Heroku
Initialize a git repository if you haven't already:
git init
git add .
git commit -m "Initial commit"
Deploy the code to Heroku:

git push heroku main
Step 7: Scale the App
Ensure your app is running by scaling the Dynos:


heroku ps:scale web=1
Step 8: Open the App
Open your deployed app in the browser:


heroku open


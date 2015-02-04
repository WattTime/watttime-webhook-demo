# watttime-webhook-demo
Demo Flask app that sends emails based on data from a WattTime webhook. 

## Step 1: Get the code

Clone this repo and enter the directory:

```
git clone https://github.com/WattTime/watttime-webhook-demo.git
cd watttime-webhook-demo
```

## Step 2: Deploy to Heroku

If you don't have an account on Heroku, make one and get the toolbelt by following the first part of the instructions [here](https://devcenter.heroku.com/articles/getting-started-with-python-o). Once that's ready, deploying is quick and easy:

```
heroku create
git push heroku master
```

## Step 3: Configure for emails

You'll need to set up environment variables for a mail server if you want the emails to be sent correctly. ```TO_EMAIL``` is the email address that data update emails will be sent to; ```MAIL_USERNAME``` is the email address that data update emails will be sent from. The password, server, and port should match the "from" email.

```
heroku config:add MAIL_USERNAME=<email to send from>
heroku config:add MAIL_PASSWORD=<from email password>
heroku config:add MAIL_SERVER=<from mail server>
heroku config:add MAIL_PORT=<from mail port>
heroku config:add TO_EMAIL=<email to send to>
```

## Step 4: Check it out!

Run ```heroku open``` to see your snazzy new site in a web browser :)

## Step 5: Set up a webhook

Create an account for the WattTime API [here](http://api.watttime.org/accounts/register/). Click on [webhooks](http://api.watttime.org/accounts/webhooks/), then click "Add new webhook". Use the dropdowns to select the balancing authority for your region (e.g., CAISO is for California) and the kind of data you want (i.e., carbon). In "target url", type the link that's shown on your new Heroku site (should be something like [https://whispering-meadow-123.herokuapp.com/wt_feed]). Click "submit" to create the webhook.

## Step 6: Get email updates

After creating the webhook, emails will be sent to the ```TO_EMAIL``` address approximately every 5-10 minutes. This is kind of a lot of emails, so you'll probably want to set up a filter or something.

## Step 7: To infinity and beyond

Customize this to your heart's content! Edit the email template (in ```templates/email.txt```), hook it up to [IFTTT](https://ifttt.com/recipes/popular?channel=email), or do whatever else you like.

All we ask is that you comply with WattTime's terms and conditions for data use and sharing. And if you have an awesome idea that's outside of the terms, just let us know and we'll work with you to make it a reality.

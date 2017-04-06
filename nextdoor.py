import requests
import json
import datetime
import time

print "initial setup"
mail_gun_api_key = raw_input("Please enter your mailgun API Key: ")
email = raw_input("Please enter your email: ")
print "\n"
print "\n"

print "navigate to https://stevesie.com/apps/nextdoor-api and complete the steps to retrieve phone API Data"
print "\n"

trace_uuid = raw_input("Please enter your trace_uuid: ")
authorization = raw_input("Please enter your authorization: ")
cookie = raw_input("Please enter your cookie: ")
xndidtoken = raw_input("Please enter your x-nd-id-token: ")
xndsignature = raw_input("Please enter your x-nd-signature: ")
postmantoken = raw_input("Please enter your postman-token: ")

kickoff_email = requests.post(
                    "https://api.mailgun.net/v3/sandbox47aaee9808044dacb6e02729d74ce45b.mailgun.org/messages",
                    auth=("api", mail_gun_api_key),
                    data={"from": "Mailgun Sandbox <postmaster@sandbox47aaee9808044dacb6e02729d74ce45b.mailgun.org>",
                    "to": email,
                    "subject": "Script Kickoff Successful",
                     "text": "script started at " + str(datetime.datetime.now())})


#unofficial phone API request (spoofing iPhone)
url = "https://api.nextdoor.com/mobile/v1/feeds/free"
querystring = {"trace_uuid":trace_uuid,"want_feature_config":"1","want_user_data":"1"}
headers = {
    'trace_uuid': trace_uuid,
    'authorization': authorization,
    'cookie': cookie,
    'x-nd-id-token': xndidtoken,
    'x-nd-signature': xndsignature,
    'accept': "*/*",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en;q=1.0",
    'user-agent': "Nextdoor/2.48 (iPhone; iPhone OS 9.3.2; v1; 20160624151511; production build)",
    'host': "api.nextdoor.com",
    'cache-control': "no-cache",
    'postman-token': postmantoken
    }

#initialize empty list
itemCheckList = []

counter = 0
hour_counter = 0

#Loop to check for new post
while True:

    try:
        status = ''

        now = datetime.datetime.now()

        response = requests.request("GET", url, headers=headers, params=querystring)
        ret = response.json()
        free_item_list = ret['stories']

        for item in free_item_list:
            itemCreationDate = datetime.datetime.fromtimestamp(item['creation_date']).strftime('%Y-%m-%d %H:%M:%S')
            itemName = item['subject']
            try:
                itemPic = item['photo']
            except:
                itemPic = ''

            if itemName not in itemCheckList and counter == 20:

                email = requests.post(
                    "https://api.mailgun.net/v3/sandbox47aaee9808044dacb6e02729d74ce45b.mailgun.org/messages",
                    auth=("api", mail_gun_api_key),
                    data={"from": "Mailgun Sandbox <postmaster@sandbox47aaee9808044dacb6e02729d74ce45b.mailgun.org>",
                    "to": email,
                    "subject": "Item Alert: " + item['subject'],
                     "text": item['subject'] + "\n\n" + itemPic})
            else:
                status = "No New Items"
            # itemPic = item['photo']
            itemCheckList.append(itemName)
            if counter != 20:
                counter += 1
        print status

        time.sleep(3600)
        hour_counter += 300
        if hour_counter == 84600:
            exit()

    except Exception as e:
        print e
import requests
import base64


##Get captcha and save

url_captcha="https://swa.mail.ru/c/6";

headers = {
'User-Agent': 'mobmail android 13.3.0.31738 ru.mail.mailapp',
'Connection': 'Keep-Alive',
'Accept-Encoding':'gzip'
};

r = requests.get(url_captcha, headers=headers)

if r.status_code == 200:
    with open("mail_ru_captcha.png", 'wb') as f:
        f.write(r.content)
        print("Download and save captcha from mail.ru")

        #solve captcha
        base64_encoded_data = base64.b64encode(r.content)
        base64_message = base64_encoded_data.decode('utf-8')
        #print(base64_message)
        
        json = {"clientKey":"DEMO","task": {
		"type": "ImageToTextTask",
        "subType":"mail.ru",
		"body": base64_message
	    }}
        #print(json)
        url_solve_captcha="http://iamnotbot.com:5000/createTask";         
        r = requests.post(url_solve_captcha, json=json)
        print("Capthca = "+r.text)

else:
    print("Cannot download and save captcha from mail.ru")         
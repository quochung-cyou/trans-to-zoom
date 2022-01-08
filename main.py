import discord
import requests
import random
import json
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
}
client = discord.Client()
url_list = [
'https://www.reddit.com/r/ProgrammerHumor.json?sort=top&t=week',
'https://www.reddit.com/r/programmingmemes.json?sort=top&t=week',
'https://www.reddit.com/r/codinghumor.json?sort=top&t=week',
'https://www.reddit.com/r/ProgrammerHumor.json?sort=top&t=month',
'https://www.reddit.com/r/ProgrammerHumor.json?sort=hot&t=month',
'https://www.reddit.com/r/ProgrammerHumor.json?sort=top&t=year'

]
@client.event
async def on_message(message):
    if "phongid" in message.content:
        content = str(message.content)
        idphong = content[content.find("id")+2:]
        data = str(requests.get('https://trans.naviconference.com/RestApi/Service/JoinMeetingVer2?transId=' + str(idphong) + '&applicatonAllowFreeJoinMeeting=yes&displayName=test', headers=headers).content).replace("b'OK|","").replace("}'","}")
        print(data)
        if "Your host is not in the room or your internet connection is unstable" in data:
            await message.channel.send("Phòng này chưa mở") 
        elif "REQUIRED_LOGIN" in data:
            await message.channel.send("Phòng này yêu cầu đăng nhập") 
        else:
            find1 = data.find("\"HostName\"") + len("\"HostName\"") + 1
            find2 = data.find("\"TurnOnVideo\"")
            hostname = str(data[find1:find2])
            data2 = data.replace(hostname, "\"test\",")
            data_json = json.loads(data2)
            await message.channel.send("Link vào phòng: https://hoptructuyen-vn.zoom.us/j/" + data_json["MeetingID"] + "/") 
            await message.channel.send("Mật khẩu: " + data_json["Password"]) 


#client.run("") token here

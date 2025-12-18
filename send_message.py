import datetime
import requests
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

MESSAGES = {
    0: "Понеділок\nПройтись усюди з паличкою, прибрати пил",
    1: "Вівторок\nРозставити красиво настолки",
    2: "Середа\nПомити серветники і за потреби досипати/замінити сіль і перець\nПротерти вхідні двері і холодильник",
    3: "Четвер\nПротерти полицю з брудним посудом, поправити пакування, розставити красиво на полиці",
    4: "Пʼятниця\nПеревірити що порядок в комірці, прибрати зайве, охайно все поскладати",
    5: "Субота\nПеревірити що на складі порядок, порозкладати все",
    6: "Неділя\nПротерти вхідні двері і холодильник"
}

day = datetime.datetime.utcnow().weekday()
text = MESSAGES[day]

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": text
})

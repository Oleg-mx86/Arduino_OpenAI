import serial,time
from openai import OpenAI
from APIkey import key
client = OpenAI(api_key=key, base_url="https://api.deepseek.com")

def f(text):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You must give a short answer (one integer between 0 and 180) - the angle of rotation of the Arduino servo."},
            {"role": "user", "content": text},
        ],
        stream=False
    )
    s=response.choices[0].message.content.strip()
    print(s)
    try:
        a=int(s)
    except:
        a=-1
    return a

ser = serial.Serial(port='COM4', baudrate=9600) # відкрити порт COM
time.sleep(2)
print(ser.portstr) # перевірити чи порт використовується

while True:
    text = input("Enter a command (e.g., 'Move servo to 90 degrees'): ")
    a=f(text)
    if a!=-1:
        ser.write(str(a).encode()+b"\n")
        time.sleep(1)

ser.close() # закрити порт
import random
import time

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "sensors/temperature"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'Groupe 5'
password = 'sssc'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count1 = 22.9
    msg_count2= 20.7
    msg_count3= 22.6
    msg_count4= 48.5
    msg_count5 = 49.6
    time.sleep(1)
    msg1 = f"messages: {msg_count1}"
    msg2 = f"messages: {msg_count2}"
    msg3 = f"messages: {msg_count3}"
    msg4 = f"messages: {msg_count4}"
    msg5 = f"messages: {msg_count5}"
    result = client.publish(topic, msg1+msg2+msg3+msg4+msg5)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send {msg1}and{msg2}and{msg3}and{msg4}and{msg5}to topic {topic}")
    else:
            print(f"Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

run()

# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime

#def on_publish(client, userdata, result):
#    print("Mengirimkan \n")

# definisikan nama broker yang akan digunakan
broker_address="127.0.0.1"

# buat client baru bernama SMTOWN
print("Creating New Instance")
client = mqtt.Client("SMTOWN") 
#client.on_publish=on_publish

# koneksi ke broker
print("Connecting to Broker")
client.connect(broker_address, port=3333) 

# mulai loop client
client.loop_start()

# lakukan 5x publish SMTOWN
print("Publish Something")
for i in range (5):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang SMTOWN
    schedule = datetime.datetime(2020,3,1+i,17,30)
    client.publish('Korean Ballad','Date : ' + schedule.strftime('%d %b %Y') 
	+ '\n Hour : ' + schedule.strftime('%H') + ':' + schedule.strftime('%M') + '\n Day : ' + schedule.strftime('%A') + '\n Place : Sky Dome')

#stop loop
client.loop_stop() 
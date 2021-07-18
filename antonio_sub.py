# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    print("Schedule : \n" ,str(message.payload.decode("utf-8")))
    print(" Theme : ",message.topic)
########################################
    
# buat definisi nama broker yang akan digunakan
broker_address="127.0.0.1"

# buat client baru bernama Antonio
client = mqtt.Client("Antonio")

# kaitkan callback on_message ke client
client.on_message=on_message

# buat koneksi ke broker
client.connect(broker_address, port=3333)

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1
variabel = input('Input Theme: ')
if(variabel == 'Girlband'):
    client.subscribe('Girlband')
else :
    client.subscribe('Korean Ballad')
# loop forever
while True:
    # berikan waktu tunggu 1 detik 
    time.sleep(1)

#stop loop
client.loop_stop()
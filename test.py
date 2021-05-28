import client

puller = client.DataPuller(1, '172.17.0.2', 502, 0.1)
puller.load_registers()
puller.getData()
print(puller.RORegisterVal)
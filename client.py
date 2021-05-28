import allregisters
import sunspec2.modbus.modbus as modbus
import sunspec2.mb as util


# main loop
# decoding
# payload

class DataPuller(object):
	def __init__(self, slave_id=1, ipaddress='127.0.0.1', TCPport=502, timeout=0.1):
		self.slave_id=slave_id
		self.ipaddress=ipaddress
		self.TCPport=TCPport
		self.timeout=timeout
		self.RORegisterVal={}
		self.holdingRegisters=list()
		
		self.client = modbus.ModbusClientTCP(timeout=5)

	def load_registers(self):
		self.holdingRegisters = list(filter(lambda d: d['direction']=='RX', allregisters.data))

	def getData(self):
		for register in self.holdingRegisters:
			if register['type']=='STR':
				self.RORegisterVal[register['name']] = util.data_to_str(self.client.read(register['address'],register['length']))

			elif register['type']=='U16':  
				self.RORegisterVal[register['name']] = util.data_to_u16(self.client.read(register['address'],register['length']))

			elif register['type']=='S16':  
				self.RORegisterVal[register['name']] = util.data_to_s16(self.client.read(register['address'],register['length']))

			elif register['type']=='U32':  
				self.RORegisterVal[register['name']] = util.data_to_u32(self.client.read(register['address'],register['length']))

			elif register['type']=='S32':  
				self.RORegisterVal[register['name']] = util.data_to_s32(self.client.read(register['address'],register['length']))

			elif register['type']=='U64':  
				self.RORegisterVal[register['name']] = util.data_to_u64(self.client.read(register['address'],register['length']))

			elif register['type']=='F32':  
				self.RORegisterVal[register['name']] = util.data_to_f32(self.client.read(register['address'],register['length']))

			elif register['type']=='F64':  
				self.RORegisterVal[register['name']] = util.data_to_f64(self.client.read(register['address'],register['length']))

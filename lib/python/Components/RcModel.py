import os

class RcModel:
	RCTYPE_DMM = 0
	RCTYPE_ET9X00 = 1
	RCTYPE_ET6X00 = 2
	RCTYPE_ET9500 = 3
	RCTYPE_VU = 4
	RCTYPE_ET4X00 = 5
	RCTYPE_XP1000 = 6
	RCTYPE_INI0 = 7
	RCTYPE_INI1 = 8
	RCTYPE_INI2 = 9
	RCTYPE_INI3 = 10
	RCTYPE_INI4 = 11
	
	def __init__(self):
		self.currentRcType = self.RCTYPE_DMM
		self.readRcTypeFromProc()

	def rcIsDefault(self):
		if self.currentRcType != self.RCTYPE_DMM:
			return False
		return True

	def readFile(self, target):
		fp = open(target, 'r')
		out = fp.read()
		fp.close()
		return out.split()[0]

	def readRcTypeFromProc(self):
		if os.path.exists('/proc/stb/info/boxtype'):
			model = self.readFile('/proc/stb/info/boxtype')
			if model.startswith('et') or model.startswith('xp'):
				rc = self.readFile('/proc/stb/ir/rc/type')
				if rc == '4':
					self.currentRcType = self.RCTYPE_DMM
				elif rc == '5' or rc == '11':
					self.currentRcType = self.RCTYPE_ET9X00
				elif rc == '6':
					self.currentRcType = self.RCTYPE_DMM
				elif rc == '7':
					self.currentRcType = self.RCTYPE_ET6X00
				elif rc == '8':
					self.currentRcType = self.RCTYPE_VU
				elif rc == '9':
					self.currentRcType = self.RCTYPE_ET9500
				elif rc == '13':
					self.currentRcType = self.RCTYPE_ET4X00
				elif rc == '14':
					self.currentRcType = self.RCTYPE_XP1000
			elif model == 'ini-3000':
				fp_version = str(getFPVersion())
				if fp_version.startswith('1'):
					self.currentRcType = self.RCTYPE_INI0
				else:
					self.currentRcType = self.RCTYPE_INI2
			elif model == 'ini-5000' or model == 'ini-7000' or model == 'ini-7012' or model== 'ini-9000':
				self.currentRcType = self.RCTYPE_INI1
			elif model == 'ini-1000' or model == 'ini-1000ru' or model == 'ini-5000ru' or model== 'ini-9000ru':
				self.currentRcType = self.RCTYPE_INI2
			elif model == 'ini-1000sv' or model == 'ini-5000sv':
				self.currentRcType = self.RCTYPE_INI3
			elif model == 'ini-1000de':
				self.currentRcType = self.RCTYPE_INI4
		elif os.path.exists('/proc/stb/info/vumodel'):
			self.currentRcType = self.RCTYPE_VU

	def getRcLocation(self):
		if self.currentRcType == self.RCTYPE_ET9X00:
			return '/usr/share/enigma2/rc_models/et9x00/'
		elif self.currentRcType == self.RCTYPE_ET9500:
			return '/usr/share/enigma2/rc_models/et9500/'
		elif self.currentRcType == self.RCTYPE_ET6X00:
			return '/usr/share/enigma2/rc_models/et6x00/'
		elif self.currentRcType == self.RCTYPE_ET4X00:
			return '/usr/share/enigma2/rc_models/et4x00/'
		elif self.currentRcType == self.RCTYPE_XP1000:
			return '/usr/share/enigma2/rc_models/xp1000/'
		elif self.currentRcType == self.RCTYPE_VU:
			return '/usr/share/enigma2/rc_models/vu/'
		elif self.currentRcType == self.RCTYPE_INI0:
			return '/usr/share/enigma2/rc_models/ini0/'
		elif self.currentRcType == self.RCTYPE_INI1:
			return '/usr/share/enigma2/rc_models/ini1/'
		elif self.currentRcType == self.RCTYPE_INI2:
			return '/usr/share/enigma2/rc_models/ini2/'
		elif self.currentRcType == self.RCTYPE_INI3:
			return '/usr/share/enigma2/rc_models/ini3/'
		elif self.currentRcType == self.RCTYPE_INI4:
			return '/usr/share/enigma2/rc_models/ini4/'      

rc_model = RcModel()

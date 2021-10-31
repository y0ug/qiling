#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

import ctypes
from qiling.hw.peripheral import QlPeripheral


class STM32F4xxCrc(QlPeripheral):
    class Type(ctypes.Structure):
        """ the structure available in :
			stm32f413xx.h
			stm32f407xx.h
			stm32f469xx.h
			stm32f446xx.h
			stm32f427xx.h
			stm32f401xc.h
			stm32f415xx.h
			stm32f412cx.h
			stm32f410rx.h
			stm32f410tx.h
			stm32f439xx.h
			stm32f412vx.h
			stm32f417xx.h
			stm32f479xx.h
			stm32f429xx.h
			stm32f412rx.h
			stm32f423xx.h
			stm32f437xx.h
			stm32f412zx.h
			stm32f401xe.h
			stm32f410cx.h
			stm32f405xx.h
			stm32f411xe.h 
		"""

        _fields_ = [
			('DR'       , ctypes.c_uint32),  # CRC Data register,             Address offset: 0x00
			('IDR'      , ctypes.c_uint8),   # CRC Independent data register, Address offset: 0x04
			('RESERVED0', ctypes.c_uint8),   # Reserved, 0x05
			('RESERVED1', ctypes.c_uint8),   # Reserved, 0x06
			('CR'       , ctypes.c_uint32),  # CRC Control register,          Address offset: 0x08
        ]
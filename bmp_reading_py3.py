import bmpBackend_py3 as bmp

pressure = bmp.BMP085(bus=1)

print( pressure.readTemperature() )

# barometric-sensor
Issues with reading from a barometric sensor

The file I am executing is `bmp_reading_py3.py` and the function I want to use from `bmpBackend_py3.py` is `readPressure()`.

I converted the Adafruit/BMP085/bmpBackend files to Python 3 using the 2to3 utility.

The sensor can read using the code in bmpBackend (e.g. the readRawPressure() function works) so there is no problem with the hardware. 
However, the bit shifts seem to not work in Python 3, presumably because of incompatible data types?

```
Traceback (most recent call last):
  File "/home/pi/bmp/ls_bmp_reading.py", line 5, in <module>
    print( pressure.readPressure() )
  File "/home/pi/bmp/bmpBackend_py3.py", line 194, in readPressure
    X1 = (self._cal_B2 * (B6 * B6) >> 12) >> 11
TypeError: unsupported operand type(s) for >>: 'float' and 'int'
```

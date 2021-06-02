import thinkdsp
from matplotlib import pyplot

wave=thinkdsp.read_wave(r"D:\1.wav")
spectrum=wave.make_spectrum()
spectrum.low_pass(cutoff=600,factor=0.01)
spectrum.plot()
pyplot.show()
wave=spectrum.make_wave()
wave.write(r"D:\1.2.wav")


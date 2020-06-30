import numpy as np

try:
    from stingray import Lightcurve, Powerspectrum
except ImportError:
    import sys
    print("Install stingray first")
    sys.exit()

# Benchmarking from 1,000 to 100,000,000 data-points for safety
test_arr_size = [10**i for i in range(3, 9)]


class Init:
    """
    Time and Memory benchmarks for initializing a power spectra..
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_init(self, array_size):
        Powerspectrum(self.lc)

    def peakmem_init(self, array_size):
        Powerspectrum(self.lc)

    def teardown(self, array_size):
        del self.lc


class Rebin:
    """
    Time and Memory benchmarks for rebinning  a power spectra.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100
        lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

        self.pspec = Powerspectrum(lc)

    def time_init(self, array_size):
        self.pspec.rebin(df=0.01)

    def peakmem_init(self, array_size):
        self.pspec.rebin(df=0.01)

    def teardown(self, array_size):
        del self.pspec


class ClassificalSignificance:
    """
    Time and Memory benchmarks for generating classifical significances for a power spectra.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100
        lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

        self.pspec = Powerspectrum(lc, norm="leahy")

    def time_class_sign(self, array_size):
        self.pspec.classical_significances()

    def peakmem_class_sign(self, array_size):
        self.pspec.classical_significances()

    def teardown(self, array_size):
        del self.pspec


class ComputeRMS:
    """
    Time and Memory benchmarks for computing RMS of a power spectra.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100
        lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

        self.pspec = Powerspectrum(lc)

    def time_init(self, array_size):
        self.pspec.compute_rms(min_freq=0.001, max_freq=0.499)

    def peakmem_init(self, array_size):
        self.pspec.compute_rms(min_freq=0.001, max_freq=0.499)

    def teardown(self, array_size):
        del self.pspec

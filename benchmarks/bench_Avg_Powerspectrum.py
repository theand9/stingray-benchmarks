import numpy as np

try:
    from stingray import Lightcurve, AveragedPowerspectrum
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
        AveragedPowerspectrum(self.lc, 1000)

    def peakmem_init(self, array_size):
        AveragedPowerspectrum(self.lc, 1000)

    def teardown(self, array_size):
        del self.lc

import numpy as np

try:
    from stingray import Lightcurve, AveragedCrossspectrum
except ImportError:
    import sys
    print("Install stingray first")
    sys.exit()

# Benchmarking from 1,000 to 10,000,000 data-points for safety
test_arr_size = [10**i for i in range(3, 8)]


class Init:
    """
    Time and Memory benchmarks for initializing an averaged cross spectra.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc1 = Lightcurve(times, counts, dt=1.0, skip_checks=True)
        self.lc2 = Lightcurve(times,
                              counts + np.random.rand() * 10,
                              dt=1.0,
                              skip_checks=True)

    def time_init(self, array_size):
        AveragedCrossspectrum(self.lc1, self.lc2, 1000, silent=True)

    def peakmem_init(self, array_size):
        AveragedCrossspectrum(self.lc1, self.lc2, 1000, silent=True)

    def teardown(self, array_size):
        del self.lc1, self.lc2


class Coherence:
    """
    Time and Memory benchmarks for calculating the coherence of an averaged cross spectra.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        lc1 = Lightcurve(times, counts, dt=1.0, skip_checks=True)
        lc2 = Lightcurve(times,
                         counts + np.random.rand() * 10,
                         dt=1.0,
                         skip_checks=True)
        self.avg_Cspec = AveragedCrossspectrum(lc1, lc2, 1000, silent=True)

    def time_coher(self, array_size):
        self.avg_Cspec.coherence()

    def peakmem_coher(self, array_size):
        self.avg_Cspec.coherence()

    def teardown(self, array_size):
        del self.avg_Cspec


class TimeLag:
    """
    Time and Memory benchmarks for calculating the time lag of an averaged cross spectra.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        lc1 = Lightcurve(times, counts, dt=1.0, skip_checks=True)
        lc2 = Lightcurve(times,
                         counts + np.random.rand() * 10,
                         dt=1.0,
                         skip_checks=True)
        self.avg_Cspec = AveragedCrossspectrum(lc1, lc2, 1000, silent=True)

    def time_Tlag(self, array_size):
        self.avg_Cspec.time_lag()

    def peakmem_Tlag(self, array_size):
        self.avg_Cspec.time_lag()

    def teardown(self, array_size):
        del self.avg_Cspec

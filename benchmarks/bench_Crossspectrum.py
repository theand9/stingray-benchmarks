import numpy as np

try:
    from stingray import Lightcurve, Crossspectrum
except ImportError:
    import sys
    print("Install stingray first")
    sys.exit()

# Benchmarking from 1,000 to 100,000,000 data-points for safety
test_arr_size = [10**i for i in range(3, 9)]


class Init:
    """
    Time and Memory benchmarks for initializing a cross spectra.
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
        Crossspectrum(self.lc1, self.lc2)

    def peakmem_init(self, array_size):
        Crossspectrum(self.lc1, self.lc2)

    def teardown(self, array_size):
        del self.lc1, self.lc2


class Rebin:
    """
    Time and Memory benchmarks for rebinning cross spectra.
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
        self.Cspec = Crossspectrum(lc1, lc2)
        print(self.Cspec.freq)

    def time_rebin(self, array_size):
        self.Cspec.rebin(df=2.0)

    def peakmem_rebin(self, array_size):
        self.Cspec.rebin(df=2.0)

    def time_log_rebin(self, array_size):
        self.Cspec.rebin(f=1.0)

    def peakmem_log_rebin(self, array_size):
        self.Cspec.rebin(f=1.0)

    def teardown(self, array_size):
        del self.Cspec


class Coherence:
    """
    Time and Memory benchmarks for calculating the coherence of a cross spectra.
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
        self.Cspec = Crossspectrum(lc1, lc2)

    def time_coher(self, array_size):
        self.Cspec.coherence()

    def peakmem_coher(self, array_size):
        self.Cspec.coherence()

    def teardown(self, array_size):
        del self.Cspec


class TimeLag:
    """
    Time and Memory benchmarks for calculating the time lag of a cross spectra.
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
        self.Cspec = Crossspectrum(lc1, lc2)

    def time_Tlag(self, array_size):
        self.Cspec.time_lag()

    def peakmem_Tlag(self, array_size):
        self.Cspec.time_lag()

    def teardown(self, array_size):
        del self.Cspec


class ClassicalSignificances:
    """
    Time and Memory benchmarks for calculating the time lag of a cross spectra.
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
        self.Cspec = Crossspectrum(lc1, lc2, norm='leahy')

    def time_classSign(self, array_size):
        self.Cspec.classical_significances()

    def peakmem_classSign(self, array_size):
        self.Cspec.classical_significances()

    def teardown(self, array_size):
        del self.Cspec

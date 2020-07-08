import numpy as np

try:
    from stingray import Lightcurve
except ImportError:
    import sys
    print("Install stingray first")
    sys.exit()

test_arr_size = [10**i for i in range(3, 7)]


class Init:
    """
    Time and Memory benchmarks for initializing a lightcurve.
    Uses parameterized and non-parameterized initialization.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        self.times = np.arange(array_size)
        self.counts = np.random.rand(array_size) * 100

    def time_no_param(self, array_size):
        Lightcurve(self.times, self.counts)

    def peakmem_no_param(self, array_size):
        Lightcurve(self.times, self.counts)

    def time_param(self, array_size):
        Lightcurve(self.times, self.counts, dt=1.0, skip_checks=True)

    def peakmem_param(self, array_size):
        Lightcurve(self.times, self.counts, dt=1.0, skip_checks=True)

    def teardown(self, array_size):
        del self.times, self.counts


class ChangeMJDREF:
    """
    Time and Memory benchmarks for changing the mjdref of a lightcurve.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100
        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_MJD(self, array_size):
        self.lc.change_mjdref(-2379826)

    def peakmem_MJD(self, array_size):
        self.lc.change_mjdref(-2379826)

    def teardown(self, array_size):
        del self.lc


class Rebin:
    """
    Time and Memory benchmarks for rebinning a lightcurve.
    Benchmarks sum as well as average, mean rebinning methods.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100
        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_rebin_sum(self, array_size):
        self.lc.rebin(2.0)

    def peakmem_rebin_sum(self, array_size):
        self.lc.rebin(2.0)

    def time_rebin_mean_avg(self, array_size):
        self.lc.rebin(2.0, method='avg')

    def peakmem_rebin_mean_avg(self, array_size):
        self.lc.rebin(2.0, method='avg')

    def teardown(self, array_size):
        del self.lc


class AddLightcurve:
    """
    Time and Memory benchmarks for adding two lightcurves.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc1 = Lightcurve(times, counts, dt=1.0, skip_checks=True)
        self.lc2 = Lightcurve(times,
                              counts * np.random.rand(array_size),
                              dt=1.0,
                              skip_checks=True)

    def time_bench(self, array_size):
        self.lc1.__add__(self.lc2)

    def peakmem_bench(self, array_size):
        self.lc1.__add__(self.lc2)

    def teardown(self, array_size):
        del self.lc1, self.lc2


class SubLightcurve:
    """
    Time and Memory benchmarks for subtracting two lightcurves.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc1 = Lightcurve(times, counts, dt=1.0, skip_checks=True)
        self.lc2 = Lightcurve(times,
                              counts * np.random.rand(array_size),
                              dt=1.0,
                              skip_checks=True)

    def time_bench(self, array_size):
        self.lc1.__sub__(self.lc2)

    def peakmem_bench(self, array_size):
        self.lc1.__sub__(self.lc2)

    def teardown(self, array_size):
        del self.lc1, self.lc2


class CheckEqLightcurve:
    """
    Time and Memory benchmarks for checking if two lightcurves are equal.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc1 = Lightcurve(times, counts, dt=1.0, skip_checks=True)
        self.lc2 = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_bench(self, array_size):
        self.lc1.__eq__(self.lc2)

    def peakmem_bench(self, array_size):
        self.lc1.__eq__(self.lc2)

    def teardown(self, array_size):
        del self.lc1, self.lc2


class NegLightcurve:
    """
    Time and Memory benchmarks for negating a lightcurves.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_bench(self, array_size):
        self.lc.__neg__()

    def peakmem_bench(self, array_size):
        self.lc.__neg__()

    def teardown(self, array_size):
        del self.lc


class Truncate:
    """
    Time and Memory benchmarks for truncating a lightcurve.
    Benchmarks for truncate by index and time.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100
        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_trunc_index(self, array_size):
        self.lc.truncate(0, 1000)

    def peakmem_trunc_index(self, array_size):
        self.lc.truncate(0, 1000)

    def time_trunc_time(self, array_size):
        self.lc.truncate(0, array_size / 2, method='time')

    def peakmem_trunc_time(self, array_size):
        self.lc.truncate(0, array_size / 2, method='time')

    def teardown(self, array_size):
        del self.lc


class Join:
    """
    Time and Memory benchmarks for joining  two lightcurves.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc1 = Lightcurve(times, counts, dt=1.0, skip_checks=True)
        self.lc2 = Lightcurve(times,
                              counts * np.random.rand(array_size),
                              dt=1.0,
                              skip_checks=True)

    def time_bench(self, array_size):
        self.lc1.join(self.lc2)

    def peakmem_bench(self, array_size):
        self.lc1.join(self.lc2)

    def teardown(self, array_size):
        del self.lc1, self.lc2


class Split:
    """
    Time and Memory benchmarks for splitting a lightcurves.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(0, array_size, np.random.randint(4, 9))
        counts = np.random.rand(len(times)) * 100

        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_bench(self, array_size):
        self.lc.split(4)

    def peakmem_bench(self, array_size):
        self.lc.split(4)

    def teardown(self, array_size):
        del self.lc


class MakeLightcurve:
    """
    Time and Memory benchmarks for making a lightcurve.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        self.times = np.arange(array_size)

    def time_bench(self, array_size):
        Lightcurve.make_lightcurve(self.times, dt=1.0)

    def peakmem_bench(self, array_size):
        Lightcurve.make_lightcurve(self.times, dt=1.0)

    def teardown(self, array_size):
        del self.lc


class Sort:
    """
    Time and Memory benchmarks for sorting a lightcurve.
    Benchmarks for sorting by times and counts.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.random.rand(array_size) * 10
        counts = np.random.rand(array_size) * 100
        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_sort_times(self, array_size):
        self.lc.sort()

    def peakmem_sort_times(self, array_size):
        self.lc.sort()

    def time_sort_counts(self, array_size):
        self.lc.sort_counts()

    def peakmem_sort_counts(self, array_size):
        self.lc.sort_counts()

    def teardown(self, array_size):
        del self.lc


class AnalyzeChunks:
    """
    Time and Memory benchmarks for analyzing lightcurve chunks.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_bench(self, array_size):
        self.lc.analyze_lc_chunks(1000, lambda x: np.mean(x))

    def peakmem_bench(self, array_size):
        self.lc.analyze_lc_chunks(1000, lambda x: np.mean(x))

    def teardown(self, array_size):
        del self.lc


class EstimateChunkLength:
    """
    Time and Memory benchmarks for estimating lightcurve chunk length.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_bench(self, array_size):
        self.lc.estimate_chunk_length(100, 100)

    def peakmem_bench(self, array_size):
        self.lc.estimate_chunk_length(100, 100)

    def teardown(self, array_size):
        del self.lc


class SplitGTI:
    """
    Time and Memory benchmarks for splitting lightcurve object according to GTI's.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_bench(self, array_size):
        self.lc.split_by_gti()

    def peakmem_bench(self, array_size):
        self.lc.split_by_gti()

    def teardown(self, array_size):
        del self.lc


class ApplyGTI:
    """
    Time and Memory benchmarks to apply GTI to lightcurve.
    """
    params = test_arr_size
    param_names = ['array_size']
    timeout = 120.0

    def setup(self, array_size):
        times = np.arange(array_size)
        counts = np.random.rand(array_size) * 100

        self.lc = Lightcurve(times, counts, dt=1.0, skip_checks=True)

    def time_bench(self, array_size):
        self.lc.apply_gtis()

    def peakmem_bench(self, array_size):
        self.lc.apply_gtis()

    def teardown(self, array_size):
        del self.lc


# class MakeLIghtcurve:

from subprocess import call
from sys import executable, exit
import re


class Dependencies:
    """
    Track number of dependencies.
    """
    def setup(self):
        try:
            # replace with absolute path to your setup.cfg
            with open('/home/apollo/stingray/setup.cfg', 'r+') as f_ptr:
                content = f_ptr.read()

            substr1 = 'install_requires =\n'
            substr2 = '[options.entry_points]'
            substr3 = 'all =\n'
            substr4 = 'test =\n'

            start_idx1 = content.index(substr1)
            end_idx1 = content.index(substr2)
            start_idx1 += len(substr1)

            start_idx2 = content.index(substr3)
            end_idx2 = content.index(substr4)
            start_idx2 += len(substr3)

            base_imports = content[start_idx1:end_idx1]
            self.core_import_list = [
                re.sub(r"[^a-zA-Z]+", '', char)
                for char in base_imports.split("\n") if char
            ]

            opt_imports = content[start_idx2:end_idx2]
            self.opt_import_list = [
                re.sub(r"[^a-zA-Z]+", '', char)
                for char in opt_imports.split("\n") if char
            ]

        except (FileNotFoundError, ValueError):
            exit()

    def track_core_dependencies(self):
        return len(self.base_import_list)

    def track_optional_dependencies(self):
        return len(self.opt_import_list)


class Imports:
    """
    Time and Memory benchmarks for importing stingray.
    """
    def execute(self, command):
        call((executable, '-c', command))

    def time_stingray(self):
        self.execute('import stingray')

    def time_Lightcurve(self):
        self.execute('from stingray import Lightcurve')

    def time_Powerspectrum(self):
        self.execute('from stingray import Lightcurve, Powerspectrum')

    def time_AveragedPowerspectrum(self):
        self.execute('from stingray import Lightcurve, AveragedPowerspectrum')

    def time_DynamicalPowerspectrum(self):
        self.execute('from stingray import Lightcurve, DynamicalPowerspectrum')

    def time_Crossspectrum(self):
        self.execute('from stingray import Lightcurve, Crossspectrum')

    def time_AveragedCrossspectrum(self):
        self.execute('from stingray import Lightcurve, AveragedCrossspectrum')

    def time_Bispectra(self):
        self.execute('from stingray.bispectrum import Bispectrum')

    def time_CrossCorrelation(self):
        self.execute('from stingray.crosscorrelation import CrossCorrelation')

    def time_Covariancepectrum(self):
        self.execute('from stingray import Lightcurve, Covariancespectrum')

    def time_AveragedCovariancepectrum(self):
        self.execute('from stingray import Lightcurve, Covariancespectrum')

    def peakmem_stingray(self):
        self.execute('import stingray')

    def peakmem_Lightcurve(self):
        self.execute('from stingray import Lightcurve')

    def peakmem_Powerspectrum(self):
        self.execute('from stingray import Lightcurve, Powerspectrum')

    def peakmem_AveragedPowerspectrum(self):
        self.execute('from stingray import Lightcurve, AveragedPowerspectrum')

    def peakmem_DynamicalPowerspectrum(self):
        self.execute('from stingray import Lightcurve, DynamicalPowerspectrum')

    def peakmem_Crossspectrum(self):
        self.execute('from stingray import Lightcurve, Crossspectrum')

    def peakmem_AveragedCrossspectrum(self):
        self.execute('from stingray import Lightcurve, AveragedCrossspectrum')

    def peakmem_Bispectra(self):
        self.execute('from stingray.bispectrum import Bispectrum')

    def peakmem_CrossCorrelation(self):
        self.execute('from stingray.crosscorrelation import CrossCorrelation')

    def peakmem_Covariancepectrum(self):
        self.execute('from stingray import Lightcurve, Covariancespectrum')

    def peakmem_AveragedCovariancepectrum(self):
        self.execute('from stingray import Lightcurve, Covariancespectrum')

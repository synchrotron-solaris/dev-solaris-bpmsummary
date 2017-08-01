from setuptools import find_packages, setup

from bpm_summary_ds.version import __version__, licence
from bpm_summary_ds import __doc__, __author__, __author_email__

setup(
    name="tangods-bpm_summary",
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    license=licence,
    description="A simple facade device for calculating mean, RMS and maximum "
                "deviation values of Beam Position Monitors.",
    long_description=__doc__,
    url="https://github.com/synchrotron-solaris/dev-solaris-shutter.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["setuptools"],
    entry_points={
        "console_scripts": ["BPMSummary = "
                            "bpm_summary_ds.bpm_summary:run"]}
)

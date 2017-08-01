"""
This module contains device class BPMSummary and run method for it.
"""

# Imports
from tango import DevState, AttrWriteType
from facadedevice import Facade, combined_attribute
from numpy import std, mean
from math import sqrt


class BPMSummary(Facade):
    """
    This Tango Device Class implements Facade Device to summarize Beam
    Position Motors. It allows to compute following values:

    * mean
    * root mean square
    * maximum peak to peak value
    * standard deviation
    * maximum deviation

    Those calculations are performed on BPMs' attributes provided via BPMList.
    They can be provided in two ways:

    * explicit list of all attributes for calculations. It's useful when BPMs
    are on different Device Servers. For example: some/bpm/somewhere/attr,
    some/other/bpm/attr, here/some/other/attr

    * simple comprehension containing '*' character in place which should accept
    any value. For example: some/bpm/*/attr. This will allow BPMSummary Device
    to use in calculations every single device which name fulfill this
    comprehension, like:

    -- some/bpm/here/attr
    -- some/bpm/there/attr
    -- some/bpm/out_there/attr
    -- etc.

    """

    def safe_init_device(self):
        """
        This is a method to safely initialize the BPMSummary device,
        overrode from Facade base class
        """
        super(BPMSummary, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running.")

    # combined attributes

    @combined_attribute(
        dtype=float,
        property_name='BPMList',
        access=AttrWriteType.READ,
        description="This function calculates mean of all provided BPMs' attributes")
    def Mean(self, *args):
        return mean(args)

    @combined_attribute(
        dtype=float,
        property_name='BPMList',
        access=AttrWriteType.READ,
        description="This function calculates root mean square of all provided "
                    "BPMs' attributes")
    def RMS(self, *args):
        squared = list(map(lambda x: x ** 2, args))
        return sqrt(mean(squared))

    @combined_attribute(
        dtype=float,
        property_name='BPMList',
        access=AttrWriteType.READ,
        description="This function calculates peak to peak value of all provided "
                    "BPMs' attributes")
    def PeakToPeak(self, *args):
        return max(args) - min(args)

    @combined_attribute(
        dtype=float,
        property_name='BPMList',
        access=AttrWriteType.READ,
        description="This function calculates standard deviation of all provided "
                    "BPMs' attributes")
    def StandardDeviation(self, *args):
        return std(args)

    @combined_attribute(
        dtype=float,
        property_name='BPMList',
        access=AttrWriteType.READ,
        description="This function calculates maximum deviation of all provided "
                    "BPMs' attributes")
    def MaximumDeviation(self, *args):
        return max(args)

# run server

run = BPMSummary.run_server()

if __name__ == '__main__':
    run()

# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, print_function)
__metaclass__ = type

import re

from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
        Ansible file jinja2 tests
    """
    def filters(self):
        return {
            'gotosocial_checksum': self.checksum,
            'gotosocial_assets_checksum': self.assets_checksum,
        }

    def checksum(self, data, os, arch):
        """
        """
        checksum = None

        if isinstance(data, list):
            # XXX   gotosocial_0.6.0_linux_amd64.tar.gz
            # filter OS and ARCH
            checksum = [x for x in data if re.search(fr".*gotosocial_.*_{os}_{arch}.tar.gz", x)][0]

        if isinstance(checksum, str):
            checksum = checksum.split(" ")[0]

        # display.v("= checksum: {}".format(checksum))

        return checksum

    def assets_checksum(self, data, filter="web-assets"):
        """
        """
        checksum = None

        if isinstance(data, list):
            # XXX   gotosocial_0.6.0_web-assets.tar.gz
            # filter OS and ARCH
            checksum = [x for x in data if re.search(fr".*gotosocial_.*_{filter}.tar.gz", x)][0]

        if isinstance(checksum, str):
            checksum = checksum.split(" ")[0]

        # display.v("= checksum: {}".format(checksum))

        return checksum

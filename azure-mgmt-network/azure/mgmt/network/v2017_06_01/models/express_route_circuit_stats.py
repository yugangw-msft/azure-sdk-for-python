# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExpressRouteCircuitStats(Model):
    """Contains stats associated with the peering.

    :param primarybytes_in: Gets BytesIn of the peering.
    :type primarybytes_in: long
    :param primarybytes_out: Gets BytesOut of the peering.
    :type primarybytes_out: long
    :param secondarybytes_in: Gets BytesIn of the peering.
    :type secondarybytes_in: long
    :param secondarybytes_out: Gets BytesOut of the peering.
    :type secondarybytes_out: long
    """

    _attribute_map = {
        'primarybytes_in': {'key': 'primarybytesIn', 'type': 'long'},
        'primarybytes_out': {'key': 'primarybytesOut', 'type': 'long'},
        'secondarybytes_in': {'key': 'secondarybytesIn', 'type': 'long'},
        'secondarybytes_out': {'key': 'secondarybytesOut', 'type': 'long'},
    }

    def __init__(self, primarybytes_in=None, primarybytes_out=None, secondarybytes_in=None, secondarybytes_out=None):
        self.primarybytes_in = primarybytes_in
        self.primarybytes_out = primarybytes_out
        self.secondarybytes_in = secondarybytes_in
        self.secondarybytes_out = secondarybytes_out
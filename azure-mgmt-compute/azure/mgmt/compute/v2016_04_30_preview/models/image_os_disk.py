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


class ImageOSDisk(Model):
    """Describes an Operating System disk.

    :param os_type: This property allows you to specify the type of the OS
     that is included in the disk if creating a VM from a custom image.
     <br><br> Possible values are: <br><br> **Windows** <br><br> **Linux**.
     Possible values include: 'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.OperatingSystemTypes
    :param os_state: The OS State. Possible values include: 'Generalized',
     'Specialized'
    :type os_state: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.OperatingSystemStateTypes
    :param snapshot: The snapshot.
    :type snapshot: ~azure.mgmt.compute.v2016_04_30_preview.models.SubResource
    :param managed_disk: The managedDisk.
    :type managed_disk:
     ~azure.mgmt.compute.v2016_04_30_preview.models.SubResource
    :param blob_uri: The Virtual Hard Disk.
    :type blob_uri: str
    :param caching: Specifies the caching requirements. <br><br> Possible
     values are: <br><br> **None** <br><br> **ReadOnly** <br><br> **ReadWrite**
     <br><br> Default: **None for Standard storage. ReadOnly for Premium
     storage**. Possible values include: 'None', 'ReadOnly', 'ReadWrite'
    :type caching: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.CachingTypes
    :param disk_size_gb: Specifies the size of empty data disks in gigabytes.
     This element can be used to overwrite the name of the disk in a virtual
     machine image. <br><br> This value cannot be larger than 1023 GB
    :type disk_size_gb: int
    """

    _validation = {
        'os_type': {'required': True},
        'os_state': {'required': True},
    }

    _attribute_map = {
        'os_type': {'key': 'osType', 'type': 'OperatingSystemTypes'},
        'os_state': {'key': 'osState', 'type': 'OperatingSystemStateTypes'},
        'snapshot': {'key': 'snapshot', 'type': 'SubResource'},
        'managed_disk': {'key': 'managedDisk', 'type': 'SubResource'},
        'blob_uri': {'key': 'blobUri', 'type': 'str'},
        'caching': {'key': 'caching', 'type': 'CachingTypes'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
    }

    def __init__(self, os_type, os_state, snapshot=None, managed_disk=None, blob_uri=None, caching=None, disk_size_gb=None):
        self.os_type = os_type
        self.os_state = os_state
        self.snapshot = snapshot
        self.managed_disk = managed_disk
        self.blob_uri = blob_uri
        self.caching = caching
        self.disk_size_gb = disk_size_gb
